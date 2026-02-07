punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    for ch in punctuation_chars:
        word = word.replace(ch, "")
    return word
