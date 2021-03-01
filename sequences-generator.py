from random import randrange

person_list = ['John', 'Michael', 'Mary', 'Jennifer', 'Linda', 'Elizabeth', 'William',
               'David', 'Susan', 'Jessica', 'Richard', 'Thomas', 'Sarah', 'Anthony', 'Lisa',
               'Sean', 'Jason', 'Samantha', 'Hannah', 'James', 'William', 'Tiffany', 'David',
               'Nancy', 'Sarah', 'Mark', 'Steven', 'Emily', 'Andrew', 'Ashley', 'Betty', 'Kimberly', 'Leslie']

location_list = ['market', 'movies', 'park', 'restaurant', 'house', 'bedroom', 'restroom', 'amusement park',
                 'bakery', 'coffee shop', 'bookstore', 'clothing store', 'dance studio', 'art studio',
                 'art show', 'orchestra room', 'physics classroom', 'gas station', 'basketball court',
                 'swimming pool', 'beach', 'soccer field', 'construction site', 'football field', 'museum']

predicate_list = ['stretching at a yoga studio', 'buying cookies at a bakery', 'getting a coffee at the cafe',
                  'buying lunch at the deli', 'playing tennis court', 'buying a phone at the Apple Store',
                  'taking photos near the Eifel Tower', 'working out at the gym',
                  'taking photos near the Leaning Tower of Pisa', 'walking towards the Statue of Liberty',
                  'driving to the water park', 'walking in the garden', 'sitting on a rooftop',
                  'attending class at the school', 'reading at the library', 'working at the office',
                  'waiting at the airport', 'waiting at the train station',
                  'buying clothes at the mall', 'fixing their computer at the electronic store',
                  'buying a bike at the bike shop']
num_questions = 0

def rand_options(input_list):
    a = input_list[randrange(len(input_list))]
    b = input_list[randrange(len(input_list))]
    c = input_list[randrange(len(input_list))]
    return a, b, c


def find_times():
    time_1 = str(randrange(5, 9)) + "am"
    time_2 = str(randrange(10, 12))

    if time_2 == "12":
        time_2 = "12pm"
    else:
        time_2 = time_2 + "am"
    time_3 = str(randrange(1, 4)) + "pm"
    time_4 = str(randrange(5, 8)) + "pm"
    time_5 = str(randrange(9, 11)) + "pm"
    return time_1, time_2, time_3, time_4, time_5


for num in range(200):
    # target is in range of time_1 and time_2
    for i in range(1):
        target_loc = location_list[randrange(len(location_list))]

        loc_1, loc_2, loc_3 = rand_options(location_list)
        predicate_1, predicate_2, predicate_3 = rand_options(predicate_list)
        person_1, person_2, person_3 = rand_options(person_list)

        time_1, time_2, time_3, time_4, time_5 = find_times()

        # print scenarios
        print("{\"input\":  \"query: When did", person_1, "go to the", target_loc + "?", "knowledge:",
              person_1, "wakes up at", time_1 + ".", person_1, "stayed at the", loc_1, "from", time_4, "to",
              time_5 + ".",
              person_2, "saw", person_1, predicate_1, "from", time_2, "to", time_3 + ".",
              person_3, "saw", person_1, predicate_2, "from", time_3, "to", time_4 + ".",
              "The", target_loc, "was closed after", time_5 + ".\" , ")
        print("\"target\": \"", time_1, "-", time_2 + "\" }, ")
        num_questions += 1

    # target is in range of time_2 and time_3
    for i in range(1):
        target_loc = location_list[randrange(len(location_list))]

        loc_1, loc_2, loc_3 = rand_options(location_list)
        predicate_1, predicate_2, predicate_3 = rand_options(predicate_list)
        person_1, person_2, person_3 = rand_options(person_list)

        time_1, time_2, time_3, time_4, time_5 = find_times()

        # print scenarios
        print("{\"input\":  \"query: When did", person_1, "go to the", target_loc + "?", "knowledge:",
              person_1, "wakes up at", time_1 + ".", person_1, "stayed at the", loc_1, "from", time_4, "to",
              time_5 + ".",
              person_2, "saw", person_1, predicate_1, "from", time_1, "to", time_2 + ".",
              person_3, "saw", person_1, predicate_2, "from", time_3, "to", time_4 + ".",
              "The", target_loc, "was closed after", time_5 + ".\" , ")
        print("\"target\": \"", time_2, "-", time_3 + "\" }, ")
        num_questions += 1

        # target is in range of time_3 and time_4
    for i in range(1):
        target_loc = location_list[randrange(len(location_list))]

        loc_1, loc_2, loc_3 = rand_options(location_list)
        predicate_1, predicate_2, predicate_3 = rand_options(predicate_list)
        person_1, person_2, person_3 = rand_options(person_list)

        time_1, time_2, time_3, time_4, time_5 = find_times()

        # print scenarios
        print("{\"input\":  \"query: When did", person_1, "go to the", target_loc + "?", "knowledge:",
              person_1, "wakes up at", time_1 + ".", person_1, "stayed at the", loc_1, "from", time_4, "to",
              time_5 + ".",
              person_2, "saw", person_1, predicate_1, "from", time_2, "to", time_3 + ".",
              person_3, "saw", person_1, predicate_2, "from", time_1, "to", time_2 + ".",
              "The", target_loc, "was closed after", time_5 + ".\" , ")
        print("\"target\": \"", time_3, "-", time_4 + "\" }, ")
        num_questions += 1

    # target is in range of time_4 and time_5
    for i in range(1):
        target_loc = location_list[randrange(len(location_list))]

        loc_1, loc_2, loc_3 = rand_options(location_list)
        predicate_1, predicate_2, predicate_3 = rand_options(predicate_list)
        person_1, person_2, person_3 = rand_options(person_list)

        time_1, time_2, time_3, time_4, time_5 = find_times()

        # print scenarios
        print("{\"input\":  \"query: When did", person_1, "go to the", target_loc + "?", "knowledge:",
              person_1, "wakes up at", time_1 + ".", person_1, "stayed at the", loc_1, "from", time_3, "to",
              time_4 + ".",
              person_2, "saw", person_1, predicate_1, "from", time_2, "to", time_3 + ".",
              person_3, "saw", person_1, predicate_2, "from", time_1, "to", time_2 + ".",
              "The", target_loc, "was closed after", time_5 + ".\" , ")
        print("\"target\": \"", time_4, "-", time_5 + "\" }, ")
        num_questions += 1

print("Number of questions:", num_questions)
