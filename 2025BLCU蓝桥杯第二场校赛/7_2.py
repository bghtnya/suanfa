A = list(input())
B = list(input())
table = []
def game(a, b):
  global table
  if not a:
    return b #牌都在b手上
  if not b:
    return a
  card = a[0]
  table.append(a[0])
  a.pop(0)
  temp = []
  if table.count(card) > 1:#赢牌
    idx = table.index(card)
    temp = table[idx:]
    table = table[:idx]
    a.extend(temp[::-1])
    return game(a, b)
  else:
    return game(b, a)
rs = game(A, B)
print(''.join(rs))
