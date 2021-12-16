
class superHero:

    """
    Any simple class should be defined here. You must code some business logic, which can be
    executed on its instance.
    """
    def __init__(self, name, power, secretName, city, location):
        self.name = name

        if power < 1024:
            print('Invalid amount of power, power has set to 1024')
            self.power = 1024
        else:
            self.power = power

        self.secretName = secretName
        self.city = city
        self.location = location

    def maxPower(self, newPower):
        if newPower < 1024:
            print('maxPower has to be >= 1024')
        else:
            self.power = newPower
    


    