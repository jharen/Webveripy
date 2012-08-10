import webtest

class SimpleWebtest(webtest.Webtest):
    def testGood(self):
        car = self.request("http://google.com")
        assert(car.responseInfo.status == 200)
    
    def testBad(self):
        car = self.request("http://google.com")
        assert(car.responseInfo.status != 200)
        

