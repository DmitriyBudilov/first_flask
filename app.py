from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/departures/<departures>/')
def index_page(departures):
    return render_template('departure.html')

@app.route('/tours/<id>/')
def about_page(id):
    return render_template('tour.html')

if __name__ == '__main__':
    app.run(debug=True)