import os
from flask import Flask
from flask import render_template
from sklearn.externals import joblib
app = Flask(__name__)

@app.route("/")
def hello():
    clf = joblib.load('Final.pkl')
    # print("work")
    preictioMade = clf.predict([[16., 12., 22., 12., 24.]])
    print("work")
    return str(preictioMade)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
