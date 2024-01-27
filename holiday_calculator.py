# Calculate the total holiday cost including flights, hotel and car rental cost
# Get the user to enter the city they are flying to 
# plane_cost returns a cost based on the city
# Get the user to enter the no. of nights staying at hotel
# hotel_cost returns the a total cost for the hotel
# Get the user to enter the no. of days they will be hiring a car
# car_rental returns the total cost for the car hire
# holiday_cost returns the total of all three costs together 

import math

# Made a function multiply_90 so that when the number of nights is entered 
# Multiplies by 90 (nightly rate) and returns the total hotel cost 
# With a breakdown of nights x rate 

def multiply_90(num1, num2 =90):
    total = num1 * num2
    print(f"\nYou have selected {num1} nights at £{num2}.\nTotal cost of " +
          f"Hotel is £{total}")

# Made a def multiply_75 so that when the number of days is entered 
# Multiplies by 75 (daily rate) and returns the total car rental cost 
# With a breakdown of days x rate 

def multiply_75(num1, num2 =75):
    total = num1 * num2
    print(f"\nYou have selected {num1} days at £{num2}.\nTotal cost of " +
          f"car rental is £{total}")
    
# Made a def addition_total to add flight, hotel and car rental
# print out each single cost breakdown and then total at bottom
# Also includes a thank you message and have a great trip

def addition_total(num1, num2, num3):
    total = num1 + num2 + num3
    print(f"Flight cost is £{num1}.")
    print(f"Hotel cost is £{num2}.")
    print(f"Car rental cost is £{num3}.")
    print(f"\nTotal cost of holiday is £{total}.")
    print(f"\nThanks for using Holiday calculator, have a great trip!")

# Dictionary containing flight destinations (keys) + prices (values)

flight_destinations = {'Paris': 125,
                       'Hong Kong': 300,
                       'London': 175,
                       'Mexico City': 350,
                       'Los Angeles': 425,
                       'Amsterdam': 85, 
                       }

# Created a list of the keys from flight destination Dictionary

destinations_list = list(flight_destinations.keys())

# Created a list of values from flight destination dictionary 

flight_price_list = list(flight_destinations.values())

# Also created an all upper case version of this list 
# Minimise errors when checking against user input later

destinations_list_upper = []
for i in range(len(destinations_list)):
    destination_upper = (destinations_list[i]).upper()
    destinations_list_upper.append(destination_upper)

# Print welcoming statement 
    
print("Welcome to the Holiday calculator!")
print(" ")
print(*destinations_list, sep = "\n")
print(" ")

# Ask the user for their destination airport
# If input not on the list promtp the user to choose from list
# Once a correct city is chosen find the index in destination list 
# Then find the correlating price from the price (values) list 
# Print chosen airpot and price, save plane_cost as an integer, then break

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

# Ask user to enter the number of nights staying at hotel
# Made a while loop so that error message displayed 
# Until an integer is entered 

while True:
    try:
        nights = int(input("Please enter the number of nights you will " +
                           "be staying at the Hotel?: "))
        break
        
    except ValueError:
        print("\nPlease enter a valid number.\n")

# Once valid integer is entered calculate total hotel cost
# Nights x fixed rate of £90 per night
# Saved as hotel_cost and print out breakdown of cost

hotel_cost = nights * 90
multiply_test = multiply_90(nights)
print( )

# Ask the user if they will be renting a car while on holiday
# Strip and convert to uppercase before checking answer
# If neither Y or N selected, prompt user to enter valid answer

while True:
    car_rental_ans = input("Will you be renting a car while on your " +
                           "Holiday? Y or N: ")
    car_rental_ans = car_rental_ans.strip()
    car_rental_ans = car_rental_ans.upper()

    if car_rental_ans == "N":
        print( )
        print("N selected")
        print( )
        break

    elif car_rental_ans == "Y":
        print( )
        print("Y selected")
        print( )
        break

    else:
        print( )
        print("Pleas select either Y or N.")
        print( )

# If Y selected then user asked for number of days renting
# Prompted to enter valid answer if no integer entered 
# Once integer entered car rental price saved
# Multiply_75 used as defined above for fixed rate 75
# Breakdown of cost is printed
# If N then the car_rental price is saved as 0 so we still can use later

if car_rental_ans == "Y":
    while True:
        try:
            rental_days = int(input("Please enter the number of days will you " +
                                "be renting a car for?: "))
            break
        
        except ValueError:
            print("\nPlease enter a valid number.\n")

    car_rental = rental_days * 75
    multiply_test = multiply_75(rental_days)
    print( )

else:
    car_rental = 0

# Once all data is collected we can use def addition_total
# Prints a breakdown of the 3 seperate costs in a readable way
# Also includes the total cost and then a thankyou message 

multiply_test = addition_total(plane_cost, hotel_cost, car_rental)