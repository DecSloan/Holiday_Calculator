# Holiday_Calculator
**Simple program to calculate total cost of a holiday, adding separate components e.g. flight + hotel**

The aim of this task is to total the cost of a holiday based on user inputs for destination, amount of days in a hotel and whether they are renting a car.

---
## Functions

I have recently learnt about functions and how they can improve efficiency while repeating certain tasks, so I had a go at creating some!

Firstly I made a function to calculate the hotel cost, using a standard cost of £90 per night. 
This function will take the users input for amount of nights and times it by the cost per night.

The second function is to calculate the car rental cost, again using a standard cost of £75 per day.
This function takes the users input for amount of days and times it by the cost per day. 

The last function is to get the total cost of the holiday by adding the three totals, flight, hotel and car rental.
As well as adding the prices to get a total I also decided to print the separate costs for a detailed overview for the customer.
The final line is a sign off line, thanking the customer for using the service and wishing them a good holiday.

    import math

    def multiply_90(num1, num2 =90):
        total = num1 * num2
        print(f"\nYou have selected {num1} nights at £{num2}.\nTotal cost of " +
              f"Hotel is £{total}")

    def multiply_75(num1, num2 =75):
        total = num1 * num2
        print(f"\nYou have selected {num1} days at £{num2}.\nTotal cost of " +
              f"car rental is £{total}")

    def addition_total(num1, num2, num3):
        total = num1 + num2 + num3
        print(f"Flight cost is £{num1}.")
        print(f"Hotel cost is £{num2}.")
        print(f"Car rental cost is £{num3}.")
        print(f"\nTotal cost of holiday is £{total}.")
        print(f"\nThanks for using Holiday calculator, have a great trip!")

## Flights

I created a dictionary with the destinations as the keys and costs as the values, I also then created two lists form these so I can access them seperately.
Lastly I created an all uppercase list so I could check against this later while minimising errors.

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

## Destination

Print welcome statement and then the list of pre-saved destinations. 
User asked for thier input which is stripped and converted to upper case. 
If input not in destination list then prompted to choose fro list.
Once a correct city is chosen, index is found and the corresponding cost is found through the values list.
Print statement with the chosen destination and the price is displayed.

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
