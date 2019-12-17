'''
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
'''

print("The programs starts from here: ")


widgets = 75
gizmos = 112 

quantity_of_widgets = int(input("Enter the number of widgets: "))
quantity_of_gizmos  = int(input("Enter the number of gizmos: "))

total_weight = quantity_of_widgets * widgets + quantity_of_gizmos * gizmos

print("The total of your order is",total_weight,"grams ")
print("Thanks for your order :)")