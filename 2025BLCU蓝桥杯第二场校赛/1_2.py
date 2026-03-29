from datetime import date, timedelta

# 生成所有天数
d = date(2022, 1, 1)
end = date(2022, 12, 31)

patterns = [f"{i}{i + 1}{i + 2}" for i in range(8)]

s = set()
while d <= end:
    ymd = d.strftime("%Y%m%d")
    if any(p in ymd for p in patterns):
        s.add(ymd)
    d += timedelta(days=1)

print(len(s))
