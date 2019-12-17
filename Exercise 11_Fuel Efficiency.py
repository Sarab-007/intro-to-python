'''
In the United States, fuel efficiency for vehicles is normally expressed in miles-per-
gallon(MPG).InCanada,fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100km). Use your research skills to determine how to convert from
MPGtoL/100km.Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
'''
print("The programs starts from here...")

units = int(input("Enter the value in american dollars: "))

fuel_eff = units * 235.214583/100

print("The fuel efficiency of your vehicle is ",fuel_eff,"units")

print("finished :)")


 


