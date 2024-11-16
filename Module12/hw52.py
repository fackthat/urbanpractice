from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('TestRunner')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, 'Distance after 10 walks should be 50')

    def test_run(self):
        runner = Runner('TestRunner')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, 'Distance after 10 walks should be 100')

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
