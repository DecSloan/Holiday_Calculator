while True:
    try:
        nights = int(input("Please enter the number of nights you will " +
                           "be staying at the Hotel?: "))
        break
        
    except ValueError:
        print("\nPlease enter a valid number.\n")

hotel_cost = nights * 90
multiply_test = multiply_90(nights)
print( )