import DetectCards

def IsPlayable(myHand):
    #myHand = myHand.strip("'")
    UNIV_R = ["AAo","AKs","KAs","AQs","QAs","AJs","JAs","ATs","TAs","A9s","9As","A8s","8As","A7s",
              "7As","A6s","6As","A5s","5As","A4s","4As","A3s","3As","A2s","2As","AKo","KAo","KKo",
              "KQs","QKs","KJs","JKs","KTs","TKs","K9s","9Ks","AQo","QAo","KQo","QKo","QQo","QJs",
              "JQs","QTs","TQs","Q9s","9Qs","AJo","JAo","KJo","JKo","KTo","TKo","QJo","JQo","JJo",
              "JTs","TJs","ATo","TAo","TTo","A9o","9Ao","T9s","9Ts","99o","A8o","8Ao","98s","89s",
              "88o","A8o","8Ao","87s","78s","77o","76s","67s","66o","65s","56s","55o","A5o","5Ao",
              "44o","A4o","4Ao","33o","A3o","3Ao","22o","A2o","2Ao"]
    print(myHand)
    if myHand in UNIV_R:
        isPlayable = True
    else:
        isPlayable = False

    return isPlayable
