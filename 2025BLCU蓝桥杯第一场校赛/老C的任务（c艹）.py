import sys


# 设置递归深度，以防排序或其他操作栈溢出
# sys.setrecursionlimit(200000)

# 使用 sys.stdin.readline() 提高 IO 速度
def input_line():
    return sys.stdin.readline().strip()


# 使用列表和全局变量来模拟 C++ 数组和全局状态
# Python 中更推荐封装在类或函数内，但为了匹配 C++ 结构，我们使用全局或传入参数。

# 全局变量（在 Python 中，大型可变对象如列表或字典在函数中可以直接修改）
# C++ 中的全局数组和 vector 在 Python 中用列表或字典实现
y_coords = []  # 存储待离散化的y坐标
final_answers = []  # 存储 m 个查询的最终答案
num_discrete_y = 0  # 离散化后y坐标的总数
tree = []  # 树状数组


# -------------------- 树状数组 (Fenwick Tree) --------------------

def lowbit(x):
    """计算 x 的最低位 1 及其后面的 0 所表示的数值"""
    return x & -x


def add(base, val):
    """增加值 (单点更新): O(log N)"""
    global num_discrete_y, tree
    while base <= num_discrete_y:
        tree[base] += val
        base += lowbit(base)


def query(base):
    """查询前缀和: O(log N)"""
    res = 0
    while base > 0:
        res += tree[base]
        base -= lowbit(base)
    return res


# -------------------- 事件结构和辅助函数 --------------------

# 在 Python 中，使用元组或命名元组来模拟结构体 Event。
# 结构：(x, type, y, val, query_id)
# type: #0=加点(基站), 1=查询边界
# val: type=0 时是功率 p；type=1 时是容斥符号 (+1/-1)

# 重载排序规则：按 x 排序；x 相同按 type 排序 (0 在前, 1 在后)
# Python 的 tuple 默认按元素顺序排序，所以我们把 type 放在第二位。

def get_discrete_y(y):
    """
    获取 y 坐标离散化后的索引 (从 1 开始)
    使用二分查找 (bisect_left 对应 C++ 的 lower_bound)
    """
    import bisect
    # bisect_left 找到第一个 >= y 的索引 (从 0 开始)
    index = bisect.bisect_left(y_coords, y)
    # + 1 转换成从 1 开始的树状数组下标
    return index + 1


# -------------------- 主函数 --------------------

def solve():
    global y_coords, final_answers, num_discrete_y, tree

    # 读取 N 和 M
    try:
        n_m_line = input_line().split()
        if not n_m_line:
            return
        n, m = map(int, n_m_line)
    except:
        return

    events = []

    # 1. 读入 n 个基站 (加点事件, type=0)
    for _ in range(n):
        line = input_line().split()
        x, y, p = map(int, line)
        # (x, type=0, y, val=p, query_id=0)
        events.append((x, 0, y, p, 0))
        y_coords.append(y)

    # 2. 读入 m 个查询 (拆分成 4*m 个查询事件, type=1)
    for i in range(m):
        line = input_line().split()
        x1, y1, x2, y2 = map(int, line)

        # Q(x2, y2): +1
        events.append((x2, 1, y2, 1, i))
        # Q(x1-1, y2): -1
        events.append((x1 - 1, 1, y2, -1, i))
        # Q(x2, y1-1): -1
        events.append((x2, 1, y1 - 1, -1, i))
        # Q(x1-1, y1-1): +1
        events.append((x1 - 1, 1, y1 - 1, 1, i))

        # 收集 y 坐标 (注意，这里只收集了查询的y坐标，点的y已在上面收集)
        y_coords.append(y2)
        y_coords.append(y1 - 1)

    # 3. 离线化 y 坐标
    # 排序和去重 (对应 C++ 的 sort 和 unique)
    y_coords.sort()

    # 使用 set 去重并重新排序是 Python 中去重常用且高效的方式
    # 但为了模拟 C++ 的 sort/unique 效果：
    y_coords = sorted(list(set(y_coords)))
    num_discrete_y = len(y_coords)  # 树状数组的有效大小

    # 初始化树状数组和答案数组
    # tree[0] 不用，大小为 num_discrete_y + 1
    tree = [0] * (num_discrete_y + 1)
    final_answers = [0] * m

    # 4. 排序所有事件
    # Python 元组默认按元素顺序排序，满足 (x 升序, type 升序) 的要求
    events.sort()

    # 5. 执行扫描线
    for x, type_, y, val, q_id in events:
        y_disc = get_discrete_y(y)  # 获取离散化后的 y 坐标索引

        if type_ == 0:
            # 加点事件
            add(y_disc, val)  # val 是功率 p_i
        else:
            # 查询事件
            prefix_sum = query(y_disc)
            # val 是容斥符号 (+1 或 -1)
            final_answers[q_id] += val * prefix_sum

    # 6. 输出结果
    sys.stdout.write('\n'.join(map(str, final_answers)) + '\n')


if __name__ == "__main__":
    solve()