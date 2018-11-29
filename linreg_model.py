"""
Playability Project
"""

# TODO
# - add function bodies
# - add new functions and helper functions as needed
# - add comments where code is unclear
# - read up on the difference between Ordinary Least Square (OLS) and gradient descent (GD) approaches to Lin Reg
# - briefly read up on mini-batch, batch, and stochastic GD as variants to the standard GD algorithm
# --- After looking at the different methods, you may find that you don't need all of the functions listed here

# SPECIAL NOTES:
# 1. Earlier we treated y as a binary variable. Now, y has a range of values. We still want to calculate cost as sum of squared error.
# 2. This code outline was drafted quickly. It's not guaranteed to be correct or helpful. Feel free to remove and edit functions as needed.

# For the future (ignore presently):
# - The magic of sklearn, numpy, and matplotlib
# - L1 and L2 regularization

STEP_SIZES = [1] # also called the learning rate

def predict(x, weights):
	"""Returns the y^ prediction of the sample x, given weight parameters"""
	return None

def cost(Y, Y_hat):
	"""Returns the sum of squared error difference between two vectors, y and y^"""
	return None
	

def gradient(X, Y, weights):
	"""Given dataset X, labels Y, and weights, return gradient"""
	# Note that the gradient is dependent on the dataset, since you need to know the cost of *every* data point
	# Notice also that gradient descent is a slow calculation - you need to compute the cost of every data point for each iteration step
	return None

	
def train_model(X, Y):
	"""Given dataset X and labels Y, return weight vector"""
	# TODO
	# - initialize weights
	# - while not finished, step along the gradient
	return [0] * len(X[0]) # by default, return a vector of all 0s
	
def test_model(V, Y, weights):
	"""Given validation data V, labels Y, and weight vector, report accuracy of model (error)"""
	return None
	
	
def main():
	"""Main function, reads input from file, calls the training function"""

	# Argparse is a handy library for reading arguments from the cmd line
	import argparse
	prog_desc = "Linear regression model for use with the Playability project."
	parser = argparse.ArgumentParser(description=prog_desc)
	parser.add_argument('input', help="Input file name")
	args = parser.parse_args()
	
	X = []
	Y = []
	
	import csv
	with open(args.input, 'r') as file:
		csv_reader = csv.reader(file)
		# Assume that csv has header file and skip it
		csv_reader.next()
		# Assume that csv has this form: id, x1, x2, x3, ..., y
		for row in csv_reader:
			Y.append(row[-1])
			X.append(row[1:-1])
	
	weights = train_model(X, Y)
	print("The model decided on these weights: " + str(weights))
	

if '__main__' == __name__:
	main()