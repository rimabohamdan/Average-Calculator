print("Apply calculate the average numbers")
number = int(input("Enter the number of values : "))
values_list = []

for i in range(1, number + 1):
    value = float(input(f"Enter values {i} : "))
    values_list.append(value)

len_values = len(values_list)
sum_values = sum(values_list)
result = sum_values / len_values
print(f"The average is : {result}")
