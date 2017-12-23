import random
import math

# The gap used when searching improvements
search_gap = 0.00001

# Search the values around the current value
def searchImprovements(x1, x2, prev):
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
		return [pairs[max_index][0], pairs[max_index][1], max_value]
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
	x1_start = x1
	x2_start = x2
	# The maximum got from the last search
	prev = None
	while 1:
		loop_count += 1
		can_continue = searchImprovements(x1, x2, prev)
		if can_continue:
			# New x1 and new x2 should be in the range limited by the question
			if can_continue[0] < x1_upper_bound and can_continue[0] > x1_lower_bond and can_continue[1] > x2_lower_bond and can_continue[1] < x2_upper_bound:
				x1 = can_continue[0]
				x2 = can_continue[1]
				prev = can_continue[2]
			else:
				break
		else:
			break
		if loop_count > max_loop:
			return False
			break
	return [prev, x1_start, x2_start, loop_count, x1, x2]

# Entry point
if __name__ == '__main__':
	# Try the search n times
	tries = 10
	for i in range(tries):
		result = search()
		if result:
			print "- Result %d:" % (i+1)
			print "  Y = %.6f\n  X1 = %.6f, X2 = %.6f, Loop = %d\n  Max_X1 = %.6f, Max_X2 = %.6f" % (result[0], result[1], result[2], result[3], result[4], result[5])
		else:
			print "- Result %d: exceeds maximum loop limit." % i