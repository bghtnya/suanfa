def calculate(x, a, b, c, d):
    """计算一元三次方程的值 f(x) = a*x^3 + b*x^2 + c*x + d"""
    return a * x ** 3 + b * x ** 2 + c * x + d


def find_root(left, right, a, b, c, d):
    """在 [left, right] 区间内用二分法找根"""
    eps = 1e-6  # 提高精度，减少近似误差
    while right - left > eps:
        mid = (left + right) / 2
        f_mid = calculate(mid, a, b, c, d)
        f_left = calculate(left, a, b, c, d)

        if abs(f_mid) < eps:
            return mid
        elif f_left * f_mid < 0:
            right = mid
        else:
            left = mid
    return (left + right) / 2


# 读取输入
a, b, c, d = map(float, input().split())
roots = []
eps = 1e-4  # 根的去重精度阈值

# 遍历 [-100, 100] 所有长度为1的区间（不提前退出）
for x in range(-100, 100):
    left = x
    right = x + 1
    f_left = calculate(left, a, b, c, d)
    f_right = calculate(right, a, b, c, d)

    # 情况1：左端点是根，且未重复
    if abs(f_left) < eps:
        # 检查是否和已有的根重复（差值<0.1就视为同一个根）
        is_duplicate = False
        for r in roots:
            if abs(left - r) < 0.1:
                is_duplicate = True
                break
        if not is_duplicate:
            roots.append(left)

    # 情况2：区间内有根（符号相反），且未重复
    elif f_left * f_right < 0:
        root = find_root(left, right, a, b, c, d)
        # 去重检查
        is_duplicate = False
        for r in roots:
            if abs(root - r) < 0.1:
                is_duplicate = True
                break
        if not is_duplicate:
            roots.append(root)

# 排序（确保从小到大）+ 格式化输出
roots.sort()
print(f"{roots[0]:.2f} {roots[1]:.2f} {roots[2]:.2f}")