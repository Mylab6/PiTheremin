class BasicControllableItem:
    def __init__(self, screenInstance, buttonInstance, rotaryReadInstance, tfInstance):
        self.screen = screenInstance
        self.button = buttonInstance
        self.rotaryReadInstance = rotaryReadInstance
        self.tfReader = tfInstance

        # self.rotaryReadInstance.runDial()
