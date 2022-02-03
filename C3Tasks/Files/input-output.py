with open('input.txt', 'r') as f1:
    with open('output.txt', 'w') as f2:
        for line in f1:
            f2.write(line)