from flask import Flask, render_template, url_for, request, session, redirect
from linkbuilder.builder import *
import random
import pymongo

from pymongo import MongoClient
client = MongoClient('')
db = client.bitcoin.users

app = Flask(__name__)
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    link = request.form['link']
    short_link = build_link(request.form['link'])
    return short_link

@app.route('/<s>')
def link(s):
    if is_exsisting(s):
        print('INSIDE IF')
        return redirect('http://{}'.format(get_url(s)))
    return redirect(url_for('index'))






#Functions vvvv

def build_link(url):
    size = random.randint(4, 12)
    new_link = ''
    print('Creating a new Link with size of {}'.format(size))
    for i in range(size):
        new_link += letters[random.randint(1, len(letters))]
    if check_link(new_link,url):
        print('Passed Check, and adding to DB')
        db.insert({'short' : new_link, 'url' : url})
        return new_link
    build_link(url)

def check_link(short,link):
    return db.find({'short' : short, 'url' : link }).count() == 0 #Makes sure link hasn't been created yet

def is_exsisting(i):
    return db.find({'short' : i}).count() >= 1

def get_url(s):
    print(db.find_one({'short' : s}))
    return db.find_one({'short' : s})['url']

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run()
