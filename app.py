from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # Data to send to the HTML
    user_data = {
        "name": "John Doe",
        "color": "blue",
        "items": ["Flask", "Python", "HTML", "CSS"]
    }
    # Render the HTML and pass data
    return render_template('home.html', **user_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)