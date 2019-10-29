def solution(n, poles):
    poles.sort()
    diffs = diffEachPoles(poles)
    minDist = GCDargs(diffs)
    return (poles[-1] - poles[0]) / minDist + 1 - n

def diffEachPoles(poles):
    diffs = []
    for index in range(0, len(poles) - 1):
        diffs.append(poles[index + 1] - poles[index])
    return diffs

def GCD(a, b= None):
    if not b:
        return a
    
    if b > a:
        temp = a
        a = b
        b = temp
 
    while(b>0):
        temp = b
        b = a%b
        a = temp
    return a
        
def GCDargs(args):
    currentGCD = None
    for i in args:
        currentGCD = GCD(i, currentGCD)
    return currentGCD
