def solution(n, messages):
    results = []
    for message in messages:
        cnt = 0
        for index in range(0, int(len(message) / 2)):
            if message[index] != message[len(message) - index - 1]:
                cnt += abs(ord(message[index]) - ord(message[len(message) - index - 1]))
        results.append(cnt)

    return results
