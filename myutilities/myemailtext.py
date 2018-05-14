#!/usr/bin/env python3
from twilio.rest import Client

def validate_address(address, messagetype):
    """ Validates email or phone syntax by returning a Boolean value

    Args:
        address (str): 'sms' or 'email' for the type of message one is trying to send
        messagetype (str): senders email adddres or phone number
    
    Returns:
        True or False (bool): returns True if the address is valid and False otherwise

    Example: 
        import myutilities.mymenu as mymenu
        mymenu.mymenu('Test Project', ['JJ Espinoza'], '0.1', 'test.git', {'test': 'test explanation'})  
    """
    if messagetype == 'email' and ('@' not in address or '@' not in address or '.com' not in address or '.com' not in address):
        print('EXIT PROGRAM - invalide email address: {}'.format(address))
        return False
    elif messagetype == 'sms' and ('@' in address or '@' in address or '.com' in address or '.com' in address):
        print('EXIT PROGRAM - invalide email address: {}'.format(address))
        return False
    else:
        return True

def message_builder(messagetype, fromaddr, toaddr, subject, body):
    """Generates the parameters for a message.

    Generates the parameters for a message

    Args:
        type (str): 'sms' or 'email' for the type of message one is trying to send
        fromaddr (str): senders email adddres or phone number
        toaddr (str): recipients of email
        subject (str): subject line of email (only applicable if type = 'email')
        body (str): Text that is to be the subject of the email

    Returns:
        message_info (dict): dictionary of parameters needed to send someone a message

    Example: 
        import myutilities.mymenu as mymenu
        mymenu.mymenu('Test Project', ['JJ Espinoza'], '0.1', 'test.git', {'test': 'test explanation'})  
    """
    if validate_address(fromaddr, messagetype) and validate_address(toaddr, messagetype):
            print('Verified Address Validity')
    else:
        print('Invalid Address')
        return
    message_info = {'fromaddr': fromaddr, 
                    'toaddr': toaddr, 
                    'subject':subject, 
                    'body':body}
    return message_info

def send_email(subject, body, fromaddr, toaddr):
    fromaddr = fromaddr
    #toaddr = ["MiguelAngel.Campo-Rembado@fox.com","abhinav.taliyan@fox.com","JJ.Espinoza@fox.com"]
    toaddr = toaddr
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ", ".join(toaddr)
    msg['Subject'] = subject
    body = body
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    server.starttls()
    server.login(fromaddr, "JOAv4IP4ivQQ")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def send_text(fromaddr, toaddr, body):
    #Find auth codes in evernote
    account_sid = input('Twilio ID: ')
    auth_token = input('Twilio Token: ')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    toaddr,
    body=body,
    from_=fromaddr)
    print(message.sid)

def send_message(messagetype, fromaddr, toaddr, subject, body):
    message_info = message_builder(messagetype, fromaddr, toaddr, subject, body)
    
    if messagetype == 'sms':
        print('Sending SMS Message')
        send_text(fromaddr, toaddr, body)
    elif  messagetype == 'email':
        print('Sending Email')
    return message_info

if __name__ == '__main__':
    messagetype = 'sms'
    fromaddr = '+15555555'
    toaddr = '+15555555'
    subject='My subject'
    body = 'This is a message from Python'

    print(send_message(messagetype=messagetype, fromaddr=fromaddr, 
                    toaddr=toaddr, subject='', 
                    body='This is a text from Python'))


