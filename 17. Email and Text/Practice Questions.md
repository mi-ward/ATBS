1. What is the protocol for sending email? For checking and receiving email?
    SMTP is for sending email. IMAP is for checking and receiving email.

2. What four smtplib functions/methods must you call to log in to an SMTP server?
    smtplib.SMTP(), smtpObj.ehlo(), smtpObj.starttls(), smtpObj.login()

3. What two imapclient functions/methods must you call to log in to an IMAP server?
    imapclient.IMAPClient(), imapObj.login()

4. What kind of argument do you pass to imapObj.search()?
    Strings, specifically IMAP keywords

5. What do you do if your code gets an error message that says got more than 10000 bytes?
    assign a maxvalue

6. The imapclient module handles connecting to an IMAP server and finding emails. What is one module that handles reading the emails that imapclient collects?
    pyzmail

7. When using the Gmail API, what are the credentials.json and token.json files?
    they handle authentication to the gmail API

8. In the Gmail API, what’s the difference between “thread” and “message” objects?
    A message is a single email and a thread is the back and forth.

9. Using ezgmail.search(), how can you find emails that have file attachments?
    use has:attachment

10.  What three pieces of information do you need from Twilio before you can send text messages?
    SID, auth token, phone number