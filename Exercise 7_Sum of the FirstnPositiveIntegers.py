'''
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum =
(n)(n + 1)/2
'''


print("The programs starts now... ")

n = int(input("Enter the integer number to sum:  "))

sum = n * (n+1) / 2

print("The sum or your integer number is ",sum)
