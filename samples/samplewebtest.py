import webtest

class SimpleWebtest(webtest.Webtest):
    def testGood(self):
        assert(True)
    
    def testBad(self):
        assert(False)
        

