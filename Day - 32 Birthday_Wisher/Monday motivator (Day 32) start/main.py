import smtplib
import datetime as dt
import random

# smtplib
# my_email = "Your mail"
# password = "Your password"
#
# with smtplib.SMTP('outlook.office365.com', port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="recepients mail",
#         msg="Subject:Farewell\n\nThis is a good bye."
#     )

# datetime library
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=2001, month=9, day=13, hour=4)
# print(date_of_birth)


# Monday motivation mail
EMAIL = "Your mail"
PASSWORD = "Your Password"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:
    with open("quotes.txt", "r") as file:
        data = file.read()
        data_into_list = data.split("\n")
        quote = random.choice(data_into_list)
    print(quote)
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Monday motivation\n\n{quote}"
        )
