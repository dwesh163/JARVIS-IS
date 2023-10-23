from flask import Flask, render_template, request
import subprocess

app = Flask(__name__, template_folder='HTML')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérer le script Python envoyé via le formulaire
        command = request.form['command']

        print(command)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
