'''Createaprogramthatreadstwointegers,a andb,fromtheuser.Yourprogramshould
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log 10 a
• The result of a b
Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list.
'''
print("Program starts here... \n")

from math import log10
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

add = a+b
sub = b-a
div = a/b
mul = a * b
exp = a**b
rem = a % b
log = log10(a)

print ("a+b = \t",add)
print ("b-a = \t",sub)
print ("a/b = \t",div)
print ("a*b = \t",mul)
print ("a**b = \t",exp)
print ("a%b = \t",rem)
print ("alog10b = \t",log)