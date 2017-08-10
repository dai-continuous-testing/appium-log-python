from appium import webdriver


class NewDriver(webdriver.Remote):

    def __init__(self, a, b):
        print("Hello")
        super(NewDriver, self).__init__(a, b)

    def execute(self, driver_command, params=None):
        print("execute driver_command " + driver_command + " with params: ")

        if isinstance(params,dict):
            for k, v in params.items():
                print("     [", k, " : ", v, "]")
        return super().execute(driver_command, params)


    def execute_script(self, script, *args):
        print("execute_script driver_command " + script)
        return super().execute_script(script, *args)

