# -*- coding: utf-8 -*-
import os
import os.path

def main():
    dir1 = 'separate_jornaldata/'
    dir2 = 'sepv2/'
    filelist1 = os.listdir(dir1)
    filelist2 = os.listdir(dir2)
    print(len(filelist1))
    print(len(filelist2))
    pattern = re.compile('(.*)\.csv')
    for item in filelist2:
        result = pattern.search(item)


if __name__ == '__main__':
    main()
