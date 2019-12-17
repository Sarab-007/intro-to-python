'''
Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
'''

print("your programs starts here...")

width = float(input("Enter the value in feet or meter:"))
length = float(input("Enter the value in feet or meters:"))

Area_of_room = width * length

print("your Area of room is",Area_of_room)



