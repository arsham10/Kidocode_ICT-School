from flask import Flask,render_template, request, redirect

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quary' , methods = ['POST'])
def quary():
    info = request.form
    f = open('quaries.txt','a')
    f.write(str(info)+'\n')
    f.close()
    return redirect('/')
    
@app.route('/Admin/<password>')
def Admin(password):
    if password == 'Arsham1010':
        f=open('quaries.txt','r')
        info=f.read()
        f.close()
        return info
    else:
        return 'you are not allowed'
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
