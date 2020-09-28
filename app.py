# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:20:32 2020

@author: Dev SynerSense 3500
"""


from flask import Flask
app = Flask(__name__)

@app.route('/home')
def hello_world():
    return '<h1>Synersense Demo</h1>'

if __name__ == '__main__':
    app.run()
