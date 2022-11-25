from random import sample, randint, choice, shuffle
from time import time
from sys import exit

suspects = ['Duke Hautdog', 'Maximum Powers', 'Bill Monopolis',
            'Senator Schmear', 'Mrs. Feathertoss', 'Dr. Jean Splicer',
            'Raffles the Clown', 'Espressa Toffeepot', 'Cecil Edgar Vanderton']
items = ['flashlight', 'candlestick', 'rainbow flag', 'hamster wheel',
         'anime VHS tape', 'jar of pickles', 'one cowboy boot',
         'clean underpants', '5 dollar gift card']
places = ['zoo', 'old barn', 'duck pond', 'city hall', 'hipster cafe',
          'bowling alley', 'video game museum', 'university library', 'albino alligator pit']
time_to_solve = 300
place_first_letters = {}
longest_place_name_length = 0
for place in places:
    place_first_letters[place[0].upper()] = place
    if len(place) > longest_place_name_length:
        longest_place_name_length = len(place)

assert len(suspects) == 9
assert len(places) == 9
assert len(items) == 9
assert len(place_first_letters.keys()) == len(places)

known_suspects_and_items = []
visited_places = {}
current_location = 'taxi'
accused_suspects = []
liars = sample(suspects, randint(3, 4))
accusations_left = 3
culprit = choice(suspects)
shuffle(suspects)
shuffle(items)
shuffle(places)
clues = {}
for i, interviewee in enumerate(suspects):
    if interviewee in liars:
        continue
    clues[interviewee] = {}
    clues[interviewee]['liar'] = False
    for item in items:
        if randint(0, 1) == 0:
            clues[interviewee][item] = places[items.index(item)]
        else:
            clues[interviewee][item] = suspects[items.index(item)]
    for suspect in suspects:
        if randint(0, 1) == 0:
            clues[interviewee][suspect] = places[suspects.index(suspect)]
        else:
            clues[interviewee][suspect] = items[suspects.index(suspect)]
for i, interviewee in enumerate(suspects):
    if interviewee not in liars:
        continue
    clues[interviewee] = {}
    clues[interviewee]['liar'] = True
    for item in items:
        if randint(0, 1) == 0:
            while True:
                clues[interviewee][item] = choice(places)
                if clues[interviewee][item] != places[items.index(item)]:
                    break
        else:
            while True:
                clues[interviewee][item] = choice(suspects)
                if clues[interviewee][item] != suspects[items.index(item)]:
                    break
    for suspect in suspects:
        if randint(0, 1) == 0:
            while True:
                clues[interviewee][suspect] = choice(places)
                if clues[interviewee][suspect] != places[suspects.index(suspect)]:
                    break
        else:
            while True:
                clues[interviewee][suspect] = choice(items)
                if clues[interviewee][suspect] != items[suspects.index(suspect)]:
                    break
zophie_clues = {}
for interviewee in sample(suspects, randint(3, 4)):
    kind_of_clue = randint(1, 3)
    if kind_of_clue == 1:
        if interviewee not in liars:
            zophie_clues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                zophie_clues[interviewee] = choice(suspects)
                if zophie_clues[interviewee] != culprit and zophie_clues[interviewee] != interviewee:
                    break
    elif kind_of_clue == 2:
        if interviewee not in liars:
            zophie_clues[interviewee] = places[suspects.index(culprit)]
        elif interviewee in liars:
            while True:
                zophie_clues[interviewee] = choice(places)
                if zophie_clues[interviewee] != places[suspects.index(culprit)]:
                    break
    elif kind_of_clue == 3:
        if interviewee not in liars:
            zophie_clues[interviewee] = items[suspects.index(culprit)]
        elif interviewee in liars:
            while True:
                zophie_clues[interviewee] = choice(items)
                if zophie_clues[interviewee] != items[suspects.index(culprit)]:
                    break

