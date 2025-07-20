print("This is the HCF finder game.")
# Program to find HCF/GCD

#Enter 2 numbers
numberLargest = int(input("Enter Largest Number: "))
numberSmallest = int(input("Enter the smallest number: "))

# Using Eucliden Algorithms
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is: ", numberLargest)



print("This is the LCM finder game.")
# Program to find LCM

# Enter 2 numbers
numberLargest = int(input("Enter Largest Number: "))
numberSmallest = int(input("Enter the smallest number: "))

# Using Euclidean Algorithm to find GCD
a = numberLargest
b = numberSmallest

while(b):
    temp = b
    b = a % b
    a = temp

# Calculate LCM using GCD
lcm = abs(numberLargest * numberSmallest) // a

print("LCM is: ", lcm)





# Palidrome game

def is_palidrome_number(number):
    return number == number[::-1]

def start_game():
    print("Welcome to the Number Palidrome Game!")
    print("A palidrome number reads the same forward and backward.")

    while True:
        number = input("Enter a number to check (or type 'exit' to quit): ")

        if number.lower() == "exit":
            print("Thanks for playing! keep having fun with numbers.")

            break
        if not number.isdigit():
            print("Please enter numbers only! No letters or symbols!")
            continue

        if is_palidrome_number(number):
            print(f"Awesome! {number} is a Palidrome \n")
        else:
            print(f"Oops! {number} is not a palidrome. Try again! \n")

# Start the game
start_game()
