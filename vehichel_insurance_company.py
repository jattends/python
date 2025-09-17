# -----------------------------------------------------------
# Project Title : Auto Insurance Policy Management System
# Description   : This project is designed to collect customer
#                 and vehicle details, calculate auto insurance
#                 premiums based on car age, apply a user-defined
#                 discount, and validate inputs like phone numbers
#                 and vehicle registration numbers.
#
#                 The program supports:
#                 - Customer data input and validation
#                 - Registration number format checking
#                 - Insurance premium calculation logic
#                 - File handling to save all policy records
#
# File Output   : All collected data is saved to
#                 'TRUSTED_INSURANCE_COMPANY.txt' for future reference.
#
# Author        : NITHANTH HARSHA
# -----------------------------------------------------------

import re

class AutoInsurance:
    discount = 0

    def __init__(self, car_model, car_age):
        self.car_model = car_model
        self.car_age = car_age

    @classmethod
    def set_discount(cls, discount):
        cls.discount = discount

    def calculate_premium(self):
        base_premium = 500
        if self.car_age > 5:
            base_premium += 100
        return base_premium - AutoInsurance.discount

    @staticmethod
    def validate_registration(registration_number):
        pattern = r'^[A-Z]{2} \d{2} [A-Z]{1,2} \d{1,4}$'
        return bool(re.fullmatch(pattern, registration_number))


class Customer:
    customer_count = 0

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def display(self):
        print(f"Customer Name : {self.name}")
        print(f"Customer number  : {self.number}")

    @staticmethod
    def validate_phone_number(number):
        pattern = r'^[6-9]\d{9}$'
        return bool(re.fullmatch(pattern, number))


try:
    print("\n------- Customer Details --------")
    cust_name = input("ENTER YOUR NAME : ")

    while True:
        cust_number = input("ENTER YOUR PHONE NUMBER : ")
        if Customer.validate_phone_number(cust_number):
            break
        else:
            print("Invalid phone number! Please enter a valid 10-digit number starting with 6-9.")

    customer = Customer(cust_name, cust_number)

    print("\n______ Vehicle Registration ______")
    while True:
        registration_number = input("Enter your vehicle registration number (Format: 'KL 09 QW 728'): ")
        if not registration_number:
            print("Registration number cannot be empty. Please try again.")
            continue

        is_valid = AutoInsurance.validate_registration(registration_number)
        if is_valid:
            print(f"Your registration number is valid: {registration_number}")
            break
        else:
            print("Invalid registration number! Format should be like 'KL 09 QW 728'. Please re-enter.")

    print("\n______ Enter your vehicle details _____")
    car_model1 = input("Enter your car model: ")
    car_age1 = int(input("Enter your car age: "))
    policy1 = AutoInsurance(car_model1, car_age1)

    car_model2 = input("Enter your second car model: ")
    car_age2 = int(input("Enter your second car age: "))
    policy2 = AutoInsurance(car_model2, car_age2)

    user_discount = int(input("\nEnter discount amount to apply on all policies (₹): "))
    AutoInsurance.set_discount(user_discount)

    print("\n------- Customer and Policy Summary -------")
    customer.display()

    premium1 = policy1.calculate_premium()
    premium2 = policy2.calculate_premium()

    print(f"\nUpdated premiums after applying ₹{user_discount} discount:")
    print(f"{policy1.car_model} - After discount: ₹{premium1}")
    print(f"{policy2.car_model} - After discount: ₹{premium2}")

    # File Handling - Save all details to a file
    with open("TRUSTED_INSURANCE_COMPANY.txt", "w") as file:
        file.write("\n----------- New Insurance Record -----------\n")
        file.write(f"Customer Name: {customer.name}\n")
        file.write(f"Phone Number: {customer.number}\n")
        file.write(f"Vehicle Registration Number: {registration_number}\n")
        file.write(f"First Car: {policy1.car_model}, Age: {policy1.car_age}, Premium: ₹{premium1}\n")
        file.write(f"Second Car: {policy2.car_model}, Age: {policy2.car_age}, Premium: ₹{premium2}\n")
        file.write(f"Discount Applied: ₹{user_discount}\n")
        file.write("------------------------\n")

    print("\nAll details saved successfully to 'TRUSTED_INSURANCE_COMPANY.txt'.")

except ValueError:
    print("Invalid input! Please enter valid numbers for age and discount.")
