import random
import math
LIMIT = 100000

def updateT(T):
    return T - 0.001

def move(index, results, T):
    new_index = random.randint(0, len(results))
    delta = results[new_index][2] - results[index][2]

    if delta > 0:
        return new_index
    else:
        p = math.exp(delta / T)
        return new_index if random.random() < p else index

def simulatedAnnealing(results):
    loop_count = 0
    start_index = random.randint(0, len(results))
    curr_index = start_index
    best_index = start_index
    T = 1.

    while T > 1e-3:
        curr_index = move(curr_index, results, T)
        if results[curr_index][2] > results[best_index][2]:
            best_index = curr_index
        T = updateT(T)
        loop_count += 1

    return curr_index, best_index, start_index

# Function given in the question
def func(x1, x2):
    return 21.5 + x1 * math.sin(4 * math.pi * x1) + x2 * math.sin(20 * math.pi * x2)

# Generate random results
def getRandomResults():
    # The range for x1 and x2
    x1_upper_bound = 12.1
    x1_lower_bond = -3
    x2_upper_bound = 5.8
    x2_lower_bond = 4.1
    vals = []
    for i in range(LIMIT):
        # Randomly select x1 and x2
        x1 = random.uniform(x1_lower_bond, x1_upper_bound)
        x2 = random.uniform(x2_lower_bond, x2_upper_bound)
        new_val = [x1, x2, func(x1,x2)]
        vals.append(new_val)
    return vals

# Entry point
if __name__ == '__main__':
    tries = 5
    for i in range(tries):
        random_results = getRandomResults()
        last, best, first = simulatedAnnealing(random_results)
        print "- Result %d:" % (i)
        print "  Last solution (%d): X1=%.6f, X2=%.6f, Y=%.6f" % (last, random_results[last][0], random_results[last][1], random_results[last][2])
        print "  Best solution (%d): X1=%.6f, X2=%.6f, Y=%.6f" % (best, random_results[best][0], random_results[best][1], random_results[best][2])
        print "  First solution (%d): X1=%.6f, X2=%.6f, Y=%.6f" % (first, random_results[first][0], random_results[first][1], random_results[first][2])
