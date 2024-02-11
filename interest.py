# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
# Test Data : amt = 10000, int = 3.5, years = 7

def interest(amt, intr, years):
    total = amt * ((1 + (0.01 * intr)) ** years)
    return round(total, 2)
print(interest(10000, 3.5, 7))
