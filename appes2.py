from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

utenti = []

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET'])
def login():
    for user in utenti:
        if user["username"] == request.args["username"]:
            if user["password"] == request.args['password']:
                return render_template('#pagina benvenuto.html')
            #modificare pagina benvenuto/a
    return render_template('login.html')

@app.route('/data1', methods=['GET'])
def data():
    name = request.args['name']
    username = request.args['username']
    password = request.args['password']
    confirm = request.args['confirmpassword']
    sex = request.args['sex']
    if password == confirm:
        if sex:
            if username:
                if password:
                    if confirm:
                        if name:
                            utenti.append({"name": name, "username": username, "password": password, "confirm": confirm, "sex": sex})
                            return redirect(url_for("/login"))
    

    return render_template('error.html', nome = username)





    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)