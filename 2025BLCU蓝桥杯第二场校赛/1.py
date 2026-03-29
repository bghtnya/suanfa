s = set()
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
qwq = [f"{i}{i + 1}{i + 2}" for i in range(8)]      # 坏诶为什么012也算

for i in range(1, 13):
    ymd = "2022" + (f"0{i}" if i < 10 else f"{i}")
    day = days_in_month[i - 1]
    for j in range(1, day + 1):
        ymd2 = ymd + (f"0{j}" if j < 10 else f"{j}")
        if any(p in ymd2 for p in qwq):
            s.add(ymd2)

print(len(s))
