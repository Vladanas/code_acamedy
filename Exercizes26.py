                             # Exercizes 26

                             # Task 1

# class Faktorialas:
#     @classmethod
#     def skaiciuoti_faktoriala(cls, n):
#         if n < 0:
#             raise ValueError
#         elif n == 0 or n == 1:
#             return 1
#         else:
#             faktorialas = 1
#             for i in range(2, n + 1):
#                 faktorialas *= i
#             return faktorialas
#
# skaicius = 5
# rezultatas = Faktorialas.skaiciuoti_faktoriala(skaicius)
# print(f"{skaicius} faktorialas yra {rezultatas}")


                        # Task 2

# class Atvirkstinimas:
#     @classmethod
#     def atvirkstinti_eilute(cls, eilute):
#         return eilute[::-1]
#
# pradinė_eilutė = "Vladislav Devgut"
# atvirkstinė_eilutė = Atvirkstinimas.atvirkstinti_eilute(pradinė_eilutė)
# print(f"Pradinė eilutė: {pradinė_eilutė}")
# print(f"Atvirkštinė eilutė: {atvirkstinė_eilutė}")


                        # Task 3

# class BankAccount:
#     skaicius_saskaitu = 0
#
#     def __init__(self, savininkas, pradinis_balansas=0):
#         self.savininkas = savininkas
#         self.balansas = pradinis_balansas
#
#         BankAccount.skaicius_saskaitu += 1
#
#     def ideti_pinigus(self, suma):
#         self.balansas += suma
#         print(f"{self.savininkas}, įskaityta {suma} į sąskaitą. Naujas balansas: {self.balansas}")
#
#     def isimti_pinigus(self, suma):
#         if suma <= self.balansas:
#             self.balansas -= suma
#             print(f"{self.savininkas}, išsiimta {suma} iš sąskaitos. Naujas balansas: {self.balansas}")
#         else:
#             print(f"{self.savininkas}, nepakanka lėšų sąskaitoje. Operacija neįvyko.")
#
#     @classmethod
#     def bendras_saskaitu_skaicius(cls):
#         return cls.skaicius_saskaitu
#
#     @staticmethod
#     def banko_informacija():
#         return "SEB BANKAS."
#
# saskaita1 = BankAccount("Vladas", pradinis_balansas=9000)
# saskaita2 = BankAccount("Deividas", pradinis_balansas=10000)
#
# saskaita1.ideti_pinigus(2650)
# saskaita2.isimti_pinigus(4560)
#
# print(f"Bendras sukurtų sąskaitų skaičius: {BankAccount.bendras_saskaitu_skaicius()}")
# print(BankAccount.banko_informacija())


                        # Exercizes 2

# class BankoSaskaita:
#     total_accounts = 0
#
#     def __init__(self, savininkas, likutis=0.0):
#         self.savininkas = savininkas
#         self.likutis = likutis
#         BankoSaskaita.total_accounts += 1
#
#     def show_balance(self):
#         print(f"Saskaitos likutis paskyros {self.savininkas}: {self.likutis}")
#
#     @classmethod
#     def get_total_accounts(cls):
#         return cls.total_accounts
#
#     @staticmethod
#     def validate_amount(amount):
#         return isinstance(amount, (int, float)) and amount > 0
#
# saskaita1 = BankoSaskaita("Vladas", likutis=2000.0)
# saskaita2 = BankoSaskaita("Kajus", likutis=1000.0)
#
# saskaita1.show_balance()
# saskaita2.show_balance()
#
# print(f"Bendras sukurtų sąskaitų skaičius: {BankoSaskaita.get_total_accounts()}")
#
# suma = 600
# if BankoSaskaita.validate_amount(suma):
#     print(f"Suma {suma} yra teigiamas skaičius.")
# else:
#     print(f"Suma {suma} nėra teigiamas skaičius.")


                            # Exercizes 3

