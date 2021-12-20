
import smtplib

# This will setup the domain and port number(domain, portnumber)
smtpobj = smtplib.SMTP("smtp.gmail.com",587) 
smtpobj.ehlo()

# To put the smtp in the Tls mode
smtpobj.starttls()

#To set the login credientals
smtpobj.login("anonymus9604@gmail.com","Saikiran@9604") # --> str: ("usergmail","password")

#To send the mail
smtpobj.sendmail("anonymus9604@gmail.com","shivkounsalye@gmail.com",'Sub : Hi Team') # --> str: ("sendersmail","recieversmail","sub:")

# to quit the mail
smtpobj.quit()

print("Email Sent sucessfully")
