# 2021-12-workshop-python-reto-01

![image](https://user-images.githubusercontent.com/16636086/144272202-b607b039-55ab-433e-902f-29ce08469110.png)

## Superhero Assistant Challenge

Welcome to the ***challenge 1***, due to the increase in crime in our city the local superhero needs to reinforce his team with an assistant.

For this reason, an interview must be carried out with 5 possible candidates. The following properties will be valued for each of them:

- `name`
- `power`
- `secretName`
- `city`
- `location`

On the other hand, each applicant must have the ability to increase her power at certain times, if the situation requires it by calling the maxPower function.

For all this, it is requested to create a superhero object that meets the aforementioned requirements. Create as many instances as you need.

Remember that you can find clues to solve the challenge in the same repository.

## The requirement

Feel free to make any changes to the `superHero` class and add any necessary code, as long as everything follows the requirements outlined. However, *** don't alter the `main.py` class or its properties *** as this lets us know if the interviews are working properly.

## Final notes

To clarify: a candidate can never have a `power` lower than` 1024`. All attributes and methods created must be public.

## Help

- pip install -e .
- pip install pytest
- python3 -m pytest test/TestSuperHero.py
