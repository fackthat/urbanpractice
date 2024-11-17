import logging
from runner import Runner
import unittest

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8'
)

def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @staticmethod
    def log_exception(exc, message):
        logging.warning(f'{message}: {exc}')

    def test_walk(self):
        try:
            runner = Runner('TestRunner', speed=-5)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as exc:
            self.log_exception(exc, 'Неверная скорость для Runner')

    def test_run(self):
        try:
            runner = Runner(12345, speed=5)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as exc:
            self.log_exception(exc, 'Неверный тип данных для объекта Runner')

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