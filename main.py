class Film:
    def __init__(self, T = "", LW = 0):
        self._T = T
        self._LW = LW

    def get_T(self):
        return f"Tytuł: {self._T}"

    def set_T(self, value):
        self._T = value

    def get_LW(self):
        return f"Liczba wypożyczeń: {self._LW}"

    def dodaj_LW(self):
        self._LW += 1

    def __str__(self):
        return f"Tytuł: {self._T}\nLiczba wypożyczeń: {self._LW}"

Obiekt = Film("Jakis Tytuł")
print(Obiekt)
Obiekt.set_T("Inny Tytuł")
print(Obiekt.get_T())
print(Obiekt.get_LW())
Obiekt.dodaj_LW()
print(Obiekt.get_LW())