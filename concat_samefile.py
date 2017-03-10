# -*- coding: utf-8 -*-
import os
import os.path

def main():
    original_dir = 'separate_jornaldata/'
    append_dir = 'sepv2/'
    original_filelist = os.listdir(original_dir)
    append_filelist = [item for item in os.listdir(append_dir) if os.path.splitext(item)[1] == '.csv']
    print(append_filelist)
    print(len(append_filelist))


if __name__ == '__main__':
    main()
