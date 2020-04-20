card_number = list(input('Please enter a card number: ').strip())

# Remove the last digit of the card number
check_digit = card_number.pop()

# Reverse the order of the remaining numbers
card_number.reverse
processed_digits = []

# Check if the index of the number is even and then double it
for index, number in enumerate(card_number):
    if index % 2 == 0:
        doubled = int(number) * 2
# Subtract 9 from any results that are greater than 9
    if doubled > 9:
        doubled -= 9
        processed_digits.append(doubled)
    else:
        processed_digits.append(int(number))

total = int(check_digit)

# Add up the processed digits
for digit in processed_digits:
    total += digit

# Verify that the sum of the digits is divisible by 10
if total % 10 == 0:
    for number in card_number:
        if number[0] == 3:
            print('This is a valid Amex (American Express card')
        elif number[0] == 4:
            print('This is a Visa card')
        elif number[0] == 5:
            print('This is a valid Mastercard')
        elif number[0] == 6:
            print('This is a valid Discover card')
else:
    print('Invalid card number')
