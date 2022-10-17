import random
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']*4
for card in deck:
    value = {'2': 2,
    '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
              'Queen': 10, 'King': 10, 'Ace': 10
            }

end_game = False
while end_game == False:
         user_first_card = random.choice(deck)
         user_second_card = random.choice(deck)
         dealer_first_card = random.choice(deck)
         user_score = value[user_first_card] + value[user_second_card]
         dealer_score = value[dealer_first_card]
         print("\nOk. Your first card is a(n)", user_first_card,". Your second card is a",
               user_second_card,". Your score is", user_score)
         print("\nDealer is showing a(n)",dealer_first_card,", and their second card is hidden. "
                                                            "The Dealer's score is", dealer_score)
         while True:
             wants_to_hit = input("Do you want to hit?\n (a) Yes\n (b) No: ")
             if wants_to_hit == "a":
                 user_hit_card = random.choice(deck)
                 user_score += value[user_hit_card]
                 print("You hit a",user_hit_card,". Your new score is", user_score)
                 if user_score > 21:
                     print("Busted. GG.")
                     run_it_back = input("Do you wish to play again?\n (a) Yes\n (b) No: ")
                     if run_it_back == "a":
                         end_game = False
                         break
                     elif run_it_back == "b":
                         end_game = True
                         break
                 elif user_score == 21:
                     print("21. You win.")
                     run_it_back = input("Do you wish to play again?\n (a) Yes\n (b) No: ")
                     if run_it_back == "a":
                         end_game = False
                         break
                     elif run_it_back == "b":
                         end_game = True
                         break
             elif wants_to_hit == "b":
                 dealer_hidden_card = random.choice(deck)
                 dealer_score += value[dealer_hidden_card]
                 print("The Dealer was hiding a",dealer_hidden_card,". The Dealer's new score is", dealer_score)
                 if 21 > dealer_score > user_score:
                     print("You lose.")
                     run_it_back = input("Do you wish to play again?\n (a) Yes\n (b) No: ")
                     if run_it_back == "a":
                         end_game = False
                         break
                     elif run_it_back == "b":
                         end_game = True
                         break
                 elif 21 < dealer_score:
                     print("You win.")
                     run_it_back = input("Do you wish to play again?\n (a) Yes\n (b) No: ")
                     if run_it_back == "a":
                         end_game = False
                         break
                     elif run_it_back == "b":
                         end_game = True
                         break
                 elif dealer_score == user_score:
                     print("Draw.")
                     run_it_back = input("Do you wish to play again?\n (a) Yes\n (b) No: ")
                     if run_it_back == "a":
                         end_game = False
                         break
                     elif run_it_back == "b":
                         end_game = True
                         break
                 elif 21 > dealer_score < user_score:
                     print("You win.")
                     run_it_back = input("Do you wish to play again?\n (a) Yes\n (b) No: ")
                     if run_it_back == "a":
                         end_game = False
                         break
                     elif run_it_back == "b":
                         end_game = True
                         break