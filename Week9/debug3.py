# example 3
year = int(input("What is your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a Millennial")
elif year >= 1994: # Changed condition to include 1994
    print("You are a Gen Z")