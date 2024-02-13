import re
cardNumber = input("Enter your debit card number: ")
if not re.match(r'^\d{4}\s\d{4}\s\d{4}\s\d{4}$', cardNumber):
    print("Invalid debit card number format.")
else:
    card_number = cardNumber.replace(" ", "")

    if len(card_number) != 16:
        print("Invalid debit card number length.")
    else:
        if not re.match(r'^4|5|6', card_number):
            print("Invalid debit card number prefix.")
        else:
            print("Valid debit card number.")