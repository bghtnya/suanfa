import sys


# 提高输入速度
def input():
    return sys.stdin.readline().strip()


# ----------------------------------------------------
# 树状数组 (Fenwick Tree / BIT)
class FenwickTree:
    """用于在离散化后的 Y 轴上维护功率和"""

    def __init__(self, size):
        # size 是离散化后 Y 坐标的最大索引
        self.tree = [0] * (size + 1)
        self.size = size

    # 单点更新: O(log N)
    def add(self, i, delta):
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)

    # 前缀求和: O(log N)
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s


# ----------------------------------------------------

def solve():
    try:
        N, M = map(int, input().split())
    except:
        return

    points = []
    queries = []
    y_coords = set()

    # 1. 读取基站 (x, y, p)
    for _ in range(N):
        try:
            x, y, p = map(int, input().split())
            points.append((x, y, p))
            y_coords.add(y)
        except:
            pass

    # 2. 读取查询 (x1, y1, x2, y2)
    for i in range(M):
        try:
            x1, y1, x2, y2 = map(int, input().split())
            queries.append((x1, y1, x2, y2, i))
            y_coords.add(y1 - 1)  # 容斥边界 y1-1
            y_coords.add(y2)
        except:
            pass

    # 3. 坐标离散化 Y 轴
    sorted_y = sorted(list(y_coords))
    y_map = {y: i + 1 for i, y in enumerate(sorted_y)}  # 映射到 [1, size]
    y_size = len(sorted_y)

    # 4. 构建统一的扫描线事件列表 (x, type, y, value, query_id)
    # Type: 1: Point (+); 2,3,4,5: Query (-) or (+)
    events = []

    # Base event type (Point): x, type=1, y, value=p, id=-1
    for x, y, p in points:
        if y in y_map:  # 确保 y 在离散化范围内
            events.append((x, 1, y_map[y], p, -1))

            # Query events (容斥原理): Query(x1, y1, x2, y2) = Q(x2, y2) - Q(x1-1, y2) - Q(x2, y1-1) + Q(x1-1, y1-1)
    for x1, y1, x2, y2, q_id in queries:
        # Q(x2, y2): +1 * result
        if y2 in y_map:
            events.append((x2, 2, y_map[y2], 1, q_id))

        # Q(x1-1, y2): -1 * result
        if y2 in y_map:
            events.append((x1 - 1, 3, y_map[y2], -1, q_id))

        # Q(x2, y1-1): -1 * result
        if y1 - 1 in y_map:
            events.append((x2, 4, y_map[y1 - 1], -1, q_id))

        # Q(x1-1, y1-1): +1 * result
        if y1 - 1 in y_map:
            events.append((x1 - 1, 5, y_map[y1 - 1], 1, q_id))

    # 5. 排序事件
    # 排序优先级: x坐标升序 -> type升序 (点在前，查询在后)
    events.sort(key=lambda item: (item[0], item[1]))

    # 6. 扫描线和 BIT
    bit = FenwickTree(y_size)
    results = [0] * M

    for x, type_, y_idx, val, q_id in events:
        if type_ == 1:
            # 基站事件: 在 BIT 中添加功率
            bit.add(y_idx, val)
        else:
            # 查询事件: 计算结果并容斥
            # val 在这里代表容斥的符号 (+1 或 -1)
            query_sum = bit.query(y_idx)  # 查询 BIT 中 y_idx 范围内的总和
            results[q_id] += query_sum * val

    # 7. 输出结果
    sys.stdout.write('\n'.join(map(str, results)) + '\n')


if __name__ == "__main__":
    # 增加递归深度，防止在某些复杂I/O或排序场景中出现问题
    sys.setrecursionlimit(200000)
    solve()