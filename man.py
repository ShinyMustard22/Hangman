class Man:
    def __init__(self):
        self.stage = 1

    def addBodyPart(self):
        if self.stage == 1:
            # print head to console

        elif self.stage == 2:
            # print body to console

        elif self.stage == 3:
            # print left arm to console

        elif self.stage == 4:
            # print right arm to console

        elif self.stage == 5:
            # print left leg to console

        elif self.stage == 6:
            # print right leg to console

        self.stage += 1

    def isHanged(self):
        return self.stage == 7