"""
*************************************************************************
*    Course: 100 Days of Code - Dra. Angela Yu                          *
*    Author: Jorge Chavarriaga                                          *
*    Day: 56- Rendering Html Files with Flask - Project DAy 44          *
*    Date: 2021-01-20                                                   *
*************************************************************************
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def game():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8082 )