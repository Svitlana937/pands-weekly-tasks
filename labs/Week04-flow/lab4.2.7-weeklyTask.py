number = int(input("Please enter a positive integer: "))
n = number
n_list = [n]
# n_list.append(n)
while n != 1:
    if n % 2 == 0:
        n = n // 2
        n_list.append(n)
    else:
        n = 3 * n + 1  
        n_list.append(n)
print(n_list)  # Print the list of numbers
