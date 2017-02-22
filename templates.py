import hashlib
import hmac
import jinja2
import random
import re
import os
import webapp2
from webapp2 import WSGIApplication
from handlers.blogfront import BlogFront
from handlers.bloghandler import BlogHandler
from handlers.commenterror import CommentError
from handlers.deletecomment import DeleteComment
from handlers.deletepost import DeletePost
from handlers.editdeleteerror import EditDeleteError
from handlers.likepost import LikePost
from handlers.login import Login
from handlers.logout import Logout
from handlers.newcomment import NewComment
from handlers.newpost import NewPost
from handlers.postpage import PostPage
from handlers.signup import Signup
from handlers.updatecomment import UpdateComment
from handlers.updatepost import UpdatePost
from handlers.signup import Register
from handlers.likeerror import LikeError

from models.user import User
from models.post import Post
from models.comment import Comment

from string import letters
from google.appengine.ext import db

from helpers import *




app = webapp2.WSGIApplication([('/', BlogFront),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/newpost', NewPost),
                               ('/commenterror', CommentError),
                               ('/blog/([0-9]+)/like', LikePost),
                               ('/signup', Register),
                               ('/blog/([0-9]+)/deletepost', DeletePost),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/blog/([0-9]+)/updatepost', UpdatePost),
                               ('/blog/([0-9]+)/newcomment', NewComment),
                               ('/blog/([0-9]+)/updatecomment/([0-9]+)', UpdateComment),
                               ('/blog/([0-9]+)/deletecomment/([0-9]+)', DeleteComment),                               
                               ('/editDeleteError', EditDeleteError),
                               ('/likeError', LikeError)],
                              debug=True)
