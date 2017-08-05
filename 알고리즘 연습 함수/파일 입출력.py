with open('Ofile.txt', 'w') as f:
    with open('file.txt', 'r') as ff:
        f.write(ff.read().lower().replace('z', '0').replace('o','1'))
