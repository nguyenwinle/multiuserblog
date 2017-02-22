import webapp2
from bloghandler import BlogHandler

# this allows for user to logout
class Logout(BlogHandler):
    '''constructor for this class.'''
    def get(self):
        self.logout()
        self.redirect('/blog')
