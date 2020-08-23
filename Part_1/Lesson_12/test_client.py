from client_hw12 import json_convert
import unittest
import time
import json

class Test(unittest.TestCase):
    def test_json_convert(self):
        base = {'name' : 'Mike',
            'message' : 'Hi',
            'time' : '15:12'}
        answere = json.dumps(base)

        self.assertEqual(json_convert('Mike', 'Hi', '15:12'), answere)


if __name__ == "__main__":
    unittest.main()

