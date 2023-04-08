import puzzle8 as p8
from typing import List
import time

solution = p8.solution()


finalResult = []
reachedFinal = False


def iterative_deepening_search(state: int) -> List[int]:
    """Finds path to solution via iterative deepening. Returns a list of
    squares that the blank moves to in order to get to solution.
    """
    i = 0
    while (True):
        result = depth_limited_search_for_test(state, i, [])
        if result != None:
            return result
        i += 1


def depth_limited_search_optimal(currentState, depth, path):
    if currentState == solution:
        return path
    if depth <= 0:
        return None
    blank_space_square = p8.blank_square(currentState)
    neighbors = p8.neighbors(blank_space_square)
    for neighbor in neighbors:
        temp = path.copy()
        temp.append(neighbor)
        newState = p8.move_blank(currentState, neighbor)
        result = depth_limited_search_optimal(newState, depth-1, temp.copy())
        if result != None:
            return result


def depth_limited_search_for_test(currentState, depth, path):
    global finalResult, reachedFinal
    if currentState == solution:
        reachedFinal = True
        finalResult = path
    if depth <= 0:
        return None
    blank_space_square = p8.blank_square(currentState)
    neighbors = p8.neighbors(blank_space_square)

    for neighbor in neighbors:
        temp = path.copy()
        temp.append(neighbor)
        newState = p8.move_blank(currentState, neighbor)
        result = depth_limited_search_for_test(newState, depth-1, temp.copy())
        if result != None:
            return result
    if reachedFinal == True:
        return finalResult


print(depth_limited_search_for_test(253206748, 4, []), "jij")


def timeTest(state):
    # state = 152293420
    depth = len(iterative_deepening_search(state))
    # Start time
    startTime = time.time()
    depth_limited_search_for_test(state, depth, [])
    # Finish Time
    finishTime = time.time()
    print("For solution has the length of " + str(depth) +
          ", Time taken to run the last iteration", finishTime-startTime)

    # Start time
    startTime = time.time()
    iterative_deepening_search(state)
    # Finish Time
    finishTime = time.time()
    print("For solution has the length of " + str(depth) +
          ", Time taken to run full", finishTime-startTime)


# main()
timeTest(253206748)
timeTest(253780508)
timeTest(152293420)
timeTest(300501380)
