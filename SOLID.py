# TODO SOLID პრინციპის დაცვით შეცვალეთ კლასების იმპლემენტაცია

# Single Responsibility Principle
class Book:
    def set_details(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def get_discount_price(self, discount):
        return self.price * (discount/100)


from abc import ABC, abstractclassmethod

# TODO დაამატეთ  PayPal-ის გადახდების კლასი, და  Payment
# Open/Closed Principle

class Payment(ABC):
    
    def __init__(self, payment) -> None:
        self.payment = payment
    
    @abstractclassmethod
    def process_credit(self, amount):
        pass
        

class PaypalPayment(Payment):
    
    def __init__(self) -> None:
        super().__init__("paypal")

        
    def process_credit(self, amount):
        
        print(f"Full payment will be {amount} + {amount * 0.02} comission = {amount + amount*0.02}")
    
    

pay1 = PaypalPayment()
    
pay1.process_credit(100)
        


# TODO გადააკეთეთ კლასები ისე, რომ დაიცვან ლისკოვის ჩანაცვლების პრინციპი
# Liskov Substitution Principle
class Vehicle:
    def fuel_capacity(self):
        return "100 liters"

class ElectricCar(Vehicle):
    def fuel_capacity(self):
        return "Battery capacity is 100 kWh"



# TODO შეცვალეთ იმპლემენტაცია, რადგან ყველა მოთამაშეს არ აქვს აუდიოს ან ვიდეოს მხარდაჭერა
# Interface Segregation Principle
class MultimediaPlayer:
    def play_audio(self):
        pass
    def play_video(self):
        pass


# TODO შეცვალეთ კლასის იმპლემენტაცია, რომ დაიცვას დამოკიდებულების ინვერსიის პრინციპი.
# Dependency Inversion Principle (DIP)
class ConsoleDisplay:
    def show(self, data):
        pass

class WeatherStation:
    def report(self, display):
        display.show("Weather Data")

