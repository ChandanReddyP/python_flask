from flask import Flask
FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return "hai sir"

if __name__=='__main__':
    FAI.run(debug=True)