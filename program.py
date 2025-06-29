#program of Secret Auction program Instruction
from art import logo
print(logo)
print("Welcome to the secret auction program.")
choice = "yes"
members = {}
while choice == "yes":
    name = input("What is your name?: ")
    bid = int(input("Whats your bid?: $"))
    members[name] = bid 
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    check_choice = choice
    while (check_choice != "yes" and check_choice != "no"):
        print("\nError!\nPlease try again:")
        choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        check_choice = choice
    if(choice == "yes"):
        print("\n" * 100)
# finding greatest Bidder
max_value_key = max(members, key=members.get)
#Printing Greatest Bidder name and bid
print("\n"*100)
print(f"The winner is {max_value_key} with a bid of ${members[max_value_key]}")