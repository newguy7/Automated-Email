import os
import yagmail
import pandas
import datetime
import time

from dotenv import load_dotenv
from news import NewsFeed

load_dotenv()

user = os.environ.get('EMAIL')
password = os.environ.get('APP_PASSWORD')

# Send the email autoamtically at a specific time
def send_email():
    current_date=(datetime.datetime.now()).strftime('%Y-%m-%d')

            # current_date - 1; days=1(value of how many days behind from todays date)
    start_date = datetime.datetime.now() - datetime.timedelta(days=1)
    news_feed = NewsFeed({row['interest']}, 
                                from_date=start_date, 
                                to_date=current_date, 
                                language='en')
    email = yagmail.SMTP(user=user,password=password)
    email.send(to=row['email'],
                        subject=f"Your {row['interest']} news for today!",
                        contents=f"Hi {row['name']},\n See what's on about {row['interest']} today.\n\n {news_feed.get()}\nRegards")

while True:
    if datetime.datetime.now().hour == 20 and datetime.datetime.now().minute == 48:
        df = pandas.read_excel("people.xlsx")

        # iterate through the excel file and access the interest, email and name
        for index, row in df.iterrows():
            # print(row[1])
            send_email()

    time.sleep(60)
    

