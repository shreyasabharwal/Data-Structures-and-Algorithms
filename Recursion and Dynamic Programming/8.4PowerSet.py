'''8.4 Power Set: Write a method to return all subsets of a set.
'''

# Backtracking problem

import copy
import pdb


def getSubsets(main_set, depth=0, subset=[], power_set=[]):
    print('Function start', depth, subset, power_set)
    # base case

    if depth == len(main_set):
        # pdb.set_trace()
        power_set.append(copy.deepcopy(subset))
        # pdb.set_trace()
        print('base case', depth, subset, power_set)
        return
    # pdb.set_trace()
    subset.append(main_set[depth])
    print('before first call', depth, subset, power_set)
    getSubsets(main_set,  depth+1, subset, power_set)
    del subset[-1]
    print('\nbefore second call', depth, subset, power_set)
    getSubsets(main_set,  depth+1, subset, power_set)
    return power_set


def getPowerSet(main_set):
    return getSubsets(main_set)


if __name__ == "__main__":
    master_set = [1, 2, 3]
    print(getPowerSet(master_set))
