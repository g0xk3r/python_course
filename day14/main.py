import random
import game_data
import art

def get_type():
    type = random.choice(game_data.data)
    return type

def compare(type1, type2, score):
    print(f"Compare A: {type1['name']}, a {type1['description']}, from {type1['country']}.")
    print(art.vs)
    print(f"Against B: {type2['name']}, a {type2['description']}, from {type2['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer.lower() == 'a':
        if type1['follower_count'] > type2['follower_count']:
            print(f"You are right! Current score: {score + 1}")
            return True
        elif type1['follower_count'] < type2['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}")
            return False
        else:
            print(f"A and B have the same number of followers. You are right! Current score: {score + 1}")
            return True
    elif answer.lower() == 'b':
        if type2['follower_count'] > type1['follower_count']:
            print(f"You are right! Current score: {score + 1}")
            return True
        elif type2['follower_count'] < type1['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}")
            return False
        else:
            print(f"A and B have the same number of followers. You are right! Current score: {score + 1}")
            return True

def main():
    score = 0
    game_continue = True
    type1 = get_type()
    type2 = get_type()
    while game_continue:
        print(art.higer_lower)
        game_continue = compare(type1, type2, score)
        if game_continue:
            score += 1
            type1 = type2
            type2 = get_type()
        else:
            break

main()