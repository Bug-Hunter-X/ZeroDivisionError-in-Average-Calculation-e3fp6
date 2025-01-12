def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

#Example of the error:
my_list = []
result = calculate_average(my_list)
print(result) # This will print 0 as intended
my_list = [10, 20, 30, 40, 0]
result = calculate_average(my_list) # ZeroDivisionError if 0 is the only element in the list
print(result)