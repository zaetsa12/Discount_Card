import random


class DiscountCard:

    def __init__(self, card_number, discount, date, suma):
        self.__card_number = card_number
        self.__discount = discount
        self.__date = date
        self.__suma = suma

    def card_info(self):
        print("Card number:", self.__card_number, ", Discount:",
              self.__discount, "%, ", "Date:", self.__date)

    @property
    def suma(self):
        return self.__suma

    @property
    def discount(self):
        return self.__discount

    @suma.setter
    def suma(self, add_suma):
        if float(add_suma) > 0:
            self.__suma += add_suma

            print("You have:", int(
                add_suma - ((add_suma * buy.discount)/100)), "UAH")
            self.__discount = self.__suma // 1000
            print("Your discount is:", int(
                (add_suma * self.__discount)/100), "UAH")
            print('Discount :', self.__discount)
            print("You need :",
                  1000 - self.__suma % 1000, "UAH to the next discount")


buy = DiscountCard(random.randint(100000000, 999999999), 1, "20/02/2018", 0)

while buy.suma <= 10000:
    print("==============================================")
    buy.card_info()
    print("==============================================")
    buy.suma = float(input("Enter your suma: "))
