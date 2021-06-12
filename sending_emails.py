import smtplib

x = smtplib.SMTP('smtp.gmail.com', 587)
myemail = "abdulmalikmohamed360@gmail.com"
receiver_email = "godwin@lifechoices.com"
password = input("Please Enter Password: ")
x.starttls()
x.login(myemail, password)

message = "Hey Mr G\n"
message = message + "Thank You Sir"

x.sendmail(myemail, receiver_email, message)
x.quit()


