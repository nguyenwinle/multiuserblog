import webapp2
from bloghandler import BlogHandler
from google.appengine.ext import db
from helpers import *
from models.post import Post
from models.user import User
from models.comment import Comment

# handler for posting a new story/blog
class NewPost(BlogHandler):
    '''constructor for this class.'''
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            return self.redirect("/login")

    def post(self):
        if not self.user:
            return self.redirect('/blog')

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent=blog_key(),
                     subject=subject,
                     content=content,
                     created_by=User.by_name(self.user.name).name)

            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
            return 
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content,
                        error=error)
