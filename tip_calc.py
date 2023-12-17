# Tip calculator
# Writen by spid3r404
# 12/17/2023

# Get all the information regarding the price and tip
def get_tip_info():
    bill_amount = float(input("[+] What is the total bill amount: "))
    percent_tip = int(input("[+] What percentage tip would you like to give: "))
    split = int(input("[+] How many people to split the bill (enter 1 if no split): "))
    return bill_amount, percent_tip, split


# Use to calculate the total bill for each person including the tip
def calc_tip(b, t, s):
    try:
        percent = t / 100
        tip_amount = b * percent
        total_bill = b + tip_amount
        bill_per_person = total_bill / s
    except ZeroDivisionError:
        print("[-] Please provide a value other than 0. If you are not splitting the bill, enter 1!")

    return bill_per_person


print("Welcome to the Tip Calculator.")
print("----------------------------------------------------------------")
bill, tip, spl = get_tip_info()
print("[+] Total bill per person: {:.2f}".format(round(calc_tip(float(bill), float(tip), float(spl)), 2)))
