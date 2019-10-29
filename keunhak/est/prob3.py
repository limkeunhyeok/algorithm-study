def solution(u,l,c):
    if sum(c) != u + l:
        return 'IMPOSSIBLE'
    else:
        m = [[0 for i in range(len(c))] for j in range(2)]
        u_cnt = 0
        l_cnt = 0

        for i in range(len(c)):
            if c[i] == 2:
                m[0][i] = 1
                m[1][i] = 1
                u_cnt += 1
                l_cnt += 1

        for i in range(len(c)):
            if c[i] == 1:
                if u_cnt < u:
                    m[0][i] = 1
                    u_cnt += 1
                elif l_cnt < l:
                    m[1][i] = 1
                    l_cnt += 1
            else:
                continue

        ans = ''
        for i in range(2):
            for j in range(len(c)):
                ans += str(m[i][j])
            ans += ','

        return ans[:len(c) * 2 + 1]
