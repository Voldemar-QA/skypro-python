class Address:
    def __init__(self, zip, city, street, house, apart):
        self.zip = zip
        self.city = city
        self.street = street
        self.house = house
        self.apart = apart

    def __str__(self):
        return (f"{self.zip}, {self.city}, {self.street} "
                f"{self.house} - {self.apart}")
