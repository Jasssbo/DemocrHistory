# Regole Storiografiche, Deontologiche e di Integrità del Repository (Always-On)

Queste direttive sono **sempre attive** per qualsiasi operazione sul progetto **Guazzabuglio Politico**, anche per modifiche rapide o puntuali. Quando il task riguarda l'aggiunta, la modifica o la verifica di eventi storici, attiva e consulta sempre anche la skill [`democr_history`](../skills/democr_history/SKILL.md) e i suoi prontuari in `references/`.

## 1. Rigore Storiografico e 4 Livelli di Accertamento (Non Negoziabili)
Non fondere mai fatti materiali, sentenze definitive, atti istruttori/parlamentari e ipotesi storiografiche o giornalistiche in un'unica narrazione indistinta. Ogni periodo della `descrizione` deve esplicitare la propria fonte e natura:
1. **Fatto materiale accertato**: data, luogo, vittime, dinamica materiale oggettiva.
2. **Verità giudiziaria passata in giudicato**: sentenze definitive (Corte di Cassazione o sentenze irrevocabili di merito). Specifica sempre l'esito esatto (*condanna definitiva*, *assoluzione con formula piena*, *assoluzione ex art. 530 co. 2 c.p.p.*, *non doversi procedere per prescrizione*) e distingui tra esecutori materiali, organizzatori e mandanti.
3. **Atti istruttori e Commissioni parlamentari d'inchiesta**:
   - Le **ordinanze-sentenze di giudici istruttori** (es. Salvini 1995, Priore 1999, Lombardi 1998) sono atti istruttori/di rinvio a giudizio: **non presentarli mai come sentenze definitive di condanna**, ma come *"L'ordinanza-sentenza del giudice istruttore X ha ricostruito/evidenziato..."*.
   - Per le **Commissioni parlamentari** (Antimafia, P2, Stragi, Moro, SIFAR, Sindona), specifica sempre se si tratta di **Relazione conclusiva di maggioranza**, **Relazione di minoranza** o **proposta di relazione non votata**.
4. **Dibattito storiografico, inchieste giornalistiche e dichiarazioni di collaboratori**:
   - Introduci sempre con formule di attribuzione esplicita (*"Secondo la ricostruzione dello storico X..."*, *"Il collaboratore di giustizia Y ha dichiarato..."*), specificando se tali dichiarazioni hanno trovato riscontro processuale o sono rimaste prive di riscontri in giudicato.
5. **Divieto di citare compilazioni generiche (Wikipedia / Strano Network / Treccani) nella prosa della `descrizione`**:
   - Nella `descrizione` **cita letteralmente una fonte solo quando è una fonte specifica** (es. un atto giudiziario o parlamentare in `Documents/`, una monografia d'autore, uno studio specifico come Filodiritto o Fondazione Perini, o un sito istituzionale specifico come CSM o Camera dei Deputati).
   - **NON scrivere mai nella `descrizione`** formule come *"secondo Wikipedia"*, *"come ricostruito nella voce di Wikipedia"*, *"secondo la cronologia di Strano Network"* o *"secondo Treccani"*: i fatti storici generali vanno esposti direttamente in prosa enciclopedica con i `[[Wikilink]]`, lasciando Wikipedia, Strano Network e Treccani nell'array `"fonti"`.

## 2. Standard Linguistico e Neutralità (NPOV)
- **Prosa enciclopedica completa**: vietato lo stile telegrafico (niente omissione di articoli, preposizioni o verbi). Ogni frase deve essere grammaticalmente autonoma, scorrevole e neutrale.
- **Tipografia italiana**: usa le virgolette basse `«...»` per citazioni ed espressioni storiche/gergali, date estese in italiano (`1° maggio 1947`, `2 agosto 1980`) e minuscole per le cariche istituzionali (*presidente del Consiglio*, *ministro dell'Interno*, *carabinieri*).
- **Coerenza JSON**: in `data/DiacroniaDellaRepubblicaItaliana.json` la chiave del dizionario in `PRE-EVENTI` o `EVENTI` deve coincidere esattamente con il campo `"titolo"` dell'evento.

## 3. Regola di Nomenclatura per `Documents/` (Prevenzione Rottura Link Markdown)
- Ogni file PDF salvato o aggiunto nella cartella `Documents/` deve avere un nome **privo di parentesi tonde `(` `)` e privo di spazi** (usa `PascalCase` o `Kebab-Case`, es. `Cassazione-StrageDiBologna-23Novembre1995.pdf`).
- *Motivo tecnico*: il parser Markdown `[testo](Documents/file.pdf)` dell'interfaccia web si interrompe alla prima parentesi chiusa `)`, troncando qualsiasi URL o percorso che contenga parentesi nel nome file.

## 4. Salvaguardia del Lavoro dell'Utente e Allineamento Interfacce
- **Divieto di sovrascrittura**: prima di modificare `data/DiacroniaDellaRepubblicaItaliana.json` (o altri file in `data/`), leggi sempre lo stato attuale del file su disco per non sovrascrivere correzioni manuali recenti dell'utente.
- **Validazione obbligatoria**: dopo qualsiasi modifica ai file JSON in `data/`, esegui sempre lo script `.agents/skills/democr_history/scripts/validate_archive.py` e risolvi ogni errore segnalato prima di concludere.
- **Sincronia UI**: quando modifichi funzionalità dell'interfaccia web, mantieni allineati `index.html`, `mobile.html` e `OpenChronichles.html` (salvo diversa indicazione esplicita dell'utente).
