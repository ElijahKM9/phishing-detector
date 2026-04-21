
compAdd = "@gmail.com"
def emailTest(sender):
    score = 0
    sender = sender.lower().strip()
    if not sender.endswith(compAdd):
            print("Not internal email address!")
            score += 2
    print("internal address!")
    with open("readfile/whitelist.txt") as f:
        for address in f:
            address = address.strip()
            if sender == address:
                print("Address in whitelist!")
                return score
    with open("readfile/blacklist.txt") as f:
        for address in f:
            address = address.strip()
            if sender == address:
                print("Address in BlACKLIST!")
                return score + 5
        
    print("External Not Pr-approved Email Address!")
    return score


