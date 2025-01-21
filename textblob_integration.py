from textblob import TextBlob

text = "What are the latest updates on the crisis"
blob = TextBlob(text)

# Sentiment analysis
print("Sentiment:", blob.sentiment)

# Basic noun phrase extraction
print("Noun phrases:", blob.noun_phrases)
