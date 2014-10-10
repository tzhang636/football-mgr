from Staff import Staff
from google.appengine.ext import db

class GenerateNewStaff:
    
    def generate(self, teamUserId, role, firstAttribute, secondAttribute, level, upgradeCosts, probability):
        
        staff = Staff()
        staff.teamUserId = teamUserId
        staff.role = role
        staff.firstAttr = firstAttribute
        staff.secondAttr = secondAttribute
        staff.level = level
        staff.upgradeCosts = upgradeCosts
        staff.probability = probability
        return staff
        
    def storeToDatabase(self, staff):
        staff.put()