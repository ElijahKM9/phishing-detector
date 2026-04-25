
compAdd = "@gmail.com"
def emailTest(sender):
    score = 0
    sender = sender.lower().strip()

    if not sender.endswith(compAdd):
            score += 1
    else:
        print("internal address!")


    with open("readfile/whitelist.txt") as f:
        for address in f:
            address = address.strip()
            if sender == address:
                print("Address in whitelist!")
                return 0
            
    with open("readfile/blacklist.txt") as f:
        for address in f:
            address = address.strip()
            if sender == address:
                print("Address in BlACKLIST!")
                return score + 5
        
    print("External Not Pr-approved Email Address!")
    return score


