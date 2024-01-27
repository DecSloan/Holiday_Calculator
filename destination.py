print("Welcome to the Holiday calculator!")
print(" ")
print(*destinations_list, sep = "\n")
print(" ")

while True:
    city_flight = str(input("Please enter your destination airport from the list: "))
    city_flight = city_flight.strip()
    city_flight = city_flight.upper()

    if any(word in city_flight for word in destinations_list_upper):
        print( )
        i = destinations_list_upper.index(city_flight)
        print(f"{city_flight} selected, price is £{flight_price_list[i]}")
        print( )
        plane_cost = int(flight_price_list[i])
        break

    else:
        print( )
        print(f"{city_flight} airport not available, pleas select any from list below\n")
        print(*destinations_list, sep = "\n")
        print( )