a=0
for r in range(256):
    for g in range(256):
        for b in range(256):
            if b>r and b>g:
                a+=1
print(a)


a = sum(b * b for b in range(256))
print(a)