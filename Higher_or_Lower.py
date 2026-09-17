
import random
from game_data import data
from art import logo,vs

# bring in the game art
print(logo)

score = 0
should_continue = True
ques_B = data[random.randint(0, len(data) - 1)]

while should_continue:

    # get the two questions to compare
    ques_A = ques_B
    ques_B = data[random.randint(0, len(data) - 1)]

    options = {"A":ques_A['name'],"B":ques_B['name']}

    #Check the higher follower_count
    if ques_A['follower_count'] == ques_B['follower_count']:
        ques_B = data[random.randint(0, len(data) - 1)]
    elif ques_A['follower_count'] > ques_B['follower_count']:
        higher_follower  = ques_A['name']
    else:
        higher_follower = ques_B['name']

    # get user's answers
    user_input = input(f"""
 Compare A: {ques_A['name']},{ques_A['description']}, from {ques_A['country']}
 {vs}
 Against B: {ques_B['name']},{ques_B['description']}, from {ques_B['country']}
 Who has more followers, A or B? :
 """).upper()


    # check User's answer

    #def check_answer(user_ans, actual_answer):

    if user_input == "A" and ques_A['name'] == higher_follower:
        score += 1
        is_correct = True
        print(f"Correct!!! Your total score is {score}")


    elif user_input == "B" and ques_B['name'] == higher_follower:
        score += 1
        is_correct = True
        print(f"Correct!!! Your total score is {score}")


    else:
        is_correct = False
        should_continue = False
        print(f"Wrong!!! Your total score is {score}")
            #"Enter a valid answer"

# if is_correct:
#     print(f"Correct!!! Your total score is {score}")
# else:
#     print(f"Wrong!!! Your total score is {score}")

    # user_answer = options[user_input]
    # #total_score = check_answer(user_input, higher)
    #
    # if user_answer != higher:
    #     print(f"You're wrong!!! Your total score is {score}")
    #     should_continue = False
    #
    # else:
    #     print(f"Correct!!! Your total score is {score}")
            #ques_2 = ques_1




