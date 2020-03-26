from flask import Flask, jsonify, render_template, request
import os
import logging
import ast
import BidsValidatorA as BVA
from collections import OrderedDict
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/end_stu_live_session', methods=["GET", "POST"])
def end_stu_live_session():
    if request.method == 'POST':
        data = request.json
        length = len(data)
        x = list()
        for i in range(length):
            if data[i] not in x:
                x += splitall(data[i].encode('ascii', 'ignore'))
                print(x)
                l = del_file(x)
                l = list(OrderedDict.fromkeys(x))
        BVA.verify_name(l)
        print(l)

        return jsonify(l)


def del_file(Ilist):
    length = len(Ilist)
    for i in range(length):
        if "." in Ilist[i]:
            Ilist.remove(Ilist[i])


def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path:  # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts


if __name__ == "__main__":
    app.run()
