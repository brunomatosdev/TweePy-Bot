import tweepy
import time
import random
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
  

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def read_tweets_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tweets = file.readlines()
    return [tweet.strip() for tweet in tweets]

def post_tweet(client, tweet):
    try:
        response = client.create_tweet(text=tweet)
        print("Tweet postado:", response)
    except Exception as e:
        print(f"Erro ao postar tweet: {e}")

def main():
    tweets_file_path = "tweets.txt"
    tweets = read_tweets_from_file(tweets_file_path)
    used_tweets = set()

    while True:
        unused_tweets = list(set(tweets) - used_tweets)
        if not unused_tweets:
            print("Todos os tweets foram usados. Reiniciando.")
            used_tweets = set()

        random.shuffle(unused_tweets)
        tweet = unused_tweets[0]

        try:
            post_tweet(client, tweet)
            used_tweets.add(tweet)
        except Exception as e:
            print(f"Erro ao postar tweet: {e}")

        print("Esperando 4 horas...")
        time.sleep(4 * 60 * 60)

if __name__ == "__main__":
    main()