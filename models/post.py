from google.appengine.ext import db
from helpers import *
from models.comment import Comment
from models.user import User

# database for our posts
class Post(db.Model):
    '''constructor for this class'''
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    created_by = db.TextProperty()
    likes = db.IntegerProperty(default=0)
    liked_by = db.ListProperty(str)

    @classmethod
    def by_post_name(cls, name):
        u = cls.all().filter('name =', name).get()
        return u

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p=self)

    @property
    def comments(self):
        return Comment.all().filter( "post = ", str(self.key().id()) )

