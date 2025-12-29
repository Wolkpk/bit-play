def find_prob(a, b):
    if a == 1:
        prob_a = 0.2
        if b == 1:
            prob_b_given_a = 0.85
        elif b == 2:
            prob_b_given_a = 0.15
        else:
            print("Invalid Choice")
        print(prob_b_given_a)
        prob_a_and_b = prob_a*prob_b_given_a
        print(prob_a_and_b)
    elif a == 2:
        prob_a = 0.8
        if b == 1:
            prob_b_given_a = 0.02
        elif b == 2:
            prob_b_given_a = 0.98
        else:
            print("Invalid Choice")
        print(prob_b_given_a)
        prob_a_and_b = prob_a*prob_b_given_a
        print(prob_a_and_b)

print("Person has step throat? \n 1. Yes \n 2. No")

a = int(input("Enter your choice (1/2): "))

print("Person has tested positive? \n 1. Yes \n 2. No")

b = int(input("Enter your choice (1/2): "))

print("Probabilities for event a and b:")

find_prob(a,b)