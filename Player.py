from google.appengine.ext import db

""" Models an individual Player entry. """
class Player(db.Model):
    
    ''' First name of a player '''
    firstName = db.StringProperty(required=True)
    
    ''' Last name of a player'''
    lastName = db.StringProperty(required=True)
    
    ''' The identifier of the team the player belongs to '''
    teamUserId = db.StringProperty(required=True)
    
    ''' The number of the player on the team '''
    playerNumber = db.IntegerProperty()
    
    '''
    The passing ability of a player.
    
    This includes the ability to accurately pass the ball to a teammate as well
    as the vision and intelligence to pick out a good pass for a teammate.
    '''
    passing = db.IntegerProperty()
  
    '''
    The crossing ability of a player.
    
    This is the ability to pick out a teammate near the goal and deliver an
    accurate cross to them.
    '''
    crossing = db.IntegerProperty()
    
    '''
    The footwork ability of a player.
    
    This is the player's ability to run past an opponent with the ball. It
    includes skills such as ball control, agility, and speed.
    '''
    footwork = db.IntegerProperty()
    
    '''
    The attacking ability of a player.
    
    This includes the ability to shoot the ball well while keeping one's
    composure   when under pressure from defenders. This also includes the
    ability to make intelligent runs off the ball or be in good positions to
    contribute to team attacks.
    '''
    attacking = db.IntegerProperty()
    
    '''
    The defending ability of a player.
    
    This includes the ability to accurately take the ball away from opponents or
    pressure them into making a mistake and losing the ball. This also includes
    the ability to read and predict the movements of opposing attackers and be in
    good defensive positions to nullify opponent attacks.
    '''
    defending = db.IntegerProperty()
    
    '''
    The strength ability of a player.
    
    This ability helps attackers hold onto the ball when under pressure from
    defenders as well as be able to shoot the ball harder.
    This ability helps defender steal the ball from attackers more easily.
    '''
    strength = db.IntegerProperty()
    
    '''
    The stamina of a player.
    
    The more stamina a player has, the longer they can run and play at a normal
    level.
    '''
    stamina = db.IntegerProperty()
    
    '''
    The experience of a player.
    
    Experience helps players be able to make better choices during a game.
    '''
    experience = db.IntegerProperty()
    
    '''
    The goalkeeping ability of a player.
    '''
    goalkeeping = db.IntegerProperty()

