import smtplib


class Email:
    def __init__(self):
        self.EMAIL = "er.koushiksadhu@gmail.com"
        self.KEY = "clloyfyxqxsodxbn"
        self.PORT_NO = 587

    def send(self, recipient, mesg):
        with smtplib.SMTP("smtp.gmail.com", port=self.PORT_NO) as connection:
            connection.starttls()
            connection.login(user=self.EMAIL, password=self.KEY)
            connection.sendmail(
                from_addr=self.EMAIL,
                to_addrs=recipient,
                msg=mesg
            )
            connection.quit()
