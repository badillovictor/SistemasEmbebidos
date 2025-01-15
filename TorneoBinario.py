import random


def GetNextGenerationParents(solutions, scores, totalParents):
    # Create parents vector
    parents = []
    for i in range(totalParents):
        # Get 2 random parents
        parent1 = random.randint(0, len(solutions) - 1)
        parent2 = random.randint(0, len(solutions) - 1)
        # Make sure they are different
        while parent1 == parent2:
            parent2 = random.randint(0, len(solutions))
        # Compare their scores and see who is the best
        # Append the best to the parents vector
        if scores[parent1] < scores[parent2]:
            parents.append(solutions[parent1])
        else:
            parents.append(solutions[parent2])
    # Return the parents vector
    return parents
