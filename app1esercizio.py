#pip install pytz
from flask import Flask, render_template
app = Flask(__name__)
from datetime import datetime
import pytz


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index1.html', bgcolore='Hello, world!')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)