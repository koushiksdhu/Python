import smtplib


class Email:
    def __init__(self):
        self.email = "er.koushiksadhu@gmail.com"
        self.password = "refkbmrbnrotierd"
        self.PORT = 587  # PORT number should be 587.

    def send_mail(self, sender_id, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=sender_id,
                msg=f"Subject: Newsletter from Koushik Sadhu!\n\n{message}"
            )
            connection.quit()
