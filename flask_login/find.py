__author__ = 'raghavendra'

from flask import Flask, render_template, request
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.test1
informations = db.informations
app = Flask(__name__)
import json

@app.route('/')
def index():
    return render_template("search.html")
    # return render_template("temp.html")

@app.route('/data',methods=['GET', 'POST'])
def data():
    name = request.form.get("username")

    # l=[]
    post = informations.find_one({"username":name}, {"_id" : 0})

        # post = informations.find_one()
    if not post:
        post = "Data not Found"
    print post
    return render_template("search1.html",data=post)
        # l.append(post)
    # return json.dumps(l)


    return "Succesfull"
        # print post
        # db.informations.find()



#     for post in infos:
#         print post
#         result = post
#         print result
#
#         result["_id"] = str(result["_id"])
#         return json.dumps(result)
#
#     print db.informations.find_one()
#     # print db.informations.find()
#     result = db.informations.find_one()
#     result["_id"] = str(result["_id"])
#     return json.dumps(result)
# #
#     print db.informations.find_one()
#     print "Number of id's are", informations.count()
#     result = db.informations.find_one()
#     result["_id"] = str(result["_id"])
#     return json.dumps(result)
# data()
#
if __name__ == '__main__':
    app.run(host='localhost', debug=True,  port=12345)
