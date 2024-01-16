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

class BankoSaskaita:
    total_accounts = 0

    def __init__(self, savininkas, likutis=0.0):
        self.savininkas = savininkas
        self.likutis = likutis
        BankoSaskaita.total_accounts += 1

    def show_balance(self):
        print(f"Saskaitos likutis paskyros {self.savininkas}: {self.likutis}")

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

saskaita1 = BankoSaskaita("Vladas", likutis=2000.0)
saskaita2 = BankoSaskaita("Kajus", likutis=1000.0)

saskaita1.show_balance()
saskaita2.show_balance()

print(f"Bendras sukurtų sąskaitų skaičius: {BankoSaskaita.get_total_accounts()}")

suma = 600
if BankoSaskaita.validate_amount(suma):
    print(f"Suma {suma} yra teigiamas skaičius.")
else:
    print(f"Suma {suma} nėra teigiamas skaičius.")



