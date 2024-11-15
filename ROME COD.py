class Coder:
    def __init__(self, message):
        self.message = message
        self.__coding()

    def __coding(self):
        self.__list_mess = list(self.message)
        self.__result = " "
        for i in self.__list_mess:
            self.__result += chr(ord(i)+5)

    def print(self):
        print(self.__result)

Input = Coder(input())
Input.print()

class Decoding():
    def __init__(self, message):
        self.message = message
        self.result = " "
        self.mess = list(self.message)
        for i in self.mess:
            self.result += chr(ord(i) - 5)

        print(self.result)

InputD = Decoding(input())

