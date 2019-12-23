import unittest

import hseling_api_wikingrams


class HSELing_API_WikingramsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hseling_api_wikingrams.app.test_client()

    def test_index(self):
        rv = self.app.get('/healthz')
        self.assertIn('Application WikiNGrams', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
