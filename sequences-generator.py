from random import randrange

name_list = ['John', 'Michael', 'Mary', 'Jennifer', 'Linda', 'Elizabeth', 'William',
             'David', 'Susan', 'Jessica', 'Richard', 'Thomas', 'Sarah', 'Anthony', 'Lisa',
             'Sean', 'Jason', 'Samantha', 'Hannah', 'James', 'William', 'Tiffany', 'David',
             'Nancy', 'Sarah', 'Mark', 'Steven', 'Emily', 'Andrew', 'Ashley', 'Betty', 'Kimberly', 'Leslie']

location_list = ['market', 'movies', 'park', 'restaurant', 'house', 'bedroom', 'restroom', 'amusement park',
                 'bakery', 'coffee shop', 'bookstore', 'clothing store',
                 'dance studio', 'art studio', 'art show', 'orchestra room', 'physics classroom', 'gas station',
                 'car wash', 'convenience store',
                 'basketball court', 'swimming pool', 'beach', 'soccer field', 'construction site',
                 'football field', 'museum'
                 ]

predicate_list = ['stretching at a yoga studio', 'buying cookies at a bakery', 'getting a coffee at the cafe',
                  'buying lunch at the deli', 'playing tennis court',
                  'taking photos near the Eifel Tower', 'working out at the gym',
                  'taking photos near the Leaning Tower of Pisa', 'walking towards the Statue of Liberty',
                  'driving to the water park', 'walking in the garden', 'sitting on a rooftop',
                  'attending class at the school',
                  'reading at the library', 'buying a phone at the Apple Store',
                  'working at the office', 'waiting at the airport', 'waiting at the train station',
                  'buying clothes at the mall', 'fixing their computer at the electronic store',
                  'buying a bike at the bike shop']
