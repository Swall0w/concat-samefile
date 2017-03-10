# -*- coding: utf-8 -*-
import os
import os.path
import difflib
from io import StringIO
import pandas as pd

def main():
    original_dir = 'separate_jornaldata/'
    append_dir = 'sepv2/'
    original_filelist = os.listdir(original_dir)
    append_filelist = [item for item in os.listdir(append_dir) if os.path.splitext(item)[1] == '.csv']
    print(append_filelist)
    print(len(append_filelist))
    print(len([item for item in os.listdir(original_dir) if os.path.splitext(item)[1]=='.csv']))
    print(set([item for item in os.listdir(original_dir) if os.path.splitext(item)[1]=='.csv']) - set(append_filelist))

    item = append_filelist[0]
    with open(append_dir+item,'r') as appendfile, open(original_dir+item,'r') as originalfile:
        
        read_originalfile = originalfile.readlines()
        read_appendfile = appendfile.readlines()
    originalset = set(read_originalfile)
    appendset = set(read_appendfile)
    results = originalset.difference(appendset)
    if len(results) >= 2:
        originaldataframe = pd.read_csv(StringIO(''.join(read_originalfile)),sep=',')
        appenddataframe = pd.read_csv(StringIO(''.join(read_appendfile)),sep=',')
        originaldataframe = pd.concat([originaldataframe, appenddataframe])
        originaldataframe = originaldataframe.reset_index(drop=True)
        originaldataframe.to_csv(item,index=False)




if __name__ == '__main__':
    main()
