N = int(input())
times = list(map(int, input().split()))

times.sort()

total = 0
cur = 0

for t in times:
    cur += t
    total += cur

print(total)