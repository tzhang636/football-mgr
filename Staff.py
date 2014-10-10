from google.appengine.ext import db

class Staff(db.Model):
    
    '''
    The teamUserId of the staff.
    '''
    teamUserId = db.StringProperty()
    
    '''
    The role of the staff.
    '''
    role = db.StringProperty()
    
    '''
    First attribute coached.
    '''
    firstAttr = db.StringProperty()
    
    '''
    Second attribute coached.
    '''
    secondAttr = db.StringProperty()
    
    '''
    Level of the staff.
    '''
    level = db.IntegerProperty()
    
    '''
    Cost for upgrade between levels (1-2, 2-3, 3-4, 4-5).
    '''
    upgradeCosts = db.ListProperty(int)
    
    '''
    Number between 1 and 10.
    Corresponds to the probability of success in training the first and second attributes, when the attribute is < 20.
    Probability of success lowers by 10% for each attribute +20 segment (20-40, 40-60, 60-80 etc).
    Depends on level of the staff, the higher the level, the higher the probability.
    '''
    probability = db.IntegerProperty()
    
    
    