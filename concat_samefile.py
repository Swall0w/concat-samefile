# -*- coding: utf-8 -*-
import os
import os.path
import difflib

def main():
    original_dir = 'separate_jornaldata/'
    append_dir = 'sepv2/'
    original_filelist = os.listdir(original_dir)
    append_filelist = [item for item in os.listdir(append_dir) if os.path.splitext(item)[1] == '.csv']
    print(append_filelist)
    print(len(append_filelist))

    item = append_filelist[0]
    print(item)
    with open(append_dir+item,'r') as appendfile, open(original_dir+item,'r') as originalfile:
        appendstr = appendfile.read()
        originalstr = originalfile.read()


if __name__ == '__main__':
    main()
