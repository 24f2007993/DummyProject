from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')
@app.route('/')
def home():
    return 'hello world!'
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register')
def register():
    return 
if __name__ == '__main__':
    app.run(debug = True)