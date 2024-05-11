with open('/Users/dasha/Desktop/2_task.txt', 'r') as f1:
    with open('output.txt', 'w') as f2:
        for line in f1:
            if line[0] == 'a' or line[0] == 'A':
                f2.write(line)
