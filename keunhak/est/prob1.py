def solution(s):
    slideSize = 1
    startIndex = 0

    while True:
        if startIndex + slideSize == len(s): 
            break;
        if isSemiAlternating(s[startIndex:startIndex + slideSize]):
            slideSize += 1
        else:
            startIndex += 1

    if isSemiAlternating(s[startIndex:startIndex+slideSize]):
        return slideSize
    else:
        return slideSize - 1

def isSemiAlternating(s):
    isSA = True
    for i in range(len(s) - 2):
        if s[i:i+3] == 'aaa' or s[i:i+3] == 'bbb':
            isSA = False
    return isSA
