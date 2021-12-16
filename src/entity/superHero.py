
class superHero:

    def __init__(self, name, power, secretName, city, location, maxPower1):
        self.name = name
        self.power = power
        self.secretName = secretName
        self.city = city
        self.location = location
        self.maxPower1 = maxPower1


    def maxPower(self,x):
        return self.power+x



s1 = superHero('Robin', 1024, 'Dick Grayson', 'Gotham', 'BatCave', 8000)
s2 = superHero('Robin II', 2500, 'Jason Todd', 'Gotham', 'BatCave', 8000)
s3 = superHero('Robin III', 2500, 'Tim Drake', 'Gotham', 'BatCave', 8000)
s4 = superHero('Robin IV', 2500, 'Stephanie Brown', 'Gotham', 'BatCave', 8000)
s5 = superHero('Robin V', 2500, 'Damian Wayne', 'Gotham', 'BatCave', 8000)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)


