import random
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

for i in range(200):
    target_person = person_list[randrange(len(person_list))]
    target_loc = location_list[randrange(len(location_list))]

    location_choices = []
    predicate_choices = []
    person_choices = []


    def get_random_description(time, count):
        begin, end = time
        return person_choices[count] + " saw " + target_person + " " + predicate_choices[count] + " from " + str(begin) + " to " + str(end) + "."


    N = random.randint(2, 6) + 1
    times = random.sample(range(24), N)
    times.sort()


    answer_interval = random.randint(0, N-2)
    answer = ""
    times_to_descriptions = {}



    for i in range(N-1):
        location_choices.append(location_list[randrange(len(location_list))])
        predicate_choices.append(predicate_list[randrange(len(predicate_list))])
        person_choices.append(person_list[randrange(len(person_list))])


    count = 0
    print("{\"input\": \"query: When did", target_person, "go to the", target_loc + "?", "knowledge:")
    print(target_person + " wakes up at "+ str(times[0]) + ".")
    for i in range(N-1):
        begin, end = times[i], times[i+1]
        if i == answer_interval:
            answer = str(begin) + "-" + str(end)
        else:
            #times_to_descriptions[(begin, end)] = get_random_description((begin,end), count)
            print(get_random_description((begin, end), count))
        count+=1


    print("The", target_loc, "was closed after", str(times[N-1]) + ".\" , ")
    print("\"target\": \""+ str(answer) + "\" }, ")
