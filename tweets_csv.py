import csv

# öppna csv-filen med twitterdata
with open("project_twitter_data.csv", "r") as infile: # öppnar csv-filen
    reader = csv.reader(infile) # Skapar en csv-läsare (reader) som kan läsa filen rad för rad.
    header = next(reader)  # hoppa över första raden (rubriker) / läsen in rubrikerna till header. Den första raden innehåller ofta rubriker, t.ex.: ["tweet_text", "retweet_count", "reply_count"]. Huvudpoängen: du hoppar över rubrikerna så loopen börjar på riktig data.
    
    # skapa en lista för att lagra all bearbetad data
    result_data = [] # Skapar en tom lista där du ska lägga in alla “bearbetade rader” (resultatet). Varje element som läggs in kommer vara en lista, t.ex.: [retweets, replies, pos, neg, net]
    
    # loopen läser varje tweet / Exempel på en rad i filen kan bli: ["I love sunny days!", "3", "1"]
    for row in reader: # Varje row är en lista med kolumnerna från filen.
        tweet = row[0]           # Tar första kolumnen från raden → själva tweet-texten. Exempel: tweet = "I love sunny days!"
        retweets = int(row[1])   # antal retweets Tar andra kolumnen, som är antal retweets. Den kommer in som en sträng (t.ex. "3"), så du gör int(...) för att få ett heltal 3.
        replies = int(row[2])    # Tar tredje kolumnen, antal replies.  Också sträng → görs till heltal.
    
        # beräkna sentimentpoäng
        positive_score = get_pos(tweet) # Anropar din funktion get_pos. Den räknar hur många positiva ord som finns i tweeten.
        negative_score = get_neg(tweet) # Anropar get_neg. Den räknar hur många negativa ord som finns i tweeten.
        net_score = positive_score - negative_score # Räknar netto-känslan: positivt minus negativt Exempel: om pos = 4 och neg = 1 → net = 3 (mer positiv) om pos = 1 och neg = 3 → net = -2 (mer negativ)
        
        # spara raden som en lista
        result_data.append([retweets, replies, positive_score, negative_score, net_score]) # Lägger in en ny rad i din resultatlista. Du sparar en lista med exakt de värden du vill ha i output-filen. Exempel: [3, 1, 2, 0, 2]

# skriv resultatet till ny csv-fil
with open("project_twitter_data.csv", "w", newline='') as outfile: # newline='' är viktigt i Windows för att undvika tomma rader mellan raderna i CSV.
    writer = csv.writer(outfile) # Skapar en csv-skrivare som kan skriva rader till filen.
    writer.writerow(["Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score"]) #  Skriver första raden i outputfilen = rubrikerna. Den raden blir kolumnnamnen i den nya CSV-filen.
    writer.writerows(result_data) # Skriver alla rader från result_data till filen, en per tweet. writerows betyder “skriv många rader”.


Din resulting_data.csv kommer få formatet:

Number of Retweets	Number of Replies	Positive Score	Negative Score	Net Score
…	…	…	…	…
