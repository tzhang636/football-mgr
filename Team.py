from google.appengine.ext import db

""" Models a Team, minus the Players. """
class Team(db.Model):
    
    '''
    The name of the team.
    '''
    teamName = db.StringProperty(multiline=False, required=True)
    
    '''
    The name of the stadium.
    '''
    stadiumName = db.StringProperty(multiline=False, required=True)
    
    '''
    The budget of the team.
    '''
    budget = db.IntegerProperty(required=True)
    
    '''
    The user the team belongs to.
    '''
    userId = db.StringProperty(multiline=False, required=True)
    
