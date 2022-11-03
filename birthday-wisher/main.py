# smtplib domains: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
import random
import datetime as dt
import smtplib

import pandas as pd

# You can use env or fill it  with your info in plain text
my_email = ""
password = ""
my_name = ""


actual_date = dt.datetime.now()
actual_day = actual_date.day
actual_month = actual_date.month
data_frame = pd.read_csv("birthdays.csv")
data_dict = {(row.month, row.day): row.to_dict() for (index, row) in data_frame.iterrows()}
# Here you can add letters
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]


def birthday_today(bth_date=(0, 0)):
    global actual_day, actual_month
    if bth_date == (actual_month, actual_day):

        return True


for month, day in data_dict:
    if birthday_today((month, day)):
        with open(f"letter_templates/{random.choice(letters)}") as fl:
            # Extract the name of the person
            name = data_dict[(month, day)]["name"]
            text = fl.read()
            text = text.replace("[NAME]", f"{name}")
            text = text.replace("[ME]", f"{my_name}")
            print(text)
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="alejandro-perry2011@hotmail.com",
                                msg=f"Subject:Daily Message\n\n{text}")






