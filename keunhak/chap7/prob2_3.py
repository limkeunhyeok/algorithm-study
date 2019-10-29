def centerMax(start,end): 
    global Board
    center = (start+end)//2
    curH =  min(Board[center],Board[center+1]) 
    curMax= -1                                 
    curW = 1                                   
    right = center                             
    left = center                              
    while True:
        if left == start and right == end:     
            break
        if right == end:                       
            left -= 1
            curH = curH if curH < Board[left] else Board[left]
        elif left == start:                    
            right += 1
            curH = curH if curH < Board[right] else Board[right]
        else:
            if Board[right+1] >= Board[left-1]:
                right += 1
                curH = curH if curH < Board[right] else Board[right]
            else:
                left -= 1
                curH = curH if curH < Board[left] else Board[left]
        curW += 1
        curMax = curMax if curMax > curH * curW else curH * curW
    return curMax


def findMax(Start,N):    
    global Board
    if Start == N:       
        return Board[N]
    if N - Start == 1 :  
        return max(Board[Start],Board[N], 2*min(Board[Start],Board[N]))
    return max(findMax(Start,(N+Start)//2), findMax((N+Start)//2+1,N), centerMax(Start,N))

for C in range(int(input())):
    N = int(input())
    Board=list(map(int,input().split()))
    print(findMax(0, N-1))
