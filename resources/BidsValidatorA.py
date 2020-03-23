#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import errno
import json
import sys
import re


def path_hierarchy(path):
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

    for my_dict in list_dict:

        if my_dict['type'] == 'directory':
            names.append(my_dict['name'])
            names = get_name_in_dir(my_dict['children'], names)

    return names


def verify_name(names):

    if (names[0] == "data" or names[0] == "Data"):
        print("Folder Data found ")
    else:
        print("ERROR :  Data folder not found. Please check this name : " +
              names[0])

    if "sub-" or "Sub-" in str(names[2]):
        print("Folder Name found : " + names[2])
    else:
        print(
            "ERROR :  Folder name does not contain sub-."
            ".Please check this name : " + names[2])

    if re.search("^\d{6}_\d{3}_([a-zA-Z]{1})_([a-zA-Z]*)_([a-zA-Z]*)",
                 names[3]):
        print("Date format ok ")
    else:
        print(
            "ERROR : Folder name does not follow the rules : \n /Date[yymmdd]_"
            "numéro de session (expérience) _ espèce [m, o, r, s] _ "
            "UFID animal(User friendly ID) _ commentaire . "
        )

    if "source " or "Sources" in names:
        print("Folder Sources Found . ")
    else:
        print("ERROR : Folder Sources not found .")

    if "META-DATA" in names:
        print("Folder META-DATA Found ")
    else:
        print("WARNING : Folder META-DATA not found .")
    if "Row-data" in names:
        print("Folder Row data Found ")
    else:
        print("WARNING : Folder Row data not found .")


if __name__ == '__main__':
    import json
    import sys

    try:
        directory = sys.argv[1]

    except IndexError:
        directory = "."

    print(json.dumps(path_hierarchy(directory), indent=2, sort_keys=True))

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
