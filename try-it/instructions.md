# Step 1: Include necessary imports
```
from flask import Flask, render_template, request
import json
```

# Step 2: Create a Flask app
```
app = Flask(__name__)
app.static_folder = 'static'
chat_log = ["Hello, I am a chat bot (as you can tell). I merely repeat what you say."]
```

# Step 3: Create a route for the main page
```
@app.route('/')
def index():
    return render_template('index.html')
```

# Step 4: Display chat log in index.html
In index.html:
```
{% for log in chat_log %}
    <p>{{ log }}</p>
{% endfor %}
```

In app.py:
```
render_template('index.html', chat_log=chat_log)
```

# Step 5: Create POST request within website
```
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_chat = request.form['chatInp']
        chat_log.append(new_chat)
        response_to_chat = f'You said "{new_chat}"'
        chat_log.append(response_to_chat)

    return render_template('index.html', chat_log=chat_log)
```

# Step 6: Make computer's chat on left side and user's chat on right side
```
{% for log in chat_log %}
    {% if loop.index0 is divisibleby(2) %}
        <p class="botchat">{{ log }}</p>
    {% else %}
        <p>{{ log }}</p>
    {% endif %}
{% endfor %}
```

# Step 7: API GET request for all chat logs
```
@app.route('/api/chat/', methods=['GET'])
def get_log():
    return json.dumps([
        {
            "result": "success",
            "chat_log": chat_log
        }
    ])
```

# Step 8: API GET request for a single chat log
```
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
```

# Step 9: API POST request
```
@app.route('/api/newpost/<string:new_message>', methods=['POST'])
def add_chat(new_message):
    chat_log.append(new_message)
    response_to_chat = f'You said "{new_message}"'
    chat_log.append(response_to_chat)
    return json.dumps([{"result": "success"}])
```