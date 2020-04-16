from flask import Flask, jsonify, render_template, request
import os

import BidsValidatorA as BVA
from collections import OrderedDict
app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/end_stu_live_session', methods=["GET", "POST"])
def end_stu_live_session():
    if request.method == 'POST':
        data = request.json
        length = len(data)
        out=""
        x = list()
        l=list()
        for i in range(length):
            if data[i] not in x:
                x += splitall(data[i])
                #print(x)
                l = del_file(x)#delete files
                l = list(OrderedDict.fromkeys(x)) #remove doublon
        out = BVA._verify_name(l)
        date=BVA.is_date(l)
        data=BVA.is_data(l)
        subject=BVA.is_sub(l)
        source=BVA.is_source(l)
        ap=[date, source,subject,data]
        if (all(ap)):
            print("à quand cet apero en visio du NIT?!")
       #print(out)

        return jsonify({
         "out" : out,
         "date" : date,
         "data" : data,
         "subject" : subject,
         "source" : source,
         "list" :l
         })

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
