import webapp2
from bloghandler import BlogHandler
from models.user import User
from models.post import Post
from models.comment import Comment
from helpers import *

class UpdatePost(BlogHandler):
    '''constructor for this class.'''
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if not self.user:
            self.redirect('/login')

        if not post:
            self.write("This post no longer exists")
            return
        
        else:
            username_1 = post.created_by
            username_2 = self.user.name
            if username_1 == username_2:
                key = db.Key.from_path('Post', int(post_id), parent=blog_key())
                post = db.get(key)
                print "post = ", post
                error = ""
                self.render("updatepost.html", subject=post.subject,
                            content=post.content, error=error)
            else:
                self.redirect("/editDeleteError")

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        username_1 = post.created_by
        username_2 = self.user.name

        if username_1 == username_2:
                key = db.Key.from_path('Post', int(post_id), parent=blog_key())
                post = db.get(key)
                print "post = ", post
                error = ""
                self.render("updatepost.html", subject=post.subject,
                            content=post.content, error=error)
                
        else:
            self.redirect("/login")
        
        if not post:
            self.write("This post no longer exists")
            return
        
        else:
            subject = self.request.get('subject')
            content = self.request.get('content')
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            p = db.get(key)
            p.subject = self.request.get('subject')
            p.content = self.request.get('content')
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
            pid = p.key().id()
            print "pid = ", str(pid)
