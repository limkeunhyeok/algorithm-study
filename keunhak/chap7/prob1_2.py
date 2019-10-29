def solution(tree):
    return reverse(iter(tree))

def reverse(it):
    current = next(it)
    if current == 'w' or current == 'b':
        return current
    
    upperLeft = reverse(it)
    upperRight = reverse(it)
    lowerLeft = reverse(it)
    lowerRight = reverse(it)

    return 'x' + lowerLeft + lowerRight + upperLeft + upperRight
