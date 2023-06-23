import smtplib
import random
import datetime as dt
# ------------------------------------------------ CONSTANTS ------------------------------------------------------

email = "ksprojecttesting@gmail.com"
password = "kgnpcimslpnaxtrh"

PORT = 587      # PORT number should be 587.


# ------------------------------------------------ NOTES ----------------------------------------------------------

# SMTP (Simple Mail Transfer Protocol): Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers.
# Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
# Connection: smtplib.SMTP(host = '', port = 0, local_hostname = None, [timeout,] source_address = None)
# Locations of SMTP server for different email providers:
    # Gmail: smtp.gmail.com
    # Yahoo: smtp.mail.yahoo.com
    # Hotmail: smtp.live.com
    # Outlook: outlook.office365.com
# TLS(Transport Layer Security): It is now deprecated predecessor. It is a way of securing our connection to email server. If somebody tries to intercept in between and tries to read it then he/she cannot read it as it is being encrypted using TLS. It is basically used to make our connection secure.
# SSL(Secured Sockets Layer): It is a cryptographic protocolsdesigned to provide communication security over a computer network.
# Sender: from_addr
# Recipient: to_addrs

# Google by default don't allow outsider provider to access the mail service. so, you need to lower the security by going to Manage Google Account >> Security >> Less Secure App Access should be ON.
# This feautre will not work nowadays because google and also other email service providers has stopped providing the feautre of less secure app access from May, 2022.
# New Feautre added i.e., App password which you will get after 2 step verification in Google under Security page.

# -----------------------------------------------------------------------------------------------------------------

# connection = smtplib.SMTP("smtp.gmail.com")     # Creating object of the class by providing the necessary parameters.
# We can also write the above line by using with keyword:


weekday = dt.datetime.now().weekday() + 1

if weekday == 7:        # if current day is Monday then, perform the below operations
    with open("quotes.txt") as quotes: 
        all_quotes = quotes.readlines()             # It returns a list of all the quotes.
        random_quote = random.choice(all_quotes)    # No need to declare global to use outside because global declaration is only required in function not in the case of opening file using with keyword.
    
    with smtplib.SMTP("smtp.gmail.com", port = PORT) as connection:
        connection.starttls()                           # For making our connection secure by encrypting using Transport Layer Security.
        connection.login(user = email, password = password)      # Logging in with provided credentials.
        connection.sendmail(
            from_addr = email,
            to_addrs = "kkoushikssadhu@gmail.com",
            msg = f"Subject: Monday Motivation.\n\n{random_quote}"
        )
        connection.quit()
    
    


