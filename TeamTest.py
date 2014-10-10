import unittest

from GenerateNewTeam import GenerateNewTeam

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.__teamFactory = GenerateNewTeam() 

    # Test that a Team object is correctly created
    def testCorrectCreation(self):
        team = self.__teamFactory.generate('Team', 'Stadium', 'username')
        
        self.assertEqual('Team', team.teamName, 'Team name is ' + team.teamName + ' instead of Team')
        self.assertEqual('Stadium', team.stadiumName, 'Stadium name is ' + team.stadiumName + ' instead of Stadium')
        self.assertEqual('username', team.userId, 'userId is ' + team.userId + ' instead of username')


if __name__ == "__main__":
    unittest.main()