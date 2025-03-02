
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
        total = int(self.__rental_price_per_day) * int(days)
        return total
    
    def rentalGetter(self):
        return self.__rental_price_per_day
    
    def rentalSetter(self, new_rental_price_per_day):
        self.__rental_price_per_day += new_rental_price_per_day

class Cars(Vehicals):
    def __init__(self, brand, model, year, seating_capacity ):
        self.seating_capacity = seating_capacity
        super().__init__(brand, model, year)
        
 # cars display format Car: Toyota Corolla, Year: 2020, Seats: 5, Rental Price: $50/day
    def display_info(self):
        information = super().display_info()
        print(f"Car: {information} ,  Seats: {self.seating_capacity}, Rental price: ${self.rentalGetter()}/day ")
#Rental cost for Toyota Corolla for 3 days: $150
    def calculate_rental_cost(self, days):
        rentalperday = super().calculate_rental_cost(days)
        print(f"Rental cost for {self.brand} {self.model} for {days} days: ${rentalperday}")


class Bikes(Vehicals):
    def __init__(self, brand, model, year, engine_capacity):
        self.engine_capacity  = engine_capacity
        super().__init__(brand, model, year)
        
 # Bike: Yamaha R1, Year: 2019, Engine: 998cc, Rental Price: $30/day
    def display_info(self):
        information = super().display_info()
        print(f"Bike: {information} , Engine: {self.engine_capacity}, Rental price: ${self.rentalGetter()}/day ")

    def calculate_rental_cost(self, days):
        rentalperday = super().calculate_rental_cost(days)
        print(f"Rental cost for {self.brand} {self.model} for {days} days: ${rentalperday}")

def show_vehicle_info(vehicle):
    vehicle.display_info()


car = Cars("Toyota","Corolla","2020","5")
car.rentalSetter(50)
car.display_info()
#show_vehicle_info(car)
days = input("For how many days you need to rent: ")
car.calculate_rental_cost(days)

print("===============================================")

bike = Bikes("Yamaha","R1","2019","998cc")
bike.rentalSetter(30)
#show_vehicle_info(bike)
bike.display_info()
days = input("For how many days you need to rent: ")
bike.calculate_rental_cost(days)

#Cars_list = ["Toyota" , "BMW" , "Audi"]
#bikes_list = ["Yamaha" , "Bianchi"]

'''def rental():
    vehical_type = input("Do you want to rent a Car or a Bike? ")
    vehical_brand = input("Please enter the brand of the vehicle you need to rent: ")
    vehical_model = input("Please enter the model of the vehicle you need to rent: ")
    vehical_year = input("Please enter the year of the vehicle you need to rent: ")

    target = None
    if vehical_type == "Car" :
        seats_number = input("Please enter the number of seats you want: ")
        for cr in Cars_list :
            if cr == vehical_brand:
                target = cr
                
            
    elif vehical_type == "Bike":
        engine_cap = input("Enter the engine capacity: ")
        for bk in bikes_list :
            if bk == vehical_brand:
                target = bk
                return target
            
    else :
        print("Sorry we don't rent this type of vehicles.")

   ''' 


    
