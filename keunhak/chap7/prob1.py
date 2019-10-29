# solution 1 (not use divide & conquer)
def solution(tree):
    return turnOver(tree)

def turnOver(tree):
    if len(tree) == 1: 
        return tree

    quadrant = []
    cnt = 0
    startIndex = 1
    for i in range(1, len(tree)):
        if tree[i] == 'x':
            cnt += 3
        else:
            if cnt == 0:
                quadrant.append(tree[startIndex:i+1])
                startIndex = i + 1
            else:
                cnt -= 1
    
    return 'x' + turnOver(quadrant[2]) + turnOver(quadrant[3]) + turnOver(quadrant[0]) + turnOver(quadrant[1])

        
    
