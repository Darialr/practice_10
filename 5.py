with open('/Users/dasha/Desktop/5_task.txt', 'r') as f1:
    numbers = list(map(str.strip, f1.readlines()))

with open('output.txt', 'w') as f2:
    try:
        res = int(numbers[0]) / int(numbers[1]) + int(numbers[2])
        f2.write(str(res))
    except ValueError:
        f2.write('data error')
    except ZeroDivisionError:
        f2.write('division by 0')
