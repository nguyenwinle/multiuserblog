import webapp2
from bloghandler import BlogHandler
from models.user import User
from models.post import Post
from models.comment import Comment
from helpers import *

# page that shows error when liking a post you're not supposed to
class LikeError(BlogHandler):
    '''constructor for this class.'''
    def get(self):
        self.write("You are not allowed to like this post.")
