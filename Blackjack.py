import random
from logo import art

def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def display_results(user_score, computer_score):
    if user_score == 21 and len(user_cards) == 2:
        return "Blackjack! You Win!"
    elif computer_score == 21 and len(computer_cards) == 2:
        return "Blackjack! You Lose!"
    elif user_score > 21:
        return "You Lose!"
    elif computer_score > 21:
        return "You Win!"
    elif user_score > computer_score:
        return "You Win!"
    elif user_score < computer_score:
        return "You Lose!"
    else:
        return "It's a Draw!"
    
print(art)
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(get_card())
    computer_cards.append(get_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")


while user_score < 21:
    another_card = input("Do you want to get another card? Type 'y' for yes, 'n' for no: ")
    if another_card == 'y':
        user_cards.append(get_card())
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
    else:
        break

while computer_score < 17:
    computer_cards.append(get_card())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(display_results(user_score, computer_score))
