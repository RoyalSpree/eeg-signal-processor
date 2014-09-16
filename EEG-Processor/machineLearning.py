"""
This module sets up different machines for machine learing algorithms based on the needs for the user. Set up as a library to import with mirrored commands for each machine.
"""

#This is the Support Vector Machine Section

from sklearn import svm
SVM = svm.SVC()

def SVMfit(x, y):
        """
        Input: x, y
        x (Array): An array of training points for the svm to set up an algorithm.
        y (Array): An array of values for their corresponding training point.
        Returns: NA
        Description: Sets the svm with an algorithm to predict the input data values.
        """
        SVM.fit(x, y)

def SVMpredict(x):
        """
        Input: x
        x (Array): An array of a data point to predict the value of.
        Returns: The predicted value of the data point.
        Description: Uses a svm to predict the value of the input data point.
        """
        return SVM.predict(x)

#This is the Linear Discriminant Analysis Section

from sklearn import lda
LDA = lda.LDA()

def LDAfit(x, y):
	"""
	Input: x, y
	x (Array): An array of training points for the svm to set up an algorithm.
	y (Array): An array of values for their corresponding training point.
	Returns: NA
	Description: Sets the lda with an algorithm to predict the input data values.
	"""
	LDA.fit(x,y)

def LDApredict(x):
	"""
	Input: x
	x (Array): An array of a data point to predict the value of.
	Returns: The predicted value of the data point.
	Description: Uses a lda to predict the value of the input data point.
	"""
	return LDA.predict(x)

#This is the Quadratic Discriminant Analysis Section

from sklearn import qda
QDA = qda.QDA()

def QDAfit(x, y):
	"""
	Input: x, y
	x (Array): An array of training points for the svm to set up an algorithm.
	y (Array): An array of values for their corresponding training point.
	Returns: NA
	Description: Sets the qda with an algorithm to predict the input data values.
	"""
	QDA.fit(x,y)

def QDApredict(x):
	"""
	Input: x
	x (Array): An array of a data point to predict the value of.
	Returns: The predicted value of the data point.
	Description: Uses a qda to predict the value of the input data point.
	"""
	return QDA.predict(x)

