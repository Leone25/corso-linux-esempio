'''
Script principale per interagire con il sistema di gestione della biblioteca.
Permette all'utente di aggiungere, rimuovere, cercare e visualizzare libri.
'''
from libro import Libro
from biblioteca import Biblioteca

def mostra_menu():
    """Mostra il menu delle opzioni all'utente."""
    print("\n--- Menu Biblioteca ---")
    print("1. Aggiungi un nuovo libro")
    print("2. Rimuovi un libro")
    print("3. Cerca un libro")
    print("4. Mostra tutti i libri")
    print("5. Esci")
    print("-----------------------")

def input_libro():
    """Richiede all'utente i dettagli di un nuovo libro."""
    while True:
        try:
            titolo = input("Inserisci il titolo del libro: ").strip()
            if not titolo:
                raise ValueError("Il titolo non può essere vuoto.")
            autore = input("Inserisci l'autore del libro: ").strip()
            if not autore:
                raise ValueError("L'autore non può essere vuoto.")
            
            while True:
                try:
                    anno_str = input("Inserisci l'anno di pubblicazione: ").strip()
                    anno_pubblicazione = int(anno_str)
                    if anno_pubblicazione <= 0:
                        raise ValueError("L'anno deve essere un numero positivo.")
                    break
                except ValueError as e:
                    print(f"Errore: {e}. Riprova.")

            genere = input("Inserisci il genere del libro: ").strip()
            if not genere:
                raise ValueError("Il genere non può essere vuoto.")
            
            return Libro(titolo, autore, anno_pubblicazione, genere)
        except ValueError as e:
            print(f"Errore nell'input: {e}. Riprova.")
        except Exception as e:
            print(f"Errore imprevisto: {e}. Riprova.")

def main():
    """Funzione principale per eseguire l'applicazione della biblioteca."""
    with Biblioteca() as biblio: # Usa il context manager per salvare automaticamente all'uscita
        while True:
            mostra_menu()
            scelta = input("Scegli un'opzione (1-5): ").strip()

            if scelta == '1':
                try:
                    nuovo_libro = input_libro()
                    if nuovo_libro:
                        biblio.aggiungi_libro(nuovo_libro)
                except ValueError as e:
                    print(f"Errore: {e}")
                except TypeError as e:
                    print(f"Errore: {e}")
                except Exception as e:
                    print(f"Errore imprevisto durante l'aggiunta del libro: {e}")

            elif scelta == '2':
                titolo_da_rimuovere = input("Inserisci il titolo del libro da rimuovere: ").strip()
                if titolo_da_rimuovere:
                    biblio.rimuovi_libro(titolo_da_rimuovere)
                else:
                    print("Il titolo non può essere vuoto.")

            elif scelta == '3':
                query = input("Inserisci il termine di ricerca: ").strip()
                if not query:
                    print("Il termine di ricerca non può essere vuoto.")
                    continue
                
                criterio_input = input("Cerca per (titolo, autore, genere) [default: titolo]: ").strip().lower()
                if criterio_input not in ['titolo', 'autore', 'genere', '']:
                    print("Criterio non valido. Uso 'titolo' come default.")
                    criterio = 'titolo'
                elif criterio_input == '':
                    criterio = 'titolo'
                else:
                    criterio = criterio_input
                
                risultati = biblio.cerca_libro(query, criterio)
                if risultati:
                    print(f"\n--- Risultati della Ricerca ({criterio}: '{query}') ---")
                    for i, libro in enumerate(risultati):
                        print(f"\nLibro #{i+1}:")
                        print(libro)
                    print("--------------------------------------------")
                else:
                    print(f"Nessun libro trovato per '{query}' nel criterio '{criterio}'.")

            elif scelta == '4':
                biblio.mostra_tutti_i_libri()

            elif scelta == '5':
                print("Grazie per aver usato la Biblioteca. Arrivederci!!!!!")
                break
            else:
                print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
