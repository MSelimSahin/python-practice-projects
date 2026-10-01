# from menu import Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()
#
#

#
# is_on = True
#
# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink):
#             if money_machine.make_payment(drink.cost):
#                 coffee_maker.make_coffee(drink)
#







# is_on = True
#
# while is_on:
#     choice = input("What would you like? (latte/espresso/cappuccino): ")
#
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         try:
#             drink = menu.find_drink(choice)
#             if coffee_maker.is_resource_sufficient(drink):
#                 print(f"Your {choice} order is prepared.")
#                 if money_machine.make_payment(drink.cost):
#                     coffee_maker.make_coffee(drink)
#         except AttributeError:
#             pass
#






class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h")


class Car(Vehicle):

    def __init__(self, fuel_type, brand, speed):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def move(self):

        if self.fuel_type == "electric":
            print(f"{self.brand} is silently moving at {self.speed} km/h")
        else:
            super().move()


car1 = Car("electric", "Tesla", 120)
car2 = Car("gasoline", "Toyota", 90)

car1.move()
car2.move()
























