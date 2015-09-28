def madlibs():
    print 'Wellcome to the mad libs game'

    name = raw_input('Insert a name :')
    animals = raw_input('Insert animals :')
    verb = raw_input('Insert a verb :')
    adjective = raw_input('Insert an adjective :')
    place = raw_input('Insert a place :')

    print 'I am', name, 'a full stack ninja from', place, 'where I', verb, 'with wild', adjective, animals

madlibs()