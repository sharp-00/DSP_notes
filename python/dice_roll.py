import random
from collections import Counter

def roll(n):
    
    outcome = None
    result = [outcome]


    for _ in range(n):
        outcome = random.randint(1,6)
        
        result.append(outcome)

    return result

dice= roll(500)

frequency = Counter(dice)

print(frequency)


prob_1 = frequency[1]/ 500
prob_2 = frequency[2]/ 500
prob_3 = frequency[3]/ 500
prob_4 = frequency[4]/ 500
prob_5 = frequency[5]/ 500
prob_6 = frequency[6]/ 500

print(f"probability of 1 {prob_1}, probability of 2 {prob_2}, probability of 3 {prob_3}, probability of 4 {prob_4}, probability of 5 {prob_5}, probability of 6 {prob_6}")

