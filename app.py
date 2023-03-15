from flask import Flask, render_template, request
from chatGPT_output import chatGPT_output

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        output = chatGPT_output(question, answer)
        return render_template('index.html', output=output)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
