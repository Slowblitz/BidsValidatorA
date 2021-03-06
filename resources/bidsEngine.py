
from Error import DataError,SourceError,DateError,SubError
import os
import errno
import json
import sys
import re
dir_rules=os.path.join(os.path.dirname(__file__)) + "/rules/" 

def is_bids(names):
        """Checks if a file path appropriate for BIDS.

        Main method of the validator. uses other class methods for checking
        different aspects of the file path.

        Parameters
        ----------
            path: string
                A path of a file you want to check.
        """

        validate= []
        validate.append(is_data(names))
        validate.append(is_date(names))
        validate.append(is_source(names))
        validate.append(is_sub(names))

        return (all(validate))



def is_bids_verbose(names):
    bool_error=0
    if is_data(names):
        bool_error=0
    else:
        try:
            raise DataError(names)
        except DataError as e:
            print( e.strerror)
            bool_error=1

    if is_date(names):
        bool_error=0
    else:
        try:
            raise DateError(names)
        except DateError as e:
            print( e.strerror)
            bool_error=1
    if is_sub(names):
        bool_error=0
    else:
        try:
            raise SubError(names)
        except SubError as e:
            print( e.strerror)
            bool_error=1
    if is_source(names):
        bool_error=0
    else:
        try:
            raise SourceError(names)
        except SourceError as e:
            print( e.strerror)
            bool_error=1 

    
    return bool_error
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

