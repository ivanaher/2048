class Kvadratic(object):
    #kljuc je broj, a vrijednosti su (vrijednost, boja)
    __kvadratic_info = {1: (2, 'bijela')
                        2: (4, 'bez')
                        3: (8, 'njezno narancasta')
                        4: (16, 'narancata')
                        5: (32, 'roza')
                        6: (64, 'crvena')
                        7: (128, 'zuta')}
    @staticmethod
    def brojevi():
        return Kvadratic.__kvadratic_info.keys()

    def __init__(self, broj):
        self.__broj = broj

    @property
    def broj(self):
        return self.__broj

    def vrijednost(self):
        return Kvadratic.__kvadratic_info[self.__broj][0]

    def boja(self):
        return Kvadratic.__kvadratic_info[self.__broj][1]

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r, %r)' %(self.__broj, self.__vrijednost, self.__boja)

    @staticmethod
    def jeJaci(vrijednost, kvadratPrvi, kvadratDrugi):
        if(kvadratPrvi.vrijednost == vrijednsot and kvadratDrugi.vrijednost == vrijednost):
            return kvadratPrvi.vrijednost > kvadratDrugi.vrijednost
        elif(kvadratPrvi.vrijednost != vrijednost and kvadratDrugi.vrijednost == vrijednost):
            return False
        elif kvadratPrvi.vrijednost == vrijednost and kvadratDrugi.vrijednost != vrijednost:
            return True
        elif(kvadratPrvi.vrijednost == kvadratDrugi.vrijednost):
            return kvadratPrvi.vrijednost > kvadratDrugi.vrijednost
        return True
    
    
    def __str__(self):
        return self.boja.title() + ' ' + self.broj
for vrijednost in Kvadratic.brojevi():
    for broj in Kvadratic.brojevi():
        k = Kvadratic(broj, boja)
        print('%r %s %d %d' % (k, k, , k.broj, k.boja))


class Ploca(object):
    def __init__(self):
        self.__kvadratici = []
        for vrijednost in Kvadratic.vrijednost():
            for broj in Kvadratic.broj():
                self.__kvadratici.append(Kvadratic(broj, vrijednost))

    def __str__(self, red = 4, velicina = 4):
        return '\n'.join(''.join(str(kvadratic).ljust(velicina, ' ') for kvadratic in self.__kvadratici[i:i+red])for i in range(0, len(self.__kvadratici), red)) + '\n'

    def dajNoviKvadratic(self, broj_kvadratica = 1):
        daniKvadratici = []
        while broj_kvadratica > 0:
            daniKvadratici.append(Self.__kvadratici.pop())
            broj_kvadratica -= 1
        return daniKvadratici
class Igrac(object):
    def __init__(self, ime):
        self.__ime = ime
        self.__kvadraticiZaSpajanje = []
        self.__dobiveniKvadratici = []

    @property
    def ime(Self):
        return self.__ime

    @property
    def kvadraticiZaSpajanje():
        return self.__kvadraticiZaSpajanje

    @kvadraticiZaSpajanje.setter
    def kvadraticiZaSpajanje(self, value):
        self.__kvadraticiZaSpajanje = value

    def spojiKvadratice(izbor):
        kvadratic = self.__kvadraticiZaSpajanje.pop(izbor)
        return karta

    def imaKvadraticaZaSpajanje(self):
        return len(self.__kvadraticiZaSpajanje) > 0

    def __str__(self):
        return "Igrač" + self.__ime

class PrikazIgre(object):
    def prikaziPocetakIgre(self):
        print('-' * 20 + "2048" + '-' * 20)

    def odabirIgre(self):
        igra = input("Ako želite nastaviti prethodnu igr unesite da: ")
        
