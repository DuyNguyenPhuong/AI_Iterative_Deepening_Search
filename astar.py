import puzzle8 as p8
import heapq


def num_wrong_tiles(state) -> int:
    """Given a puzzle, returns the number of tiles that are in the wrong
    location. Does not count the blank space.
    """
    raise NotImplementedError("You must implement this method")


def manhattan_distance(state) -> int:
    """Given a puzzle, returns the Manhattan distance to the solution state.
    Does not count the distance from blank space to its correct location as
    part of the distance.
    """
    raise NotImplementedError("You must implement this method")


def astar_search(state: int, heuristic) -> List[int]:
    """Finds path to solution via A* search, using the provided heuristic.
    Returns a list of squares that the blank moves to in order to get to
    solution.
    """
    raise NotImplementedError("You must implement this method")
