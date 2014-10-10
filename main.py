import cgi
import datetime
import jinja2
import os
import urllib
import webapp2
import logging

from GenerateNewTeam import GenerateNewTeam
from GenerateNewPlayer import GenerateNewPlayer
from GenerateNewStaff import GenerateNewStaff
from GenerateNewTrainingType import GenerateNewTrainingType
from TrainingSession import TrainingSession

from google.appengine.ext import db
from google.appengine.api import users
from MatchSettings import getAllPastMatchesForUser, getAllUpcomingMatchesForUser,\
    hasPendingChallenges, GenerateNewMatch

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

""" HELPER FUNCTIONS"""
# Obtain the user's ID, or redirect them to the login page
def getUserId(page, redirectPage=None):
    if redirectPage is None:
        redirectPage = page.request.uri
    
    # Get username
    user = users.get_current_user()
    if user is None:
        page.redirect(users.create_login_url(redirectPage))
        return None
    else:
        return user.nickname()

def checkUserHasTeam(userId):
    if userId is None:
        return False
    
    query = db.GqlQuery("SELECT * FROM Team WHERE userId = '" + userId + "'")
    
    # If the query returns at least one result, then a team exists
    if query.count(limit=1) > 0:
        return True
    return False

""" END HELPER FUNCTIONS """

# CreateTeam handler.
# Loads CreateTeam.htm.
class CreateTeamForm(webapp2.RequestHandler):
    def get(self):
        
        # Check user is logged in and get userId
        userId = getUserId(self)
        if userId is None:
            return
        
        # If user already has a team, redirect to team page
        if checkUserHasTeam(userId) is True:
            self.redirect("./")
            return
        
        self.display()
        
    def display(self):
        template_values = {}
        template = jinja_environment.get_template('templates/CreateTeam.htm')        
        self.response.out.write(template.render(template_values))

# GenerateTeam handler.
# Creates a new team and inserts team into database
class GenerateTeam(webapp2.RequestHandler):
    def post(self):
        
        # Check user is logged in and get userId
        userId = getUserId(self, "./CreateTeam")
        if userId is None:
            return
        
        # If user already has a team, redirect to team page
        if checkUserHasTeam(userId) is True:
            self.redirect("./")
            return
        
        # Create team and store into database
        teamName = cgi.escape(self.request.get('teamName'))
        stadiumName = cgi.escape(self.request.get('stadiumName'))
        budget = 5000
        
        teamFactory = GenerateNewTeam()
        team = teamFactory.generate(teamName, stadiumName, budget, userId)
        teamFactory.storeToDatabase(team)
        
        # Create players and store into database
        firstName = 'Bob'
        lastName = 'Evans'
        totalPoints = 100
        maxPointsPerAbility = 25
        totalPlayers = 16
        
        for i in range(1, totalPlayers+1):
            playerNumber = i
            playerFactory = GenerateNewPlayer()
            player = playerFactory.generate(firstName, lastName, playerNumber, userId, totalPoints, 
                                            maxPointsPerAbility)
            playerFactory.storeToDatabase(player)
            
        # Create staff and store into database
        # Might not be the most elegant but allows for easy change
        staffFactory = GenerateNewStaff()
        
        level = 1
        upgradeCosts = [5000, 10000, 20000, 40000]
        probability = 5
        
        role = 'Attacking coach'
        firstAttr = 'Attacking'
        secondAttr = 'Footwork'
        costs = list(upgradeCosts)
        
        staff = staffFactory.generate(userId, role, firstAttr, secondAttr, level, costs, probability)
        staffFactory.storeToDatabase(staff)
        
        role = 'Teamwork coach'
        firstAttr = 'Passing'
        secondAttr = 'Crossing'
        costs = list(upgradeCosts)
        
        staff = staffFactory.generate(userId, role, firstAttr, secondAttr, level, costs, probability)
        staffFactory.storeToDatabase(staff)

        role = 'Defense coach'
        firstAttr = 'Defending'
        secondAttr = None
        costs = list(upgradeCosts)
                
        staff = staffFactory.generate(userId, role, firstAttr, secondAttr, level, costs, probability)
        staffFactory.storeToDatabase(staff)

        role = 'Fitness coach'
        firstAttr = 'Stamina'
        secondAttr = 'Strength'
        costs = list(upgradeCosts)
        
        staff = staffFactory.generate(userId, role, firstAttr, secondAttr, level, costs, probability)
        staffFactory.storeToDatabase(staff)
        
        role = 'Goalkeeping coach'
        firstAttr = 'Goalkeeping'
        secondAttr = None
        costs = list(upgradeCosts)
        
        staff = staffFactory.generate(userId, role, firstAttr, secondAttr, level, costs, probability)
        staffFactory.storeToDatabase(staff)
        
        # Create training types and store into database
        # Might not be the most elegant but allows for easy change
        
        trainingTypeFactory = GenerateNewTrainingType()
        
        status = 'Not in session'
        
        type = 'Dribbling'
        primaryAttr = 'Footwork'
        secondaryAttr = 'Attacking'
        tertiaryAttr = None
        
        trainingType = trainingTypeFactory.generate(userId, status, type, primaryAttr, secondaryAttr, tertiaryAttr)
        trainingTypeFactory.storeToDatabase(trainingType)
        
        type = 'Striking'
        primaryAttr = 'Attacking'
        secondaryAttr = 'Passing'
        tertiaryAttr = 'Crossing'
        
        trainingType = trainingTypeFactory.generate(userId, status, type, primaryAttr, secondaryAttr, tertiaryAttr)
        trainingTypeFactory.storeToDatabase(trainingType)
        
        type = 'Teamwork'
        primaryAttr = 'Passing'
        secondaryAttr = 'Crossing'
        tertiaryAttr = None
        
        trainingType = trainingTypeFactory.generate(userId, status, type, primaryAttr, secondaryAttr, tertiaryAttr)
        trainingTypeFactory.storeToDatabase(trainingType)
        
        type = 'Set-pieces'
        primaryAttr = 'Attacking'
        secondaryAttr = 'Defending'
        tertiaryAttr = 'Crossing'
        
        trainingType = trainingTypeFactory.generate(userId, status, type, primaryAttr, secondaryAttr, tertiaryAttr)
        trainingTypeFactory.storeToDatabase(trainingType)
        
        type = 'Marking/Tackling'
        primaryAttr = 'Defending'
        secondaryAttr = 'Stamina'
        tertiaryAttr = None
        
        trainingType = trainingTypeFactory.generate(userId, status, type, primaryAttr, secondaryAttr, tertiaryAttr)
        trainingTypeFactory.storeToDatabase(trainingType)
                        
        type = 'Strength'
        primaryAttr = 'Strength'
        secondaryAttr = None
        tertiaryAttr = None
        
        trainingType = trainingTypeFactory.generate(userId, status, type, primaryAttr, secondaryAttr, tertiaryAttr)
        trainingTypeFactory.storeToDatabase(trainingType)
        
        type = 'Cardio'
        primaryAttr = 'Stamina'
        secondaryAttr = None
        tertiaryAttr = None
        
        trainingType = trainingTypeFactory.generate(userId, status, type, primaryAttr, secondaryAttr, tertiaryAttr)
        trainingTypeFactory.storeToDatabase(trainingType)
        
        type = 'Goalkeeping'
        primaryAttr = 'Goalkeeping'
        secondaryAttr = None
        tertiaryAttr = None
        
        trainingType = trainingTypeFactory.generate(userId, status, type, primaryAttr, secondaryAttr, tertiaryAttr)
        trainingTypeFactory.storeToDatabase(trainingType)
        
        self.redirect("./")

