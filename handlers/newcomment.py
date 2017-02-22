import webapp2
from bloghandler import BlogHandler
from models.user import User
from models.post import Post
from models.comment import Comment
from helpers import *

# Handler to post new comment
class NewComment(BlogHandler):
    '''constructor for this class.'''
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        subject = post.subject
        content = post.content
        
        if not post:
            self.write("This post no longer exists.")
            return
        
        if not self.user:
            error = "You must be logged in to comment"
            self.redirect("/login")
            return

        self.render("newcomment.html", subject=subject, content=content, pkey=post.key())

    def post(self, post_id):

        # make sure the post_id exists
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if not post:
            self.error(404)
            return
        
        if not self.user:
            self.redirect('login')
        # creates comment
        comment = self.request.get('comment')
        
        if comment:
            c = Comment(comment=comment, post=post_id, parent=self.user.key())
            c.put()
            self.redirect('/blog/%s' % str(post_id))
        else:
            error = "please provide a comment!"
            self.render("permalink.html", post = post, content=content, error=error)
