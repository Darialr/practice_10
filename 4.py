with open('/Users/dasha/Desktop/4_task.txt', 'r') as f1:
    with open('output.txt', 'w') as f2:
        for line in f1:
            if len(line) > 20:
                f2.write(line)
