import smtplib
import getpass
from email.mime.text import MIMEText

def fun1(l):
    sender=input("enter sender's email address(use outlook mail)=")
    password=getpass.getpass()
    sub=input("enter subject:")
    msg=input("enter message:\n")
    print()
    try:
        server=smtplib.SMTP('smtp.outlook.com',587)
        server.starttls()
        server.login(sender,password)
        msg=MIMEText(msg)
        for i in l:
            msg['Subject']=sub
            msg['From']=sender
            msg['To']=i
            msg.set_param('importance','high value')
            server.sendmail(sender,i,msg.as_string())
            print(f"email to {i} has been sent")
            print()
        print("all mails have been sent")
    except:
        print("there is some problem in sending emails. Please try again")

l=[]
n=int(input("enter number of recipient="))
for x in range(n):
    y=input(f"enter email id of recipient {x+1}=")
    l.append(y)
if(n>0):
    fun1(l)
