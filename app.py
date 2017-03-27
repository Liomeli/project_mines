from flask import (
	Flask,
	render_template
	)
from itertools import product
from random import sample

app = Flask(__name__)
app.debug = True

def gamefield(a, b):
	L = list(product(range(a), range(b), repeat = 1))
	M = []
	for t in L:
		x = t[0]*20
		y = 40 + t[1]*20
		M.append((x,y,t))
	return M

def mines(a, b, c):
	L = list(product(range(a), range(b), repeat = 1))
	mine_list = sample(L, c)
	return mine_list

def button_action(m_l, i):
	if i in m_l:
		return 'BANG!'
	else:
		_ = [
		(i[0]-1, i[1]),
		(i[0]-1, i[1]+1),
		(i[0], i[1]+1),
		(i[0]+1, i[1]+1),
		(i[0]+1, i[1]),
		(i[0]+1, i[1]-1),
		(i[0], i[1]-1),
		(i[0]-1, i[1]-1),
		]
		count = 0
		for el in _:
			if el in mine_list:
				count += 1
		if count != 0:
			return count
		else:
			pass

@app.route("/", methods = ['GET', 'POST'])
def homepage():
    data = {}
    data['pagename'] = 'Home'
    return render_template('index.html', **data)

@app.route("/starter", methods = ['GET', 'POST'])
def starter():
	data = {}
	data['pagename'] = 'Starter'
	data['M'] = gamefield(9, 9)

	return render_template('starter.html', **data)

@app.route("/middle", methods = ['GET', 'POST'])
def middle():
	data = {}
	data['pagename'] = 'Middle'
	data['M'] = gamefield(16, 16)
	return render_template('middle.html', **data)

@app.route("/expert", methods = ['GET', 'POST'])
def expert():
	data = {}
	data['pagename'] = 'Expert'
	data['M'] = gamefield(30, 16)
	return render_template('expert.html', **data)

@app.route("/custom", methods = ['GET', 'POST'])
def custom():
	data = {}
	data['pagename'] = 'Custom'
	data['M'] = gamefield(30, 16)
	return render_template('custom.html', **data)

if __name__ == "__main__":
    app.run()	