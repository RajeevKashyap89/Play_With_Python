from Art import logo    

auction_info = []
auction = True


def add_new_bidder(bidder_name,bidder_amount):
    new_bidder = {}
    new_bidder['bid'] = bidder_amount
    new_bidder['name'] = bidder_name
    auction_info.append(new_bidder)



while auction:
    print(logo)
    print("Welcome to the private bidding auction") 
    name = input("Name:").title()
    bid_amount = float(input("Amount: $"))
    add_new_bidder(bidder_name=name,bidder_amount=bid_amount)

    others = input("any more bidders? Type 'Yes' or 'No'.\n")
    if others == 'No':
        auction = False
        highest_bidder = 0
        count = -1
        for e in auction_info:
            if e['bid'] > highest_bidder:
                highest_bidder = e['bid']
                count += 1
        winner =   auction_info[count]['name']
        print(f"Highest Bidder is {winner} with a $ {highest_bidder}")
        print("Thank you for your participation!")      
