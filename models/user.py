from google.appengine.ext import db
from helpers import *

# database for our users
class User(db.Model):
    '''constructor for this class'''
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    # cls refers to self, which here is Class User
    def by_id(cls, uid):
        return cls.get_by_id(uid, parent=users_key())

    # property that looks up a user by name
    @classmethod
    def by_name(cls, name):
        u = cls.all().filter('name =', name).get()
        return u

    # takes name, pw and email and creates a new User object
    @classmethod
    def register(cls, name, pw, email=None):
        pw_hash = make_pw_hash(name, pw)
        return cls(parent=users_key(), name=name, pw_hash=pw_hash, email=email)

    # returns the user if name and pws is a valid
    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u
