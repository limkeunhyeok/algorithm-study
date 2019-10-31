def solution(idols, fans):
    l1 = len(idols)
    l2 = len(fans)
    a = int(idols, 2)
    b = int(fans, 2)
    cnt = 0
    for i in range(l2 - l1 + 1):
        if a & b == 0:
            cnt += 1
        b = b >> 1
    return cnt


for T in range(int(input())):
    idols = input().replace('F', '0').replace('M', '1')
    fans = input().replace('F', '0').replace('M', '1')
    print(solution(idols, fans))
    
idols1 = 'FFFMMM'
fans1 = 'MMMFFF'

idols2 = 'FFFFF'
fans2 = 'FFFFFFFFFF'

idols3 = 'FFFFM'
fans3 = 'FFFFFMMMMF'

idols4 = 'MFMFMFFFMMMFMF'
fans4 = 'MMFFFFFMFFFMFFFFFFMFFFMFFFFMFMMFFFFFFF'
