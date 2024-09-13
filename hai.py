from flask import Flask,render_template

FAO=Flask(__name__)

@FAO.route('/htmlpage')
def htmlpage():
    return render_template('htmlpage.html',name='chandan',age='25')

@FAO.route('/sfiles')
def sfiles():
    return render_template('sfiles.html')

if __name__=='__main__':
    FAO.run(debug=True)