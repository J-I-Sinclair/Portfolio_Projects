'''The following program reads a csv file, preprocesses the data and
analyses the sentiment of a randomly selected review.
I have also included a function which creates a pie chart using the 
polarity of each review, grouped into seven different categories based
on positivity.'''

# Import the following modules to ensure the code runs
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import random
import matplotlib.pyplot as plt

nlp = spacy.load('en_core_web_sm') # Prep spacy as nlp
nlp.add_pipe('spacytextblob') # This allows us to find polarity

df = pd.read_csv("amazon_product_reviews.csv", low_memory=False) # Read our csv as a dataframe

reviews_data = df['reviews.text'] # Select the relevant column

clean_reviews = reviews_data.dropna() # Drop NaN values

random_sample = random.randint(0, len(clean_reviews)) # Create a random index

# A function for analysing a single review's sentiment
def sentiment_analysis(review):
    print(f'Review text: {review}') # Print review text for user's reference
    review = review.strip() # Strip trailing whitespace
    review_nlp = nlp(review) 
    trim_text = '' # Creates an empty string for concatenation
    
    for token in review_nlp:
        if token.is_stop == False: # Checks if each word is a stop word
            token = token.text.lower()

            # Concatenates with empty string if not a stop word
            trim_text = trim_text + ' ' + str(token)
    trim_text = trim_text.strip() # Trims trailing whitespaces again

    trim_text = nlp(trim_text) # Sets up our new string for analysis
    sentiment = trim_text._.blob.sentiment # Calculates the sentiment
    text_polarity = trim_text._.blob.polarity # Calculates the polarity

    # Prints a message about positivity based on polarity value
    if text_polarity >= 0.75:
        print("This review is very positive")
    elif text_polarity < 0.75 and text_polarity >= 0.25:
        print("This review is positive")
    elif text_polarity < 0.25 and text_polarity > 0:
        print("This review is slightly positive")
    elif text_polarity == 0:
        print("This review is neutral")
    elif text_polarity < 0 and text_polarity >= -0.25:
        print("This review is slightly negative")
    elif text_polarity < -0.25 and text_polarity >= -0.75:
        print("This review is negative")
    elif text_polarity < -0.75:
        print("This review is very negative")

    print(f'Review sentiment: {sentiment}') # Prints sentiment

# Function for creating a pie chart of polarity values
def pie_chart(reviews):

    # Sets up empty variables
    very_positive = 0
    positive = 0
    slightly_positive = 0
    neutral = 0
    slightly_negative = 0
    negative = 0
    very_negative = 0

    for review in reviews:

        # Prepares the review for analysis as seen above
        review = review.strip()
        review_nlp = nlp(review)
        trim_text = ''
        for token in review_nlp:
            if token.is_stop == False:
                token = token.text.lower()
                trim_text = trim_text + ' ' + str(token)
        trim_text = trim_text.strip()
        trim_text = nlp(trim_text)

        # Calculates the polarity and adds to the empty variables above
        text_polarity = trim_text._.blob.polarity
        if text_polarity >= 0.75:
            very_positive += 1
        elif text_polarity < 0.75 and text_polarity >= 0.25:
            positive += 1
        elif text_polarity < 0.25 and text_polarity > 0:
            slightly_positive += 1
        elif text_polarity == 0:
            neutral += 1
        elif text_polarity < 0 and text_polarity >= -0.25:
            slightly_negative += 1
        elif text_polarity < -0.25 and text_polarity >= -0.75:
            negative += 1
        elif text_polarity < -0.75:
            very_negative += 1

    # Prepares values in a list
    values = [very_positive, positive, slightly_positive, neutral, 
              slightly_negative, negative, very_negative]
    
    # Calculates the sum of the values, the percentage of each value of the total.
    total_sum = sum(values)
    percentages = [(value / total_sum) * 100 for value in values]

    # Designates our labels for the piechart
    labels = ['Very Positive', 'Positive', 'Slightly Positive', 
              'Neutral', 'Slightly Negative', 'Negative', 'Very Negative']
    sizes = percentages

    # Creates a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Adds a title
    plt.title('Review Polarity Overview')

    # Shows the plot
    plt.show()

sentiment_analysis(clean_reviews[random_sample])
pie_chart(clean_reviews)