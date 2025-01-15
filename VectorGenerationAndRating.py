import random

xmin = -100
xmax =  100


def CreateSolution(N):
    return [round(random.uniform(xmin, xmax), 2) for x in range(N)]


def CalculateVO(solutions):
    VO = 0
    for element in solutions:
        VO += element**2
    return round(VO, 3)


def CreateSolutionsVector(M, N):
    return [CreateSolution(N) for i in range(M)]