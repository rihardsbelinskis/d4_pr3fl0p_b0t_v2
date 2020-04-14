from DetectCards import *

def PreflopRanges(myHand, position):
    UTG_RFI = ["AAo","AKs","KAs","AQs","QAs","AJs","JAs","ATs","TAs","A9s","9As","A8s","8As","A7s",
               "7As","A6s","6As","A5s","5As","A4s","4As","A3s","3As","A2s","2As","AKo","KAo","KKo",
               "KQs","QKs","KJs","JKs","KTs","TKs","K9s","9Ks","AQo","QAo","KQo","QKo","QQo","QJs",
               "JQs","QTs","TQs","Q9s","9Qs","AJo","JAo","JJo","JTs","TJs","J9s","9Js","TTo","T9s",
               "9Ts","99o","98s","89s","88o","87s","78s","77o","76s","67s","66o","55o"]

    MP_RFI = ["AAo","AKs","KAs","AQs","QAs","AJs","JAs","ATs","TAs","A9s","9As","A8s","8As","A7s",
              "7As","A6s","6As","A5s","5As","A4s","4As","A3s","3As","A2s","2As","AKo","KAo","KKo",
              "KQs","QKs","KJs","JKs","KTs","TKs","K9s","9Ks","AQo","QAo","KQo","QKo","QQo","QJs",
              "JQs","QTs","TQs","Q9s","9Qs","AJo","JAo","KJo","JKo","QJo","JQo","JJo","JTs","TJs",
              "ATo","TAo","TTo","T9s","9Ts","99o","98s","89s","88o","87s","78s","77o","76s","67s",
              "66o","65s","56s","55o","44o","33o","22o"]

    CO_RFI = ["AAo","AKs","KAs","AQs","QAs","AJs","JAs","ATs","TAs","A9s","9As","A8s","8As","A7s",
              "7As","A6s","6As","A5s","5As","A4s","4As","A3s","3As","A2s","2As","AKo","KAo","KKo",
              "KQs","QKs","KJs","JKs","KTs","TKs","K9s","9Ks","AQo","QAo","KQo","QKo","QQo","QJs",
              "JQs","QTs","TQs","Q9s","9Qs","AJo","JAo","KJo","JKo","KTo","TKo","QJo","JQo","JJo",
              "JTs","TJs","ATo","TAo","TTo","T9s","9Ts","99o","98s","89s","88o","87s","78s","77o",
              "76s","67s","66o","65s","56s","55o","44o","33o","22o"]

    BTN_RFI = ["AAo","AKs","KAs","AQs","QAs","AJs","JAs","ATs","TAs","A9s","9As","A8s","8As","A7s",
              "7As","A6s","6As","A5s","5As","A4s","4As","A3s","3As","A2s","2As","AKo","KAo","KKo",
              "KQs","QKs","KJs","JKs","KTs","TKs","K9s","9Ks","AQo","QAo","KQo","QKo","QQo","QJs",
              "JQs","QTs","TQs","Q9s","9Qs","AJo","JAo","KJo","JKo","KTo","TKo","QJo","JQo","JJo",
              "JTs","TJs","ATo","TAo","TTo","A9o","9Ao","T9s","9Ts","99o","A8o","8Ao","98s","89s",
              "88o","A8o","8Ao","87s","78s","77o","76s","67s","66o","65s","56s","55o","A5o","5Ao",
              "44o","A4o","4Ao","33o","A3o","3Ao","22o","A2o","2Ao"]

    SB_RFI = ["AAo","AKs","KAs","AQs","QAs","AJs","JAs","ATs","TAs","A9s","9As","A8s","8As","A7s",
              "7As","A6s","6As","A5s","5As","A4s","4As","A3s","3As","A2s","2As","AKo","KAo","KKo",
              "KQs","QKs","KJs","JKs","KTs","TKs","K9s","9Ks","AQo","QAo","KQo","QKo","QQo","QJs",
              "JQs","QTs","TQs","Q9s","9Qs","AJo","JAo","KJo","JKo","KTo","TKo","QJo","JQo","JJo",
              "JTs","TJs","ATo","TAo","TTo","A9o","9Ao","T9s","9Ts","99o","A8o","8Ao","98s","89s",
              "88o","A8o","8Ao","87s","78s","77o","97s","79s","86s","68s","76s","67s","66o","65s",
              "56s","55o","A5o","5Ao","44o","A4o","4Ao","33o","A3o","3Ao","53s","35s","43s","34s",
              "22o","A2o","2Ao"]

    BB_RFI = ["AAo","AKs","KAs","AQs","QAs","AJs","JAs","ATs","TAs","A9s","9As","A8s","8As","A7s",
              "7As","A6s","6As","A5s","5As","A4s","4As","A3s","3As","A2s","2As","AKo","KAo","KKo",
              "KQs","QKs","KJs","JKs","KTs","TKs","K9s","9Ks","AQo","QAo","KQo","QKo","QQo","QJs",
              "JQs","QTs","TQs","Q9s","9Qs","AJo","JAo","JJo","JTs","TJs","J9s","9Js","TTo","T9s",
              "9Ts","T9o","9To","99o","98s","89s","88o","87s","78s","77o","76s","67s","66o","55o",
              "54s","45s","44o","A4o","4Ao","33o","A3o","3Ao","22o","A2o","2Ao"]

    if position == 'UTG':
        if myHand in UTG_RFI:
            inRange = True
        else:
            inRange = False
    elif position == 'MP':
        if myHand in MP_RFI:
            inRange = True
        else:
            inRange = False
    elif position == 'CO':
        if myHand in CO_RFI:
            inRange = True
        else:
            inRange = False
    elif position == 'BTN':
        if myHand in BTN_RFI:
            inRange = True
        else:
            inRange = False
    elif position == 'SB':
        if myHand in SB_RFI:
            inRange = True
        else:
            inRange = False
    elif position == 'BB':
        if myHand in BB_RFI:
            inRange = True
        else:
            inRange = False
    else:
        print("Error! Hand undetected!")

    return inRange
