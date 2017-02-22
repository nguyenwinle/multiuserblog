import webapp2
from google.appengine.ext import db
from bloghandler import BlogHandler

# page that renders on our home page
class BlogFront(BlogHandler):
    '''constructor for this class.'''
    def get(self):
        posts = db.GqlQuery(
            "select * from Post order by created desc limit 10")

        self.render('front.html', posts=posts)
