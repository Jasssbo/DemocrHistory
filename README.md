# Guida per creare una versione personale del JSON storico

Questo documento spiega come costruire una versione personale del database storico in modo coerente, leggibile e facili da aggiornare. L'obiettivo non e' inventare un archivio arbitrario, ma mantenere una struttura uniforme che possa essere usata da una timeline, da schede di dettaglio, da filtri e da mappe.

## 1. Principio generale

Il JSON deve descrivere eventi storici come unità autonome, ordinate cronologicamente e annotate con lo stesso livello di precisione. Ogni evento deve essere comprensibile anche senza dover leggere il resto del file.

Le regole chiave sono:

- ogni evento ha un identificatore stabile;
- il titolo e la descrizione devono essere chiari e neutrali;
- data, luogo, attori, classificazione e stato della ricostruzione sono separati;
- le interpretazioni e le accuse non devono essere presentate come fatti accertati;
- i collegamenti tra eventi devono usare riferimenti espliciti, non solo testo libero.

## 2. Struttura del file

Il file principale contiene una struttura a più livelli:

```json
{
  "titolo": "",
  "lingua": "it",
  "natura_del_documento": "",
  "nota_metodologica": "",
  "specifica_database": {
    "unita_principale": "evento_storico",
    "principi": [],
    "campi_evento": {},
    "viste_gui_consigliate": []
  },
  "distinzioni_utili_per_descrivere_i_documenti": {
    "periodo": "",
    "tipo_di_fatto": [],
    "scala": [],
    "attori": [],
    "ruolo_degli_attori": [],
    "stato_della_ricostruzione": [],
    "relazioni": []
  },
  "attori_e_sigle": {
    "partiti_e_movimenti": [],
    "istituzioni_e_servizi": [],
    "organizzazioni_e_reti": [],
    "persone_citate": []
  },
  "eventi": [
    {
      "anno": 0,
      "titolo": "",
      "data": {
        "inizio": "AAAA-MM-GG",
        "fine": "AAAA-MM-GG",
        "precisione": "anno"
      },
      "luogo": {
        "nome": "",
        "paese": "",
        "coordinate": null
      },
      "descrizione": "",
      "dati_concreti": [],
      "responsabili_o_attori": [
        {
          "nome": "",
          "ruolo": ""
        }
      ],
      "entita_coinvolte": [],
      "tipo_di_fatto": [],
      "scala": "",
      "stato_della_ricostruzione": "",
      "wikilinks": {},
      "fonti": []
    }
  ]
}
```

## 3. Ordine delle informazioni dentro ogni evento

Per evitare confusione e garantire compatibilità con filtri e viste grafiche, seguire lo stesso ordine di campi per tutti gli eventi. L'ordine consigliato e':

1. `anno`
2. `titolo`
3. `data`
4. `luogo`
5. `descrizione`
6. `dati_concreti`
7. `responsabili_o_attori`
8. `entita_coinvolte`
9. `tipo_di_fatto`
10. `scala`
11. `stato_della_ricostruzione`
12. `wikilinks`
13. `fonti`

Questo ordine rende il file più facile da leggere a colpo d'occhio e aiuta le interfacce a mostrare in modo naturale la timeline, la scheda dell'evento e i filtri.

## 4. Criteri per i campi principali

### 4.1 `anno` e `data`

- `anno` e il riferimento rapido per ordinare la timeline.
- `data.inizio` e `data.fine` vanno usati solo quando si hanno date precise o un intervallo noto.
- `precisione` deve indicare il livello di certezza:
  - `giorno`
  - `mese`
  - `anno`
  - `intervallo`

Esempio:

```json
"data": {
  "inizio": "1943-09-03",
  "fine": "1943-09-08",
  "precisione": "giorno"
}
```

Se l'evento e molto generico, usare un anno e lasciare `inizio` e `fine` come `null` oppure come anno completo, ma mantenere la precisione coerente.

### 4.2 `titolo` e `descrizione`

- `titolo` deve essere breve, chiaro e identificabile in una timeline.
- `descrizione` deve essere un riassunto neutro, senza opinioni personali.
- Evitare formule troppo lunghe e troppo interpretative.

### 4.3 `luogo`

Il campo `luogo` va scritto in modo strutturato:

```json
"luogo": {
  "nome": "Roma",
  "paese": "Italia",
  "coordinate": null
}
```

- `nome` e il nome leggibile del luogo;
- `paese` indica l'area storica o il contesto politico;
- `coordinate` e opzionale e va usato solo se realmente si hanno dati geografici affidabili.

### 4.4 `responsabili_o_attori` e `entita_coinvolte`

Gli attori vanno registrati come oggetti con nome e ruolo, non come stringhe libere.

```json
"responsabili_o_attori": [
  { "nome": "Pietro Badoglio", "ruolo": "attore istituzionale" },
  { "nome": "Governo italiano", "ruolo": "istituzione coinvolta" }
]
```

`entita_coinvolte` invece e una lista semplificata di nomi, utile per filtri e ricerche veloci.

### 4.5 `tipo_di_fatto` e `scala`

`tipo_di_fatto` deve usare una tassonomia costante. Ad esempio:

