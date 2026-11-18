#!/usr/bin/env python3
"""
Script di validazione storiografica, strutturale e documentale per gli archivi JSON di Guazzabuglio Politico.
Uso:
  python3 .agents/skills/democr_history/scripts/validate_archive.py [percorso_json]
Se non viene specificato alcun file, valida tutti i file .json nella cartella data/.
"""

import glob
import json
import os
import re
import sys

DEFAULT_CATEGORIES = {
    "politico",
    "servizi_segreti",
    "mafia",
    "gruppi_terroristici",
    "massoneria",
    "clero",
    "re",
}

KNOWN_BAD_WIKILINKS = {
    "Lodo Moro": "Usa [[Lodo Moro (1979)|Lodo Moro]] (pagina di disambiguazione)",
    "Rete (partito politico)": "Usa [[La Rete (partito politico)|La Rete]]",
    "Operazione Blue Moon": "Voce inesistente su it.wiki; usa [[Operazione Chaos|Operazione Blue Moon]]",
    "Servizio informazioni forze armate": "Usa [[SIFAR]]",
    "E (periodico)": "Usa [[È (quotidiano)|«È»]]",
    "Avanguardia Nazionale (1970)": "Usa [[Avanguardia nazionale]]",
    "Banda Giuliano": "Usa [[Salvatore Giuliano|banda Giuliano]]",
}

POV_RED_FLAGS = [
    r"\borribil[ei]\b",
    r"\bspietat[oaie]\b",
    r"\bmostruos[oaie]\b",
    r"\bagghiacciant[ei]\b",
    r"\bscandalos[oaie]\b",
]


def validate_documents_folder(repo_root):
    errors = []
    docs_dir = os.path.join(repo_root, "Documents")
    if not os.path.isdir(docs_dir):
        errors.append("Cartella Documents/ non trovata nella radice del repository.")
        return errors, set()

    files = set(os.listdir(docs_dir))
    for fname in sorted(files):
        if "(" in fname or ")" in fname or " " in fname:
            errors.append(
                f"[Documents/] Nome file non conforme (contiene spazi o parentesi che rompono i link Markdown): '{fname}'"
            )
    return errors, files


