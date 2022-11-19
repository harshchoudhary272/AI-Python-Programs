import random
import numpy as np
def crossover(offspring,parents):
    offspring = list(offspring)
    parents = list(parents)

    k = random.randint(0,8)
    print("crossover point:",k)
    #offspring = []
    for i in range(k,len(dad_mask)):
        offspring[i],parents[i] = parents[i],offspring[i]
        random_dad = parents[np.random.randint(low = 0, high = n_parents -1)]
        random_mom = parents[np.random.randint(low = 0, high = n_parents -1)]
    offspring = ''.join(offspring)
    parents = ''.join(parents)
    print(offspring)
    print(parents,"\n\n")
    return offspring, parents

dad_mask = int(input(),2)
mom_mask = int(input(),2)
print("parents")
print(dad_mask)
print(mom_mask)

for i in range(5):
    print("generation",i+1,"childrens:")
    dad_mask,mom_mask = crossover(dad_mask,mom_mask)    
    dad_mask = np.random.randint(0, 2, size = np.array(random_dad).shape)
    mom_mask = np.logical_not(dad_mask)

    child =  np.add(np.multiply(random_dad,dad_mask), np.multiply(random_mom,mom_mask))

    offspring.append(child)
    return offspring
