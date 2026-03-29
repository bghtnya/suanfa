import sys
from math import gcd

# 增加递归深度限制
sys.setrecursionlimit(2000)


def solve():
    line = sys.stdin.readline()
    if not line:
        return
    a, b = map(int, line.split())

    # 1. 构造 10^10 以内的幸运数字 (只含 6 和 8)
    lucky_all = []

    def gen_lucky(cur):
        if cur > b:
            return
        if cur > 0:
            lucky_all.append(cur)
        # 预防乘法溢出（虽然 Python 自动处理大数，但超过 b 就没意义了）
        if cur <= b // 10:
            gen_lucky(cur * 10 + 6)
            gen_lucky(cur * 10 + 8)

    gen_lucky(0)
    lucky_all.sort()

    # 2. 去重：如果 a 是 b 的倍数，去掉 a
    # 比如有了 6，就不需要 66，因为能被 66 整除的数一定能被 6 整除
    valid = []
    for i in range(len(lucky_all)):
        is_redundant = False
        for j in range(i):
            if lucky_all[i] % lucky_all[j] == 0:
                is_redundant = True
                break
        if not is_redundant:
            valid.append(lucky_all[i])

    # 3. 关键优化：从大到小排序
    # 这样在 DFS 时 LCM 会迅速变大，从而极大地触发剪枝
    valid.sort(reverse=True)
    n = len(valid)

    def get_lcm(x, y, limit):
        g = gcd(x, y)
        # 预判：x * y // g > limit -> x // g * y > limit
        if (x // g) * y > limit:
            return limit + 1
        return (x // g) * y

    def count_inclusion_exclusion(idx, cur_lcm, limit):
        """
        idx: 当前处理到的幸运数字索引
        cur_lcm: 当前组合的最小公倍数
        limit: 统计范围 (b 或 a-1)
        """
        count = 0
        for i in range(idx, n):
            new_lcm = get_lcm(cur_lcm, valid[i], limit)
            if new_lcm <= limit:
                # 容斥原理的核心：
                # 当前这一层的贡献 = limit // new_lcm - (下一层选更多数产生的重复贡献)
                count += limit // new_lcm - count_inclusion_exclusion(i + 1, new_lcm, limit)
        return count

    # 结果 = [1, b] 的个数 - [1, a-1] 的个数
    ans_b = count_inclusion_exclusion(0, 1, b)
    ans_a = count_inclusion_exclusion(0, 1, a - 1)

    print(ans_b - ans_a)


if __name__ == "__main__":
    solve()