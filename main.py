from flask import Flask

app=Flask(__name__) 

@app.route('/') 
def helloword():
    return 'Olá mundo'