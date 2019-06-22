class tower():

	def __init__(self):
		self.count = 0
		self.A = 1
		self.B = 2
		self.C = 3
		self.seq = []
		


	def hanoi(self,n,A,B,C):
		if n > 0:
			self.hanoi(n-1,A,C,B)
			self.seq.append([A,C])
			self.count += 1
			self.hanoi(n-1,B,A,C)
		return self.count

from flask import Flask , render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField , SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class IntForm(FlaskForm):

	num = IntegerField('Enter the number of discs: ')
	submit = SubmitField("Submit")

@app.route('/', methods=['GET','POST'])

def index():
	num = 4
	form = IntForm()
	if form.validate_on_submit():
		num =form.num.data
		form.num.data = ''
	l = tower()
	s = l.hanoi(num,1,2,3)
	array = l.seq
	return render_template('index.html', count = s  , seq = array , discs = num, form = form)

if __name__=='__main__' :
	app.run()