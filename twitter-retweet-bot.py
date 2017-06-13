from twython import Twython, TwythonError
import time, os

#Add Variables

f = open("config.ini", "r")
lines = f.read().splitlines()
CONSUMER_KEY = lines[0]
CONSUMER_SECRET = lines[1]
ACCESS_TOKEN = lines[2]
ACCESS_TOKEN_SECRET = lines[3]

ACCOUNT_NAME = lines[4]
LIST_NAME = lines[5]

RETWEET_COUNTER = int(lines[6])
LATEST_ID = lines[7]

f.close()

try:
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    initiated = True
except TwythonError as e:
    initiated = False
    if e.error_code != "400":
        print("Error " + e.error_code)

if initiated:
    print("Working...")

    while True:
        try:
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
            f1.write(CONSUMER_KEY + '\n')
            f1.write(CONSUMER_SECRET + '\n')
            f1.write(ACCESS_TOKEN + '\n')
            f1.write(ACCESS_TOKEN_SECRET + '\n')
            f1.write(ACCOUNT_NAME + '\n')
            f1.write(LIST_NAME + '\n')
            f1.write(str(RETWEET_COUNTER) + '\n')
            f1.write(LATEST_ID + '\n')
            f1.close()
            os.remove("config.ini")
            os.rename("config_tmp", "config.ini")

        except TwythonError as e:
            print(e.error_code)

        time.sleep(60)
else:
    print("Initiation Failed. Please check your connection / settings.")
    input("Press Enter to continue...")