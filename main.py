from sendertest import emailTest
from wordtest import wordtester



def main():
    score = 0

    sendAddress  = input("Enter their address:")

    score += emailTest(sendAddress)

    subject  = input("Enter the email subject:")

    body  = input("Enter the email body text:")

    score += wordtester(subject, body)

    if score == 0:
        print("Safe")
    elif score <= 2:
        print("Low Risk")
    elif score <= 4:
        print("Decent Risk")
    elif score <= 6:
        print("High Risk")
    else:
        print("Critical Risk")

main()