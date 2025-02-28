class Vehicals:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day



class Cars(Vehicals):
    def __init__(self, brand, year, seats, rental_price_per_day):
        super.__init__(self, brand, year, rental_price_per_day)
        self.seats = seats