count = 0
for num in range(30):

    # time_3 to time_4
    for i in range(2):
        target_loc = location_list[randrange(len(location_list))]
        loc_1 = location_list[randrange(len(location_list))]
        loc_2 = location_list[randrange(len(location_list))]
        loc_3 = location_list[randrange(len(location_list))]
        predicate_1 = predicate_list[randrange(len(predicate_list))]
        predicate_2 = predicate_list[randrange(len(predicate_list))]

        person_1 = name_list[randrange(len(name_list))]
        person_2 = name_list[randrange(len(name_list))]
        person_3 = name_list[randrange(len(name_list))]

        time_1 = str(randrange(5, 9)) + "am"
        time_2 = str(randrange(10, 12))
        if time_2 == "12":
            time_2 = "12 pm"
        else:
            time_2 = time_2 + "am"
        time_3 = str(randrange(1, 4)) + "pm"
        time_4 = str(randrange(5, 8)) + "pm"
        time_5 = str(randrange(9, 11)) + "pm"

        print("{\"input\":  \"query: When did", person_1, "go to the", target_loc + "?", "knowledge:",
              person_1, "wakes up at", time_1 + ".", person_1, "stayed at the", loc_1, "from", time_4, "to",
              time_5 + ".",
              person_2, "saw", person_1, predicate_1, "from", time_2, "to", time_3 + ".",
              person_3, "saw", person_1, predicate_2, "from", time_1, "to", time_2 + ".",
              "The", target_loc, "was closed after", time_5 + ".\" , ")
        print("\"target\": \"", time_3, "-", time_4 + "\" }, ")
        count += 2
    # time_4 to time_5
    for i in range(2):
        target_loc = location_list[randrange(len(location_list))]
        loc_1 = location_list[randrange(len(location_list))]
        loc_2 = location_list[randrange(len(location_list))]
        loc_3 = location_list[randrange(len(location_list))]

        predicate_1 = predicate_list[randrange(len(predicate_list))]
        predicate_2 = predicate_list[randrange(len(predicate_list))]

        person_1 = name_list[randrange(len(name_list))]
        person_2 = name_list[randrange(len(name_list))]
        person_3 = name_list[randrange(len(name_list))]

        time_1 = str(randrange(5, 9)) + "am"
        time_2 = str(randrange(10, 12))
        if time_2 == "12":
            time_2 = "12 pm"
        else:
            time_2 = time_2 + "am"
        time_3 = str(randrange(1, 4)) + "pm"
        time_4 = str(randrange(5, 8)) + "pm"
        time_5 = str(randrange(9, 11)) + "pm"

        print("{\"input\":  \"query: When did", person_1, "go to the", target_loc + "?", "knowledge:",
              person_1, "wakes up at", time_1 + ".", person_1, "stayed at the", loc_1, "from", time_3, "to",
              time_4 + ".",
              person_2, "saw", person_1, predicate_1, "from", time_2, "to", time_3 + ".",
              person_3, "saw", person_1, predicate_2, "from", time_1, "to", time_2 + ".",
              "The", target_loc, "was closed after", time_5 + ".\" , ")
        print("\"target\": \"", time_4, "-", time_5 + "\" }, ")
        count += 2

    # time_1 to time_2
    for i in range(2):
        target_loc = location_list[randrange(len(location_list))]
        loc_1 = location_list[randrange(len(location_list))]
        loc_2 = location_list[randrange(len(location_list))]
        loc_3 = location_list[randrange(len(location_list))]

        predicate_1 = predicate_list[randrange(len(predicate_list))]
        predicate_2 = predicate_list[randrange(len(predicate_list))]

        person_1 = name_list[randrange(len(name_list))]
        person_2 = name_list[randrange(len(name_list))]
        person_3 = name_list[randrange(len(name_list))]

        time_1 = str(randrange(5, 9)) + "am"
        time_2 = str(randrange(10, 12))
        if time_2 == "12":
            time_2 = "12 pm"
        else:
            time_2 = time_2 + "am"
        time_3 = str(randrange(1, 4)) + "pm"
        time_4 = str(randrange(5, 8)) + "pm"
        time_5 = str(randrange(9, 11)) + "pm"

        print("{\"input\":  \"query: When did", person_1, "go to the", target_loc + "?", "knowledge:",
              person_1, "wakes up at", time_1 + ".", person_1, "stayed at the", loc_1, "from", time_4, "to",
              time_5 + ".",
              person_2, "saw", person_1, predicate_1, "from", time_2, "to", time_3 + ".",
              person_3, "saw", person_1, predicate_2, "from", time_3, "to", time_4 + ".",
              "The", target_loc, "was closed after", time_5 + ".\" , ")
        print("\"target\": \"", time_1, "-", time_2 + "\" }, ")
        count += 2

    # time_2 to time_3
    for i in range(2):
        target_loc = location_list[randrange(len(location_list))]
        loc_1 = location_list[randrange(len(location_list))]
        loc_2 = location_list[randrange(len(location_list))]
        loc_3 = location_list[randrange(len(location_list))]

        predicate_1 = predicate_list[randrange(len(predicate_list))]
        predicate_2 = predicate_list[randrange(len(predicate_list))]

        person_1 = name_list[randrange(len(name_list))]
        person_2 = name_list[randrange(len(name_list))]
        person_3 = name_list[randrange(len(name_list))]

        time_1 = str(randrange(5, 9)) + "am"
        time_2 = str(randrange(10, 12))
        if time_2 == "12":
            time_2 = "12 pm"
        else:
            time_2 = time_2 + "am"
        time_3 = str(randrange(1, 4)) + "pm"
        time_4 = str(randrange(5, 8)) + "pm"
        time_5 = str(randrange(9, 11)) + "pm"

        print("{\"input\":  \"query: When did", person_1, "go to the", target_loc + "?", "knowledge:",
              person_1, "wakes up at", time_1 + ".", person_1, "stayed at the", loc_1, "from", time_4, "to",
              time_5 + ".",
              person_2, "saw", person_1, predicate_1, "from", time_1, "to", time_2 + ".",
              person_3, "saw", person_1, predicate_2, "from", time_3, "to", time_4 + ".",
              "The", target_loc, "was closed after", time_5 + ".\" , ")
        print("\"target\": \"", time_2, "-", time_3 + "\" }, ")
        count += 2

print("Number of questions:", count)
