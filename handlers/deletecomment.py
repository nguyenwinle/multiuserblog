import webapp2
from bloghandler import BlogHandler
from models.user import User
from models.post import Post
from models.comment import Comment
from helpers import *

# Handler to delete a comment
class DeleteComment(BlogHandler):
    '''constructor for this class.'''
    def get(self, post_id, comment_id):
        post = Post.get_by_id( int(post_id), parent=blog_key() )
        comment = Comment.get_by_id( int(comment_id), parent=self.user.key() )
        
        if comment.parent().key().id() == self.user.key().id():
            comment.delete()
            self.redirect('/blog/%s' % str(post_id))
        else:
            self.redirect('/commenterror')