# TeamProfile handler.
# Linked from CreateTeam.htm.
# Loads TeamProfile.htm.
class TeamProfile(webapp2.RequestHandler):
    def get(self):
        
        # Check user is logged in and get userId
        userId = getUserId(self)
        if userId is None:
            return
        
        # User does not have a team, redirect to page for team creation
        if checkUserHasTeam(userId) is False:
            self.redirect("./CreateTeam")
            return
        
        # Check to see if there is a training session in progress
        # If there is, then check to see if the current time has reached the end time of that session
        # If yes, then reset the corresponding training type in the database
        # Display the team profile page

        # Query all the players under userId
        players = db.GqlQuery("SELECT * FROM Player WHERE teamUserId = '" + userId + "'")
        
        # Query the training types that are in progress
        # Note that there can only be a max of 1 match in the query
        trainingTypes = db.GqlQuery("SELECT * FROM TrainingType WHERE teamUserId = '" + userId + 
                                    "' AND status = 'In session'")
        
        # trainingInProgress is true when there is a match in the query
        trainingInProgress = trainingTypes.count(limit=1) > 0
        
        # Check if the current time has passed the end time of the training session
        # If yes, then train the players, reset the trainingType and updates the database
        currentTime = datetime.datetime.now()
        for trainingType in trainingTypes:
            if currentTime >= trainingType.endTime:
                trainingSession = TrainingSession()
                for player in players:
                    trainingSession.trainPlayer(userId, player, trainingType.primaryAttr, trainingType.secondaryAttr, trainingType.tertiaryAttr)
                    player.put()
                
                trainingType.status = 'Not in session'
                trainingType.startTime = None
                trainingType.endTime = None
                trainingInProgress = False
                trainingType.put()
                
        # Display the team profile page 
        team = db.GqlQuery("SELECT * FROM Team WHERE userId = '" + userId + "'").get()
        players = db.GqlQuery("SELECT * FROM Player WHERE teamUserId = '" + userId + "'")
        staff = db.GqlQuery("SELECT * FROM Staff WHERE teamUserId = '" + userId + "'")
        trainingTypes = db.GqlQuery("SELECT * FROM TrainingType WHERE teamUserId = '" + userId + "'")
        pastMatches = getAllPastMatchesForUser(userId)
        upcomingMatches = getAllUpcomingMatchesForUser(userId)
        pendingChallenges = hasPendingChallenges(userId)
        
        self.display(team, players, staff, trainingTypes, trainingInProgress, pastMatches, upcomingMatches, pendingChallenges)
          
    def display(self, team, players, staff, trainingTypes, trainingInProgress, pastMatches, upcomingMatches, pendingChallenges):
        template_values = {
            'myteam': team,
            'players': players,
            'staff': staff,
            'trainingTypes': trainingTypes,
            'trainingInProgress': trainingInProgress,
            'pastMatches': pastMatches,
            'upcomingMatches': upcomingMatches,
            'pendingChallenges': pendingChallenges
        }
        template = jinja_environment.get_template('templates/TeamProfile.htm')        
        self.response.out.write(template.render(template_values))

