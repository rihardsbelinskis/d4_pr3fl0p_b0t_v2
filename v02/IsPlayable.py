import DetectCards

def IsPlayable(myHand, handMy):
    
    UNIV_R = ('AAo','AKs','AQs','AJs','ATs','A9s','A8s','A7s','A6s','A5s','A4s','A3s','A2s','AKo', 
             'KKo','KQs','KJs','KTs','K9s','K8s','K7s','K6s','K5s','K4s','AQo','KQo','QQo','QJs',
             'QTs','Q9s','Q8s','Q7s','Q6s','AJo','KJo','QJo','JJo','JTs','J9s','J8s','J7s','ATo',
             'KTo','QTo','JTo','TTo', 'T9s','T8s','T7s','A9o','K9o','Q9o','J9o','T9o','99o','98s',
             '97s','96s','A8o','88o','87s','86s','85s','A7o','77o','76s','75s','A6o','66o','65s',
             '64s','A5o','55o','54s','53s','A4o','44o','43s','33o','22o')
    
    if myHand in UNIV_R:
        isPlayable = True
    else:
        isPlayable = False

    return isPlayable
