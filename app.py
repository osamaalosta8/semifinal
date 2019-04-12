from flask import Flask , render_template, request,redirect
import dataset

app =  Flask(__name__)
db = dataset.connect('sqlite:///scholars.db')
scholars_tb = db['books']

@app.route('/')
def home():
	return render_template('homepage.html')
	print "Hello"
@app.route('/germany')
def germany():
	return render_template('germany.html')

@app.route('/germany/khaled')
def khaled():
	return render_template('khaled.html')
@app.route('/america')
def america():
	return render_template('america.html')
@app.route('/america/akram', methods =["POST" , "GET"])

def akram():
	if request.method=="GET":
		return render_template ('akram.html')
	elif request.method=="POST":
		name= request.form['name']
		subject=request.form['subject']
		email=request.form['email']
		message=request.form['message']
		table_entry={message:"message", email:"email",subject:"subject",name:'name'}
		scholars_tb.insert(table_entry)
		return render_template("akram.html",message=message,email=email,subject=subject,name=name)
if __name__ =='__main__':
	app.run(debug= True,port=5110)		