digit = {
    1: (1, 1),
    2: (1, 2),
    3: (1, 3),
    4: (2, 1),
    5: (2, 2),
    6: (2, 3),
    7: (3, 1),
    8: (3, 2),
    9: (3, 3),
    0: (4, 2)
}

left, right = (4, 1), (4, 3)


def getHand(x, hand):
    global left, right
    
    if x in [1, 4, 7]:
        left = digit[x]
        return 'L'
    elif x in [3, 6, 9]:
        right = digit[x]
        return 'R'
    else:
        l1, l2 = left
        r1, r2 = right
        x1, x2 = digit[x]
        d1 = abs(l1-x1)+abs(l2-x2)
        d2 = abs(r1-x1)+abs(r2-x2)
        if d1 == d2:
            if hand == 'left':
                left = digit[x]
                return 'L'
            else:
                right = digit[x]
                return 'R'
        elif d1 > d2:
            right = digit[x]
            return 'R'
        else:
            left = digit[x]
            return 'L'
            

def solution(numbers, hand):
    answer = ''
    for x in numbers:
        answer += getHand(x, hand)
    return answer