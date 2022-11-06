from http import client
import tweepy
import config
import pandas as pd
import numpy
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Players_Sentiment_Data {Name: [Sentiment_Coefficient, Tweet_Count]} 
Players_Sentiment_Data = {}

# get_player_data(first, last, username, tweet_amount) takes an athlete's first name, last name,
#       and twitter username, and returns tweet object containing tweets equivalent to tweet_amount 
#       corresponding to the player
def get_player_data(first, last, username, tweet_amount):
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
    full_name = str(first) + ' ' + str(last)
    query = str(full_name)  + ' -is: retweet' + ' OR ' + str(username) + ' -is: retweet'
    result = client.search_recent_tweets(query=query, max_results=int(tweet_amount), tweet_fields=['text'])
    return result

# get_player_data(first, last, username) takes an athlete's first name, last name,
#       and twitter username, and creates a dataframe for the player containing 100 tweets pulled from twitter,
#       along with adding the player's name and corresponding sentiment analysis on tweets to Player_Sentiment_Data dictionary
def init_player(first, last, username):
    #Retrieves 100 tweets to create db
    result = get_player_data(first, last, username, 100)

    #Initializes playerdatabase
    dataframe = pd.DataFrame( [tweet.text for tweet in result.data], 
                            columns=[str(first) + ' Tweets'])
    pd.set_option('max_colwidth', 200)
    pd.options.display.max_rows = 100000
    sentiment_score = [] #Will be added to df as new column

    #Iterates through db to conduct sentiment analysis
    sentiment = 0
    SIA = SentimentIntensityAnalyzer()
    for ind in dataframe.index:
        assessed_tweet = SIA.polarity_scores(dataframe[str(first) + ' Tweets'][ind])['compound']
        sentiment_score.append(assessed_tweet)
        sentiment += assessed_tweet
    sentiment = (sentiment / 100)

    #Adds sentiment column to df, then exports as CSV
    dataframe['Sentiment Score'] = sentiment_score
    dataframe.to_csv('tweet_data' + str(first) + '.csv')

    #Adds player's sentiment data to dictionary
    Players_Sentiment_Data[str(first)] = [sentiment, 100]
    return dataframe

# add_data(first, last, dataframe) takes an athlete's first name, last name,
#       and twitter username, then updates the player's dataframe with 100 additional tweets requested from tweepy, and updates
#       Sentiment_Coefficient and Tweet_Count in Player_Sentiment_Data dictionary
def add_data(first, last, username, dataframe):
    #Retrieves 100 tweets to add to db
    result = get_player_data(first, last, username, 100)
    
    #Creates temp dataframe to concat to total data
    dataframe_temp = pd.DataFrame([tweet.text for tweet in result.data], 
                                columns=[str(first) + ' Tweets'])
    pd.set_option('max_colwidth', 200)
    pd.options.display.max_rows = 100
    sentiment_score = [] # Will be added to df as new column

    #Conducts sentiment analysis on new tweets
    sentiment = 0
    SIA = SentimentIntensityAnalyzer()
    for ind in dataframe_temp.index:
        assessed_tweet = SIA.polarity_scores(dataframe_temp[str(first) + ' Tweets'][ind])['compound']
        sentiment_score.append(assessed_tweet)
        sentiment += assessed_tweet
    
    #Adds sentiment column to temp df
    dataframe_temp['Sentiment Score'] = sentiment_score

    #Updates dictionary with new opinion coefficient
    sentiment_old = Players_Sentiment_Data[str(first)][0]
    count_oldtweets = Players_Sentiment_Data[str(first)][1]
    new_count = count_oldtweets + 100
    new_sentiment = (sentiment + (sentiment_old * count_oldtweets)) / new_count
    Players_Sentiment_Data[str(first)][0] = new_sentiment
    Players_Sentiment_Data[str(first)][1] = new_count

    #Concatenates temp dataframe into existing data
    dataframe = pd.concat([dataframe, dataframe_temp], ignore_index=True)
    dataframe.to_csv('tweet_data' + str(first) + '.csv')

    return dataframe

# show_rankings() iterates through Player_Sentiment_Data dictionary
#       and prints players rankings in order
def show_rankings():
    i = 1
    for k, v in sorted(Players_Sentiment_Data.items(), key = lambda x:x[1][0], reverse = True):
        print("#" + str(i) + ") " + k, '-->', v[0])
        i += 1




df_steph = init_player('Steph', 'Curry', '@StephenCurry30')
df_steph = add_data('Steph', 'Curry', '@StephenCurry30', df_steph)

df_lebron = init_player('Lebron', 'James', '@KingJames')
df_lebron = add_data('Lebron', 'James', '@KingJames')

df_kevin = init_player('Kevin', 'Durant', '@KDTrey5')
df_kevin = add_data('Kevin', 'Durant', '@KDTrey5')

show_rankings()




