# Swapping two variables

first_variable = "hello"
second_variable = "world"

temp_variable = first_variable
first_variable = second_variable
second_variable = temp_variable

# This also swaps the two variables, because it initializes a 'temporary' variable as a tuple and unpacks it
first_variable, second_variable = second_variable, first_variable
