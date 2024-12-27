import argparse

def get_bool_input(prompt):
    """ Get a boolean input from the user. [Y/n], empty input is considered as yes."""
    while True:
        choice = input("[Y/n] " + prompt).lower()
        if choice in {"", "y"}:
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid input, please enter y or n.")

def get_int_input(prompt, min_val, max_val):
    """ Get an integer input from the user. """
    while True:
        try:
            choice = int(input(f"[{min_val}-{max_val}] " + prompt))
            if min_val <= choice <= max_val:
                return choice
            else:
                print("Invalid input, please enter a valid number.")
        except ValueError:
            print("Invalid input, please enter a valid number.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Oh Hell Scoring System")

    # Four players
    parser.add_argument("name1", help="The name of the first player")
    parser.add_argument("name2", help="The name of the second player")
    parser.add_argument("name3", help="The name of the third player")
    parser.add_argument("name4", help="The name of the fourth player")

    # Optional arguments
    parser.add_argument("--win-metric", type=str, default="5+x**2", help="How to calculate the winning score. Default 5+x**2")
    parser.add_argument("--lose-metric", type=str, default="5*sum(range(x+1))", help="How to calculate the losing score. Default 5*sum(range(x+1))")

    args = parser.parse_args()

    print("""
  ____  __     __ __    ______
 / __ \/ /    / // /__ / / / /
/ /_/ / _ \  / _  / -_) / /_/ 
\____/_//_/ /_//_/\__/_/_(_)  
""")

    print("Configuration:")
    print(f"Winning metric: {args.win_metric}")

    def w_score(x):
        return eval(args.win_metric.replace("x", str(x)))

    print(f"Losing metric: {args.lose_metric}")
    print()

    def l_score(x):
        return eval(args.lose_metric.replace("x", str(x)))

    players = [args.name1, args.name2, args.name3, args.name4]

    print("Players:")
    for i, player in enumerate(players):
        print(f"{i+1}. {player}")
    
    total_scores = {
        args.name1: 0,
        args.name2: 0,
        args.name3: 0,
        args.name4: 0
    }

    curr = get_int_input("Who deals first? ", 1, 4) - 1

    # Game loop, 1 to 13 hands
    for round in range(1, 14):
        round_name = f" Round {round} "
        padding = (80 - len(round_name)) // 2
        print("="*padding + round_name + "="*padding)

        # Bidding phase
        print("===== Bidding Phase =====")
        while True:
            bids = []
            for i in range(4):
                bid = get_int_input(f"{players[(curr + i) % 4]:<10} bid: ", 0, round)
                bids.append(bid)

            if sum(bids) == round:
                print("Total bids cannot be equal to the round number, please bid again.")
            else:
                break
        
        # Trick phase
        print("===== Trick Phase =====")
        while True:
            tricks = []
            for i in range(4):
                trick = get_int_input(f"{players[(curr + i) % 4]:<10} tricks: ", 0, round)
                tricks.append(trick)

            if sum(tricks) != round:
                print("Total tricks must be equal to the round number, please enter again.")
            else:
                break

        # Scoring phase
        print("===== Scoring Phase =====")
        for i in range(4):
            if bids[i] == tricks[i]:
                total_scores[players[(curr + i) % 4]] += w_score(bids[i])
                print(f"{players[(curr + i) % 4]:<10} hit  {bids[i]} and wins {w_score(bids[i])}")
            else:
                total_scores[players[(curr + i) % 4]] -= l_score(abs(bids[i] - tricks[i]))
                print(f"{players[(curr + i) % 4]:<10} miss {abs(bids[i] - tricks[i])} and lose {l_score(abs(bids[i] - tricks[i]))}")
        
        # Print total scores
        print(f"Round {round} scores:")
        for player in players:
            print(f"{player:<10}: {total_scores[player]}")

        curr = (curr + 1) % 4
    
    # Who won
    max_score = max(total_scores.values())
    winners = [player for player in players if total_scores[player] == max_score]
    print(f"The winner(s) are: {', '.join(winners)}")