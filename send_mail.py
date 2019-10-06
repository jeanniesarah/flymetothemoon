import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'd21e072e198d22'
    password = 'e6508470dc18aa'
    message = f"<h3>New Feedback Submission</h3><ul><li>Passenger: {customer}</li><li>Astronaut: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'hello@jeannierombough.com'
    receiver_email = 'jeannie.wesell@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Fly Me To The Moon Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
