from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('indexes1.html')


@app.route('/data', methods=['GET'])
def data():
    username = request.args['username']
    password = request.args['password']
    if username == 'admin':
        if password == 'XXX123##':
            return render_template('welcome1.html', nome = username)
    return render_template('error.html', nome = username)





    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)