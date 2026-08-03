from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Smart Expense Tracker</h1>
    <p>Project setup is successful.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)