with open('/Users/dasha/Desktop/6_task.txt', 'r') as f1:
    sp = list(map(str.strip, f1.readlines()))

with open('output.txt', 'w') as f2:
    try:
        if len(sp) - 1 == int(sp[0]):
            f2.write('YES')
        else:
            f2.write('NO')
    except ValueError:
        f2.write('ERROR')
