from models import Human, Child

person = Human(
    name=input('Enter your name '),
    age=int(input('Enter your age ')),
    weight=float(input('Your weight? ')),
    is_drinking=bool(input('Do you drink alcohol? Enter "True" or "False" ')),
    is_smoking=bool(input('Do you drink tabacco? Enter "True" or "False" ')),
    is_ill=bool(input('Do you have any serious illness? Enter "True" or "False" ')),
    salary=int(input('Enter your salary '))
)

while True:
    print('Hello, what do you want to do?\nEnter a corresponding number:\n"1" to get your life expectancy, \n"2" to check how many years you should expect to live, \n"3" to discover of you are elegible for a Pfizer shot')
    choice=input(':')
    if choice == "1":
        print(person.life_expectancy())
    elif choice == "2":
        print(person.expected_years_left())
    elif choice == "3":
        print(person.pfizer_eligibility())