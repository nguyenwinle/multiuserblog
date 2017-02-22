import webapp2
from bloghandler import BlogHandler
from models.user import User
from models.post import Post
from models.comment import Comment
from helpers import *

# Handler to shows error message to delete or edit a comment
class CommentError(BlogHandler):
    '''constructor for this class.'''
    def get(self):
        self.write('You can only edit or delete comments you have created.')
