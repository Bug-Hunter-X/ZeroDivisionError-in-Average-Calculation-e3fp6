def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if sum(numbers) == 0 and len(numbers)>0:
        return 0 # Handle list with all zeros
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_list = []
result = calculate_average(my_list)
print(result)  # Output: 0

my_list = [10, 20, 30, 40, 0]
result = calculate_average(my_list)
print(result)  # Output: 20.0

my_list = [0,0,0]
result = calculate_average(my_list)
print(result) # Output: 0.0