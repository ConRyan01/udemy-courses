##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import random
import smtplib
import datetime
import os

PATH = r'C:\Users\ryanc\OneDrive - CCL Industries\Documents\GitHub\udemy-courses\100 days of code - python bootcamp\intermediate+\birthday_wisher'
MY_EMAIL = 'birthday.wisher2024@gmail.com'
MY_PASSWORD = 'hgkz ucrb iozw toev'

df = pd.read_csv(os.path.join(PATH, 'birthdays.csv'))

today = datetime.datetime.now()

# Find birthdays matching today's month and day
matching_bdays = df[(df['month'] == today.month) & (df['day'] == today.day)]

# Get list of letter templates
try:
    files = [file for file in os.listdir(os.path.join(PATH, 'letter_templates')) 
             if os.path.isfile(os.path.join(PATH, 'letter_templates', file))]
except:
    print("No Files in directory")
    files = []

# Send emails if there are matching birthdays and available templates
for _, birthday in matching_bdays.iterrows():
    if files:
        random_letter = random.choice(files)
        
        # Read the template file
        with open(os.path.join(PATH, 'letter_templates', random_letter)) as file:
            content = file.read()
            content = content.replace('[NAME]', birthday['name'])
        
        # Set up the email server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday['email'],
                msg=f"Subject:Happy Birthday!\n\n{content}"
            )
            print(f"Sent birthday email to {birthday['name']}")
