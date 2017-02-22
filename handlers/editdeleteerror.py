import webapp2
from bloghandler import BlogHandler
from models.user import User
from models.post import Post
from models.comment import Comment
from helpers import *

# page that shows error when trying to edit or delete someone else's post
class EditDeleteError(BlogHandler):
    '''constructor for this class.'''
    def get(self):
        self.write('You are not allowed to edit or delete this post.')
