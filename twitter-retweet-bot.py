from twython import Twython
import time

#Get Variables from https://apps.twitter.com/

CONSUMER_KEY = "XXX"
CONSUMER_SECRET = "XXX"
ACCESS_TOKEN = "XXX"
ACCESS_TOKEN_SECRET = "XXX"

# List to be retweetet & Screen Name of Owner Account
ACCOUNT_NAME = "XXX"
LIST_NAME = "XXX"

latest_id = "873315818863566849" # Random Tweet

retweet_counter = 0

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

print("Working...")

while True:

    ids = twitter.get_list_statuses(slug=LIST_NAME, owner_screen_name=ACCOUNT_NAME, include_rts=0, since_id=latest_id)

    if not len(ids) == 0:
        latest_id_save = ids[0]["id"]
        latest_id = str(latest_id_save)

    for i in range(len(ids)):
        if not ids[i]['retweeted']:
            twitter.retweet(id=ids[i]["id_str"])
            retweet_counter += 1
            print("Retweeted", "ID", ids[i]["id_str"], "Retweet Number:", retweet_counter)

    time.sleep(60)
