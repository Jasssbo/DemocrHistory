# DemocrHistory 🇮🇹📜
### Archivio e Timeline Interattiva per la Storia della Repubblica Italiana

**DemocrHistory** è un progetto **open source e divulgativo** nato per rendere accessibile, consultabile e partecipata la ricostruzione storiografica della storia della Repubblica Italiana — dal secondo dopoguerra agli anni 2000 — attraverso una timeline dinamica, filtri tematici e schede di approfondimento analitico.

---

## 💡 La Missione: Divulgazione e Valorizzazione delle Fonti

Questo progetto **non nasce per sostituirsi agli archivi esistenti**, ma al contrario per **dare massima visibilità, modernità espositiva e fruibilità digitale** all'immenso patrimonio informativo raccolto da ricercatori, storici e progetti indipendenti nel corso dei decenni.

In particolare, il database di DemocrHistory è stato arricchito ed è debitamente debitore del lavoro straordinario svolto da **Strano Network** con il loro storico archivio digitale:

> 🔗 **Fonte di riferimento essenziale**: [Strano Network - Cronologia delle Stragi (1942-2002)](https://www.strano.net/stragi/stragi/crono/indcro.htm)  
> Visita il progetto originale e la loro bibliografia su [strano.net](https://www.strano.net/).

L'obiettivo di DemocrHistory è permettere a studenti, cittadini e ricercatori di esplorare questi fatti storici con strumenti web moderni (timeline interattiva, filtri per stato della ricostruzione, attori, entità e dispositivi mobili).

---

## 👐 Progetto Open Source e Partecipato

DemocrHistory è un **progetto aperto a tutti**. La struttura dei dati è concepita per essere semplice, trasparentemente verificabile e modificabile a mano senza sovrastrutture complesse.

### Come contribuire:

1. **Aggiungere o correggere eventi via GitHub (Pull Request)**:
   - I file dei dati risiedono nella cartella [`data/`](file:///home/mintmzu/MyRepos/DemocrHistory/data/) (es. `data/Italian DemocrHistory.json`).
   - Puoi modificare un file JSON esistente o aggiungerne uno nuovo nella cartella `data/` ed aprire una **Pull Request**. Quando approvata, la tua integrazione apparirà automaticamente sul sito!
2. **Caricamento locale nell'interfaccia**:
   - Puoi caricare ed esplorare un tuo file JSON personale direttamente nell'interfaccia web (tramite il pulsante *"📂 Carica JSON"*), senza bisogno di effettuare commit.

---

## 📱 Interfaccia Web Responsive (Desktop & Mobile)

L'applicazione web è progettata per essere utilizzata con la massima fluidità su qualsiasi dispositivo:
- **Vista Desktop (`index.html`)**: Layout a colonne con timeline principale, dettagli affiancati e filtri avanzati.
- **Vista Mobile (`mobile.html`)**: Interfaccia *mobile-first* per smartphone con scheda di approfondimento in sovrapposizione (*modal sheet*) e navigazione ottimizzata al tocco.

---

## 📐 Struttura del Database JSON

Tutti i file JSON posizionati in `data/` seguono uno schema rigoroso per garantire uniformità e compatibilità.

### Schema di un evento standard:

```json
{
  "anno": 1969,
  "titolo": "Strage di Piazza Fontana",
  "data": {
    "inizio": "1969-12-12",
    "fine": "1969-12-12",
    "precisione": "giorno"
  },
  "luogo": {
    "nome": "Milano",
    "paese": "Italia"
  },
  "descrizione": "Una bomba esplode nella sede della Banca Nazionale dell'Agricoltura a Piazza Fontana a Milano, provocando 17 morti e oltre 80 feriti.",
  "dati_concreti": [
    "Attentato del 12 dicembre 1969 a Milano.",
    "Ritenuto l'evento d'inizio della strategia della tensione in Italia."
  ],
  "responsabili_o_attori": [
    { "nome": "Ordine Nuovo", "ruolo": "gruppo eversivo della destra radicale" },
    { "nome": "Franco Freda", "ruolo": "esponente di Ordine Nuovo" }
  ],
  "entita_coinvolte": ["Banca Nazionale dell'Agricoltura", "Ordine Nuovo", "Polizia di Stato"],
  "tipo_di_fatto": [
    "violenza politica o strage",
    "servizi segreti e apparati dello Stato"
  ],
  "scala": "nazionale",
  "stato_della_ricostruzione": "fatto documentato ed accertato in sede giudiziaria e parlamentare",
  "wikilinks": {
    "Strage_di_Piazza_Fontana": "https://it.wikipedia.org/wiki/Strage_di_Piazza_Fontana"
  },
  "fonti": [
    {
      "tipo": "voce di sintesi",
      "titolo": "Strano Network - Cronologia delle stragi (1969)",
      "url": "https://www.strano.net/stragi/stragi/crono/crono69.htm"
    }
  ]
}
```

### Vocabolario Controllato Ufficiale:

Per garantire la massima pulizia del database, sono ammessi esclusivamente i seguenti valori per i campi di classificazione:

#### `tipo_di_fatto` (Ammessi):
- `"politico-istituzionale"`
- `"sociale-economico"`
- `"violenza politica o strage"`
- `"servizi segreti e apparati dello Stato"`
- `"mafia e criminalita organizzata"`
- `"massoneria e rapporti con la Chiesa"`
- `"politica internazionale e Guerra fredda"`
- `"inchiesta giudiziaria o parlamentare"`
- `"cultura e societa civile"`

#### `scala` (Ammessi):
- `"locale"`, `"nazionale"`, `"internazionale"`

#### `data.precisione` (Ammessi):
- `"giorno"`, `"mese"`, `"anno"`, `"intervallo"`

#### `fonti[].tipo` (Ammessi):
- `"voce di sintesi"`, `"monografia"`, `"relazione parlamentare"`, `"enciclopedia"`, `"atti giudiziari"`

---

## 📜 Licenza e Crediti

- **Licenza**: Progetto distribuito sotto licenza Open Source.
- **Ringraziamenti speciali**: A tutti i ricercatori, archivi indipendenti e in particolare a **Strano Network** per la loro preziosa opera di storiografia e documentazione digitale.
