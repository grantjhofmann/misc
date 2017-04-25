from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import tweepy
import csv
import sys

#consumer key, consumer secret, access token, access secret.
ckey="nRPMtovBVwdTTYy2BmD9sGTg5"
csecret="wC05xA8aYdvaGDfX6KJ4YOOMOoaXjaKaGaee5ASp1MDJZy2U7t"
atoken="2528946115-kMTAKSOYltZNUEcWNkZxWYQKOu3dAOhOYJnIOmy"
asecret="ppBmfGTiplgBAbc7I6yqZqPETStPL4YS4XdAi2kPz0GzG"


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

#emoji may give trouble when printing (not saving) so creating a translation table
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
stop = 0
f = open('wholefoods_tweets.csv', 'a')
writer = csv.writer(f)
writer.writerow(["id","created_at","text"])
f.close()
#for status in tweepy.Cursor(api.mentions_timeline).items():
# print(status)
#for page in tweepy.Cursor(api.mentions_timeline).pages():
# print(page)
#try:
alltweets = tweepy.Cursor(api.search, q='whole foods', include_entities = True).items()
while True:
    try:
        f = open('wholefoods_tweets.csv', 'a')
        writer = csv.writer(f)
        tweet = alltweets.next()
        outtweets = [tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")]
        writer.writerow(outtweets)
        f.close()
        #print(outtweets)
    except tweepy.TweepError:
        print("sleeping...")
        time.sleep(900)
        
        continue
    except StopIteration:
        break
    
    #for tweet in alltweets:
        #print(str(tweet).translate(non_bmp_map))
        #outtweets = [tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")]
        #writer.writerow(outtweets)
        #print(outtweets)
        #id = tweet.id
#except tweepy.TweepError as e:
    #print(e.reason)

#sleep(900)
#f.close()
