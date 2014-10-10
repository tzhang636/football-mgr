import datetime
from google.appengine.ext import db

""" Class that represents a new training session. """
class TrainingType(db.Model):
    
    teamUserId = db.StringProperty()
    
    status = db.StringProperty()
    
    startTime = db.DateTimeProperty()
    
    endTime = db.DateTimeProperty()
        
    type = db.StringProperty()
    
    primaryAttr = db.StringProperty()
    
    secondaryAttr = db.StringProperty()
    
    tertiaryAttr = db.StringProperty()
    
    
    
    
    
