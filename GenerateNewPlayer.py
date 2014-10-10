import random

from Player import Player

from google.appengine.ext import db

""" Class that generates a new player and stores it in the database """
class GenerateNewPlayer:
    
    """ Generate a new player """
    def generate(self, firstName, lastName, playerNumber, teamUserId, totalPoints, maxPointsPerAbility):
        
        # Create new player and set the players name and team
        player = Player(firstName = firstName, lastName = lastName, teamUserId = teamUserId)

        # Sets the player's id
        player.playerNumber = playerNumber
        
        # Sets the player's team ID       
        player.teamUserId = teamUserId
        
        # Player starts with no experience
        player.experience = 0
        
        # Lower the total number of attribute points if there are more attribute points
        # than can be given.
        numberOfAbilities = 8
        if totalPoints > maxPointsPerAbility * numberOfAbilities:
            totalPoints = maxPointsPerAbility * numberOfAbilities
        
        # Initialize abilities
        player.passing = 0
        player.crossing = 0
        player.footwork = 0
        player.attacking = 0
        player.defending = 0
        player.strength = 0
        player.stamina = 0
        player.goalkeeping = 0
        
        # Assign points randomly until all points are assigned
        while totalPoints > 0:
            ability = random.randint(1, numberOfAbilities)
            
            if ability == 1 and player.passing < maxPointsPerAbility:
                player.passing += 1
            elif ability == 2 and player.crossing < maxPointsPerAbility:
                player.crossing += 1
            elif ability == 3 and player.footwork < maxPointsPerAbility:
                player.footwork += 1
            elif ability == 4 and player.attacking < maxPointsPerAbility:
                player.attacking += 1
            elif ability == 5 and player.defending < maxPointsPerAbility:
                player.defending += 1
            elif ability == 6 and player.strength < maxPointsPerAbility:
                player.strength += 1
            elif ability == 7 and player.stamina < maxPointsPerAbility:
                player.stamina += 1
            elif ability == 8 and player.goalkeeping < maxPointsPerAbility:
                player.goalkeeping += 1
            else:
                continue
            
            totalPoints -= 1
        
        return player
        
    """ Store a player to the database """
    def storeToDatabase(self, player):
        # Store player into database
        player.put()