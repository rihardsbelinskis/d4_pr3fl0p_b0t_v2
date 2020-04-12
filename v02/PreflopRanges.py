#from DetectCards import handMy, myHand  <--- currently shows a bug
import DetectCards

def PreflopRanges(myHand, position):
    UTG_RFI = ["AAo","AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s","AKo",
               "KKo","KQs","KJs","KTs","K9s","AQo","KQo","QQo","QJs","QTs","Q9s","AJo","JJo","JTs",
               "J9s","TTo","T9s","99o","98s","88o","87s","77o","76s","66o","55o"]

    MP_RFI = ["AAo","AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s","AKo",
              "KKo","KQs","KJs","KTs","K9s","AQo","KQo","QQo","QJs","QTs","Q9s","AJo","KJo","QJo",
              "JJo","JTs","J9s","ATo","TTo","T9s","99o","98s","88o","87s","77o","76s","66o", "65s",
              "55o","44o","33o","22o"]

    CO_RFI = ["AAo","AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s","AKo",
              "KKo","KQs","KJs","KTs","K9s","K8s","K7s","K6s","AQo","KQo","QQo","QJs","QTs","Q9s",
              "Q8s","AJo","KJo","QJo","JJo","JTs","J9s","J8s","ATo","KTo","QTo","JTo","TTo", "T9s",
              "T8s","99o","98s","97s","88o","87s","86s","77o","76s","75s","66o","65s","55o","54s",
              "44o","33o","22o"]

    BTN_RFI = ["AAo","AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s","AKo",
             "KKo","KQs","KJs","KTs","K9s","K8s","K7s","K6s","K5s","K4s","AQo","KQo","QQo","QJs",
             "QTs","Q9s","Q8s","Q7s","Q6s","AJo","KJo","QJo","JJo","JTs","J9s","J8s","J7s","ATo",
             "KTo","QTo","JTo","TTo", "T9s","T8s","T7s","A9o","K9o","Q9o","J9o","T9o","99o","98s",
             "97s","96s","A8o","88o","87s","86s","85s","A7o","77o","76s","75s","A6o","66o","65s",
             "64s","A5o","55o","54s","53s","A4o","44o","43s","33o","22o"]

    SB_RFI = ["AAo","AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s","AKo",
            "KKo","KQs","KJs","KTs","K9s","K8s","K7s","K6s","K5s","K4s","K3s","AQo","KQo","QQo",
            "QJs","QTs","Q9s","Q8s","Q7s","Q6s","Q5s","AJo","KJo","QJo","JJo","JTs","J9s","J8s",
            "J7s","J6s","ATo","KTo","QTo","JTo","TTo", "T9s","T8s","T7s","T6s","A9o","K9o","Q9o",
            "J9o","T9o","99o","98s","97s","96s","A8o","K8o","98o","88o","87s","86s","85s","A7o",
            "77o","76s","75s","A6o","66o","65s","64s","A5o","55o","54s","53s","A4o","44o","43s",
            "A3o","33o","A2o","22o"]

    BB_RFI = ["AAo","AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s","AKo",
            "KKo","KQs","KJs","KTs","K9s","K8s","K7s","K6s","AQo","KQo","QQo","QJs","QTs","Q9s",
            "Q8s","Q7s","Q6s","Q5s","AJo","KJo","QJo","JJo","JTs","J9s","J8s","J7s","ATo","KTo",
            "QTo","JTo","TTo", "T9s","T8s","A9o","K9o","Q9o","J9o","T9o","99o","98s","97s","A8o",
            "88o","87s","86s","77o","76s","66o","65s","A5o","55o","54s","A4o","44o","A3o","33o",
            "A2o","22o"]

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
