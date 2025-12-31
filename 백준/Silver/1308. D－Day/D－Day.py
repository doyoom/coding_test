def is_leap(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    return y % 4 == 0

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def to_days(y, m, d):
    total = 0
    for year in range(1, y):
        total += 366 if is_leap(year) else 365
    for month in range(1, m):
        if month == 2 and is_leap(y):
            total += 29
        else:
            total += days_in_month[month - 1]
    return total + d
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
if (y2, m2, d2) >= (y1 + 1000, m1, d1):
    print("gg")
else:
    print(f"D-{to_days(y2, m2, d2) - to_days(y1, m1, d1)}")