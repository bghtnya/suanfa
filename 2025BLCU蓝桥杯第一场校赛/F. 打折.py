from collections import defaultdict
INF = 4 * 10 ** 18

def solve():
    n, m = map(int, input().split())
    shops = []
    events = []

    mp = [INF] * (n + 1)

    for i in range(m):
        line = input().split()
        s, t, p, c = map(int, line)

        items = []
        for _ in range(c):
            try:
                line = input().split()
                a, b = map(int, line)
            except Exception:
                continue

            dp = (b * p) // 100

            items.append((a, b, dp))  # (类型, 原价, 折后价)
            mp[a] = min(mp[a], b)

        shops.append({'items': items})

        events.append((s, i, 1))
        if t < 2 * 10 ** 9:
            events.append((t + 1, i, -1))

    # 按日期排序，同一天先处理 -1 再处理 +1
    events.sort(key=lambda x: (x[0], x[2]))

    # ds[i]: 物品 i 的折扣价计数多重集 {price: count}
    ds = defaultdict(lambda: defaultdict(int))

    # 初始总成本
    current_cost = sum(mp[1:])
    min_cost = current_cost

    # 扫描线主循环
    for day, shop_idx, type_ in events:
        shop = shops[shop_idx]

        for item_type, _, dp in shop['items']:

            dset = ds[item_type]

            # --- 1. 获取旧的最低价 ---
            old_keys = dset.keys()
            old_min_dp = min(old_keys) if old_keys else INF
            old_min_p = min(old_min_dp, mp[item_type])

            # --- 2. 更新折扣价多重集 ---
            if type_ == 1:  # 折扣开始 (+1)
                dset[dp] += 1
            else:  # 折扣结束 (-1)
                dset[dp] -= 1
                if dset[dp] == 0:
                    del dset[dp]

            # --- 3. 获取新的最低价 ---
            new_keys = dset.keys()
            new_min_dp = min(new_keys) if new_keys else INF
            new_min_p = min(new_min_dp, mp[item_type])

            # --- 4. 更新总成本 ---
            if new_min_p != old_min_p:
                current_cost += (new_min_p - old_min_p)

        min_cost = min(min_cost, current_cost)

    print(min_cost)


if __name__ == "__main__":
    solve()