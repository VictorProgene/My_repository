import smtplib

from_my_email = "your sender E-mail"
to_email = "your receiver E-mail"
passwword = "your password"



def iss_notification():

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(from_my_email, passwword)
        connection.sendmail(from_addr=from_my_email, to_addrs=to_email,
                            msg=f"Subject: ISS Location\n\nLook up, ISS is over your heads!")