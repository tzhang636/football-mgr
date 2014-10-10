import random
from Player import Player
from google.appengine.ext import db

class TrainingSession:
    
    def trainPlayer(self, teamUserId, player, primaryAttr, secondaryAttr, tertiaryAttr):
        primaryAttrInc = 3
        secondaryAttrInc = 2
        tertiaryAttrInc = 1
        self.train(teamUserId, player, primaryAttr, primaryAttrInc)
        if secondaryAttr != None:
            self.train(teamUserId, player, secondaryAttr, secondaryAttrInc)
        if tertiaryAttr != None:
            self.train(teamUserId, player, tertiaryAttr, tertiaryAttrInc)
        
    def train(self, teamUserId, player, attr, attrInc):
        rand = random.randint(1, 10)
        
        # Can't get a query of more than three WHERE statements
        # So split into two queries
        firstStaff = db.GqlQuery("SELECT * FROM Staff WHERE teamUserId = '" + teamUserId + "' AND firstAttr = '" + attr + "'" )
        secondStaff = db.GqlQuery("SELECT * FROM Staff WHERE teamUserId = '" + teamUserId + "' AND secondAttr = '" + attr + "'")
        
        # Assign staff to either firstStaff or secondStaff (both limited to one or less query entity)
        staff = firstStaff
        if firstStaff.count(limit=1) == 0:
            staff = secondStaff
 
        for staffMember in staff:
            if attr == 'Passing':
                if ( (player.passing < 20 and rand <= staffMember.probability) or 
                     (player.passing < 40 and rand <= staffMember.probability-1) or 
                     (player.passing < 60 and rand <= staffMember.probability-2) or
                     (player.passing < 80 and rand <= staffMember.probability-3) or 
                     (player.passing < 99 and rand <= staffMember.probability-4) ):
                    player.passing += attrInc
                    
            elif attr == 'Crossing':
                if ( (player.crossing < 20 and rand <= staffMember.probability) or 
                     (player.crossing < 40 and rand <= staffMember.probability-1) or 
                     (player.crossing < 60 and rand <= staffMember.probability-2) or
                     (player.crossing < 80 and rand <= staffMember.probability-3) or 
                     (player.crossing < 99 and rand <= staffMember.probability-4) ):
                    player.crossing += attrInc      
                  
            elif attr == 'Footwork':
                if ( (player.footwork < 20 and rand <= staffMember.probability) or 
                     (player.footwork < 40 and rand <= staffMember.probability-1) or 
                     (player.footwork < 60 and rand <= staffMember.probability-2) or
                     (player.footwork < 80 and rand <= staffMember.probability-3) or 
                     (player.footwork < 99 and rand <= staffMember.probability-4) ):
                    player.footwork += attrInc
                            
            elif attr == 'Attacking':
                if ( (player.attacking < 20 and rand <= staffMember.probability) or 
                     (player.attacking < 40 and rand <= staffMember.probability-1) or 
                     (player.attacking < 60 and rand <= staffMember.probability-2) or
                     (player.attacking < 80 and rand <= staffMember.probability-3) or 
                     (player.attacking < 99 and rand <= staffMember.probability-4) ):
                    player.attacking += attrInc    
                        
            elif attr == 'Defending':
                if ( (player.defending < 20 and rand <= staffMember.probability) or 
                     (player.defending < 40 and rand <= staffMember.probability-1) or 
                     (player.defending < 60 and rand <= staffMember.probability-2) or
                     (player.defending < 80 and rand <= staffMember.probability-3) or 
                     (player.defending < 99 and rand <= staffMember.probability-4) ):
                    player.defending += attrInc            
                
            elif attr == 'Strength':
                if ( (player.strength < 20 and rand <= staffMember.probability) or 
                     (player.strength < 40 and rand <= staffMember.probability-1) or 
                     (player.strength < 60 and rand <= staffMember.probability-2) or
                     (player.strength < 80 and rand <= staffMember.probability-3) or 
                     (player.strength < 99 and rand <= staffMember.probability-4) ):
                    player.strength += attrInc    
                        
            elif attr == 'Stamina':
                if ( (player.stamina < 20 and rand <= staffMember.probability) or 
                     (player.stamina < 40 and rand <= staffMember.probability-1) or 
                     (player.stamina < 60 and rand <= staffMember.probability-2) or
                     (player.stamina < 80 and rand <= staffMember.probability-3) or 
                     (player.stamina < 99 and rand <= staffMember.probability-4) ):
                    player.stamina += attrInc    
                        
            elif attr == 'Goalkeeping':
                if ( (player.goalkeeping < 20 and rand <= staffMember.probability) or 
                     (player.goalkeeping < 40 and rand <= staffMember.probability-1) or 
                     (player.goalkeeping < 60 and rand <= staffMember.probability-2) or
                     (player.goalkeeping < 80 and rand <= staffMember.probability-3) or 
                     (player.goalkeeping < 99 and rand <= staffMember.probability-4) ):
                    player.goalkeeping += attrInc            