# Q1

for counter in range (10, 0, -1):
    print(counter)
print("Liftoff!")

# Q2

adult_counter = 0
child_counter = 0
for i in range (1,6):
    age = int(input(f"Age of visitor {i}: "))
    if age >= 18:
        adult_counter += 1
    else:
        child_counter += 1
print(f"Child tickets: {child_counter}")
print(f"Adult tickets: {adult_counter}")

# Q3 Answer is "1 3 5 7 9"

# Q4

count = 5
total = 0
for counter in range (1, count+1):
    price = float(input(f"Price of item {counter}: "))
    total += price
average = total / count
print(f"Total: {total}")
print(f"Average: {average}")

# Q5

req = 8   #Least amount of characters required
while True:
    password = input("new password:")
    if len(password) >= 8:
        print("Password accepted")
        break
    else:
        print("Too short, try again")

# Q6 Answer:

# 70
# 40
# 10
# -20
# Done

# Q7

daily_rec= 1200      # Steps every day
days = 7             # Number of days 
total_rec = 0
for counter in range(1, days+1):
    total_rec += daily_rec
    print(f"Day {counter}: {total_rec}")

# Q8

attempts = 3
counter = 0
user = "admin"
password = "0000"
while counter < attempts:
    e_user = input("Username: ")            # Entered username
    e_password = input("Password:")         # Entered password
    counter += 1
    if e_user == user and e_password == password:
        print("Welcome!")
        break
    else:
        print("Wrong username or password")
    if counter == 3:
        print("Account locked")

# Q9

balance = 500
while True:
    amount = int(input("Amount:"))
    if amount == 0:
        print("Goodbye")
        break
    elif amount < 0:
        print("Invalid amount")
    elif balance - amount < 0:
        print("Insufficient funds")
    else:
        balance -= amount
        print(f"Balance: {balance}")

# Q10 Answer:

# Wrong PIN, 2 attempts left
# Wrong PIN, 1 attempts left
# Acces granted
# Attempts used: 3

# Q11
passed = 0
failed = 0
sum_grades = 0
max_grade = 0
counter = 0
while True:
    grade = int(input("Grade: "))
    if grade == -1:
        break
    sum_grades += grade
    counter += 1
    if grade >= 51:
        passed += 1
    else:
        failed += 1
    if max_grade < grade:
        max_grade = grade
average = sum_grades / counter
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Highest: {max_grade}")
print(f"Average: {average}")

# Q12

free_spaces = 20
while True:
    command = input("Command: ")
    if command == "in":
        if free_spaces == 0:
            print("Garage is full")
            continue
        else:    
            change = -1
    elif command == "out":
        if free_spaces < 20:
            change = 1
        else:
            print("Garage is empty")
            continue
    elif command == "stop":
        break
    else:
        print("Unknown command")
        continue
    free_spaces += change
    print(f"Free spaces: {free_spaces}")

# Q13

hot_days = 0
max_temp = 0
for day in range (1, 8):
    temp = int(input(f"Day {day}: "))
    if temp > 30:
        hot_days += 1
    if max_temp < temp:
        max_temp = temp
        hottest = day
print(f"Hot days: {hot_days}")
print(f"Hottest day: {hottest}")

# Q14 Answer: the line "attempts = 0" must be outside the loop, not in it.

password = "secret"
attempts = 0
while True:
    entered = input("Password: ")
    if entered == password:
        print("Welcome")
        break
    attempts += 1
    if attempts == 3:
        print("Account locked")
        break

# Q15

password = input("Password: ")
digit = False
upper = False
lower = False
reason = ""
for character in password:
    if character.isdigit():
        digit = True
    if character.isupper():
        upper = True
    if character.islower():
        lower = True
if not digit:
    reason += "no digit  "
if not upper:
    reason += "no uppercase letters  "
if not lower:
    reason += "no lowercase letters  "
if len(password) < 8:
    reason += "less than 8 characters  "
if digit and upper and lower and len(password) >= 8:
    print("Strong password")
else:
    print(f"Weak password: {reason}")

# Q16

total = 0
increase = 10
saving = 50
month = 0
while total < 1000:
    total += saving 
    month += 1
    saving += increase
    print(f"Month {month}: {total}")
print(f"Goal reached in month {month}")

# Q17 Break stops the program if number can be divided by 7 and if number is odd. Answer is 105

# Q18
