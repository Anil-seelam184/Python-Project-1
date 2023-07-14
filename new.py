import phonenumbers
from phonenumbers import geocoder
#from test import number
import folium
number=input("Enter number with country code")
Key="336a9226fc59410d87f0fd8452827168"
# country codes
check_number=phonenumbers.parse(number)
number_location=geocoder.description_for_number(check_number,"en")
print(number_location)
# service providers
from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))
#use of maps
from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(Key)
query=str(number_location)
results= geocoder.geocode(query)
#latitude and logitude
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

# display of lat and lng on map
map_location=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(map_location)
map_location.save("mylocation.html")
