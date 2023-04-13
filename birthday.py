import datetime
import random

# Function to generate random birthdays
def getBirthdays(numberOfBirthdays):
    birthdays = []
    startOfYear = datetime.date(2001, 1, 1)
    for i in range(numberOfBirthdays):
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

# Function to check for matching birthdays
def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA

def main():
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    # Get user input for number of birthdays to generate
    while True:
        print("How many birthdays shall I generate? Max(100)")
        response = input('> ')
        if response.isdecimal() and (0 < int(response) <= 100):
            numBDays = int(response)
            break
    print()
    print('Here are', numBDays, 'birthdays:')

    # Generate and display random birthdays
    birthdays = getBirthdays(numBDays)

    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(',', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = f'{monthName} {birthday.day}'
        print(dateText, end='')
    print()
    print()

    # Check for matching birthdays
    match = getMatch(birthdays)
    print('In this simulation, ', end='')
    if match is not None:
        monthName = MONTHS[match.month - 1]
        dateText = f'{monthName} {match.day}'
        print('multiple people have a birthday on', dateText)
    else:
        print('there are no matching birthdays.')

    print()
    print('Generating', numBDays, 'random birthdays 100,000 times...')
    input('Press Enter to begin...')
    print('Let\'s run another 100,000 simulations.')

    simMatch = 0  # How many simulations had matching birthdays in them.
    for i in range(100_000):
        # Report on the progress every 10,000 simulations
        if i % 10_000 == 0:
            print(i, 'simulations run...')
        birthdays = getBirthdays(numBDays)
        if getMatch(birthdays) is not None:
            simMatch = simMatch + 1

    print('100,000 simulations run.')

    # Calculate and display probability of matching birthdays
    probability = round(simMatch / 100_000 * 100, 2)
    print('Out of 100,000 simulations of', numBDays, 'people, there was a')
    print('matching birthday in that group', simMatch, 'times. This means')
    print('that', numBDays, 'people have a', probability, '% chance of')
    print('having a matching birthday in their group.')
    print('That\'s probably more than you would think!')

if __name__ == '__main__':
    main()
