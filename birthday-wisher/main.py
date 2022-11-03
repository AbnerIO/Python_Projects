##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
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






