with open('/Users/dasha/Desktop/9_task.txt', 'r') as f1:
    with open('output.txt', 'w') as f2:
        sp = list(map(str.strip, f1.readlines()))
        for i in range(0, len(sp)):
            if i % 2 == 0:
                f2.write(sp[i])
                f2.write('\n')
