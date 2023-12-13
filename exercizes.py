                        # Exercizes
                        # Task 1

class Skaiciuokle:
    def __init__(self, skaicius1, skaicius2):
        self.skaicius1 = skaicius1
        self.skaicius2 = skaicius2

    def sudeti(self):
        return self.skaicius1 + self.skaicius2

    def atimti(self):
        return self.skaicius1 - self.skaicius2

    def dauginti(self):
        return self.skaicius1 * self.skaicius2

    def dalinti(self):
        if self.skaicius2 != 0:
            return self.skaicius1 / self.skaicius2
        else:
            return "Dalyba iš nulio negalima"

# Inicijuojame skaičiuoklės objektą
sk = Skaiciuokle(10, 5)

# Atlikti skaičiavimus
print("Suma:", sk.sudeti())
print("Skirtumas:", sk.atimti())
print("Sandauga:", sk.dauginti())
print("Dalyba:", sk.dalinti())


                        # Task 2


class Darbuotojas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

    def visu_vardas(self):
        return f"{self.vardas} {self.pavarde}"

    def el_pastas(self):
        return f"{self.vardas.lower()}.{self.pavarde.lower()}@company.com"

# Sukuriame Darbuotojas objektus
darbuotojas1 = Darbuotojas("Jonas", "Jonaitis")
darbuotojas2 = Darbuotojas("Petras", "Petraitis")

# Išspausdiname visus vardus ir el. paštus
print("Pirmo darbuotojo vardas ir pavardė:", darbuotojas1.visu_vardas())
print("Pirmo darbuotojo el. paštas:", darbuotojas1.el_pastas())

print("Antro darbuotojo vardas ir pavardė:", darbuotojas2.visu_vardas())
print("Antro darbuotojo el. paštas:", darbuotojas2.el_pastas())


                        # Task 3


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return "Title: " + self.title

    def get_author(self):
        return "Author: " + self.author

# Instantiate Book objects
PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamlet", "William Shakespeare")
WP = Book("War and Peace", "Leo Tolstoy")

# Accessing attributes and methods
print(PP.title)  # Output: "Pride and Prejudice"
print(H.author)  # Output: "William Shakespeare"
print(WP.get_title())  # Output: "Title: War and Peace"
print(PP.get_author())  # Output: "Author: Jane Austen"
