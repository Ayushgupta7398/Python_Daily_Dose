                             # Tip Calculator 
import random
print("=" * 45) 
welcome_message =["WELCOME TO THE MAD HATTER'S TIP CALCULATOR!",
    "GET READY TO SPLIT SOME BILLS... THE FUN WAY!",
    "YOUR QUEST FOR BILL-SPLITTING STARTS HERE!"]

print(random.choice(welcome_message))


def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value> 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_positive_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")




bill = get_positive_float_input("What was the total bill ₹ ?")

tip_percent = get_positive_int_input("What percentage tip would you like to give? 10, 12, or 15? ")

people = get_positive_int_input("How many people are splitting the bill? ")



# calculate tip amount 
tip_amount = bill*(tip_percent/100)

#Total bill  to pay 
total_bill_to_pay = (bill+tip_amount)

# bill for each person to pay 

each_person_to_pay = (total_bill_to_pay/people)

print("-" *40)
print(f"The total tip amount is: ₹{tip_amount:.2f}")
print(f"The total bill (including tip) is: ₹{total_bill_to_pay:.2f}")
print(f"\n ecah person should pay:₹ {each_person_to_pay:.2f} ")

print("-" *40)


print("\nThank you for using the Tip Calculator!")
print("Your friendly bill-splitting wizard,  Ayush.😊")
