TEXT = "the cat sat on the mat and the cat ate the fish and the dog sat on the rug"
WORDS = TEXT.split()

TEST_WORDS = [
    ("the", "cat"),
    ("sat", "on"),
    ("and", "the"),
    ("dog", "sat"),
    ("pizza", "the"),
    ("cat", "ate"),
]

def build_bigrams(words):
    model = {}

    for current, following in zip(words, words[1:]):
        if current not in model:
            model[current] = {}

        model[current][following] = model[current].get(following, 0) + 1

    return model

BIGRAMS = build_bigrams(WORDS)

print("Word Pairs:")
print(BIGRAMS.get("the"), BIGRAMS.get("pizza", "not found"))

def probabilities(word):
    result = {}
    counts = BIGRAMS.get(word, {})
    total = sum(counts.values())

    if total == 0:
        return result

    for following, count in counts.items():
        result[following] = count / total

    return result

print("\nNext Word Chances:")
print({w: round(p, 2) for w, p in probabilities("the").items()})

def predict(word):
    chances = probabilities(word)

    if not chances:
        return "the"

    return max(chances, key=chances.get)

print("\nWord Predictions:")
print(predict("the"), "|", predict("pizza"))

print("\nPrediction Tests:")
mistakes = 0

for word, wanted in TEST_WORDS:
    answer = predict(word)

    if answer != wanted:
        mistakes += 1

    print(f"{word} -> {answer}")

print(f"Mistakes: {mistakes} out of {len(TEST_WORDS)}")
