import unittest
from my_driver import NewDriver



class Android(unittest.TestCase):
    reportDirectory = 'c:\\reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'testName'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['platformName'] = 'Android'
        self.dc['appPackage'] = "<APP_PACKAGE>"
        self.dc['appActivity'] = "<APP_ACTIVITY>"

        self.driver = NewDriver('http://localhost:4722/wd/hub', self.dc)

    def test_login(self):
            print("test")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

