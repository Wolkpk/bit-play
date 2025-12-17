import random

def pickaball():
    balls = ["red", "green", "blue"]
    prob_red = balls.count("red") / len(balls)
    print("the probability of picking a red ball is:", round(prob_red,2))
    result = random.choice(balls)
    print("the random ball picked is:", result)
    if result == "red":
        print("you win, red ball picked")
    else:
        print("you lose, try again")
pickaball()
