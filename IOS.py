import unittest
from my_driver import NewDriver



class IOS(unittest.TestCase):
    reportDirectory = 'c:\\reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'testName'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['platformName'] = 'ios'
        self.dc['bundleId'] = "com.experitest.ExperiBank"
        self.driver = NewDriver('http://localhost:4722/wd/hub', self.dc)

    def test_login(self):
            print("test")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

