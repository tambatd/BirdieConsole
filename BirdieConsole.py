# -*- coding: utf-8 -*-
import tweepy
import os

 
api_key = ""
api_secrets = ""
access_token = ""
access_secret = ""
 
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
  
def tweeter():
  tweet = input("🐦: ")
  if tweet == "exit":
    exit()
  api.update_status(tweet)
  print("✨ Tweet Sent ✨")
  tweeter()

def main():
    os.system('clear')
    tweeter()

if __name__ == "__main__":
    main()