def validate_json_file(path, repo_root, docs_on_disk):
    errors = []
    warnings = []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return [f"[{path}] Errore di parsing JSON: {e}"], []

    if not isinstance(data, dict):
        return [f"[{path}] La radice del JSON deve essere un oggetto."], []

    allowed_cats = set(DEFAULT_CATEGORIES)
    custom_cats = data.get("CATEGORIE") or data.get("categorie")
    if isinstance(custom_cats, list):
        for c in custom_cats:
            if isinstance(c, dict) and c.get("id"):
                allowed_cats.add(str(c["id"]).strip())

    sections = []
    if isinstance(data.get("PRE-EVENTI"), dict):
        sections.append(("PRE-EVENTI", data["PRE-EVENTI"]))
    if isinstance(data.get("EVENTI"), dict):
        sections.append(("EVENTI", data["EVENTI"]))

    if not sections:
        errors.append(f"[{path}] Nessuna sezione 'PRE-EVENTI' o 'EVENTI' valida trovata.")
        return errors, warnings

    date_pattern = re.compile(r"^$|^\d{4}(-\d{2}(-\d{2})?)?$")

    for sec_name, sec_dict in sections:
        for key, ev in sec_dict.items():
            if not isinstance(ev, dict):
                errors.append(f"[{sec_name}] '{key}' non è un oggetto valido.")
                continue

            prefix = f"[{sec_name} -> '{key[:45]}']"
            titolo = str(ev.get("titolo", "")).strip()
            anno = ev.get("anno")
            data_str = str(ev.get("data", "")).strip()
            desc = str(ev.get("descrizione", "")).strip()
            cats = ev.get("categorie", [])
            fonti = ev.get("fonti", [])

            # 1. Titolo e coerenza chiave
            if not titolo:
                errors.append(f"{prefix} Campo 'titolo' mancante o vuoto.")
            elif titolo != key:
                warnings.append(f"{prefix} La chiave JSON ('{key}') differisce da 'titolo' ('{titolo}').")
            if len(titolo) > 120:
                warnings.append(f"{prefix} Titolo troppo lungo ({len(titolo)} caratteri, max consigliato 120).")
            if titolo.endswith("..."):
                warnings.append(f"{prefix} Il titolo sembra troncato con '...'.")

            # 2. Anno e Data
            if not isinstance(anno, int) or isinstance(anno, bool) or not (1700 <= anno <= 2100):
                errors.append(f"{prefix} Campo 'anno' non valido: {anno!r}.")
            if not date_pattern.match(data_str):
                errors.append(f"{prefix} Campo 'data' non in formato ISO YYYY-MM-DD: '{data_str}'.")
            elif data_str and isinstance(anno, int) and not data_str.startswith(str(anno)):
                warnings.append(f"{prefix} L'anno in 'data' ('{data_str}') non coincide con 'anno' ({anno}).")

            # 3. Categorie
            if not isinstance(cats, list) or not cats:
                warnings.append(f"{prefix} Nessuna categoria assegnata.")
            else:
                if len(cats) != len(set(cats)):
                    errors.append(f"{prefix} Categorie duplicate in {cats}.")
                for c in cats:
                    if c not in allowed_cats:
                        errors.append(f"{prefix} Categoria non riconosciuta: '{c}'.")

            # 4. Descrizione, bilanciamento link e Wikilink
            if not desc:
                errors.append(f"{prefix} Campo 'descrizione' mancante o vuoto.")
            else:
                word_count = len(desc.split())
                if word_count < 30:
                    warnings.append(f"{prefix} Descrizione molto breve ({word_count} parole; consigliate 60-180).")

                if desc.count("[[") != desc.count("]]"):
                    errors.append(f"{prefix} Parentesi Wikilink [[...]] non bilanciate nella descrizione.")

                for wl in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", desc):
                    wl_clean = wl.strip()
                    if wl_clean in KNOWN_BAD_WIKILINKS:
                        errors.append(
                            f"{prefix} Wikilink errato o disambiguo '[[{wl_clean}]]': {KNOWN_BAD_WIKILINKS[wl_clean]}"
                        )

                for md_label, md_url in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", desc):
                    url_clean = md_url.strip()
                    if url_clean.startswith("Documents/"):
                        doc_name = url_clean.replace("Documents/", "", 1)
                        if doc_name not in docs_on_disk:
                            errors.append(
                                f"{prefix} Link Markdown a documento inesistente in Documents/: '{url_clean}'"
                            )

                for rf in POV_RED_FLAGS:
                    if re.search(rf, desc, flags=re.IGNORECASE):
                        warnings.append(f"{prefix} Possibile aggettivo non neutrale (NPOV) rilevato da pattern '{rf}'.")

                if re.search(r"(it\.wikipedia\.org|strano\.net|\bstrano\s+network\b|\bvoce\s+wikipedia\b|\bvoci\s+di\s+wikipedia\b)", desc, flags=re.IGNORECASE):
                    errors.append(
                        f"{prefix} Citazione esplicita di Wikipedia o Strano Network nella prosa della descrizione (usare [[Wikilink]] nel testo e inserire Wikipedia/Strano Network solo in 'fonti')."
                    )

            # 5. Fonti
            if not isinstance(fonti, list) or not fonti:
                warnings.append(f"{prefix} Nessuna fonte in 'fonti'.")
            else:
                for f_item in fonti:
                    if not isinstance(f_item, dict) or not f_item:
                        errors.append(f"{prefix} Elemento in 'fonti' non valido: {f_item!r}")
                        continue
                    for f_label, f_url in f_item.items():
                        f_label_s = str(f_label).strip()
                        f_url_s = str(f_url).strip()
                        if not f_label_s or not f_url_s:
                            errors.append(f"{prefix} Fonte con etichetta o URL vuoto: {f_item!r}")
                        elif f_url_s.startswith("Documents/"):
                            doc_name = f_url_s.replace("Documents/", "", 1)
                            if doc_name not in docs_on_disk:
                                errors.append(
                                    f"{prefix} Fonte locale punta a file inesistente in Documents/: '{f_url_s}'"
                                )

    return errors, warnings


def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
    targets = sys.argv[1:] if len(sys.argv) > 1 else sorted(glob.glob(os.path.join(repo_root, "data", "*.json")))

    doc_errors, docs_on_disk = validate_documents_folder(repo_root)
    total_errors = list(doc_errors)
    total_warnings = []

    for path in targets:
        errs, warns = validate_json_file(path, repo_root, docs_on_disk)
        total_errors.extend(errs)
        total_warnings.extend(warns)

    print(f"=== VALIDAZIONE ARCHIVIO ({len(targets)} file JSON, {len(docs_on_disk)} PDF in Documents/) ===")
    if total_warnings:
        print(f"\nAvvisi ({len(total_warnings)}):")
        for w in total_warnings[:25]:
            print(f"  [WARN] {w}")
        if len(total_warnings) > 25:
            print(f"  ... e altri {len(total_warnings) - 25} avvisi.")

    if total_errors:
        print(f"\nERRORI CRITICI ({len(total_errors)}):")
        for e in total_errors:
            print(f"  [ERR]  {e}")
        sys.exit(1)

    print("\n[OK] Tutti i controlli strutturali, documentali e sui link sono stati superati (0 errori critici).")
    sys.exit(0)


if __name__ == "__main__":
    main()
