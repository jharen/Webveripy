import unittest
import httplib2

class Webtest(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName)
        self.history = []
        self.httpClient = httplib2.Http(".cache")


