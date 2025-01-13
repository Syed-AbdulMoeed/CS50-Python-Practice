# American Express uses 15-digit numbers, 
# MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers
# Express numbers start with 34 or 37; most MasterCard numbers start with 51, 52, 53, 54, or 55 
# (they also have some other potential starting numbers which we won’t concern ourselves with for this problem); 
# and all Visa numbers start with 4
# Identiy wether its AE, MC or Visa using Regular expression
# Implement Luhn's Algorithim



import re
def get_card():
    while True:
        try:
            return int(input("Number: "))
            
        except ValueError:
            ...



def validate_card(card):  # card is str
    ae_pattern = r"^(34|37)[0-9]{13}$"
    mc_pattern = r"^(51|52|53|54|55)[0-9]{14}$"
    vs_pattern = r"^(4[0-9]{12}|4[0-9]{15})"
    
    ae_match = re.search(ae_pattern,card)
    mc_match = re.search(mc_pattern,card)
    vs_match = re.search(vs_pattern,card)

    if ae_match:
        return "AMEX"
    elif mc_match:
        return "MASTERCARD"
    elif vs_match:
        return "VISA"
    else:
        return None


def lhun_check(card):
    check = lstep_1(str(card))
    for digit in str(card)[-1::-2]:
        check += int(digit)
    if check%10==0:
        return True


def lstep_1(num):  #num is a str
    # adding alternating digits starting from 2nd last position
    
    numbers = []
    for digit in num[-2::-2]:
        numbers.append(int(digit)*2)

    # adding digits of each number in list 
    total = 0
    for number in numbers:
        for digit in str(number):
            total = int(digit) + total
    return total



def main():
    card = get_card()  # get input from user consisting of numbers only
    type = validate_card(str(card))  # identify card type based on digit format
    if type:
        if lhun_check(card):
            print(type)
        else:
            print("INVALID")
    else:
        print("INVALID")


main()