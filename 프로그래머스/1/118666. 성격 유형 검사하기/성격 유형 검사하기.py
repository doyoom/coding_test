def solution(survey, choices):
    scores = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        if c < 4:
            scores[s[0]] += 4 - c
        elif c > 4:
            scores[s[1]] += c - 4
    answer = ''
    indicators = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    for a, b in indicators:
        if scores[a] >= scores[b]:
            answer += a
        else:
            answer += b
    return answer