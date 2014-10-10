from google.appengine.ext import db

import datetime

"""
The DB model for a match
"""
class Match(db.Model):
    '''
    The team playing at home
    '''
    homeTeam = db.StringProperty(required=True)
    homeTeamName = db.StringProperty()
    
    '''
    The visiting team
    '''
    awayTeam = db.StringProperty(required=True)
    awayTeamName = db.StringProperty()
    
    '''
    The date and time the game started
    '''
    date = db.DateTimeProperty()
    
    '''
    Whether the match has been played or not
    '''
    matchPlayed = db.BooleanProperty()
    
    '''
    Scores
    '''
    homeScore = db.IntegerProperty()
    awayScore = db.IntegerProperty()

"""
The DB model for the location of each player on the field
"""
class PlayerLocation(db.Model):
    ''' The identifier of the match for this formation '''
    matchId = db.IntegerProperty(required=True)
    
    ''' The identifier of the team the player belongs to '''
    teamUserId = db.StringProperty(required=True)
    
    ''' The unique number of the player on the team '''
    playerNumber = db.IntegerProperty(required=True)
    
    ''' The initial position of the player across and along the field '''
    horizontalPosition = db.IntegerProperty()
    verticalPosition = db.IntegerProperty()
    
"""
Class that creates a new match
"""
class GenerateNewMatch:
    def generate(self, homeId, awayId):
        # Cannot challenge yourself
        if homeId == awayId:
            return None
        
        match = Match(homeTeam = homeId, awayTeam = awayId)
        
        homeTeamQuery = db.GqlQuery("SELECT * FROM Team WHERE userId = '" + homeId + "'")
        homeTeamResult = homeTeamQuery.get()
        
        awayTeamQuery = db.GqlQuery("SELECT * FROM Team WHERE userId = '" + awayId + "'")
        awayTeamResult = awayTeamQuery.get()
        
        if homeTeamResult is None or awayTeamResult is None:
            return None
        
        match.homeTeamName = homeTeamResult.teamName
        match.awayTeamName = awayTeamResult.teamName
        
        match.date = datetime.datetime.now()
        
        match.matchPlayed = False
        
        match.homeScore = 0
        match.awayScore = 0
        
        return match
    
    def storeToDatabase(self, match):
        # Store match into database
        match.put()

""" Library functions """

''' GQL doesn't support the OR operator?! '''

''' Merges two lists of games and sorts them in chronological order '''
def mergeMatchLists(homeGames, awayGames, ascending = True):
    # Merge two lists into one
    games = []
    for homeGame in homeGames:
        games.append(homeGame)
    for awayGame in awayGames:
        games.append(awayGame)
        
    # Sort games
    games = sorted(games, key=lambda game: game.date)
    
    # Reverse if want descending
    if ascending is False:
        games.reverse()
        
    # Return the first ten results
    games = games[0:10]
    return games

''' Retrieves a list of upcoming home matches for a user'''
def getAllUpcomingMatchesForUser(userId):
    homeGames = db.GqlQuery("SELECT * FROM Match WHERE homeTeam = '" + userId + "' AND matchPlayed = FALSE ORDER BY date ASC LIMIT 10")
    awayGames = db.GqlQuery("SELECT * FROM Match WHERE awayTeam = '" + userId + "' AND matchPlayed = FALSE ORDER BY date ASC LIMIT 10")
    
    return mergeMatchLists(homeGames, awayGames)
    
''' Retrieves a list of upcoming home matches for a user'''
def getAllPastMatchesForUser(userId):
    homeGames = db.GqlQuery("SELECT * FROM Match WHERE homeTeam = '" + userId + "' AND matchPlayed = TRUE ORDER BY date ASC LIMIT 10")
    awayGames = db.GqlQuery("SELECT * FROM Match WHERE awayTeam = '" + userId + "' AND matchPlayed = TRUE ORDER BY date ASC LIMIT 10")
    
    return mergeMatchLists(homeGames, awayGames, ascending = False)

''' Returns whether a friend has challenged you or not '''
def hasPendingChallenges(userId):
    if userId is None:
        return False
    
    query = db.GqlQuery("SELECT * FROM Match WHERE awayTeam = '" + userId + "' AND matchPlayed = FALSE")
    
    # If the query returns at least one result, then a pending challenge exists
    if query.count(limit=1) > 0:
        return True
    return False