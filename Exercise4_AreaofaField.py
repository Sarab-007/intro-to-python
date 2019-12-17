SQFT_PER_ACRE = 43560
length = float(input("Enter the numbe rin feet or meter:"))
width = float(input("Enter the number in meter or feet"))

acres = length * width / SQFT_PER_ACRE

print("The area of the field is",acres,"acres")