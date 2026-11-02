# DemocrHistory 🇮🇹📜
### Archivio e Timeline Interattiva per la Storia della Repubblica Italiana

**DemocrHistory** è un progetto **open source e divulgativo** nato per rendere accessibile, consultabile e partecipata la ricostruzione storiografica della storia italiana attraverso una timeline dinamica e schede di approfondimento essenziali.

---

## 💡 La Missione

Questo progetto nasce per dare massima visibilità, modernità e fruibilità digitale all'immenso patrimonio informativo raccolto da ricercatori, storici e archivi indipendenti.

> 🔗 **Fonte di riferimento essenziale**: [Strano Network - Cronologia delle Stragi (1942-2002)](https://www.strano.net/stragi/stragi/crono/indcro.htm)  
> Visita il progetto originale e la loro bibliografia su [strano.net](https://www.strano.net/).

---

## 🌐 Come usare il sito da `github.io`: dalla Ricerca Personale alla Pubblicazione su Git

Chiunque visiti la pagina online tramite **GitHub Pages (`github.io`)** può usarla non solo per consultare l'archivio principale, ma anche come **editor visuale personale** per strutturare una propria ricerca storica in linea temporale, senza dover installare alcun programma e senza che i propri dati vengano inviati a server esterni (tutto avviene localmente nel browser).

### 1️⃣ Creare e salvare una ricerca personale dal browser

1. **Inizia dal Template Guida**: nella colonna di sinistra (su PC in `index.html`) o nella scheda **⚙️ Gestione** (su smartphone in `mobile.html`), clicca su **📄 Nuovo Archivio**. L'applicazione caricherà un **Template Guida interattivo in 3 punti** che mostra subito un esempio pratico di evento compilato e tutte le istruzioni essenziali.
2. **Imposta il titolo del tuo studio**: clicca su **⚙️ Titolo & Info** per inserire il titolo della tua ricerca (es. *"Cronologia delle Riforme Costituzionali"*) e una breve introduzione che descriva la natura del documento.
3. **Aggiungi e struttura i tuoi eventi**:
   - Clicca su **➕ Nuovo Evento** per inserire ogni tappa della tua ricerca specificando **Anno**, eventuale **Data esatta** (`AAAA-MM-GG`), **Titolo**, **Categorie** (una o più categorie tematiche), **Descrizione** e **Fonti** verificabili.
   - Nella descrizione puoi creare collegamenti automatici alle voci di Wikipedia scrivendo semplicemente `[[Nome Voce]]` (oppure `[[Nome Voce|testo mostrato]]`) e link esterni con `[testo](https://...)`.
   - Se vuoi inserire avvenimenti antecedenti di contesto, scegli *"Pre-Evento (Sezione Preludio)"* nel menu *Tipologia Evento*.
4. **Salva il tuo documento sul dispositivo**:
   - Mentre lavori, ogni modifica viene salvata automaticamente come **bozza nel tuo browser** (`localStorage`), così non perdi il lavoro se chiudi o ricarichi la pagina.
   - Clicca su **⬇️ Scarica JSON** per scaricare subito il file `.json` nella cartella Download predefinita, oppure clicca su **📁 Salva in...** per aprire il selettore di sistema e scegliere manualmente la cartella e il nome del file dove salvarlo.
5. **Riapri la tua ricerca o torna all'archivio principale**:
   - Per riprendere in seguito il tuo lavoro (anche da un altro dispositivo), ti basta aprire la pagina `github.io` e selezionare il tuo file tramite **Carica un JSON Locale**.
   - In qualsiasi momento puoi cliccare sul pulsante **Ricarica Originale** (accanto al nome del file attivo) per tornare a consultare l'archivio principale del sito (`DiacroniaDellaRepubblicaItaliana.json`).

---

### 2️⃣ Come pubblicare la tua ricerca e contribuire tramite Git / GitHub

Se dopo aver strutturato la tua ricerca personale (o dopo aver arricchito l'archivio esistente con nuovi eventi e fonti) desideri **renderla pubblica e metterla a disposizione di tutti**, puoi inviarla al repository tramite **Git / GitHub** in due modi:

#### Metodo A — Direttamente dal browser su GitHub (senza usare il terminale)
Ideale per ricercatori, studenti e contributori che hanno esportato il proprio file `.json` dal sito `github.io`:
1. Esporta il tuo lavoro dal sito cliccando su **⬇️ Scarica JSON** o **📁 Salva in...**.
2. Apri la pagina del repository su GitHub e clicca in alto a destra su **Fork** per creare una copia personale del progetto sul tuo account GitHub.
3. Entra nella cartella [`data/`](data/) del tuo fork:
   - **Per pubblicare una nuova ricerca**: clicca su **Add file &rarr; Upload files** e carica il tuo file `.json` appena esportato.
   - **Per aggiornare l'archivio principale**: apri `data/DiacroniaDellaRepubblicaItaliana.json`, clicca sull'icona della matita (**Edit this file**) e incolla il contenuto del JSON esportato.
   - **Per allegare studi o documenti PDF citati**: entra nella cartella [`Documents/`](Documents/) e carica i relativi file.
4. Clicca su **Commit changes...**, inserisci una breve descrizione del tuo contributo e apri una **Pull Request** verso il repository principale cliccando su **Contribute &rarr; Open pull request**.

#### Metodo B — Tramite Git da riga di comando (terminale)
Per chi preferisce lavorare in locale con `git`:
```bash
# 1. Fai un Fork del repository su GitHub e clona la tua copia in locale
git clone https://github.com/<tuo-username>/DemocrHistory.git
cd DemocrHistory

# 2. Crea un nuovo branch dedicato alla tua ricerca o modifica
git checkout -b ricerca/nome-del-tuo-studio

# 3. Copia il file .json esportato dall'app dentro la cartella data/
#    (ed eventuali documenti PDF/studi dentro Documents/)
cp ~/Scaricati/nome_del_tuo_studio.json data/
cp ~/Scaricati/documento_fonte.pdf Documents/

# 4. Registra e invia le modifiche sul tuo repository GitHub
git add data/ Documents/
git commit -m "Aggiunta ricerca cronologica e documenti: Nome del tuo studio"
git push origin ricerca/nome-del-tuo-studio
```
Dopo il `git push`, apri la pagina del repository su GitHub e clicca sul pulsante **Compare & pull request** per proporre la pubblicazione della tua ricerca a tutti.

---

## 📐 Struttura Semplificata del Database JSON

Il database di DemocrHistory è stato progettato per essere estremamente **essenziale, pulito e facile da compilare** anche per chi non ha competenze informatiche avanzate.

### 📝 Struttura di un evento:

```json
{
  "anno": 1947,
  "titolo": "Strage di Portella della Ginestra",
  "data": "1947-05-01",
  "descrizione": "Il 1 maggio 1947 una manifestazione contadina a [[Portella della Ginestra]] fu colpita da colpi d'arma da fuoco. Morirono 11 persone e decine rimasero ferite. La banda di [[Salvatore Giuliano]] fu indicata come responsabile materiale.",
  "fonti": [
    {
      "Strano Network": "https://www.strano.net/stragi/stragi/crono/crono47.htm"
    }
  ]
}
```

### 🔑 Campi dell'evento:

- **`anno`** *(obbligatorio)*: Anno numerico dell'evento (es. `1947`).
- **`titolo`** *(obbligatorio)*: Nome sintetico dell'evento.
- **`data`** *(opzionale)*: Data specifica in formato stringa (es. `"1947-05-01"`). Se omessa, l'interfaccia mostrerà semplicemente l'anno.
- **`descrizione`** *(obbligatorio)*: Descrizione sintetica dell'evento con link integrati nel testo, per integrare il link in una parola basterà usare le doppie quadre `[[nome_pagina]]`  oppure `[[nome_pagina|testo_alternativo]]`, in questo modo il link verrà creato automaticamente.
- **`fonti`** *(opzionale)*: Lista di oggetti con il nome della fonte e il relativo URL `[ { "Nome Fonte": "https://url.com" } ]`.
- **`categorie`** *(opzionale)*: Lista di una o più categorie dell'evento, es. `"categorie": ["mafia", "politico"]`. Valori ammessi:

  | Valore | Categoria | Colore |
  |---|---|---|
  | `politico` | Politico | 🟢 verde |
  | `servizi_segreti` | Servizi segreti | 🔵 blu |
  | `mafia` | Mafia | ⚫ nero |
  | `gruppi_terroristici` | Gruppi terroristici | 🔴 rosso |
  | `massoneria` | Massoneria | 🟣 viola |
  | `clero` | Clero | ⚪ bianco |
  | `re` | Re | 🟡 giallo |

  Nell'interfaccia le categorie si scelgono dal form di inserimento/modifica e si possono usare per filtrare la timeline.

---

## 🔗 Come inserire i link nella descrizione

Per rendere la creazione dei contenuti semplice ed intuitiva, l'interfaccia supporta diverse modalità di inserimento dei link:

### 1. Wikilink (Scrittura rapida - Consigliato)
Basta racchiudere il nome della voce di Wikipedia tra doppie parentesi quadre:
- `[[Portella della Ginestra]]` &rarr; crea in automatico il link alla pagina Wikipedia `https://it.wikipedia.org/wiki/Portella_della_Ginestra`.
- `[[Salvatore Giuliano|Giuliano]]` &rarr; se vuoi mostrare un testo diverso dal nome della pagina Wikipedia.

### 2. Auto-linking tramite campo `"wikipedia"`
Puoi scrivere il testo in italiano normale senza simboli e aggiungere nell'evento una lista di termini da collegare a Wikipedia:
```json
{
  "anno": 1947,
  "titolo": "Strage di Portella della Ginestra",
  "descrizione": "Una manifestazione contadina a Portella della Ginestra fu colpita...",
  "wikipedia": ["Portella della Ginestra", "Salvatore Giuliano"]
}
```

### 3. Markdown classico
Puoi anche usare il formato Markdown standard: `[testo visibile](https://url.com)`.

### 4. Link a Documenti e Studi Locali (Cartella `Documents/`)
Puoi inserire i tuoi documenti storici, saggi, atti giudiziari o relazioni in formato PDF direttamente nella cartella `Documents/` e richiamarli o linkarli all'interno degli eventi:
- **Nella descrizione**: usa il formato Markdown con il percorso relativo, es. `[Relazione P2](Documents/CommissioneParlamentareDInchiestaSullaP2-1981.pdf)`.
- **Nelle fonti dell'evento**: inserisci il percorso relativo come valore dell'oggetto fonte:
  ```json
  "fonti": [
    { "Commissione P2 (1981)": "Documents/CommissioneParlamentareDInchiestaSullaP2-1981.pdf" }
  ]
  ```
L'interfaccia web riconosce automaticamente i documenti salvati in `Documents/` rendendoli cliccabili e consultabili direttamente dal browser.

---

## 📁 Formati JSON Supportati

L'interfaccia web supporta sia file con la lista classica degli eventi (`"eventi": [...]`), sia file con gli eventi definiti come chiavi singole nel JSON (stile dizionario/schema):

```json
{
  "struttura_file": {
    "titolo": "Cronologia Storica",
    "natura_del_documento": "Raccolta di eventi essenziali."
  },
  "Strage di Portella della Ginestra": {
    "anno": 1947,
    "titolo": "Strage di Portella della Ginestra",
    "data": "1947-05-01",
    "descrizione": "...",
    "fonti": [...]
  },
  "Assassinio di Matteotti": {
    "anno": 1924,
    "titolo": "Assassinio di Matteotti",
    "descrizione": "...",
    "fonti": [...]
  }
}
```

---

## 🖥️ Come funzionano le interfacce HTML (`index.html` e `mobile.html`)

L'applicazione web è progettata secondo un'architettura **zero-dependency** (HTML5, CSS3 e Vanilla JavaScript puro racchiusi in singoli file autonomi, senza framework esterni o fasi di build), con due interfacce dedicate in base al dispositivo che leggono e interpretano gli stessi dati JSON:

- **`index.html` (PC / Desktop – Stile Minimale Cuboide con Tema Chiaro/Scuro)**: pensato per chi apre il sito da computer; offre un layout a tre colonne con barra laterale sinistra per gestione file/opzioni, colonna centrale per ricerca, filtri e timeline interattiva (navigabile anche da tastiera con `Tab` + `Invio`/`Spazio`), e pannello laterale destro fisso per la scheda di dettaglio. Presenta un'estetica minimale e geometrica a spigolo vivo (forme cuboidi, tipografia moderna sans-serif, allineamento numerico tabulare), interamente monocromatica così che **gli unici colori siano quelli delle categorie degli eventi**, con selettore **Tema (`Chiaro` color crema / `Scuro` antracite)** salvato in `localStorage` (`democrhistory_theme`).
- **`mobile.html` (Smartphone)**: pensato per chi apre il sito da telefono; offre un'interfaccia dedicata agli schermi touch con barra di navigazione inferiore a 3 schede (*Timeline*, *Dettaglio*, *Gestione*), filtri categoria scorrevoli orizzontalmente, pulsante flottante (`+`) per l'inserimento rapido e modali a comparsa dal basso (*bottom sheet*).

### 1. Caricamento Dati e Bozze Automatiche (`localStorage`)
- **Avvio intelligente**: all'apertura, l'app verifica prima la presenza di una bozza di lavoro salvata nel browser (`localStorage` con chiave `democrhistory_auto_draft_v2`). Se non è presente alcuna bozza, carica automaticamente l'archivio predefinito `data/DiacroniaDellaRepubblicaItaliana.json` senza occupare spazio in `localStorage` finché l'utente non effettua modifiche.
- **Controllo aggiornamenti (`FNV-1a` hash)**: quando viene creata una bozza locale a partire dal file principale, l'app calcola un'impronta veloce (`hashText`) del JSON originale. Alle aperture successive confronta l'impronta della bozza con quella del file sul server e mostra un avviso se l'archivio originale è stato aggiornato nel frattempo.

### 2. Parser JSON Flessibile e Conservazione dei Dati (`parseArchiveData`)
- **Riconoscimento multi-formato**: il parser accetta indifferentemente archivi strutturati con `PRE-EVENTI` (attivabili dal pannello *Opzioni Timeline*) ed `EVENTI` annidati o a livello radice, sia sotto forma di dizionario `{ "Titolo": { ... } }` sia come lista `[ ... ]`.
- **Normalizzazione categorie**: la funzione `normalizeCategories()` converte automaticamente in ID standard anche eventuali sinonimi scritti a mano nel JSON (es. `politica` &rarr; `politico`, `terrorismo` &rarr; `gruppi_terroristici`, `chiesa`/`vaticano` &rarr; `clero`).
- **Preservazione campi extra (`_rawExtra`)**: se un evento nel JSON contiene proprietà aggiuntive non previste dal form visuale, queste vengono conservate in `_rawExtra` (insieme a `wikipedia` e `link`) e ri-esportate intatte al momento del salvataggio.

### 3. Ricerca, Filtri, Auto-Linking, Sicurezza e Memory Safety
- **Indicizzazione e Caching Memory-Safe con `WeakMap`**:
  - `searchTextCache`: indicizza una sola volta per evento i soli campi testuali ricercabili (`anno`, `data`, `titolo`, `descrizione`, `categorie`, nomi delle `fonti`). La barra di ricerca applica un debounce di `150ms` per mantenere fluida la digitazione.
  - `eventRegexCache` e `renderedEventHtmlCache`: pre-compilano le espressioni regolari dei termini `wikipedia`/`link` e memorizzano nella cache l'HTML già trasformato di titolo e descrizione per ciascun oggetto evento. Poiché le `WeakMap` mantengono riferimenti deboli alle chiavi oggetto, quando un evento viene modificato, eliminato o sostituito dal caricamento di un nuovo archivio, il Garbage Collector del browser libera automaticamente la memoria senza alcun memory leak.
  - **Gestione pulita di File, Blob e DOM**: i listener sono delegati sui contenitori statici (`#timeline`, `#detail`, `#fonti-container`, `#file-status`) evitando di allocare gestori per singola card; i buffer di `FileReader` vengono rilasciati subito dopo il parsing JSON e gli Object URL generati per l'esportazione (`URL.createObjectURL`) vengono revocati automaticamente dopo l'avvio del download.
- **Filtro Categorie e Indicatori Visivi**: i pulsanti categoria filtrano la timeline con logica `OR` (inclusa la voce *Senza categoria*) mostrando il conteggio aggiornato degli eventi corrispondenti alla ricerca attiva. Le card con più categorie generano dinamicamente una barra laterale multicolore (`linear-gradient` CSS).
- **Sicurezza e Sanitizzazione XSS**:
  - Tutti i testi vengono sottoposti a escaping HTML (`escapeHtml`) prima dell'inserimento nel DOM.
  - La funzione `sanitizeUrl()` valida gli URL nei link Markdown `[testo](url)`, nel dizionario `link` e nelle `fonti`, ammettendo esclusivamente protocolli sicuri (`http://`, `https://` o percorsi relativi `/` e `./`) con attributi `target="_blank" rel="noopener noreferrer"`.
  - Tutte le azioni interattive sulle card e sui dettagli usano *event delegation* con ID validati (`/^evt_[a-zA-Z0-9_-]{1,64}$/`), evitando qualsiasi `onclick` inline generato dinamicamente.

### 4. Editor Visuale ed Esportazione (`downloadJSON` e `saveAsJSON`)
- **Gestione completa dal browser**: tramite i modali dedicati è possibile aggiungere o modificare eventi (principali o pre-eventi), associare più categorie e fonti dinamiche, modificare titolo e descrizione dell'archivio, oppure creare un **📄 Nuovo Archivio** che carica automaticamente il template guida di base.
- **Doppio sistema di salvataggio su disco**:
  - **⬇️ Scarica JSON (`downloadJSON`)**: serializza l'archivio ordinato cronologicamente (gestendo eventuali titoli duplicati con suffissi progressivi sulla chiave JSON) e avvia immediatamente il download standard tramite `Blob` nella cartella Download del dispositivo.
  - **📁 Salva in... (`saveAsJSON`)**: utilizza la **File System Access API** (`window.showSaveFilePicker`) per aprire la finestra di dialogo del sistema operativo e permettere all'utente di scegliere esattamente in quale cartella e con quale nome salvare il file `.json` (con fallback automatico per la scelta del nome file sui browser privi di `showSaveFilePicker`).

---

## 📂 Struttura del Repository

```text
DemocrHistory/
├── index.html          # Interfaccia Desktop (stile minimale cuboide con tema Chiaro Crema / Scuro)
├── mobile.html         # Interfaccia Smartphone (navigazione touch a schede)
├── db_template.json    # Modello JSON essenziale per nuovi archivi
├── data/               # Archivi JSON degli eventi storici (es. DiacroniaDellaRepubblicaItaliana.json)
├── Documents/          # Documenti storici, relazioni d'inchiesta, atti declassificati e studi (PDF, saggi)
├── scripts/            # Script Python di supporto per arricchimento e manutenzione del dataset
└── README.md           # Documentazione del progetto
```

---

## 👐 Riepilogo Rapido per Contribuire

1. **Crea o aggiorna una ricerca dal sito (`github.io` o in locale)**: usa **📄 Nuovo Archivio** per partire dal template guida (oppure modifica l'archivio attivo) ed esporta il file con **⬇️ Scarica JSON** o **📁 Salva in...**.
2. **Condividi via Git / GitHub**: carica il tuo file `.json` nella cartella `data/` e apri una **Pull Request** seguendo i passaggi illustrati nella sezione [Come pubblicare la tua ricerca e contribuire tramite Git / GitHub](#-2%EF%B8%8F%E2%83%A3-come-pubblicare-la-tua-ricerca-e-contribuire-tramite-git--github).

---

## 📜 Licenza e Crediti

- **Licenza**: Progetto distribuito sotto licenza Open Source.
- **Ringraziamenti speciali**: A tutti i ricercatori e in particolare a **Strano Network** per la loro preziosa opera di documentazione e storiografia digitale.
