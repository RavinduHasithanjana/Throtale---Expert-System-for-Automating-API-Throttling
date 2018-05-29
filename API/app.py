import os
import datetime
import time
from flask import Flask
from flask import render_template
from sklearn.externals import joblib

app = Flask(__name__)

@app.route("/")
def hello():
    strptime = datetime.datetime.strptime
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d/%b/%Y:%H:%M:%S')
    t1 = strptime(st, "%d/%b/%Y:%H:%M:%S")
    print(t1.month)
    print(st)
    clf = joblib.load('Final.pkl')
    # print("work")
    preictioMade = clf.predict([[t1.day, t1.month, t1.hour, t1.minute, t1.second]])
    # day,month,hour,min,second
    print("work")
    return str(preictioMade)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
