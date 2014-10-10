from Team import Team
from google.appengine.ext import db

""" Class that generates a new Team and stores it into a database. """
class GenerateNewTeam:
    
    '''
    Generate a new team.
    '''
    def generate(self, teamName, stadiumName, budget, userId):
        # Creates a new team 
        team = Team(teamName = teamName, stadiumName = stadiumName, budget = budget, userId = userId)
        return team
    
    '''
    Stores the team into the database.
    '''
    def storeToDatabase(self, team):
        team.put()