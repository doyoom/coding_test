n = int(input())
switches = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    gender, k = map(int, input().split())
    k -= 1

    if gender == 1:
        for i in range(k, n, k + 1):
            switches[i] ^= 1
    else:
        left = right = k

        while left - 1 >= 0 and right + 1 < n:
            if switches[left - 1] == switches[right + 1]:
                left -= 1
                right += 1
            else:
                break

        for i in range(left, right + 1):
            switches[i] ^= 1
for i in range(n):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
