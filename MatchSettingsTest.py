import unittest
import datetime

from MatchSettings import Match, PlayerLocation, mergeMatchLists

class MatchSettingsTest(unittest.TestCase):
    def setUp(self):
        pass

    # Test mergeMatchLists for one item each
    def testMergeMatchListsOneOne(self):
        homeGame = Match(homeTeam = 'me', awayTeam = 'not me', date = datetime.datetime(2011, 3, 1), matchPlayed = False)
        awayGame = Match(homeTeam = 'not me', awayTeam = 'me', date = datetime.datetime(2011, 1, 1), matchPlayed = False)
        
        games = mergeMatchLists([homeGame], [awayGame])
        
        self.assertEquals('not me', games[0].homeTeam, 'Expected not me, but was ' + games[0].homeTeam)
        self.assertEquals('me', games[0].awayTeam, 'Expected me, but was ' + games[0].awayTeam)
        self.assertEquals('me', games[1].homeTeam, 'Expected me, but was ' + games[1].homeTeam)
        self.assertEquals('not me', games[1].awayTeam, 'Expected not me, but was ' + games[1].awayTeam)
    
    # Test mergeMatchLists for one empty list
    def testOneEmptyList(self):
        homeGame = Match(homeTeam = 'me', awayTeam = 'not me', date = datetime.datetime(2011, 3, 1), matchPlayed = False)
        awayGame = Match(homeTeam = 'not me', awayTeam = 'me', date = datetime.datetime(2011, 1, 1), matchPlayed = False)
        
        games = mergeMatchLists([homeGame, awayGame], [])
        
        self.assertEquals('not me', games[0].homeTeam, 'Expected not me, but was ' + games[0].homeTeam)
        self.assertEquals('me', games[0].awayTeam, 'Expected me, but was ' + games[0].awayTeam)
        self.assertEquals('me', games[1].homeTeam, 'Expected me, but was ' + games[1].homeTeam)
        self.assertEquals('not me', games[1].awayTeam, 'Expected not me, but was ' + games[1].awayTeam)
    
    # Test mergeMatchLists for 3 items each
    def testMergeMatchListsThreeThree(self):
        homeGames = []
        homeGames.append(Match(homeTeam = 'three', awayTeam = 'three', date = datetime.datetime(2011, 1, 3), matchPlayed = False))
        homeGames.append(Match(homeTeam = 'two', awayTeam = 'two', date = datetime.datetime(2011, 1, 2), matchPlayed = False))
        homeGames.append(Match(homeTeam = 'five', awayTeam = 'five', date = datetime.datetime(2011, 1, 5), matchPlayed = False))
        
        awayGames = []
        awayGames.append(Match(homeTeam = 'four', awayTeam = 'four', date = datetime.datetime(2011, 1, 4), matchPlayed = False))
        awayGames.append(Match(homeTeam = 'six', awayTeam = 'six', date = datetime.datetime(2011, 1, 6), matchPlayed = False))
        awayGames.append(Match(homeTeam = 'one', awayTeam = 'one', date = datetime.datetime(2011, 1, 1), matchPlayed = False))
        
        games = mergeMatchLists(homeGames, awayGames)
        
        self.assertEquals('one', games[0].homeTeam, 'Expected one, but was ' + games[0].homeTeam)
        self.assertEquals('two', games[1].homeTeam, 'Expected two, but was ' + games[1].homeTeam)
        self.assertEquals('three', games[2].homeTeam, 'Expected three, but was ' + games[2].homeTeam)
        self.assertEquals('four', games[3].homeTeam, 'Expected four, but was ' + games[3].homeTeam)
        self.assertEquals('five', games[4].homeTeam, 'Expected five, but was ' + games[4].homeTeam)
        self.assertEquals('six', games[5].homeTeam, 'Expected six, but was ' + games[5].homeTeam)
        
        self.assertEquals(6, len(games), 'Expected length of 6, was ' + str(len(games)))
        
    def testOverTenMatches(self):
        homeGames = []
        homeGames.append(Match(homeTeam = 'three', awayTeam = 'three', date = datetime.datetime(2011, 1, 3), matchPlayed = False))
        homeGames.append(Match(homeTeam = 'two', awayTeam = 'two', date = datetime.datetime(2011, 1, 2), matchPlayed = False))
        homeGames.append(Match(homeTeam = 'five', awayTeam = 'five', date = datetime.datetime(2011, 1, 5), matchPlayed = False))
        
        awayGames = []
        awayGames.append(Match(homeTeam = 'four', awayTeam = 'four', date = datetime.datetime(2011, 1, 4), matchPlayed = False))
        awayGames.append(Match(homeTeam = 'six', awayTeam = 'six', date = datetime.datetime(2011, 1, 6), matchPlayed = False))
        awayGames.append(Match(homeTeam = 'one', awayTeam = 'one', date = datetime.datetime(2011, 1, 1), matchPlayed = False))
        awayGames.append(Match(homeTeam = 'seven', awayTeam = 'seven', date = datetime.datetime(2011, 1, 7), matchPlayed = False))
        awayGames.append(Match(homeTeam = 'eight', awayTeam = 'eight', date = datetime.datetime(2011, 1, 8), matchPlayed = False))
        awayGames.append(Match(homeTeam = 'nine', awayTeam = 'nine', date = datetime.datetime(2011, 1, 9), matchPlayed = False))
        awayGames.append(Match(homeTeam = 'ten', awayTeam = 'ten', date = datetime.datetime(2011, 1, 10), matchPlayed = False))
        awayGames.append(Match(homeTeam = 'eleven', awayTeam = 'eleven', date = datetime.datetime(2011, 1, 11), matchPlayed = False))
        
        games = mergeMatchLists(homeGames, awayGames)
        
        self.assertEquals(10, len(games), 'Expected length of 10, was ' + str(len(games)))
        
if __name__ == "__main__":
    unittest.main()