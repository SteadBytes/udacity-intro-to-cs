# Dictionaries of Dictionaries (of Dictionaries)

courses = {
    'feb2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Peter C.'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian',
                          'assistant': 'Andy'}},
    'apr2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Sarah'},
                'cs212': {'name': 'The Design of Computer Programs',
                          'teacher': 'Peter N.',
                          'assistant': 'Andy',
                          'prereq': 'cs101'},
                'cs253':
                {'name': 'Web Application Engineering - Building a Blog',
                 'teacher': 'Steve',
                 'prereq': 'cs101'},
                'cs262':
                {'name': 'Programming Languages - Building a Web Browser',
                 'teacher': 'Wes',
                 'assistant': 'Peter C.',
                 'prereq': 'cs101'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian'},
                'cs387': {'name': 'Applied Cryptography',
                          'teacher': 'Dave'}},
    'jan2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                          'teacher': 'Dorina'},
                'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                          'teacher': 'Jasper'},
                }
}


def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res


def is_offered(courses, course, hexamester):
    if hexamester in courses:
        if course in courses[hexamester]:
            return True
    return False


def when_offered(courses, course):
    result = []
    for hexamester in courses:
        if course in courses[hexamester]:
            result.append(hexamester)
    return result


def involved(courses, person):
    result = {}
    for hexamester in courses:
        for c in courses[hexamester]:
            if person in courses[hexamester][c].values():
                if not hexamester in result:
                    result[hexamester] = [c]
                else:
                    result[hexamester].append(c)
    return result


# Test Cases
##############
print(is_offered(courses, 'cs101', 'apr2012'))
#>>> True

print(is_offered(courses, 'cs003', 'apr2012'))
#>>> False

print(is_offered(courses, 'cs001', 'jan2044'))
#>>> True

print(is_offered(courses, 'cs253', 'feb2012'))
#>>> False
#############

print(when_offered(courses, 'cs101'))
#>>> ['apr2012', 'feb2012']

print(when_offered(courses, 'bio893'))
#>>> []
#############

print(involved(courses, 'Dave'))
#>>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

print(involved(courses, 'Peter C.'))
#>>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

print(involved(courses, 'Dorina'))
#>>> {'jan2044': ['cs001']}

print(involved(courses, 'Peter'))
#>>> {}

print(involved(courses, 'Robotic'))
#>>> {}

print(involved(courses, ''))
#>>> {}
