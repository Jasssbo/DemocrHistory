# Regole di Interazione Git — Human in the Loop

## Principio Fondamentale
Nel repository **DemocrHistory**, il controllo di versione è strettamente **Human-in-the-Loop**. L'utente deve poter revisionare, analizzare criticamente e convalidare ogni singolo cambiamento prima che venga registrato nella cronologia Git.

## Direttive per l'Assistente IA / LLM:
1. **Nessun Commit o Push Automatico**: Non eseguire mai in autonomia `git commit` o `git push`.
2. **Trasparenza delle Modifiche**: Dopo aver modificato o creato dei file, riassumi sempre in modo chiaro e puntuale cosa è cambiato.
3. **Proposta del Messaggio di Commit**: Fornisci sempre al termine della risposta il messaggio di commit già strutturato (secondo le convenzioni del progetto) e i relativi comandi `git add` e `git commit` in un blocco di codice copiabile.
4. **Verifica Utente**: Invita l'utente a controllare le differenze (es. con `git diff`) prima di incollare ed eseguire i comandi nel proprio terminale.
