

# Write a Python program that prompts the user to enter a number, x, and displays all numbers from 1 to x that are divisible by both 3 and 5


user_nb = int(input("Enter your number : "))
divisible_by_three_five = ""

for i in range(1, user_nb+1):       # added one since it starts with Zero
    if i % 3 == 0 and i % 5 == 0:
        divisible_by_three_five += str(i) + " " 
    

print("Numbers that are divisible both by 3 and 5 are : " + divisible_by_three_five)