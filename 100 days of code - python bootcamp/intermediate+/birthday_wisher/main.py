##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas, random, smtplib, datetime, os

PATH = 'C:\\Users\\ryanc\\OneDrive - CCL Industries\\Documents\\GitHub\\udemy-courses\\100 days of code - python bootcamp\\intermediate+\\birthday_wisher\\letter_templates'
MY_EMAIL = 'birthdaywisher2024@gmail.com'

df = pandas.read_csv('birthdays.csv')

today = datetime.datetime.now()

try:
    matching_months = df[df['month'] == today.month]
    matching_bdays = matching_months[matching_months['day'] == today.day]
except:
    print("No Birthdays Today")

try:
    files = [file for file in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, file))]
except:
    print("No Files in directory")

for birthday in matching_bdays:
    if files:
        random_letter = random.choice(files)

    with open(PATH + "\\" + random_letter) as file:
        content = file.read()
        content.replace('[NAME]', birthday['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login()