# class BankoSaskaita:
#     total_accounts = 0
#
#     def __init__(self, savininkas, likutis=0.0):
#         self.savininkas = savininkas
#         self.likutis = likutis
#         BankoSaskaita.total_accounts += 1
#
#     def show_balance(self):
#         print(f"Sąskaitos likutis paskyrai {self.savininkas}: {self.likutis}")
#
#     @classmethod
#     def get_total_accounts(cls):
#         return cls.total_accounts
#
#     @staticmethod
#     def validate_amount(amount):
#         return isinstance(amount, (int, float)) and amount > 0
#
# # Sukurkime bent du banko sąskaitos egzempliorius su skirtingais savininkais ir likučiais.
# saskaita1 = BankoSaskaita("Vladas", likutis=500.0)
# saskaita2 = BankoSaskaita("Kajus", likutis=1000.0)
#
# # Naudokime egzempliorių metodą show_balance
# saskaita1.show_balance()
# saskaita2.show_balance()
#
# # Naudokime klasės metodą get_total_accounts
# print(f"Bendras sukurtų sąskaitų skaičius: {BankoSaskaita.get_total_accounts()}")
#
# # Naudokime statinį metodą validate_amount
# suma_teigiama = 200
# suma_neigiama = -50
#
# if BankoSaskaita.validate_amount(suma_teigiama):
#     print(f"Suma {suma_teigiama} yra teigiamas skaičius.")
# else:
#     print(f"Suma {suma_teigiama} nėra teigiamas skaičius.")
#
# if BankoSaskaita.validate_amount(suma_neigiama):
#     print(f"Suma {suma_neigiama} yra teigiamas skaičius.")
# else:
#     print(f"Suma {suma_neigiama} nėra teigiamas skaičius.")


                                    # Exercizes 4


# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Pridėta ${amount:.2f}. Naujas balansas: ${self.balance:.2f}")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Nepakanka lėšų.")
#         else:
#             self.balance -= amount
#             print(f"Išimta ${amount:.2f}. Naujas balansas: ${self.balance:.2f}")
#
#     @classmethod
#     def from_balance(cls, initial_balance):
#         new_account = cls()
#         new_account.balance = initial_balance
#         return new_account
#
#     @staticmethod
#     def transfer(account1, account2, amount):
#         if amount > account1.balance:
#             print("Perdavimo suma viršija sąskaitos likutį.")
#         else:
#             account1.balance -= amount
#             account2.balance += amount
#             print(f"Perdavimas sėkmingas. {account1.balance:.2f} -> {account2.balance:.2f}")
#
# # Sukurkime banko sąskaitas
# account1 = BankAccount()
# account2 = BankAccount()
#
# # Demonstruokime indėlį ir išėmimą
# account1.deposit(1000)
# account1.withdraw(400)
#
# # Sukurkime naują sąskaitą su pradiniu likučiu
# account3 = BankAccount.from_balance(900)
#
# # Demonstruokime pervedimą
# BankAccount.transfer(account1, account2, 50)
#
# # Patikrinkime likutį visose sąskaitose
# print("Balansas account1:", account1.balance)
# print("Balansas account2:", account2.balance)
# print("Balansas account3:", account3.balance)


                                # Exercizes 5

class SpaceStation:
    def __init__(self):
        self.astronautai = []

    def add_astronaut(self, vardas, tautybe, misijos_trukme):
        astronautas = {"vardas": vardas, "tautybe": tautybe, "misijos_trukme": misijos_trukme}
        self.astronautai.append(astronautas)

    def find_astronaut(self, vardas):
        for astronautas in self.astronautai:
            if astronautas["vardas"] == vardas:
                return astronautas
        return None

    @classmethod
    def from_astronaut_list(cls, astronautu_sarasas):
        nauja_stotis = cls()
        nauja_stotis.astronautai = astronautu_sarasas
        return nauja_stotis

    @staticmethod
    def is_long_term_mission(astronautas):
        return astronautas["misijos_trukme"] > 6

    def remove_astronaut(self, vardas):
        for astronautas in self.astronautai:
            if astronautas["vardas"] == vardas:
                self.astronautai.remove(astronautas)
                print(f"Astronautas {vardas} pašalintas.")
                return
        print(f"Astronautas {vardas} nerastas.")

# Sukurkime SpaceStation egzempliorių
stotis = SpaceStation()

# Pridėkime astronautus
stotis.add_astronaut("Neil Armstrong", "JAV", 12)
stotis.add_astronaut("Yuri Gagarin", "SSSR", 8)

# Raskime astronautą
astronautas = stotis.find_astronaut("Neil Armstrong")
print(astronautas)

# Patikrinkime ilgalaikių misijų sąlygą
print(SpaceStation.is_long_term_mission(astronautas))

# Šaliname astronautą
stotis.remove_astronaut("Neil Armstrong")

# Sukurkime SpaceStation egzempliorių iš esamo astronautų sąrašo
kiti_astronautai = [
    {"vardas": "Buzz Aldrin", "tautybe": "JAV", "misijos_trukme": 10},
    {"vardas": "Valentina Tereshkova", "tautybe": "SSSR", "misijos_trukme": 7}
]
nauja_stotis = SpaceStation.from_astronaut_list(kiti_astronautai)
print(nauja_stotis.astronautai)








