from flask import Flask, render_template

import generate

app = Flask(__name__)



@app.route('/')
def hello_world():
	scenes = generate.generate_story()
	return render_template('layout.html', scenes=scenes)

app.run(host='0.0.0.0', port=36868, debug=True)