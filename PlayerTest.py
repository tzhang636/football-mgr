import unittest

from GenerateNewPlayer import GenerateNewPlayer

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.__playerFactory = GenerateNewPlayer() 
    
    # Test that the generate() function terminates
    def testTermination(self):
        self.__playerFactory.generate('Player', 'Name', 1, 'id', 100, 25)
    
    # Test that all the points are assigned
    def testCorrectPointsAssigned(self):
        player = self.__playerFactory.generate('Player', 'Name', 1, 'id', 100, 25)
        
        pointsSum = 0;
        pointsSum += player.attacking
        pointsSum += player.crossing
        pointsSum += player.defending
        pointsSum += player.footwork
        pointsSum += player.passing
        pointsSum += player.stamina
        pointsSum += player.strength
        pointsSum += player.goalkeeping
        
        self.assertEqual(100, pointsSum, 'Incorrect distribution of points ('+str(pointsSum)+' instead of 100)')
        
    # Test that all the points assigned at maximum capacity
    def testMaxCapacity(self):
        player = self.__playerFactory.generate('Player', 'Name', 1, 'id', 16, 2)
        
        self.assertEqual(2, player.attacking, 'Attacking incorrectly assigned ('+str(player.attacking)+' instead of 2)')
        self.assertEqual(2, player.crossing, 'Crossing incorrectly assigned ('+str(player.crossing)+' instead of 2)')
        self.assertEqual(2, player.defending, 'Defending incorrectly assigned ('+str(player.defending)+' instead of 2)')
        self.assertEqual(2, player.footwork, 'Footwork incorrectly assigned ('+str(player.footwork)+' instead of 2)')
        self.assertEqual(2, player.passing, 'Passing incorrectly assigned ('+str(player.passing)+' instead of 2)')
        self.assertEqual(2, player.stamina, 'Stamina incorrectly assigned ('+str(player.stamina)+' instead of 2)')
        self.assertEqual(2, player.strength, 'Strength incorrectly assigned ('+str(player.strength)+' instead of 2)')
        self.assertEqual(2, player.goalkeeping, 'Goalkeeping incorrectly assigned ('+str(player.goalkeeping)+' instead of 2)')
    
    # Test that all the points are assigned correctly when over maximum capacity
    def testOverMaxCapacity(self):
        player = self.__playerFactory.generate('Player', 'Name', 1, 'id', 100, 2)
        
        self.assertEqual(2, player.attacking, 'Attacking incorrectly assigned ('+str(player.attacking)+' instead of 2)')
        self.assertEqual(2, player.crossing, 'Crossing incorrectly assigned ('+str(player.crossing)+' instead of 2)')
        self.assertEqual(2, player.defending, 'Defending incorrectly assigned ('+str(player.defending)+' instead of 2)')
        self.assertEqual(2, player.footwork, 'Footwork incorrectly assigned ('+str(player.footwork)+' instead of 2)')
        self.assertEqual(2, player.passing, 'Passing incorrectly assigned ('+str(player.passing)+' instead of 2)')
        self.assertEqual(2, player.stamina, 'Stamina incorrectly assigned ('+str(player.stamina)+' instead of 2)')
        self.assertEqual(2, player.strength, 'Strength incorrectly assigned ('+str(player.strength)+' instead of 2)')
        self.assertEqual(2, player.goalkeeping, 'Goalkeeping incorrectly assigned ('+str(player.goalkeeping)+' instead of 2)')


if __name__ == "__main__":
    unittest.main()