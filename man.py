class Man:
    def __init__(self):
        self.stage = 1

    def addBodyPart(self):
        if self.stage == 1:
            return  # print head to console

        elif self.stage == 2:
            return  # print body to console

        elif self.stage == 3:
            return  # print left arm to console

        elif self.stage == 4:
            return  # print right arm to console

        elif self.stage == 5:
            return  # print left leg to console

        elif self.stage == 6:
            return  # print right leg to console

        self.stage += 1

    def isHanged(self):
        return self.stage == 7
