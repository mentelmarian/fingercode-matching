#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:59:21 2022

@author: 
    Marian Leonard Mentel
"""

import os

# return all fingercodes contained in "folder"
def get_all_fingercode(folder):
    files = os.listdir(folder)
    files_path = []
    for i in files:
        temp = folder + '/' + i
        files_path.append(temp)
        files_path.sort()
    return files_path

# returns the fingerode's person ID (for 123_1.txt returns 123)
def get_fingercode_class(filename):
    name = filename.split('/')
    tmp = name[len(name)-1]
    label = tmp.split('.')
    return label[0].split('_')[0]

# returns the fingercode contained in "filename"
def read_from_file_fingercode(filename):
    fingercode = []
    f = open(filename)
    fingercode = f.read()
    return fingercode

# computes the euclidean distance (binary values ---> sum|xi-yi|)
def euclidean_distance(fingercode_1, fingercode_2):
    distance = 0
    for i in range(len(fingercode_1)-1):        # -1 to avoid reading the newline char
        distance += abs(int(fingercode_1[i])-int(fingercode_2[i]))
    return distance

''' # old function
def parse_fingercode(fingercode):
    parsed_fingercode = []
    for line in fingercode:
        l = re.sub(r'[^\w]', ' ', line)
        string_list = l.split()
        int_list = list(map(int, string_list))
        parsed_fingercode.append(int_list)
    return parsed_fingercode
'''