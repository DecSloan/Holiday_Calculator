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