# Training handler.
# Linked from TeamProfile.htm.
# Trains the team depending on the training method picked.
class Training(webapp2.RequestHandler):
    def post(self):
        
        # Check user is logged in and get userId
        userId = getUserId(self)
        if userId is None:
            return
        
        # If user does not have a team, redirect to team page
        if checkUserHasTeam(userId) is False:
            self.redirect("./CreateTeam")
            return
        
        # Get the type from the form in TeamProfile.htm
        type = cgi.escape(self.request.get('trainingType'))
        
        # Query all players and the trainingType that matches type 
        players = db.GqlQuery("SELECT * FROM Player WHERE teamUserId = '" + userId + "'")
        trainingTypes = db.GqlQuery("SELECT * FROM TrainingType WHERE teamUserId = '" + userId + 
                                    "' AND type = '" + type + "'")
        
        # Changes the trainingType to in progress, updates the time, and stores it into the database
        for trainingType in trainingTypes:
            trainingType.status = "In session"
            trainingType.startTime = datetime.datetime.now()
            trainingType.endTime = trainingType.startTime + datetime.timedelta(seconds=5)
            trainingType.put()
            
        self.redirect("./")

# Upgrade handler.
class Upgrade(webapp2.RequestHandler):
    def post(self):
        
        # Check user is logged in and get userId
        userId = getUserId(self)
        if userId is None:
            return
        
        # If user does not have a team, redirect to team page
        if checkUserHasTeam(userId) is False:
            self.redirect("./CreateTeam")
            return
        
        role = cgi.escape(self.request.get('staffRole'))
        
        teams = db.GqlQuery("SELECT * FROM Team WHERE userId = '" + userId + "'")
        staff = db.GqlQuery("SELECT * FROM Staff WHERE teamUserId = '" + userId + "' AND role = '" + role + "'")
        
        for team in teams:
            for staffMember in staff:
                if staffMember.level <= len(staffMember.upgradeCosts) and team.budget >= staffMember.upgradeCosts[staffMember.level-1]:
                    team.budget = team.budget - staffMember.upgradeCosts[staffMember.level-1]
                    team.put()
                    
                    staffMember.level = staffMember.level + 1
                    staffMember.probability = staffMember.probability + 1
                    staffMember.put()
                    
        self.redirect("./")
        
# ChallengeFriend handler.
# Handles challenges to a friend
class ChallengeFriend(webapp2.RequestHandler):
    def post(self):
        
        # Check user is logged in and get userId
        userId = getUserId(self)
        if userId is None:
            return
        
        # If user does not have a team, redirect to team page
        if checkUserHasTeam(userId) is False:
            self.redirect("./CreateTeam")
            return
        
        friendId = cgi.escape(self.request.get('friendId'))
        
        # If the friend does not exist, then do nothing
        if checkUserHasTeam(friendId) is False:
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write('User ' + str(friendId) + ' does not have a team!')
            return
        
        # Create match generator
        matchFactory = GenerateNewMatch()
        
        # Create match
        match = matchFactory.generate(userId, friendId)
        if match is None:
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write('Unable to create match between you and ' + str(friendId))
            return
        
        
        # Store match into database
        matchFactory.storeToDatabase(match)
        
        self.redirect("./")

# Temporary handler for logging out
class Logout(webapp2.RequestHandler):
    def get(self):
        self.redirect(users.create_logout_url('./'))
        
# Passes the two handlers into a WSGIApplication call.
app = webapp2.WSGIApplication([('/', TeamProfile),
                               ('/CreateTeam', CreateTeamForm),
                               ('/GenerateNewTeam', GenerateTeam),
                               ('/Training', Training),
                               ('/Upgrade', Upgrade),
                               ('/ChallengeFriend', ChallengeFriend),
                               ('/Logout', Logout)],                              
                              debug=True)