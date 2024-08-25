keep_shopping = True
apples = 0
grapes = 0
oranges = 0
sub_total = 0
tax = 0.05
#Step 1 Store User's name
print("Welcome to the GC Fruit Market!")
print("What is your name?")
name = input("> ")

#Step 2 Display a list of fruit and prices
while keep_shopping:
    print(f'Welcome {name}. Which Fruit would you like to buy')
    fruits = ["Apple $2","Grape $1","Orange $3"]
    print(f'1. {fruits[0]}')
    print(f'2. {fruits[1]}')
    print(f'3. {fruits[2]}')
#Step 3 Allow user to select and buy one of the fruits
    fruit_bought = int(input("> "))
    if fruit_bought == 1:
        apples += 1
        sub_total += 2
        print("You bought 1 Apple at $2")
    elif fruit_bought == 2:
        grapes += 1
        sub_total += 1
        print("You bought 1 Grape at $1")
    elif fruit_bought == 3:
        oranges += 1
        sub_total += 3
        print("You bought 1 Orange at $3")
    else:
        print("You entered an invalid fruit")
#Step 4 Give option to buy another fruit repeated
    print("Would you like to buy another piece of fruit? y/n")
    if input("> ") == "y":
        keep_shopping = True
    else:
        keep_shopping = False
#Step 5 Display Receipt with name
print(f'Order for {name}')
print(f'{apples} apple(s) at $2 apiece')
print(f'{grapes} grape(s) at $1 apiece')
print(f'{oranges} orange(s) at $3 apiece')
#Step 6 find and print subtotal
print(f'Sub Total: ${sub_total}')
#Step 7 find and print tax
tax *= sub_total
print(f'5% Tax: ${tax}')
#Step 8 add subtotal and tax to get receipt total
total = sub_total + tax
print(f'Total: ${total}')