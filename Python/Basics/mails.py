# sending mails using smtplib

import smtplib

# for gmail - turnoff all other authentication except for password
#           - Turn on less secure app access
# for yahoo - Account -> account scurity --> generate a new app password
#           - this password will be used in password field
my_email = "mohitdemo7@gmail.com"
password = "demopassword"

# first argument - location of smtp of email provider
# smtp.mail.yahoo.com - smtp of yahoo
with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls() # transport layer service -- makes connection secure
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="mohitdemo7@yahoo.com", 
        msg="Subject:Hello\n\nThis is the body of mail."
    )
