from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import random
app = Flask(__name__)

class MongoDatabase:
    def __init__(self,url,dbname,uri):
        self.db = url
        app.config['MONGO_DBNAME'] = dbname
        app.config['MONGO_URI'] = uri
    def is_link(self,link):
        return
    def build_link(self,link):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        size = random.randint(4, 12)
        link = ''
        for i in range(size):
            link += letters[random.randint(0, len(letters) - 1)]  # Get random letter capital or not, and return it
        if self.is_link(link):
            self.build_link(link)
        else:
            return link
