'''
definisce la classe Libro
'''

class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione, genere):
        """
        Inizializza un nuovo oggetto Libro.

        Args:
            titolo (str): Il titolo del libro.
            autore (str): L'autore del libro.
            anno_pubblicazione (int): L'anno di pubblicazione del libro.
            genere (str): Il genere del libro.
        """
        if not isinstance(titolo, str) or not titolo:
            raise ValueError("Il titolo non può essere vuoto.")
        if not isinstance(autore, str) or not autore:
            raise ValueError("L'autore non può essere vuoto.")
        if not isinstance(anno_pubblicazione, int) or anno_pubblicazione <= 0:
            raise ValueError("L'anno di pubblicazione deve essere un intero positivo.")
        if not isinstance(genere, str) or not genere:
            raise ValueError("Il genere non può essere vuoto.")

        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione
        self.genere = genere

    def __str__(self):
        """
        Restituisce una rappresentazione stringa del libro.
        """
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nAnno: {self.anno_pubblicazione}\nGenere: {self.genere}"

    def __eq__(self, other):
        """
        Verifica se due oggetti Libro sono uguali basandosi su titolo e autore.
        """
        if not isinstance(other, Libro):
            return False
        return self.titolo.lower() == other.titolo.lower() and \
               self.autore.lower() == other.autore.lower()

    def to_dict(self):
        """
        Converte l'oggetto Libro in un dizionario.
        """
        return {
            'titolo': self.titolo,
            'autore': self.autore,
            'anno_pubblicazione': self.anno_pubblicazione,
            'genere': self.genere
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea un oggetto Libro da un dizionario.
        """
        return cls(data['titolo'], data['autore'], data['anno_pubblicazione'], data['genere'])
