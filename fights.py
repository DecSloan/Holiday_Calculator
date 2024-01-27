flight_destinations = {'Paris': 125,
                       'Hong Kong': 300,
                       'London': 175,
                       'Mexico City': 350,
                       'Los Angeles': 425,
                       'Amsterdam': 85, 
                       }

destinations_list = list(flight_destinations.keys())

flight_price_list = list(flight_destinations.values())

destinations_list_upper = []
for i in range(len(destinations_list)):
    destination_upper = (destinations_list[i]).upper()
    destinations_list_upper.append(destination_upper)