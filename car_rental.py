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

multiply_test = addition_total(plane_cost, hotel_cost, car_rental)