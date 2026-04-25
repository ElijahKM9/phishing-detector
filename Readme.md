1.  User inputs email 3 parts (first line sender, 2nd line subject, 3rd line and beyond text body)

2.  input is tested first for in or out of organization based on user's own email
3.  subject and body are both checked for indicators of urgency by read a dictionary file of common urgent words
4.  any links contained in the text body are displayed back to user for a long with thiings to look out for in links in addition to flag anything in the link if it is not .com, .ca .gov or .org

5.  The email is assign a risk score based on the above indicators

Sendertest file contains the function for testing the sender email address based on the users email address and if it is associated with a non popular provider or if it is outside of a predetermined format it returns a value based on the addresses risk score

urgdict or Urgent dictionary contains the already mentioned commonly used urgent words

email address can be added to whitelist and blacklist always giving them the "ok" or always flagging them no matter what

