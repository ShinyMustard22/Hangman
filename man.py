class Man:
    def __init__(self):
        self.__body = []

    def addBodyPart(self):
        if len(self.__body) == 0:
            self.__body.append("0")

        elif len(self.__body) == 1:
            self.__body.append("|")

        elif len(self.__body) == 2:
            self.__body.append("/")

        elif len(self.__body) == 3:
            self.__body.append("\\")

        elif len(self.__body) == 4:
            self.__body.append("/")

        elif len(self.__body) == 5:
            self.__body.append("\\")

    def isHanged(self):
        return len(self.__body) == 6

    def head(self):
        if len(self.__body) > 0:
            return self.__body[0]

        return " "

    def abdomen(self):
        if len(self.__body) > 1:
            return self.__body[1]

        return " "

    def leftArm(self):
        if len(self.__body) > 2:
            return self.__body[2]

        return " "

    def rightArm(self):
        if len(self.__body) > 3:
            return self.__body[3]

        return " "

    def leftLeg(self):
        if len(self.__body) > 4:
            return self.__body[4]

        return " "

    def rightLeg(self):
        if len(self.__body) > 5:
            return self.__body[5]

        return " "
