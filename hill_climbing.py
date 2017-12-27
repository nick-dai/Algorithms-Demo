import random
import math
import matplotlib.pyplot as plt

# The gap used when searching improvements
search_gap = 0.00001

# Search the values around the current value
def searchImprovement(x1, x2, prev):
	# Four possible improvements: increment/decrement in x1, increment/decrement in x2
	# Every calculated result only changes in one direction
	pairs = [[(x1 + search_gap), x2], [x1, (x2 + search_gap)], [(x1 - search_gap), x2], [x1, (x2 - search_gap)]]
	# Save all results to this list
	results = []
	results.append(func(pairs[0][0], pairs[0][1]))
	results.append(func(pairs[1][0], pairs[1][1]))
	results.append(func(pairs[2][0], pairs[2][1]))
	results.append(func(pairs[3][0], pairs[3][1]))
	# Find the maximum value and its index in the list
	max_value = max(results)
	max_index = results.index(max_value)
	# Return the maximum value, new x1 and new x2 when the current maximum is greater than the last one
	if max_value > prev:
		return { 'x1': pairs[max_index][0], 'x2': pairs[max_index][1], 'y': max_value }
	else:
		return False

# Function given in the question
def func(x1, x2):
	return 21.5 + x1 * math.sin(4 * math.pi * x1) + x2 * math.sin(20 * math.pi * x2)

# Main search function
def search():
	loop_count = 0 # Search loop count
	max_loop = 1000000000 # Search loop limit
	# The range for x1 and x2
	x1_upper_bound = 12.1
	x1_lower_bond = -3
	x2_upper_bound = 5.8
	x2_lower_bond = 4.1
	# Randomly select x1 and x2
	x1 = random.uniform(x1_lower_bond, x1_upper_bound)
	x2 = random.uniform(x2_lower_bond, x2_upper_bound)
	# Preserve the initial values for x1 and x2
	x1_history = [x1]
	x2_history = [x2]
	# The maximum got from the last search
	prev = func(x1, x2)
	y_history = [prev]
	while 1:
		loop_count += 1
		improvement = searchImprovement(x1, x2, prev)
		if improvement:
			# New x1 and new x2 should be in the range limited by the question
			if improvement['x1'] < x1_upper_bound and improvement['x1'] > x1_lower_bond and improvement['x2'] > x2_lower_bond and improvement['x2'] < x2_upper_bound:
				x1 = improvement['x1']
				x2 = improvement['x2']
				prev = improvement['y']
				x1_history.append(x1)
				x2_history.append(x2)
				y_history.append(prev)
			else:
				break
		else:
			break
		if loop_count > max_loop:
			return False
			break
	return { 'y': y_history, 'count': loop_count, 'x1': x1_history, 'x2': x2_history }

# Entry point
if __name__ == '__main__':
	# Try the search n times
	tries = 5
	for i in range(tries):
		result = search()
		if result:
			print "- Result %d:" % (i+1)
			print "  Y = %.6f\n  First_X1 = %.6f, First_X2 = %.6f, Loop = %d\n  Last_X1 = %.6f, Last_X2 = %.6f" % (result['y'][len(result['y'])-1], result['x1'][0], result['x2'][0], result['count'], result['x1'][len(result['x1'])-1], result['x2'][len(result['x2'])-1])
			# plt.plot(result['y'])
			# plt.ylabel('Hill Climbing')
			# plt.show()
		else:
			print "- Result %d: exceeds maximum loop limit." % i