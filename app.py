from flask import Flask, render_template  # importing the render_template function

app = Flask(__name__)
# home route
@app.route("/")
def hello():
    return render_template('index.html', name = 'Subal', gender = 'Male')

if __name__ == "__main__":
    app.run(debug = True) 