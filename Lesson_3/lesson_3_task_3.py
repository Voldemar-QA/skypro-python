from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Тверская", "12", "45")
from_address = Address("654321", "Санкт-Петербург", "Миллионная", "9", "17")

mailing = Mailing(to_address, from_address, 470, "PM13245768")

print(mailing)
