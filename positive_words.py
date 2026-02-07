positive_words = [] # skapar tom lista som ska fyllas med positiva orden.

with open("assets/positive_words.txt") as pos_f: #Öppnar text-filen. "assets/ är sökvägen till filen.
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n': # Kollar första tecknet i raden. Två saker ignoreras: 1- rader som börjar med ; 2- (kommentarer) tomma rader (\n = radbrytning)
            positive_words.append(lin.strip()) # tar bort mellanslag och \n "happy\n" → "happy" append(...): lägger till ordet i listan

def get_pos(text):
    count = 0
    words = text.split() # delar in meningen i ord som returneras i lista.

    for word in words:
        word = strip_punctuation(word.lower()) # tar bort otillåtna tecken för varje ord samt tar bort versaler.
        if word in positive_words:
            count += 1 # räknar upp antalet gånger ett positivt ord förekommer.

    return count # returnerar antalet orden som finns i listan word.
