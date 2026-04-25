

def wordtester(subject, body):
    score = 0
    count = 0
    subject = subject.split()
    body = body.split() 
    urgset = set()
    with open("readfile/urgdict.txt") as f:
        for word in f:
            urgset.add(word.strip())

    for word in subject:
        word = word.lower().strip(".,!?;:'\"()[]")
        if word in urgset:
            count += 1

    for word in body:
        word = word.lower().strip(".,!?;:'\"()[]")
        if word in urgset:
            count += 1

    if count == 0:
        return score
    elif count <= 2:
        return score + 1
    elif count <= 5:
        return score + 3
    else:
        return score + 5



    

    
    
    