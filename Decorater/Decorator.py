class Computer:
    """ Abstract Class
    """
    def __init__(self) -> None:
        self.description = "Unknown Computer"
        if self.__class__ == Computer:
            raise NotImplementedError("Cannot make compooper")

    def getDescription(self):
        return self.description

    def cost(self):
        pass

class IntelComputer(Computer):
    """ Concrete Class """
    def __init__(self) -> None:
        Computer.__init__(self)
        self.description = "A base intel PC"
    
    def cost(self) -> None:
        return 2499

class AMDComputer(Computer):
    """ Concrete Class """
    def __init__(self) -> None:
        Computer.__init__(self)
        self.description = "A base AMD PC"
    
    def cost(self) -> None:
        return 2099

class partAdder(Computer):
    """ Abstract Decorator Class """
    
    def __init__(self) -> None:
        if self.__class__ == partAdder:
            raise NotImplementedError("Cannot make a part adder.")
        
    def getDescription(self):
        pass

class motherboard(partAdder):
    """ Concrete Class """

    def __init__(self, Computer) -> None:
        partAdder.__init__(self)
        self.__Computer = Computer # "__" means it's private, so this is private information for a class.

    def getDescription(self):
            return self.__Computer.getDescription() + ', Motherboard'

    def cost(self):
            return self.__Computer.cost() + 150


class CPU(partAdder):
    """ Concrete Class """

    def __init__(self, Computer) -> None:
        partAdder.__init__(self)
        self.__Computer = Computer # "__" means it's private, so this is private information for a class.

    def getDescription(self):
            return self.__Computer.getDescription() + ', CPU'

    def cost(self):
            return self.__Computer.cost() + 400

class RAM(partAdder):
    """ Concrete Class """

    def __init__(self, Computer) -> None:
        partAdder.__init__(self)
        self.__Computer = Computer # "__" means it's private, so this is private information for a class.

    def getDescription(self):
            return self.__Computer.getDescription() + ', RAM'

    def cost(self):
            return self.__Computer.cost() + 60
        
myComputer = IntelComputer()
myComputer = motherboard(myComputer)
myComputer = CPU(myComputer)
myComputer = RAM(myComputer)
myComputerAMD = AMDComputer()
print(myComputer.getDescription())
print(myComputer.cost())
print(myComputerAMD.getDescription())
print(myComputerAMD.cost())