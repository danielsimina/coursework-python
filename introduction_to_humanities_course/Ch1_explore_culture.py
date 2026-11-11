import re
from collections import Counter

text = """
Paste a passage from Chapter 1 here.
"""

stopwords = {"the", "a", "an", "and", "or", "of", "to", "in", "is", "are", "that",
             "it", "as", "for", "with", "on", "by", "this", "be", "was", "from", "at"}

words = re.findall(r"[a-z']+", text.lower())
counts = Counter(w for w in words if w not in stopwords and len(w) > 2)

for word, n in counts.most_common(15):
    print(f"{word:<15} {n}")