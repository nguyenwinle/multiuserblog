from google.appengine.ext import db
from helpers import *

# database for comments
class Comment(db.Model):
    '''constructor for this class'''
    comment = db.StringProperty(required=True)
    post = db.StringProperty(required=True)

    @classmethod
    def render(self):
        self.render("comment.html")
