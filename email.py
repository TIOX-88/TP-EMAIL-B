import smtplib
tp=smtplib.SMTP('smtp.gmail.com','587')
tp.ehlo()
tp.starttls()
email=str(input("Enter Your Email🥵 : "))
pwd=str(input("Enter Your Password💀 : "))

tp.login(email,pwd)
tmail=str(input("Enter The Mail Address of Victim👹 : "))
msg=str(input("Enter The Message😴 : "))
amount=int(input("Enter The Amount👻 : "))

for i in range(amount):
    tp.sendmail(email,tmail,msg)
    print(str(i+1)+" mail sent😈")
