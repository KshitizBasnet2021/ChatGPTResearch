#get_factors.py
#
#The code provided is missing a condition to handle the case when the input number is a prime number. Currently, if the input number is a prime number, the code will return an empty list. 
#
#To fix this, we can add a condition at the end of the function to check if the input number is greater than 1. If it is, we can return a list containing the input number itself as the only factor. 
#
#Here's the updated code:
#
def get_factors(n):
    if n == 1:
        return []
#
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + get_factors(n // i)
#
    if n > 1:
        return [n]
#
    return []
#
#
#