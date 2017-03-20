from flask import (
	Flask,
	render_template
	)

app = Flask(__name__)
app.debug = True


@app.route("/", methods = ['GET', 'POST'])
def homepage():
    data = {}
    data['pagename'] = 'Home'
    return render_template('index.html', **data)



if __name__ == "__main__":
    app.run()	