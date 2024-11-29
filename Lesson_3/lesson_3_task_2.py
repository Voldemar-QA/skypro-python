from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S21", "+79345678905"),
    Smartphone("Apple", "iPhone 12", "+79876543213"),
    Smartphone("Google", "Pixel 5", "+79223344554"),
    Smartphone("OnePlus", "8 Pro", "+79233445566"),
    Smartphone("Xiaomi", "Mi 11", "+79455667378")
]

for phone in catalog:
    print(f"{phone.telBrand} - {phone.telModel}. {phone.telNumber}")
