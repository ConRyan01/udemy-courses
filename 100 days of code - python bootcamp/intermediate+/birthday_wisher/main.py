import smtplib

my_email = 'birthday.wisher2024@gmail.com'
password = 'zzfw xuzb lsxw qykm'

with smtplib.SMTP('smtp.gmail.com') as connection: # connects to email providers domain
    connection.starttls() # starts transport layer security
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs='birthday.wisher2024@yahoo.com', 
        msg='subject: Hello!\n\nThis is the body!'
    )
