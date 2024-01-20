# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

#Psuedocode       
#Define a function
def calculate_two_integers(number_one, number_two):
#Calculate for the product of the given numbers
    numbers_product = number_one * number_two

#Calculate for the sum of the given numbers
    numbers_sum = number_one + number_two

#Check if the product is equal or less than 1000. If yes, return their product
    if numbers_product <= 1000:
        return numbers_product
#If the condition is not met, return the sum
    else:
        return numbers_sum

#Print the results with the given integer values
integer_result = calculate_two_integers(20, 30)
print("The result is ", integer_result)

integer_result = calculate_two_integers(40, 30)
print("The result is ", integer_result)