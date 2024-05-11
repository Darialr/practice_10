with open('/Users/dasha/Desktop/1_task.txt', 'r') as f1:
    text = f1.read()
with open('output.txt', 'a+') as f2:
    text = str(text.upper())
    f2.write(text)
