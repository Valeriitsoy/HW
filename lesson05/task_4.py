
rus_list = ['один\n', 'два\n', 'три\n', 'четыре\n']
with open('4.txt') as f:
    with open('41.txt', 'w') as f_l:
        for line in f:
            word, digit = line.split('-')
            rus = rus_list.pop(0)
            text = word + '- ' + rus
            f_l.writelines(text)
