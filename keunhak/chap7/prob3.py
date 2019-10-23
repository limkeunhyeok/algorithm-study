def solution(hyperseniors, fans):
    return fanmeeting(toBitwise(hyperseniors), toBitwise(fans), len(fans) - len(hyperseniors) + 1)

def fanmeeting(hyperseniors, fans, N):
    ret = 0
    for T in range(N):
        if hyperseniors & fans == 0:
            ret += 1
        fans = fans >> 1
    
    return ret

def toBitwise(MFStr):
    return int(MFStr.replace('M', '1').replace('F', '0'), 2)
