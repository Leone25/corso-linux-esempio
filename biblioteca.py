'''
Gestisce una collezione di libri, permettendo operazioni CRUD e di ricerca.
'''
import json
from libro import Libro # Assumendo che la classe Libro sia in libro.py

class Biblioteca:
    def __init__(self, file_salvataggio='biblioteca.json'):
        """
        Inizializza una nuova Biblioteca, caricando i dati da un file se esiste.

        Args:
            file_salvataggio (str): Il nome del file JSON per salvare e caricare i dati.
        """
        self.libri = []
        self.file_salvataggio = file_salvataggio
        self._carica_libri()

    def aggiungi_libro(self, libro):
        """
        Aggiunge un libro alla biblioteca, evitando duplicati.

        Args:
            libro (Libro): L'oggetto Libro da aggiungere.

        Raises:
            ValueError: Se il libro è già presente nella biblioteca.
        """
        if not isinstance(libro, Libro):
            raise TypeError("Puoi aggiungere solo oggetti di tipo Libro.")
        if libro in self.libri:
            raise ValueError(f"Il libro '{libro.titolo}' è già presente nella biblioteca.")
        self.libri.append(libro)
        print(f"Libro '{libro.titolo}' aggiunto con successo.")

    def rimuovi_libro(self, titolo_libro):
        """
        Rimuove un libro dalla biblioteca dato il suo titolo.

        Args:
            titolo_libro (str): Il titolo del libro da rimuovere.

        Returns:
            bool: True se il libro è stato rimosso, False altrimenti.
        """
        titolo_libro_lower = titolo_libro.lower()
        libro_da_rimuovere = None
        for libro in self.libri:
            if libro.titolo.lower() == titolo_libro_lower:
                libro_da_rimuovere = libro
                break
        
        if libro_da_rimuovere:
            self.libri.remove(libro_da_rimuovere)
            print(f"Libro '{titolo_libro}' rimosso con successo.")
            return True
        else:
            print(f"Libro '{titolo_libro}' non trovato.")
            return False

    def cerca_libro(self, query, criterio='titolo'):
        """
        Cerca libri nella biblioteca in base a un criterio (titolo, autore, genere).

        Args:
            query (str): La stringa di ricerca.
            criterio (str): Il criterio di ricerca ('titolo', 'autore', 'genere').

        Returns:
            list: Una lista di oggetti Libro che corrispondono alla ricerca.
        """
        query_lower = query.lower()
        risultati = []
        for libro in self.libri:
            if criterio == 'titolo' and query_lower in libro.titolo.lower():
                risultati.append(libro)
            elif criterio == 'autore' and query_lower in libro.autore.lower():
                risultati.append(libro)
            elif criterio == 'genere' and query_lower in libro.genere.lower():
                risultati.append(libro)
        return risultati

    def mostra_tutti_i_libri(self):
        """
        Mostra tutti i libri presenti nella biblioteca.
        """
        if not self.libri:
            print("La biblioteca è vuota.")
            return
        print("\n--- Elenco Libri nella Biblioteca ---")
        for i, libro in enumerate(self.libri):
            print(f"\nLibro #{i+1}:")
            print(libro)
        print("-------------------------------------")

    def _salva_libri(self):
        """
        Salva lo stato corrente della biblioteca su un file JSON.
        """
        try:
            with open(self.file_salvataggio, 'w', encoding='utf-8') as f:
                json.dump([libro.to_dict() for libro in self.libri], f, indent=4, ensure_ascii=False)
            # print(f"Biblioteca salvata in {self.file_salvataggio}")
        except IOError as e:
            print(f"Errore durante il salvataggio della biblioteca: {e}")

    def _carica_libri(self):
        """
        Carica lo stato della biblioteca da un file JSON, se esiste.
        """
        try:
            with open(self.file_salvataggio, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.libri = [Libro.from_dict(item) for item in data]
            # print(f"Biblioteca caricata da {self.file_salvataggio}")
        except FileNotFoundError:
            # print(f"File {self.file_salvataggio} non trovato. Inizio con una biblioteca vuota.")
            pass # Il file non esiste ancora, va bene
        except json.JSONDecodeError:
            print(f"Errore nel decodificare {self.file_salvataggio}. Inizio con una biblioteca vuota.")
            self.libri = [] # Resetta se il file è corrotto
        except Exception as e:
            print(f"Errore imprevisto durante il caricamento da {self.file_salvataggio}: {e}")
            self.libri = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._salva_libri()
