bid = {}
def get_input():

    bidder_name = input("What is your name? \n")
    bid_amount = float(input("What is your bid amount? \n"))
    bid[bidder_name] = bid_amount


has_another_bidder = True
while has_another_bidder:
    get_input()

    whether_new_bidder = input("Do you have another bidder? (y/n) \n").lower()
    
    if whether_new_bidder == "n":
        has_another_bidder = False
    else:
        has_another_bidder = True
        print('\n'  * 20)


## Get the highest bidder from the bid dictionary
highest_bid = 0
bidder  =''
for entry in bid:
    if bid[entry] > highest_bid:
        highest_bid = bid[entry]
        bidder = entry

print(f'The highest bidder is {bidder} with {highest_bid} bid')

