from flask import Flask, render_template, request, url_for, flash, redirect, make_response, session
from __main__ import app

@app.route('/',methods=['GET'])
def index():
	return render_template('index.html')