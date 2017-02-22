from google.appengine.ext import db
import webapp2
from bloghandler import BlogHandler
from helpers import *
from models.user import User
from models.post import Post
from models.comment import Comment

# Handler for our blog pages that renders the story/blog
class PostPage(BlogHandler):
    '''constructor for this class.'''
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        print post

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post=post)
