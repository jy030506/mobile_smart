from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/store/', methods=['GET'])
def store():
	name = request.args.get('name')
	tel = request.args.get('tel')

	file = open('./data/phonebook.txt', 'a')
	data = "%s,%s\n" % (name, tel)
	file.write(data)
	file.close()

	return render_template('index.html', msg='save clear')

@app.route('/search/', methods=['POST'])
def search():
	name = request.form['s_name']
	tel = request.form['s_tel']

	file = open('./data/phonebook.txt', 'r')
	for line in file:
		a = line.split(',')
		if a[0] == name:
			tel = a[1]
			msg='검색에 성공하였습니다'
			break
		msg='검색에 실패했습니다'

	return render_template('index.html', msg=msg, s_name=name, s_tel=tel)

@app.route('/view/', methods=['GET'])
def view():
	phonebook = {}
	file = open('./data/phonebook.txt', 'r')
	for line in file:
		a=line.split('\n')
		b=a[0].split(',')
		phonebook[b[0]]=b[1]

	return render_template('view.html', dict=phonebook)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
