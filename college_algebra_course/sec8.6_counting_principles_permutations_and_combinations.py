import math
import itertools

# 1. Fundamental Counting Principle
# Example: 4 shirts, 3 pairs of pants, 2 pairs of shoes
shirts, pants, shoes = 4, 3, 2
total_outfits = shirts * pants * shoes
print(f"Total Outfits: {total_outfits}")

# 2. Permutations vs. Combinations (Choosing r = 3 from n = 10)
n, r = 10, 3
print(f"Permutations P({n}, {r}) [Order matters]: {math.perm(n, r)}")
print(f"Combinations C({n}, {r}) [Order ignored]: {math.comb(n, r)}")

# 3. Distinguishable Permutations (e.g., letters in "MISSISSIPPI")
word = "MISSISSIPPI"
n_letters = len(word)
# Frequencies: M=1, I=4, S=4, P=2
distinguishable = math.factorial(n_letters) // (
    math.factorial(1) * math.factorial(4) * math.factorial(4) * math.factorial(2)
)
print(f"Distinguishable arrangements of '{word}': {distinguishable}")

# 4. Explicit Enumeration on {'A', 'B', 'C', 'D'} choosing 2
items = ['A', 'B', 'C', 'D']
perms = list(itertools.permutations(items, 2))
combs = list(itertools.combinations(items, 2))

print(f"\nPermutations of 2 from {items} ({len(perms)}):")
print(perms)

print(f"\nCombinations of 2 from {items} ({len(combs)}):")
print(combs)