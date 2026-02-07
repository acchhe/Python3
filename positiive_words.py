positive_words = []

with open("assets/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(text):
    count = 0
    words = text.split()

    for word in words:
        word = strip_punctuation(word.lower())
        if word in positive_words:
            count += 1

    return count
