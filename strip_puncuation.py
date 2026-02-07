punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@'] # lista med tecken som ska filtreras bort från tweetsen

def strip_punctuation(word): # strip_punctuation("today!")      → "today"
    for ch in punctuation_chars:
        word = word.replace(ch, "")
    return word
