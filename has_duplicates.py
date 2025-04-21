sentence = "the sky is blue and the grass is green"


words = sentence.lower().split()

has_duplicates = len(words) != len(set(words))

print("Duplicate words found?" , has_duplicates)
