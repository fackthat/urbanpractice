import unittest
import hw52
import hw53


suite = unittest.TestSuite()
suite.addTest((unittest.TestLoader().loadTestsFromTestCase(hw52.RunnerTest)))
suite.addTest((unittest.TestLoader().loadTestsFromTestCase(hw53.TournamentTest)))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)