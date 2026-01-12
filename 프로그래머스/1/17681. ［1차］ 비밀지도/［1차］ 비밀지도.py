def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        binary = bin(arr1[i] | arr2[i])[2:].zfill(n)
        line = ""
        for b in binary:
            if b == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)
    return answer