# Vocabolario e Tassonomia delle Categorie

## 1. Categorie Predefinite per `GuazzabuglioPolitico.json`
Nell'archivio storico principale (`data/GuazzabuglioPolitico.json`) sono utilizzate **7 categorie storiografiche predefinite**:

| ID Categoria | Nome Visualizzato | Colore Default (`#HEX`) | Criteri di Assegnazione Storiografica |
|---|---|---|---|
| `politico` | Politico | 🟢 Verde (`#2e7d4f`) | Elezioni, formazioni e crisi di governo, leggi cardine, referendum, vertici di partito, trattati internazionali, scandali politico-istituzionali. |
| `servizi_segreti` | Servizi segreti | 🔵 Blu (`#1f5fbf`) | Operazioni di intelligence (SIFAR, SID, Ufficio Affari Riservati, SISMI, SISDE, CESIS, CIA, KGB), strutture Stay-Behind (Gladio), guerra non ortodossa, depistaggi di Stato, fascicoli illegali. |
| `mafia` | Mafia | ⚫ Nero (`#1b1b1b`) | Cosa nostra, 'Ndrangheta, Camorra, Sacra Corona Unita, Banda della Magliana; omicidi eccellenti, stragi mafiose, maxiprocessi, rapporti mafia-politica-finanza. |
| `gruppi_terroristici` | Gruppi terroristici | 🔴 Rosso (`#c62828`) | Stragismo, eversione nera (Ordine Nuovo, Avanguardia Nazionale, Terza Posizione, NAR), terrorismo rosso (Brigate Rosse, Prima Linea, NAP), attentati, sequestri politici. |
| `massoneria` | Massoneria | 🟣 Viola (`#7b3fa8`) | Loggia P2 (Propaganda Due), Grande Oriente d'Italia, Gran Loggia d'Italia, logge coperte o deviate, inchieste parlamentari e giudiziarie su affiliazioni occulte. |
| `clero` | Clero | ⚪ Bianco (`#ffffff`) | Vaticano, Santa Sede, IOR, rapporti Stato-Chiesa, Patti Lateranensi, istituti finanziari connessi (es. Banco Ambrosiano). |
| `re` | Re | 🟡 Giallo (`#e8b400`) | Casa Savoia, monarchia sabauda, Luogotenenza, referendum istituzionale del 1946, organizzazioni o tentativi monarchici nel dopoguerra. |

### Regole per l'assegnazione multipla
- Un evento può ricevere più categorie quando gli ambiti si sovrappongono in modo documentato (es. *Strage di Portella della Ginestra* → `["mafia", "politico"]`; *Crac del Banco Ambrosiano e morte di Roberto Calvi* → `["massoneria", "clero", "mafia", "politico"]`).
- Non sovraccaricare gli eventi: assegna solo le categorie direttamente attinenti ai fatti o agli attori documentati nella scheda.

---

## 2. Categorie Personalizzabili per Archivi Tematici Diversi (`"CATEGORIE"`)
L'interfaccia web (`index.html`, `mobile.html`, `OpenChronichles.html`) permette agli utenti che creano un archivio su altri argomenti storici o disciplinari di personalizzare nomi e colori delle categorie tramite il modale **"Titolo, Info & Categorie"**, salvandole nella radice del JSON:

```json
"CATEGORIE": [
  { "id": "economia", "label": "Economia", "color": "#0d9488" },
  { "id": "scienza", "label": "Scienza", "color": "#2563eb" }
]
```

- Quando curi `data/GuazzabuglioPolitico.json`, attieniti rigorosamente alle **7 categorie predefinite** della Sezione 1.
- Quando curi un archivio tematico differente dotato del campo `"CATEGORIE"`, utilizza gli `id` definiti nell'array `"CATEGORIE"` di quell'archivio.
