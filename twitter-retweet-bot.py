from twython import Twython
import time, os

#Add Variables

f = open("config.txt", "r")

CONSUMER_KEY = f.readline()
CONSUMER_SECRET = f.readline()
ACCESS_TOKEN = f.readline()
ACCESS_TOKEN_SECRET = f.readline()

ACCOUNT_NAME = f.readline()
LIST_NAME = f.readline()

RETWEET_COUNTER = f.readline()
LATEST_ID = f.readline()

f.close()

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

print("Working...")

while True:

    ids = twitter.get_list_statuses(slug=LIST_NAME, owner_screen_name=ACCOUNT_NAME, include_rts=0, since_id=LATEST_ID)

    if not len(ids) == 0:
        LATEST_ID_SAVE = ids[0]["id"]
        LATEST_ID = str(LATEST_ID_SAVE)

    for i in range(len(ids)):
        if not ids[i]['retweeted']:
            twitter.retweet(id=ids[i]["id_str"])
            RETWEET_COUNTER += 1
            print("Retweeted", "ID", ids[i]["id_str"], "Retweet Number:", RETWEET_COUNTER)

    f1 = open("config_tmp", "w")
    f1.write(CONSUMER_KEY)
    f1.write(CONSUMER_SECRET)
    f1.write(ACCESS_TOKEN)
    f1.write(ACCESS_TOKEN_SECRET)
    f1.write(ACCOUNT_NAME)
    f1.write(LIST_NAME)
    f1.write(RETWEET_COUNTER)
    f1.write(LATEST_ID)
    f1.close()
    os.remove("config.txt")
    os.rename("config_tmp", "config.txt")

    time.sleep(60)
