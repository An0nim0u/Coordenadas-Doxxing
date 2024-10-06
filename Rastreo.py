import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode
from llave import key  # Asegúrate de que 'llave.py' contenga tu clave de API de OpenCage

def rastrear_numero():
    # Obtiene el número de teléfono del usuario
    numero_str = input("Ingresar número de teléfono: ")

    # Valida el formato del número de teléfono
    try:
        numero = phonenumbers.parse(numero_str)
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Número de teléfono inválido. Por favor, ingresa un número válido.")
        return

    # Muestra el mensaje de rastreo
    print("Cherishao Esta Rastreando el numero...")
    print("Cherishao Esta Rastreando el numero...")
    print("Cherishao Esta Rastreando el numero...")

    # Obtiene la información del número de teléfono
    zona = timezone.time_zones_for_number(numero)
    geo = geocoder.description_for_number(numero, 'en')
    carrier_info = carrier.name_for_number(numero, 'en')

    # Geolocalización
    geocoder = OpenCageGeocode(key)
    query = str(geo)
    results = geocoder.geocode(query)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    # Crea el mapa
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=geo).add_to(myMap)
    myMap.save("myLocation.html")

    # Imprime los resultados
    print(numero, zona, geo, carrier_info, lat, lng)

# Presenta las opciones al usuario
while True:
    print("1_ Quiero rastrear a un cabron, me ayudas?")
    print("2_ Mejor me voy")
    opcion = input("Elige una opción: ")

    # Procesa la opción del usuario
    if opcion == "1":
        rastrear_numero()
        print()
    elif opcion == "2":
        print("Adios!")
        break
    else:
        print("Opción inválida.")

    seguir = input("1_ Quieres rastrear a alguien más?\n2_ Salir del script y volver a tu inútil vida\nElige una opción: ")
    if seguir == "1":
        continue
    elif seguir == "2":
        break

print("\nDesarrollado Por Cherishao")