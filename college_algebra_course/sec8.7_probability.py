import math

# 1. Permutations and Combinations Demonstration
def nPr(n, r):
    return math.perm(n, r)

def nCr(n, r):
    return math.comb(n, r)

print("Permutation P(5, 3):", nPr(5, 3))
print("Combination C(5, 3):", nCr(5, 3))

# 2. Card Probability Example: Probability of drawing 4 cards of the same suit from a 52-card deck
total_hands = nCr(52, 4)
favorable_hands = 4 * nCr(13, 4)  # 4 suits, choosing 4 cards from 13 in each suit
prob_suit = favorable_hands / total_hands
print(f"Probability of 4 cards of the same suit: {favorable_hands}/{total_hands} ≈ {prob_suit:.4f}")

# 3. Dice Roll Example: Probability of rolling a sum of 8 with two six-sided dice
dice_outcomes = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7)]
sum_8_outcomes = [pair for pair in dice_outcomes if sum(pair) == 8]
prob_sum_8 = len(sum_8_outcomes) / len(dice_outcomes)
print(f"Probability of rolling a sum of 8: {len(sum_8_outcomes)}/{len(dice_outcomes)} ≈ {prob_sum_8:.4f}")