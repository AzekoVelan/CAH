import random
from cah_data import black_cards, white_cards


#rozdanie kart białych (7 sztuk / ręka)
def deal_hands(players, hand_size = 7):
    return {player:random.sample(white_cards, hand_size) for player in players}
    
# jedna runda i losowanie czarnej karty
def runda(players, hands, czar_index):
    czar = players[czar_index]
    black_card = random.choice(black_cards)
    print(f"\n Black Card: {black_card}")
    print(60 * "=")
    print(f"The {czar} is the Czar in this round.")
    print(60 * "=")

    #wybór białej karty przez graczy
    submissions = {}
    for player in players:
        if player == czar:
            continue
        
        print(f"\n{player}'s hand: ")
        for index, card in enumerate(hands[player]):
            print(f"{index + 1}. {card}")

        #prosi gracza o wybór karty                                               
        hand_size = len(hands[player])
        hint = f"{player}, choose a white card (1-{hand_size}): "

        while True:
            try:
                choice = int(input(hint)) - 1
                if 0 <= choice < hand_size:
                    break
                else:
                    print("Invalid choice, try again.")
            except ValueError:
                print("Please enter a number.")

        submissions[player] = hands[player].pop(choice)

    print("\nSubmissions: ")
    shuffled = list(submissions.items())
    random.shuffle(shuffled)
    for i, (player, card) in enumerate(shuffled):
        print(f"{i + 1}. {card}")
        
        #Czar wybiera zwycięzce                                                      
    num_choices = len(shuffled)
    hint = f"\n{czar}, choose the best response (1-{num_choices}): "

    while True:
        try:
            winner_choice = int(input(hint)) - 1
            if 0 <= winner_choice < num_choices:
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

    winner = shuffled[winner_choice][0]
    print(f"\n🏆 {winner} wins the round!")
    return winner 
        
# mózg i logika
def main():
    
    print("""====== WELCOME TO THE CARDS AGAINST HUMANITY ======""")
    players = input("Enter player names (comma-separated): ").split(",")
    players = [p.strip() for p in players] 

    hands = deal_hands(players) 
    scores = {player: 0 for player in players} 

    round_count = 3                                             #liczba rund
    for i in range(round_count):
        print(f"\n========= ROUND {i+1} =========")
        czar_index = i % len(players) 
        winner = runda(players, hands, czar_index)
        scores[winner] += 1 

    print("\n=== Final Scores ===")
    for player, score in scores.items():
        print(f"{player}: {score}")

if __name__ == "__main__":
    main()

