from abc import ABC, abstractmethod
class Document(ABC):
    def __init__(self, taille):
        self.taille = taille

    def afficher_info(self):
        print(self.taille)

    @abstractmethod
    def ouvrir(self):
        pass

    @abstractmethod
    def sauvegarder(self):
        pass

class PDF(Document):
    def __init__(self, taille, auteur):
        super().__init__(taille)
        self.auteur = auteur

    def ouvrir(self):
        print("ouvrir PDF")

    def sauvegarder(self):
        print("sauvegarder PDF")

class Ed_Document(Document, ABC):
    def __init__(self, taille):
        super().__init__(taille)

    def ouvrir(self):
        print("ouvrir Ed_document")

class Word(Ed_document):
    def __init__(self, taille):
        super().__init__(taille)

    def sauvegarder(self):
        print("sauvegarder Word")

class PWP(Ed_document):
    def __init__(self, taille):
        super().__init__(taille)

    def sauvegarder(self):
        print("sauvegarder PWP")