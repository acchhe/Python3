negative_words = []

with open("assets/negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(text):
    count = 0
    words = text.split()

    for word in words:
        word = strip_punctuation(word.lower())
        if word in negative_words:
            count += 1

    return count
