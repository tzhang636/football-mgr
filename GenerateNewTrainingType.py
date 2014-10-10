import random
import datetime
from TrainingType import TrainingType
from google.appengine.ext import db

class GenerateNewTrainingType:
    
    def generate(self, teamUserId, status, type, primaryAttr, secondaryAttr, tertiaryAttr):
        
        trainingType = TrainingType()
        
        trainingType.teamUserId = teamUserId
        
        trainingType.status = status
        
        trainingType.startTime = None
        
        trainingType.endTime = None
        
        trainingType.type = type
        
        trainingType.primaryAttr = primaryAttr
        
        trainingType.secondaryAttr = secondaryAttr
        
        trainingType.tertiaryAttr = tertiaryAttr
    
        return trainingType
    
    def storeToDatabase(self, trainingType):
        
        trainingType.put()