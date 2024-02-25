import smtplib
import pandas as pd
import datetime as dt
import random

FILEPATH = '/Users/rezaen/Downloads/birthday-wisher-extrahard-start/letter_templates/'
EMAIL = 'rezaenayatitest@gmail.com'
PASSWORD = "qddz cmwc nfjh ksiw"
SUBJECT = "HAPPY BIRTHDAY!"

now = dt.datetime.now().date()
birthdays = pd.read_csv('birthdays.csv')


def update_letter(name):
    letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
    file = FILEPATH + random.choice(letters)
    try:
        with open(file=file, mode='r') as file:
            letter = file.read()
    except FileNotFoundError as error:
        print(error)
    else:
        letter = letter.replace('[NAME]', name)
    return letter


def send_email(letter, email):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        try:
            connection.login(user=EMAIL, password=PASSWORD)
        except:
            print("ERROR")
        else:
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=email,
                                msg=f"Subject:{SUBJECT}\n\n{letter}")



for i in range(0, len(birthdays)):
    if (birthdays.month[i] == now.month) and (birthdays.day[i] == now.day):
        birthday_letter = update_letter(birthdays.name[i])
        birthday_email = birthdays.email[i]
        send_email(letter=birthday_letter, email=birthday_email)