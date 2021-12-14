import unittest
from entity.superHero import superHero

class TestSuperHero(unittest.TestCase):

    def setUp(self):
        self.s1 = superHero('Robin', 1024, 'Dick Grayson', 'Gotham', 'Batcave')

    def test_existClass(self):
        self.assertTrue(self.s1)

    def test_instanceOf(self):
        self.assertIsInstance(self.s1, superHero, 'Object is no instance of Superhero')

    def test_hasName(self):
        self.assertEqual(self.s1.name, 'Robin', 'Wrong superhero choosed.')

    def test_hasPower(self):
        self.assertGreaterEqual(self.s1.power, 1024)

    def test_secretName(self):
        self.assertEqual(self.s1.secretName, 'Dick Grayson', 'Wrong person.')

    def test_hasCity(self):
        self.assertEqual(self.s1.city, 'Gotham', 'Are you sure?.')

    def test_hasLocation(self):
        self.assertEqual(self.s1.location, 'Batcave', 'I not agree.')

    def test_maxPower(self):
        self.s1.maxPower(8000)
        self.assertGreaterEqual(self.s1.power, 1024)

    def test_instance(self):
        s2 = superHero('Robin II', 2500, 'Jason Todd', 'Gotham', 'BatCave')
        self.assertIsInstance(s2, superHero, 'Object is no instance of Superhero')
        self.assertNotEqual(id(self.s1), id(s2), 'Variables contain different superheroes')


if __name__ == '__main__':
   unittest.main()