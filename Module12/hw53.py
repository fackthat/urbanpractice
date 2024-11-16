from runner_and_tournament import Runner, Tournament
import unittest

def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return method(self, *args, **kwargs)
    return wrapper

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Usain', speed=10)
        self.andrew = Runner('Andrew', speed=9)
        self.nick = Runner('Nick', speed=3)

    @classmethod
    def tearDownClass(cls):
        for test_id, result in sorted(cls.all_results.items()):
            print(f'{test_id}: {result}')

    @skip_if_frozen
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.__class__.all_results[1] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == 'Nick')

    @skip_if_frozen
    def test_race_andrew_nick(self):
        tournament = Tournament(90, self.andrew, self.nick)
        results = tournament.start()
        self.__class__.all_results[2] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == 'Nick')

    @skip_if_frozen
    def test_race_usain_andrew_nick(self):
        tournament = Tournament(90, self.usain, self.andrew, self.nick)
        results = tournament.start()
        self.__class__.all_results[3] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == 'Nick')

    @skip_if_frozen
    def test_correct_ordering(self):
        tournament = Tournament(100, self.nick, self.andrew, self.usain)
        results = tournament.start()
        self.assertEqual(results[1].name, "Usain")
        self.assertEqual(results[2].name, "Andrew")
        self.assertEqual(results[3].name, "Nick")

if __name__ == '__main__':
    unittest.main()
