with open('/Users/dasha/Desktop/8_task.txt', 'r') as f1:
    sp = list(map(str.strip, f1.readlines()))
with open('output.txt', 'w') as f2:
    summ = 0
    for i in range(0, 31):
        sum += int(sp[i])
    f2.write(str(summ / 31))
    f2.write('\n')

    summ = 0
    for i in range(31, 31 + 28 + 1):
        sum += int(sp[i])
    f2.write(str(summ / 28))
    f2.write('\n')

    summ = 0
    d = 0
    for m in range(10):
        if m % 2 == 0:
            for d in range(31):
                sum += int(sp[d])
                d += 1
            f2.write(str(summ / 31))
            f2.write('\n')
            summ = 0
        else:
            for j in range(30):
                sum += int(sp[d])
                d += 1
            f2.write(str(summ / 30))
            f2.write('\n')
            cnt = 0
