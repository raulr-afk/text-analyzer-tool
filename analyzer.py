def analizza_testo(testo):
    # Conta i caratteri totali
    caratteri = len(testo)
    
    # Divide il testo in parole e le conta
    parole = testo.split()
    conteggio_parole = len(parole)
    
    # Conta le frasi basandosi sui punti fermi, esclamativi e interrogativi
    frasi = testo.count('.') + testo.count('!') + testo.count('?')
    if frasi == 0 and conteggio_parole > 0:
        frasi = 1  # Almeno una frase se ci sono parole senza punteggiatura
        
    # Calcola la lunghezza media delle parole
    lunghezza_media = caratteri / conteggio_parole if conteggio_parole > 0 else 0

    # Stampa i risultati a schermo
    print("--- RISULTATI DELL'ANALISI ---")
    print(f"Numero di caratteri: {caratteri}")
    print(f"Numero di parole: {conteggio_parole}")
    print(f"Numero di frasi: {frasi}")
    print(f"Lunghezza media delle parole: {lunghezza_media:.2f} caratteri")

# Testiamo il programma con una frase di esempio
testo_esempio = "Benvenuti nel mio primo progetto GitHub! Questo script analizza il testo in modo automatico. Python è fantastico."
print(f"Testo analizzato: '{testo_esempio}'\n")
analizza_testo(testo_esempio)
