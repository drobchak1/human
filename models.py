class Human:
    def __init__(
        self,
        name,
        age,
        weight,
        is_drinking,
        is_smoking,
        salary,
        is_ill,
        *args,
        **kwargs,
    ):
        self.name = name
        self.age = age
        self.weight = weight
        self.is_drinking = is_drinking
        self.is_smoking = is_smoking
        self.is_ill = is_ill
        self._salary = salary

    def __str__(self):
        return f"I am human {self.name}, I am {self.age} years old"

    def __doc__():
        return "This class can represent any human"

    def __call__(self):
        return f"{self.name} is here, ready to help you"

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def additional_message(func):
        """This is optional to notify user that his request is received"""

        def wrap(self):
            func(self)
            print(f"But {self.name} can always divorce!")

        return wrap

    @additional_message
    def get_married(self):
        print(f"{self.name} formed a family with another human")

    def pfizer_eligibility(self):
        """Check`s if human old enough to receive Pfizer shot"""
        return (
            f"Can get Pfizer vaccine"
            if self.age >= 12
            else f"Can`t get Pfizer vaccine. Additional testing required from manufacturer"
        )

    def life_expectancy(self):
        """
        This function estimates human's life expectency based on provided health stats
        """
        base = 70
        for i in [self.is_drinking, self.is_smoking, self.is_ill]:
            if i:
                base -= 5
            else:
                base += 5
        return base

    def expected_years_left(self):
        """
        This function estimates how many more years this person will live, in theory
        """
        return self.life_expectancy() - self.age


class Child(Human):
    def __str__(self):
        return f"I am child {self.name}, I am {self.age} years old"

    def pfizer_eligibility(self):
        return f"Can`t get Pfizer vaccine yet. Testing on children are under way"

    def life_expectancy(self):
        """
        This function estimates human's life expectency based on provided health stats
        """
        print("Warning! For a child this estimates are not presize")
        return super().life_expectancy()

    def __doc__():
        return "This class should only represent humans, who are children"


# illia = Human("Illia", 26, 82, False, True, 0, False)
# stepan = Child("Stepan", 10, 35, False, False, 0, False)
# print(illia.life_expectancy())
# print(illia.expected_years_left())
# print(illia.pfizer_eligibility())
# print(Human.__doc__())
# print(illia())
# print(illia.get_married())
# print(stepan.life_expectancy())
# print(illia.get_salary())
# illia.set_salary(500)
# print(illia.get_salary())
