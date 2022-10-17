import random
import time

deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', ]

value = {'2': 2,
         '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
         'Queen': 10, 'King': 10, 'Ace': 11
         }

coins = 500

user_deck = []

user_sum = 0

dealer_deck = []

dealer_sum = 0

dealer_name = 'Dealer'


def initiate_player(coins):
    name = input('Welcome to the casino player. What should I call you?: ')

    time.sleep(1)

    print('\n')

    print(f'Ok {name}, here are {coins} coins to start. Good luck')

    return name


def place_bet(coins):
    bet = int(input('How many coins do you want to bet?: '))

    while bet > coins:
        bet = int(input('Insufficient coin balance. How many coins do you want to bet?: '))

    return bet


def dealer_hit(dealer_deck, dealer_sum):
    first_card = random.choice(deck)

    dealer_deck.append(first_card)

    deck.remove(first_card)


def ask_user():
    wants_to_hit = input('Do you want to hit?: \n a) yes \n b) no: ')

    if wants_to_hit.lower() == 'a':

        return True

    else:

        return False


def user_hit(deck, user_deck, user_sum):
    pulled_card = random.choice(deck)

    user_deck.append(pulled_card)

    user_sum += value[pulled_card]

    deck.remove(pulled_card)

    return (user_deck, user_sum)


def natural_winner(user_deck):
    if (user_deck.count('Ace') == 1) and (user_deck.count('10') == 1):
        return True


def calculate_sum(user_deck):
    s = 0

    for card in user_deck:
        s += value[card]

    if (s > 21) and user_deck.count('Ace') == 2:
        s -= 10

    return s


def find_winner(user1, user2, name1, name2, coins, bet):
    if (user1 > user2) and (user1 <= 21):

        return True


    elif (user1 > user2) and (user1 > 21):

        # print(f'{name2} has won. You now have {coins} coins.')

        return False


    elif (user2 > user1) and (user2 <= 21):

        # print(f'{name2} has won. You now have {coins} coins.')

        return False


    elif (user2 > user1) and (user2 > 21):

        # print(f'Congratulations {name1}. You have won. You now have {coins} coins.')

        return True


    elif (user1 == user2) and (user1 <= 21):

        return None

        # coins = coins

        # print(f'Draw. You still have {coins} coins.')


def main(coins):
    print('\n')

    bet = place_bet(coins)

    print('\n')

    user_hit(deck, user_deck, user_sum)

    user = calculate_sum(user_deck)

    print(
        f'user {one}, Your first card has been dealt. Your current deck is {user_deck}, and your current sum is {user}')

    dealer_hit(dealer_deck, dealer_sum)

    x = calculate_sum(dealer_deck)

    print('\n')

    time.sleep(3)

    print(f'The dealers first card has been pulled. Their deck is {dealer_deck}. Their sum is {x}.')

    user_hit(deck, user_deck, user_sum)

    user = calculate_sum(user_deck)

    print('\n')

    time.sleep(3)

    print(f'user {one}, Your second card has been dealt. Your current deck is {user_deck} current sum is {user}')

    print('\n')

    dealer_hit(dealer_deck, dealer_sum)

    x = calculate_sum(dealer_deck)

    time.sleep(3)

    print(f'The dealer has pulled their second card, but is hiding it. Their deck is {dealer_deck[0]}.')

    print('\n')

    time.sleep(1)

    if natural_winner(user_deck):

        coins = coins

        print(f'You have a natural deck. Your bet is given back to you. You have {coins} coins.')

    else:

        while (user < 21) and (ask_user()):
            print('\n')

            user = calculate_sum(user_deck)

            user_hit(deck, user_deck, user)

            user = calculate_sum(user_deck)

            time.sleep(1)

            print(
                f'Another card has been drawn for {one}. Their current deck is {user_deck}, and their current sum is '
                f'{user}')

            print('\n')

        if user > 21:

            coins -= bet

            time.sleep(1)

            print(f'Sorry {one}, you have lost this round. Your new coin balance is {coins}')

        elif user == 21:

            time.sleep(1)

            print(f'21 has been achieved, your coin balance is still {coins}.')


        else:

            time.sleep(1)

            print(f'The dealer has unveiled their second card. Their deck is {dealer_deck}, and their sum is {x}.')

            print('\n')

            if x >= 17:

                if find_winner(user, x, one, dealer_name, coins, bet) is True:
                    coins += bet
                    print(f'Congratulations {one}. You have won. You now have {coins} coins.')
                elif find_winner(user, x, one, dealer_name, coins, bet) is False:
                    coins -= bet
                    print(f'{dealer_name} has won. You now have {coins} coins.')
                elif find_winner(user, x, one, dealer_name, coins, bet) is None:
                    print(f'Draw. You still have {coins} coins.')


            else:

                while x < 17:
                    dealer_hit(dealer_deck, dealer_sum)

                    x = calculate_sum(dealer_deck)

                    time.sleep(1)

                    print(f'The dealer has pulled another card. Their deck is {dealer_deck}. Their sum is {x}')

                    print('\n')

                if find_winner(user, x, one, dealer_name, coins, bet) is True:
                    coins += bet
                    print(f'Congratulations {one}. You have won. You now have {coins} coins.')
                elif find_winner(user, x, one, dealer_name, coins, bet) is False:
                    coins -= bet
                    print(f'{dealer_name} has won. You now have {coins} coins.')
                elif find_winner(user, x, one, dealer_name, coins, bet) is None:
                    print(f'Draw. You still have {coins} coins.')

    time.sleep(.5)

    print('\n')

    play_again = input('Do you want to play again:\n a) yes \n b) no: ')

    if play_again == 'a' and (coins > 0):
        user_deck.clear()
        dealer_deck.clear()
        main(coins)
    elif play_again == 'a' and (coins <= 0):
        print('Sorry, youre out of coins.')
    else:
        print('Ok. Have a nice day.')


if __name__ == "__main__":
    starting_coins = 1000
    one = initiate_player(starting_coins)
    main(starting_coins)
