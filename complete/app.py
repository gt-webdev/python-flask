from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.static_folder = 'static'

chat_log = ["Hello, I am a chat bot (as you can tell). I merely repeat what you say."]
# https://jinja.palletsprojects.com/en/2.11.x/templates/

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_chat = request.form['chatInp']
        chat_log.append(new_chat)
        response_to_chat = f'You said "{new_chat}"'
        chat_log.append(response_to_chat)

    return render_template('index.html', chat_log=chat_log)

@app.route('/api/chat/', methods=['GET'])
def get_log():
    return json.dumps([
        {
            "result": "success",
            "chat_log": chat_log
        }
    ])

@app.route('/api/newpost/<string:new_message>', methods=['POST'])
def add_chat(new_message):
    chat_log.append(new_message)
    response_to_chat = f'You said "{new_message}"'
    chat_log.append(response_to_chat)
    return json.dumps([{"result": "success"}])

@app.route('/api/chatelem/<int:id>')
def get_chat(id):
    chat_elem = chat_log[id]
    if id % 2 == 0:
        speaker = "Computer"
    else:
        speaker = "User"
    return json.dumps([
        {
            "result": "success",
            "chat": chat_elem,
            "speaker": speaker
        }
    ])