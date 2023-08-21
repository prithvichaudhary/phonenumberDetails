import phonenumbers 
from phonenumbers import geocoder,timezone,carrier
number = input("Enter your phone number with country code , eg +91... ")
phone = phonenumbers.parse(number)#thiswill create our string into number format
time = timezone.time_zones_for_number(phone)
car= carrier.name_for_number(phone,"en")#en stand for english
reg = geocoder.description_for_number(phone,"en")
print(time)
print(car)
print(reg)