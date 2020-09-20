def match(people, solved, unsolved):
    '''
        input: people - list of users
               solve - list of problems each user has solved with the index of the problems list corresponding to the user  
               unsolved - list of problems each user hasnt solved with the index of the problems list corresponding to the user
        output: list of lists of students with each list contaning the names of students sorted best to worst suited to match with the student that list corresponds to 

    '''
#   pairs = []    
    overlaps = []*len(people) #finds the number of problems each user can solve with each other user
    for i in range(len(people)):
        for j in range(len(people)):
            if(people[j] == people[i]):
                overlaps.append([-1])               
            else:
                overlaps.append([])
                overlap = 0
                for solprob in solved[i]:
                    for unsolprob in unsolved[j]:
                        if(solprob == unsolprob):
                            overlap+=1
                for unsolprob in unsolved[i]:
                    for solprob in solved[j]:
                        if(solprob == unsolprob):
                            overlap+=1
                overlaps[i].append(overlap)
    buddies = [] #creates lists of which people are best to pset with     
    for student in range(len(overlaps)):
        buddies.append([])
        while sum(overlaps[student])>-1*len(overlaps[student]):
            best = max(overlaps[student])
            bindex = overlaps[student].index(best)
            buddies[student].append(people[bindex])
            overlaps[student][bindex]=-1
#psetbuddies = [buddies[i:i+len(people)-1] for i in range(0,(len(people)-1)*len(people),len(people)-1)]
    return buddies
