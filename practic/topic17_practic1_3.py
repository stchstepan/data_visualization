import unittest
from python_repos_tests import Api

class APITestsCase(unittest.TestCase):
    def setUp(self):
        self.calling_api = Api()

    def test_check_api(self):
        self.assertEqual(self.calling_api.check_api(), 200)

    def test_len_repo_dicts(self):
        self.assertEqual(self.calling_api.len_repo_dicts(), 9128935)

if __name__ == '__main__':
    unittest.main()