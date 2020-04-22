#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import errno
import json
import sys
import re
import argparse

dir_rules=os.path.join(os.path.dirname(__file__)) + "/rules/"

def path_hierarchy(path):
    """[make a json tree structure of the folder given in parameter]
    
    Arguments:
        path {[type]} -- [Path to the folder]
    
    Returns:
        [json] -- [Tree of the folder]
    """

    hierarchy = {
        'type': 'directory',
        'name': os.path.basename(path),
        'path': path,
    }

    try:
        hierarchy['children'] = [
            path_hierarchy(os.path.join(path, contents))
            for contents in os.listdir(path)
        ]
    except OSError as e:
        if e.errno != errno.ENOTDIR:
            raise
        hierarchy['type'] = 'file'

    return hierarchy


def get_name_in_dir(list_dict, names):
    """[Get all the name of directories in the Dict recusively]
    
    Arguments:
        list_dict {[Dict]} -- [Json to dict ]
        names {[list]} -- [Names of directories founds]
    Returns:
        [list] -- [Names of directories founds]
        
    """
    for my_dict in list_dict:

        if my_dict['type'] == 'directory':
            names.append(my_dict['name'])
            names = get_name_in_dir(my_dict['children'], names)

    return names


def verify_name(names):
    """[Check names of folder that verify the rules bids]
    
    Arguments:
        names {[list]} -- [Names founds in the Json structure ]

        a faire recusivement
    """

    if (names[0] == "data" or names[0] == "Data"):
        print("SUCCESS : Folder Data found ")
    else:
        print("ERROR :  Data folder not found. Please check this name : " +
              names[0])

    if "sub-" or "Sub-" in str(names[2]):
        print("SUCCESS : Folder Name found : " + names[2])
    else:
        print("ERROR :  Folder name does not contain sub-."
              ".Please check this name : " + names[2])

    if re.search("^\d{6}_\d{3}_([a-zA-Z]{1})_([a-zA-Z]*)_([a-zA-Z]*)",
                 names[3]):
        print("SUCCESS : Date format ok ")
    else:
        print(
            "ERROR : Folder name does not follow the rules : \n /Date[yymmdd] _"
            "numéro de session (expérience) _ espèce [m, o, r, s] _ "
            "UFID animal(User friendly ID) _ commentaire . ")

    if "source " or "Sources" in names:
        print("SUCCESS : Folder Sources Found . ")
    else:
        print("ERROR : Folder Sources not found .")

    if "META-DATA" in names:
        print("SUCCESS : Folder META-DATA Found ")
    else:
        print("WARNING : Folder META-DATA not found .")
    if "Row-data" in names:
        print("SUCCESS : Folder Row data Found ")
    else:
        print("WARNING : Folder Row data not found .")

def _verify_name(names):
    """[Check names of folder that verify the rules bids]
    
    Arguments:
        names {[list]} -- [Names founds in the Json structure ]
    """
    x=list()
    if (names[0] == "data" or names[0] == "Data"):
       x.append ("SUCCESS : Folder Data found  \n")
    else:
       x.append ("ERROR :  Data folder not found. Please check this name : " +
              names[0]+"\n")

    if "sub-" or "Sub-" in str(names[2]):
       x.append ("SUCCESS : Folder Name found : " + names[2]+"\n")
    else:
       x.append ("ERROR :  Folder name does not contain sub-."
              ".Please check this name : " + names[2]+"\n")

    if re.search("^\d{6}_\d{3}_([a-zA-Z]{1})_([a-zA-Z]*)_([a-zA-Z]*)",
                 names[3]):
       x.append("SUCCESS : Date format ok \n")
    else:
       x.append(
            "ERROR : Folder name does not follow the rules : \n /Date[yymmdd] _"
            "numéro de session (expérience) _ espèce [m, o, r, s] _ "
            "UFID animal(User friendly ID) _ commentaire . \n"
            "Your path is : "+names[3])

    if "source " or "Sources" in names:
       x.append("SUCCESS : Folder Sources Found . \n")
    else:
       x.append("ERROR : Folder Sources not found .\n")

    if "META-DATA" in names:
       x.append("SUCCESS : Folder META-DATA Found ")
    else:
       x.append("WARNING : Folder META-DATA not found .\n")
    if "Row-data" in names:
       x.append("SUCCESS : Folder Row data Found ")
    else:
       x.append("WARNING : Folder Row data not found .\n")
    return x


def is_date(names):
        ''' Check if file is data. '''
        regexps = get_regular_expressions(dir_rules
                    + 'date_rules.json')
        conditions=[]
        for word in names:
            conditions.append([(re.compile(x).search(word) is not None) for x in regexps])
        # print(flatten(conditions))  
        return(any(flatten(conditions))) 

def is_data(names):
        ''' Check if file is data. '''
        regexps = get_regular_expressions(dir_rules
                    + 'data_rules.json')
        conditions=[]
        for word in names:
             conditions.append([(re.compile(x).match(word) is not None) for x in regexps])
        # print(flatten(conditions))
        return (any(flatten(conditions)))
def is_sub(names):
        ''' Check if file is data. '''
        regexps = get_regular_expressions(dir_rules
                    + 'subject_rules.json')
        conditions=[]
        for word in names:
             conditions.append([(re.compile(x).search(word) is not None) for x in regexps])
        #  print(flatten(conditions))
        return (any(flatten(conditions)))
def is_source(names):
        ''' Check if file is data. '''
        regexps = get_regular_expressions(dir_rules
                    + 'source_rules.json')
        conditions=[]
        for word in names:
             conditions.append([(re.compile(x).search(word) is not None) for x in regexps])
        #  print(flatten(conditions))
        return (any(flatten(conditions)))
        
def get_regular_expressions(fileName):

        regexps = []

        with open(fileName, 'r') as f:
            rules = json.load(f)

        for key in list(rules.keys()):
            rule = rules[key]

            regexp = rule["regexp"]

            if "tokens" in rule:
                tokens = rule["tokens"]

                for token in list(tokens):
                    regexp = regexp.replace(token, "|".join(tokens[token]))

            regexps.append(regexp)

        return regexps

def flatten(seq):
    l = []
    for elt in seq:
        t = type(elt)
        if t is tuple or t is list:
            for elt2 in flatten(elt):
                l.append(elt2)
        else:
            l.append(elt)
    return l



if __name__ == '__main__':
    # add argparse for verbose option
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="increase output verbosity")
    parser.add_argument("path", help="Path to your folder ")
    args = parser.parse_args()

    if args.verbose:
        try:
            directory = args.path

        except IndexError:
            directory = "."
        print(json.dumps(path_hierarchy(directory), indent=2, sort_keys=True))

    try:
        directory = args.path

    except IndexError:
        directory = "."

    dic_data = json.loads(
        json.dumps(path_hierarchy(directory), indent=2, sort_keys=True))

    names = []
    names = get_name_in_dir([dic_data], names)
    arr = []
    print("\n")
    print("list of folder : ")

    print(u" /".join(names))
    print("\n")
    verify_name(names)
