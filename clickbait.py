from random import randint, choice

object_pronouns = ['Her', 'Him', 'Them']
possessive_pronouns = ['Her', 'His', 'Their']
personal_pronouns = ['She', 'He', 'They']
states = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
nouns = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
'Plastic Straw','Serial Killer', 'Telephone Psychic']
places = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
'Workplace', 'Donut Shop', 'Apocalypse Bunker']
time = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

def main():
    print('Clickbait headline generator.')
    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Enter a number.')
        else:
            number_of_headlines = int(response)
            break
    for i in range(number_of_headlines):
        clickbait_type = randint(1,8)

        if clickbait_type == 1:
            headline = generate_are_millenials_killing_headline()
        elif clickbait_type == 2:
            headline = generate_what_do_you_know_headline()
        elif clickbait_type == 3:
            headline = generate_big_companies_hate_her_headline()
        elif clickbait_type == 4:
            headline = generate_dont_want_you_to_know_headline()
        elif clickbait_type == 5:
            headline = generate_you_wont_believe_headline()
        elif clickbait_type == 6:
            headline = generate_gift_idea_headline()
        elif clickbait_type == 7:
            headline = generate_reasons_why_headline()
        elif clickbait_type == 8:
            headline = generate_job_automated_headline()

        print(headline)
    print()

    website = choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                      'Facesbook', 'Tweedie', 'Pastagram'])
    when = choice(time).lower()
    print(f'Post these to our {website} {when} or you\'re fired!')

def generate_are_millenials_killing_headline():
    noun = choice(nouns)
    return f'Are millenials killing the {noun} industry?'

def generate_what_do_you_know_headline():
    noun = choice(nouns)
    plural_noun = choice(nouns) + 's'
    when = choice(time)
    return f'Without This {noun}, {plural_noun} Could Kill You {when}'

def generate_big_companies_hate_her_headline():
    pronoun = choice(object_pronouns)
    state = choice(states)
    noun_one = choice(nouns)
    noun_two = choice(nouns)
    return f'Big Companies Hate {pronoun}! See How This {state} {noun_one} Invented a Cheaper {noun_two}'

def generate_you_wont_believe_headline():
    state = choice(states)
    noun = choice(nouns)
    pronoun = choice(possessive_pronouns)
    place = choice(places)
    return f'You Won\'t Believe What This {state} {noun} Found in {pronoun} {place}'

def generate_dont_want_you_to_know_headline():
    plural_noun_one = choice(nouns) + 's'
    plural_noun_two = choice(nouns) + 's'
    return f'What {plural_noun_one} Don\'t Want You To Know About {plural_noun_two}'

def generate_gift_idea_headline():
    number = randint(7, 15)
    noun = choice(nouns)
    state = choice(states)
    return f'{number} Gift Ideas to Give Your {noun} From {state}'

def generate_reasons_why_headline():
    number_one = randint(3, 19)
    plural_noun = choice(nouns) + 's'
    number_two = randint(1, number_one)
    return f'{number_one} Reasons Why {plural_noun} Are More Interesting Than' \
           f' You Think (Number {number_two} Will Surprise You!)'

def generate_job_automated_headline():
    state = choice(states)
    noun = choice(nouns)
    i = randint(0, 2)
    pronoun_one = possessive_pronouns[i]
    pronoun_two = personal_pronouns[i]
    if pronoun_one == 'Their':
        return f'This {state} {noun} Didn\'t Think Robots Would Take ' \
               f'{pronoun_one} Job. {pronoun_two} Were Wrong.'
    else:
        return f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun_one} Job. {pronoun_two} Was Wrong.'

if __name__ == '__main__':
    main()
