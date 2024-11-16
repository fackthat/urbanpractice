from runner import Runner
import unittest

def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner('TestRunner')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, 'Distance after 10 walks should be 50')

    @skip_if_frozen
    def test_run(self):
        runner = Runner('TestRunner')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, 'Distance after 10 walks should be 100')

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner('TestRunner1')
        runner2 = Runner('TestRunner2')
        for i in range(10):
            runner1.walk()
        for i in range(10):
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance, 'Distance should not be equal')

if __name__ == "__main__":
    unittest.main()