- `politico-istituzionale`
- `sociale-economico`
- `violenza politica o strage`
- `servizi segreti e apparati dello Stato`
- `mafia e criminalita organizzata`
- `massoneria e rapporti con la Chiesa`
- `politica internazionale e Guerra fredda`
- `inchiesta giudiziaria o parlamentare`
- `cultura e societa civile`

`scala` invece deve essere una tra:

- `locale`
- `nazionale`
- `internazionale`

### 4.6 `stato_della_ricostruzione`

Questo campo e fondamentale. Serve a distinguere fatti documentati da interpretazioni, accuse o ipotesi. Un buon valore deve evidenziare il grado di certezza senza trasformare un'ipotesi in un fatto stabilito.

Valori consigliati:

- `evento documentato`
- `tesi storica da verificare`
- `responsabilita controversa`
- `informazione incompleta`
- `sintesi interpretativa`

### 4.7 `dati_concreti` e `fonti`

`dati_concreti` contiene fatti verificabili o frasi dettagliate che supportano la voce. `fonti` deve contenere le fonti documentarie o storiografiche in modo strutturato, separate dai collegamenti informativi.

Le fonti non devono essere confuse con i `wikilinks`, che servono solo come introduzione e non come prova.

### 4.8 `wikilinks`

`wikilinks` e un oggetto di collegamenti utili, con etichetta e URL. Esempio:

```json
"wikilinks": {
  "Massoneria": "https://it.wikipedia.org/wiki/Massoneria",
  "Napoleone": "https://it.wikipedia.org/wiki/Napoleone_Bonaparte"
}
```

Questi link devono essere introduttivi e non sostituire le fonti principali.

## 5. Criteri di qualità del contenuto

Per creare una versione personale, rispettare queste regole:

1. Mantieni un linguaggio neutro e storico.
2. Separare fatti, interpretazioni e accuse.
3. Non inventare attori, date o collegamenti se non sono supportati.
4. Usa sempre la stessa terminologia per tipi di fatto, attori e gradi di certezza.
5. Mantieni una cronologia coerente, cioe gli eventi vanno ordinati per anno e, quando possibile, per data di inizio.
6. Non mescolare elementi di livello diverso nello stesso campo.
7. Se un evento e controverso, lo si marca esplicitamente nello stato della ricostruzione.

## 6. Come creare una versione personale

### Passo 1: copiare la struttura di base

Copia la struttura del file principale e mantieni identici i nodi principali:

- `titolo`
- `lingua`
- `natura_del_documento`
- `nota_metodologica`
- `specifica_database`
- `distinzioni_utili_per_descrivere_i_documenti`
- `attori_e_sigle`
- `eventi`

### Passo 2: personalizzare il contenuto

Decidi quali eventi vuoi includere, aggiungere o rimuovere. La chiave e' mantenere la stessa logica di classificazione e la stessa struttura del record.

### Passo 3: preservare la coerenza dei vocaboli

Se usi un nuovo tipo di fatto, aggiungilo anche in `distinzioni_utili_per_descrivere_i_documenti.tipo_di_fatto` e usa lo stesso nome in tutti gli eventi.

### Passo 4: mantenere l'ordine cronologico

La lista `eventi` deve essere ordinata in senso cronologico, dal piu' antico al piu' recente. Se un evento non ha data certa, va inserito con la precisione piu' bassa possibile e marcato nel campo `stato_della_ricostruzione`.

### Passo 5: verificare la leggibilita'

Prima di salvare il file, controlla che:

- ogni evento abbia titolo, anno e descrizione;
- ogni attore abbia un ruolo;
- i tipi di fatto siano sempre usati nello stesso modo;
- la struttura dei campi rimanga costante.

## 7. Esempio di evento ben costruito

```json
{
  "anno": 1945,
  "titolo": "Fine dell'OSS",
  "data": {
    "inizio": "1945-09-20",
    "fine": "1945-09-20",
    "precisione": "giorno"
  },
  "luogo": {
    "nome": "Stati Uniti",
    "paese": "USA",
    "coordinate": null
  },
  "descrizione": "L'Office of Strategic Services fu sciolto il 20 settembre 1945.",
  "dati_concreti": [
    "Scioglimento dell'OSS: 20 settembre 1945.",
    "La CIA fu istituita nel 1947."
  ],
  "responsabili_o_attori": [
    { "nome": "OSS", "ruolo": "organizzazione sciolta" },
    { "nome": "CIA", "ruolo": "organizzazione successiva" }
  ],
  "entita_coinvolte": ["USA", "OSS", "CIA"],
  "tipo_di_fatto": [
    "servizi segreti e apparati dello Stato",
    "politica internazionale e Guerra fredda"
  ],
  "scala": "internazionale",
  "stato_della_ricostruzione": "evento documentato",
  "wikilinks": {
    "OSS": "https://it.wikipedia.org/wiki/Office_of_Strategic_Services"
  },
  "fonti": []
}
```

## 8. Regola pratica finale

Se vuoi creare una versione personale, non partire da zero con categorie libere. Parti dalla struttura esistente, mantieni lo stesso ordine, gli stessi nomi e la stessa logica di classificazione, poi sostituisci i contenuti con i tuoi eventi, attori e documenti.

In questo modo il JSON resta leggibile, comparabile e facilmente integrabile con una UI come timeline, scheda dettagliata, filtro e mappa.
