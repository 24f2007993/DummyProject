from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')
@app.route('/')
def home():
    return 'hello world!'
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/signUp')
def signUp():
    return render_template('signUp.html')
@app.route('/createProduct')
def create():
    return render_template('create_product.html')
@app.route('/updateProduct')
def update():
    return render_template('update_product.html')
@app.route('/requestProduct')
def request():
    return render_template('request.html')
@app.route('/user')
def user():
    return render_template('user_dash.html')
@app.route('/manager')
def manager():
    return render_template('manager_dash.html')
if __name__ == '__main__':
    app.run(debug = True)