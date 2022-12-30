from flask import Flask, url_for, redirect, render_template, request

TEMPLATE_FOLDER = './templates'
STATIC_FOLDER = './static'
app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder = STATIC_FOLDER)

def answer_system(msg):
    return msg*3

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat') 
def chatbot():
    return render_template('chat.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('a')
    return answer_system(userText)

app.run()