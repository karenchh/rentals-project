from abc import ABC, abstractmethod

class Vehicals(ABC):
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day

     # method to display cars info
    @abstractmethod
    def display_info(self):
        pass


class Cars(Vehicals):
    def __init__(self, brand, model, year, rental_price_per_day, seats):
        super.__init__(self, brand, model, year, rental_price_per_day)
        self.seats = seats

 # cars display format Car: Toyota Corolla, Year: 2020, Seats: 5, Rental Price: $50/day
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seats}, Rental price: '$' {self.rental_price_per_day}/day ")


class Bikes(Vehicals):
    def __init__(self, brand, model, year, rental_price_per_day, engine):
        super.__init__(self, brand, model, year, rental_price_per_day)
        self.engine = engine

 # Bike: Yamaha R1, Year: 2019, Engine: 998cc, Rental Price: $30/day
    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine}, Rental price: '$' {self.rental_price_per_day}/day ")