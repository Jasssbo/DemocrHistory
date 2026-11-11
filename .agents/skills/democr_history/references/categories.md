# Vocabolario Controllato delle Categorie

Nell'interfaccia di Guazzabuglio Politico e nei database JSON sono supportate **esclusivamente 7 categorie**. Non inventare nuove categorie o sinonimi:

| ID Categoria | Nome Visualizzato | Colore UI | Criteri di Assegnazione Storiografica |
|---|---|---|---|
| `politico` | Politico | 🟢 Verde | Elezioni, formazioni di governi, crisi istituzionali, votazioni parlamentari, leggi cardine, trattati internazionali, vertici di partito. |
| `servizi_segreti` | Servizi segreti | 🔵 Blu | Operazioni di intelligence (SIFAR, SID, SISMI, SISDE, CIA, KGB), apparati Stay-Behind (Gladio), depistaggi di Stato, fascicoli classificati. |
| `mafia` | Mafia | ⚫ Nero | Cosa Nostra, 'Ndrangheta, Camorra, Sacra Corona Unita, Banda della Magliana; omicidi di mafia, maxiprocessi, relazioni mafia-politica. |
| `gruppi_terroristici` | Gruppi terroristici | 🔴 Rosso | Stragismo, terrorismo nero (Ordine Nuovo, Avanguardia Nazionale, NAR), terrorismo rosso (Brigate Rosse, Prima Linea), attentati, sequestri armati. |
| `massoneria` | Massoneria | 🟣 Viola | Loggia P2 (Propaganda 2), Grande Oriente d'Italia, Gran Loggia d'Italia, inchieste parlamentari su logge coperte e influenze occulte. |
| `clero` | Clero | ⚪ Bianco | Vaticano, Santa Sede, IOR, rapporti Stato-Chiesa, Patti Lateranensi, associazioni cattoliche con impatto politico o finanziario (es. Banco Ambrosiano). |
| `re` | Re | 🟡 Giallo | Dinastia Savoia, monarchia sabauda, referendum istituzionale del 1946, complotti monarchici nel dopoguerra. |

### Regole per l'assegnazione multipla
- Un evento può avere più categorie quando gli attori o gli ambiti si sovrappongono in modo dimostrato (es. la Strage di Portella della Ginestra riceve `["mafia", "politico"]`; il caso Calvi/Ambrosiano riceve `["massoneria", "clero", "mafia"]`).
- Non sovraccaricare gli eventi: assegna solo le categorie direttamente collegate a fatti documentati.
