from flask import Flask, render_template, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test1
informations1 = db.informations
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("temp.html")
@app.route('/save', methods=['GET', 'POST'])
def details():
        a = request.form.get('username')
        b = request.form.get('designation')
        c = request.form.get("email-id")
        d = request.form.get("contact")
        e = request.form.get("emp-id")
        informations1.insert({'username': a, 'designation': b, "email-id": c,"contact": d, "emp-id": e})
        # print a,b,c,d,e
        return "Successfull"

if __name__ == '__main__':
    app.run(host='localhost', debug=True,  port=12345)





daysOfWeek = ['Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday',
              'Sunday']

months =             ['Jan', \
                      'Feb', \
                      'Mar', \
                      'Apr', \
                      'May', \
                      'Jun', \
                      'Jul', \
                      'Aug', \
                      'Sep', \
                      'Oct', \
                      'Nov', \
                      'Dec']

print "DAYS: %s, MONTHS %s" % (daysOfWeek, months)












