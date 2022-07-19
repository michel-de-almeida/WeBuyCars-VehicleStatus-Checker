import pywhatkit
import smtplib, ssl

def sendWhatsAppNotification(number,message):
    pywhatkit.sendwhatmsg_instantly(number, message,tab_close=True)

def sendEmail(port, smtpServer, fromEmail, fromEmailPassword, toEmail, message):
    sslContext = ssl.create_default_context()
    service = smtplib.SMTP_SSL(smtpServer, port, context=sslContext)
    service.login(fromEmail, fromEmailPassword) 

    service.sendmail(fromEmail,toEmail,message)
    service.quit()