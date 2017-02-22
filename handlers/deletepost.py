import webapp2
from bloghandler import BlogHandler
from models.user import User
from models.post import Post
from models.comment import Comment
from helpers import *

# Handler to delete a post
class DeletePost(BlogHandler):
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
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            username_1 = post.created_by
            username_2 = self.user.name

            if username_1 == username_2:
                key = db.Key.from_path('Post', int(post_id), parent=blog_key())
                post = db.get(key)
                post.delete()
                self.render("deletepost.html")
            else:
                self.redirect("/editDeleteError")
