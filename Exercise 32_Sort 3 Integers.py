'''Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
'''

print("Your programs starts from here: ")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


min_val = min(a,b,c)
max_val = max(a,b,c)

mid_val = (a + b + c) - (min_val - max_val)

print("The sorted order or integer are: ")
print(">",min_val)
print(">",max_val)
print(">",mid_val)
