import unittest
import samplewebtest

suite = unittest.makeSuite(samplewebtest.SimpleWebtest,'test')
runner = unittest.TextTestRunner()
runner.run(suite)
