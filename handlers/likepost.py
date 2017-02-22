import webapp2
from bloghandler import BlogHandler

from models.user import User
from models.post import Post
from helpers import *

class LikePost(BlogHandler):
    '''constructor for this class.'''
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if not post:
            self.write("This post no longer exists.")
            return
        
        if not self.user:
            self.redirect('/login')
        else:
            author = post.created_by
            current_user = self.user.name

            if author == current_user or current_user in post.liked_by:
                self.redirect('/likeError')
            else:
                post.likes = post.likes + 1
                post.liked_by.append(current_user)
                post.put()
                self.redirect('/')
