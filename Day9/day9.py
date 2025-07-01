# Ask user for birth year
birth_year = int(input("Enter your birth year (e.g., 1999): "))

# Determine generation
if birth_year >= 1925 and birth_year <= 1946:
    print("You are part of the Traditionalists generation.")
elif birth_year >= 1947 and birth_year <= 1964:
    print("You are a Baby Boomer.")
elif birth_year >= 1965 and birth_year <= 1981:
    print("You belong to Generation X.")
elif birth_year >= 1982 and birth_year <= 1995:
    print("You are a Millennial.")
elif birth_year >= 1996 and birth_year <= 2015:
    print("You belong to Generation Z.")
else:
    print("Sorry, we couldn't determine your generation.")
