
'''
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.
'''



print("your programs starts here...")

less_depo = 0.15
more_depo = 0.25

less = float(input("Enter the number of containers 1 liter or less than 1 liter:  "))
more = float(input("Enter the number of container 1 litre or more than 1 litre: "))

refund = less_depo *less + more * more_depo

print ("your final refund is $%.2f" % refund )