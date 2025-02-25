logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def blind_auction():
    print(logo)
    competitors = {}
    highest_bid = 0
    winner = ""

    while True:
        name_of_competitor = input("What is your name?: ")
        bid_of_competitor = int(input("What is your bid?: $"))
        competitors[name_of_competitor] = bid_of_competitor

        any_other_bidders = input("Are there any other bidders? Type 'Yes' or 'No'.").lower()

        if any_other_bidders == "no":
            for key in competitors:
                if competitors[key] > highest_bid:
                    highest_bid = competitors[key]
            for key in competitors:
                if competitors[key] == highest_bid:
                    winner = key
            break

    print(f"The winner is {winner} with a bid of ${highest_bid}")

blind_auction()