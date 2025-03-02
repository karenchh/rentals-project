
class Vehicals():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = 0

     # method to display cars info
    def display_info(self):
        info = f"{self.brand} {self.model}, Year: {self.year}" 
        return info
    
    def calculate_rental_cost(self, days):
        total = self.rental_price_per_day * days
        return total
    
    def rentalGetter(self):
        return self.__rental_price_per_day
    
    def rentalSetter(self, new_rental_price_per_day):
        self.__rental_price_per_day += new_rental_price_per_day

class Cars(Vehicals):
    def __init__(self, brand, model, year, seating_capacity ):
        self.seating_capacity = seating_capacity
        super().__init__(brand, model, year)
        self.rental_price_per_day = super().rentalGetter()
       

 # cars display format Car: Toyota Corolla, Year: 2020, Seats: 5, Rental Price: $50/day
    def display_info(self):
        information = super().display_info()
        print(f"Car: {information} ,  Seats: {self.seating_capacity}, Rental price: ${self.rentalGetter()}/day ")


class Bikes(Vehicals):
    def __init__(self, brand, model, year, engine_capacity):
        self.engine_capacity  = engine_capacity
        super().__init__(brand, model, year)
        
        

 # Bike: Yamaha R1, Year: 2019, Engine: 998cc, Rental Price: $30/day
    def display_info(self):
        information = super().display_info()
        print(f"Bike: {information} , Engine: {self.engine_capacity}, Rental price: ${self.rentalGetter()}/day ")

def show_vehicle_info(vehicle):
    if type(vehicle)  == Cars :
        vehicle.display_info()
    elif type(vehicle) == Bikes:
        vehicle.display_info()


car = Cars("Toyota","Corolla","2020","5")
car.rentalSetter(50)
show_vehicle_info(car)
bike = Bikes("Yamaha","R1","2019","998cc")
bike.rentalSetter(30)
show_vehicle_info(bike)
bike.display_info()

