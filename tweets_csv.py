import csv

# öppna csv-filen med twitterdata
with open("project_twitter_data.csv", "r") as infile:
    reader = csv.reader(infile)
    header = next(reader)  # hoppa över första raden (rubriker)
    
    # skapa en lista för att lagra all bearbetad data
    result_data = []
    
    # loopen läser varje tweet
    for row in reader:
        tweet = row[0]           # texten i tweeten
        retweets = int(row[1])   # antal retweets
        replies = int(row[2])    # antal replies
        
        # beräkna sentimentpoäng
        positive_score = get_pos(tweet)
        negative_score = get_neg(tweet)
        net_score = positive_score - negative_score
        
        # spara raden som en lista
        result_data.append([retweets, replies, positive_score, negative_score, net_score])

# skriv resultatet till ny csv-fil
with open("resulting_data.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    # skriv rubrikerna
    writer.writerow(["Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score"])
    # skriv all data
    writer.writerows(result_data)
