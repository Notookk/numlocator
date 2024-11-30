import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from opencage.geocoder import OpenCageGeocode
import folium

number = input("Enter a phone number with country code: ")
key = "9842ee5f04934507a1b74430cdde880e"

check_number = phonenumbers.parse(number)

time = timezone.time_zones_for_number(check_number)
car = carrier.name_for_number(check_number, "en")
number_location = geocoder.description_for_number(check_number, "en")

geocoder = OpenCageGeocode(key)
query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

my_map = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=number_location).add_to(my_map)

my_map.save("my_location.html")

print(time)
print(car)
print(number_location)
print("latitude: ",lat, "longitude: ", lng)
