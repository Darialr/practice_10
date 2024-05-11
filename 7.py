with open('/Users/dasha/Desktop/7_task.txt', 'r') as f1:
    with open('output.txt', 'w') as f2:
        for line in f1:
            if int(line) != 100:
                f2.write(line)