print("""
J'ACCUSE! (a mystery game)
By Al Sweigart
Inspired by Homestar Runner's "Where's an Egg?" game
You are the world-famous detective Mathilde Camus.
ZOPHIE THE CAT has gone missing, and you must sift through the clues.
Suspects either always tell lies, or always tell the truth. Ask them
about other people, places, and items to see if the details they give are
truthful and consistent with your observations. Then you will know if
their clue about ZOPHIE THE CAT is true or not. Will you find ZOPHIE THE
CAT in time and accuse the guilty party?
""")
input('Press Enter to begin...')
start_time = time()
end_time = start_time + time_to_solve
while True:
    if time() > end_time:
        print('You have run out of time!')
        exit()
    elif accusations_left == 0:
        print('You have accused too many innocent people!')
        culprit_index = suspects.index(culprit)
        print(f'It was {culprit} at the {places[culprit_index]} with the {items[culprit_index]} who catnapped her!')
        print('Better luck next time, detective.')
        exit()
    print()
    minutes_left = int(end_time - time()) // 60
    seconds_left = int(end_time - time()) % 60
    print(f'Time left: {minutes_left} min, {seconds_left} sec')
    if current_location == 'taxi':
        print('You are in your taxi. Where do you want to go?')
        for place in sorted(places):
            place_info = ''
            if place in visited_places:
                place_info = visited_places[place]
            name_label = '(' + place[0].upper() + ')' + place[1:]
            spacing = ' ' * (longest_place_name_length - len(place))
            print(f'{name_label} {spacing}{place_info}')
        print('(Q)uit game')
        while True:
            response = input('> ').upper()
            if response == 'Q':
                print('Thanks for playing!')
                exit()
            if response in place_first_letters.keys():
                break
        current_location = place_first_letters[response]
        continue
    print(f'You are at the {current_location}.')
    current_location_index = places.index(current_location)
    the_person_here = suspects[current_location_index]
    the_item_here = items[current_location_index]
    print(f'{the_person_here} with the {the_item_here} is here.')
    if the_person_here not in known_suspects_and_items:
        known_suspects_and_items.append(the_person_here)
    if items[current_location_index] not in known_suspects_and_items:
        known_suspects_and_items.append(items[current_location_index])
    if current_location not in visited_places.keys():
        visited_places[current_location] = f'({the_person_here.lower()}, {the_item_here})'
    if the_person_here in accused_suspects:
        print('They are offended that you accused them,')
        print('And will not help with your investigation.')
        print('You go back to your taxi.\n')
        input('Press Enter to continue...')
        current_location = 'taxi'
        continue
    print(f'\n(J) "J\'accuse!" ({accusations_left} accusations left)')
    print('(Z) Ask if they know where Zophie the Cat is.')
    print('(T) Go back to your taxi.')
    for i, suspect_or_item in enumerate(known_suspects_and_items):
        print(f'({i + 1}) Ask about {suspect_or_item}')
    while True:
        response = input('> ').upper()
        if response in 'JZT' or (response.isdecimal() and 0 < int(response)
                                 <= len(known_suspects_and_items)):
            break
    if response == 'J':
        accusations_left -= 1
        if the_person_here == culprit:
            print("You've cracked the case, Detective!")
            print(f'It was {culprit} who had catnapped Zophie the Cat.')
            mins_taken = int(time() - start_time) // 60
            secs_taken = int(time() - start_time) % 60
            print(f'Good job! You solved it in {mins_taken} min, {secs_taken} sec.')
            exit()
        else:
            accused_suspects.append(the_person_here)
    elif response == 'Z':
        if the_person_here not in zophie_clues:
            print('"I don\'t know anything about Zophie the Cat."')
        elif the_person_here in zophie_clues:
            print(f'They give you thus clue: "{zophie_clues[the_person_here]}"')
            if zophie_clues[the_person_here] not in known_suspects_and_items and \
                    zophie_clues[the_person_here] not in places:
                known_suspects_and_items.append(zophie_clues[the_person_here])
    elif response == 'T':
        current_location = 'taxi'
        continue
    elif response == '':
        continue
    else:
        thing_being_asked_about = known_suspects_and_items[int(response) - 1]
        if thing_being_asked_about in (the_person_here, the_item_here):
            print('They give you this clue: "No comment."')
        else:
            print(f'They give you this clue: "{clues[the_person_here][thing_being_asked_about]}"')
            if clues[the_person_here][thing_being_asked_about] not in known_suspects_and_items \
                    and clues[the_person_here][thing_being_asked_about]\
                    not in places:
                known_suspects_and_items.append(clues[the_person_here][thing_being_asked_about])
    input('Press Enter to continue...')
