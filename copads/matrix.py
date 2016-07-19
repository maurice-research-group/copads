'''
Matrix Data Structures and Algorithms.

Date created: 19th March 2008

Licence: Python Software Foundation License version 2
'''

import types
import operator
import math
import random
from copadsexceptions import VectorOperationError
from copadsexceptions import MatrixError, MatrixMultiplicationError
from copadsexceptions import MatrixAdditionError, MatrixSquareError
from copadsexceptions import MatrixTraceError, MatrixMinorError
from copadsexceptions import MatrixDeterminantError

class Vector(object):
    '''
    A list based vector class, based on the implementation by A. Pletzer 
    (http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52272), that 
    supports elementwise mathematical operations.
    '''
    def __init__(self, values=[]):
        '''
        Constructor method.
        
        @param values: values for the vector. Default is empty list.
        @type values: list
        '''
        self.values = [float(x) for x in values]
        
    def zeros(self, num_of_elements):
        '''
        Method to initiate the vector to a vector of zeros.
        
        @param num_of_elements: length of the vector to initiate.
        @type num_of_elements: integer
        '''
        self.values = [0.0] * int(num_of_elements)
       
    def ones(self, num_of_elements):
        '''
        Method to initiate the vector to a vector of ones.
        
        @param num_of_elements: length of the vector to initiate.
        @type num_of_elements: integer
        '''
        self.values = [1.0] * int(num_of_elements)
        
    def random(self, num_of_elements, min_value=0.0, max_value=1.0):
        '''
        Method to initiate the vector to a vector of uniformly distributed 
        random values .
        
        @param num_of_elements: length of the vector to initiate.
        @type num_of_elements: integer
        @param min_value: minimum value of the vector. Default = 0.0.
        @type min_value: float
        @param max_value: maximum value of the vector. Default = 1.0.
        @type max_value: float
        '''
        self.values = [random.uniform(min_value, max_value) 
                       for i in int(num_of_elements)]

    def log10(self):
        '''
        Method to perform element-wise log10 on the vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.log10(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.log10()')
        self.values = values
        return self.values

    def log(self, base=math.e):
        '''
        Method to perform element-wise log on the vector.
        
        @param base: base value of the logarithmic function. Default = e.
        @type base: float
        @return: result vector as a list.
        '''
        base = float(base)
        try:
            values = [math.log(x, base) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.log()')
        self.values = values
        return self.values

    def exp(self):
        '''
        Method to perform element-wise exponential (e to the power of the 
        value) on the vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.exp(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.exp()')
        self.values = values
        return self.values
        
    def pow(self, n):
        '''
        Method to perform element-wise power (value to the power of n) on 
        the vector.
        
        @param n: exponent to be raised.
        @type n: float
        @return: result vector as a list.
        '''
        n = float(n)
        try:
            values = [float(x)**n for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.pow()')
        self.values = values
        return self.values
        
    def sin(self):
        '''
        Method to perform element-wise sine in radians on the vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.sin(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.sin()')
        self.values = values
        return self.values

    def cos(self):
        '''
        Method to perform element-wise cosine in radians on the vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.cos(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.cos()')
        self.values = values
        return self.values
        
    def tan(self):
        '''
        Method to perform element-wise tangent in randians on the vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.tan(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.tan()')
        self.values = values
        return self.values
        
    def asin(self):
        '''
        Method to perform element-wise arc sine in radians on the vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.asin(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.asin()')
        self.values = values
        return self.values

    def acos(self):
        '''
        Method to perform element-wise arc cosine in radians on the vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.acos(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.a()')
        self.values = values
        return self.values
        
    def atan(self):
        '''
        Method to perform element-wise arc tangent in radians on the 
        vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.atan(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.atan()')
        self.values = values
        return self.values

    def sinh(self):
        '''
        Method to perform element-wise hyperbolic sine in radians on the 
        vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.sinh(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.sinh()')
        self.values = values
        return self.values

    def cosh(self):
        '''
        Method to perform element-wise hyperbolic cosine in radians on the 
        vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.cosh(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.cosh()')
        self.values = values
        return self.values
        
    def tanh(self):
        '''
        Method to perform element-wise hyperbolic tangent in radians on the 
        vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.tanh(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.tanh()')
        self.values = values
        return self.values
        
    def asinh(self):
        '''
        Method to perform element-wise inverse hyperbolic sine in radians 
        on the vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.asinh(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.asinh()')
        self.values = values
        return self.values

    def acosh(self):
        '''
        Method to perform element-wise inverse hyperbolic cosine in radians 
        on the vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.acosh(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.acosh()')
        self.values = values
        return self.values
        
    def atanh(self):
        '''
        Method to perform element-wise inverse hyperbolic tangent in radians 
        on the vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.atanh(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.atanh()')
        self.values = values
        return self.values
        
    def sqrt(self):
        '''
        Method to perform element-wise square root on the vector.
        
        @return: result vector as a list.
        '''
        try:
            values = [math.sqrt(x) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.sqrt()')
        self.values = values
        return self.values
        
    def root(self, n):
        '''
        Method to perform element-wise n-th root on the vector.
        
        @param n: value of the root.
        @type n: float
        @return: result vector as a list.
        '''
        n = float(n)
        try:
            values = [float(x)**(1.0/float(n)) for x in self.values]
        except:
            raise VectorOperationError('Failure in Vector.root()')
        self.values = values
        return self.values
    
    def abs(self):
        '''
        Method to perform element-wise absolute on the vector.
        
        @return: result vector as a list.
        '''
        pass
        
    def factorial(self):
        '''
        Method to perform element-wise factorial on the vector.
        
        @return: result vector as a list.
        '''
        pass
    
    def degrees(self):
        '''
        Method to perform element-wise conversion of values in radians to 
        degrees on the vector.
        
        @return: result vector as a list.
        '''
        pass
        
    def radians(self):
        '''
        Method to perform element-wise conversion of values in degrees to 
        radians on the vector.
        
        @return: result vector as a list.
        '''
        pass
        
    def sum(self):
        '''
        Method to perform summation on the vector.
        
        @return: summation of the vector.
        '''
        pass
        
    def __add__(self, vectorX):
        '''
        Method to add a vector (of the same size) to the currect vector. 
        The resulting vector will be the result of element-wise addition.
        
        @param vectorX: vector to be added.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        if len(self.values) != len(vectorX.values):
            raise VectorOperationError('Vectors have different sizes')
        try:
            values = [self.values[i] + vectorX.values[i] 
                      for i in range(len(self.values))]
            return Vector(values)
        except:
            raise VectorOperationError('Failure in Vector.__add__()')
    
    def __neg__(self):
        '''
        Method to negate the currect vector. The resulting vector will be 
        the result of element-wise negation.
        
        @return: resulting copads.matrix.Vector object
        '''
        pass
        
    def __sub__(self, vectorX):
        '''
        Method to subtract a vector (of the same size) from the currect 
        vector. The resulting vector will be the result of element-wise 
        subtraction.
        
        @param vectorX: vector to be subtracted.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        pass
        
    def __mul__(self, vectorX):
        '''
        Method to multiply a vector (of the same size) to the currect 
        vector. The resulting vector will be the result of element-wise 
        multiplication.
        
        @param vectorX: vector to be multiplied.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        pass
        
    def __div__(self, vectorX):
        '''
        Method to divide a vector (of the same size) from the currect 
        vector. The resulting vector will be the result of element-wise 
        division.
        
        @param vectorX: vector to be divided.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        pass   
    

# class Matrix:
    # """
    # A linear algebra matrix

    # This class defines a generic matrix and the basic matrix operations from
    # linear algebra.  An instance of this class is a single matrix with
    # particular values.
    
    # Arithmetic operations, trace, determinant, and minors are defined. This is a 
    # lightweight alternative to a numerical Python package for people who need to do 
    # basic linear algebra.

    # Vectors are implemented as 1xN and Nx1 matricies.  There is no separate vector
    # class.  This implementation enforces the distinction between row and column
    # vectors.

    # Indexing is zero-based, i.e. the upper left-hand corner of a matrix is element
    # (0,0), not element (1,1).

    # Matricies are stored as a list of lists, where the top level lists are the rows
    # and the sub-lists are the columns.  Because of the way Python handles list
    # references, you have be careful when copying matrix objects.  If you have a
    # matrix a, assign b=a, and then change values in b, you will change values in a
    # as well.  Matrix copying should be done with copy.deepcopy.

    # This implementation has no memory-saving optimization for sparse matricies.  A
    # derived class may implement a more sophisticated storage method by overriding 
    # the __getitem__ and __setitem__ functions.

    # Determinants are taken by expanding by minors on the top row.  The private 
    # functions supplied for expansion by minors are more generic than what is needed
    # by this implementation.  They may be used by a derived class that wishes to do
    # more efficient expansion of sparse matricies.

    # By default, Matrix elements are members of the complex field, but if you want
    # to perform linear algebra on something other than numbers you may redefine
    # Matrix.null_element, Matrix.identity_element, and Matrix.inverse_element and 
    # override the is_scalar_element function.

    # References
    # George Arfken, "Mathematical Methods for Physicists", 3rd ed. San Diego.
    # Academic Press Inc. (1985)

    # Adapted from: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/189971
    # Original author: Bill McNeill <billmcn@speakeasy.net>

    # Maintainer: Maurice H.T. Ling <mauriceling@acm.org>
    # Copyright (c) 2005 Maurice H.T. Ling <mauriceling@acm.org>
    # Date: 1st May 2005
    # """
    # null_element = 0
    # identity_element = 1
    # inverse_element = -1

    # def __init__(self, *args):
        # """Matrix constructor

        # A matrix can be created in three ways.

            # 1. A single integer argument is supplied. The constructor creates a
            # null square matrix of that size.  For example 

            # Matrix(2)

            # creates the following matrix

            # 0    0
            # 0    0

            # 2. Two integer arguments are supplied.  The constructor creates a null
            # matrix of size first argument x second argument.  For example

            # Matrix(2, 3)

            # creates the following matrix

            # 0    0    0
            # 0    0    0

            # 3. A list of lists is supplied.  It represents a set of initial matrix
            # values.  Each element is a row and each sub-list is a column.
            # For example

            # Matrix([[1,2,3], [4,5,6], [7,8,9]])

            # creates the following matrix

            # 1    2    3
            # 4    5    6
            # 7    8    9
        # """
        # if not (len(args) == 1 or len(args) == 2):
            # raise TypeError("Matrix() takes 1 or 2 arguments (%d given)") % \
                # len(args)
        # if len(args) == 2:    # Two arguments
            # # Create an null n,m matrix.
            # row, col = args
            # self.createNullMatrix(row, col)
        # else:    # One argument
            # if isinstance(args[0], types.IntType):
                # # Create a square null matrix.
                # self.create_null_matrix(args[0], args[0])
            # else:
                # # Create a matrix from initial values.
                # self.m = args[0]
                # if __debug__:
                    # # Verify correct format for m.
                    # if not isinstance(args[0], types.ListType):
                        # raise TypeError("Invalid initial data %s" % args[0])
                    # for row in args[0]:
                        # if not isinstance(row, types.ListType):
                            # raise ValueError("Invalid initial data %s" % \
                                # args[0])
                        # if not (len(row) == len(args[0][0])):
                            # raise ValueError("Non-rectangular initial data")
                    # if not (self.cols() > 0):
                        # raise ValueError("invalid number of columns %d" % \
                            # self.cols())
                    # if self.rows() == 1 and self.cols() == 1:
                        # raise ValueError("Cannot create 1x1 matrix")

    # def createNullMatrix(self, row, col):
        # """ Create a matrix using the null value

        # This is a private function called by __init__.
        # """
        # if not row > 0:
            # raise ValueError("invalid number of rows %d" % row)
        # if not col > 0:
            # raise ValueError("invalid number of columns %d" % col)
        # if row == 1 and col == 1:
            # raise ValueError("Cannot create 1x1 matrix")
        # # Note, you cannot simply write
        # #    self.m = [[self.null_element]*col]*row
        # # because this will make all the rows references of a single instance.
        # self.m = []
        # for i in xrange(row):
            # self.m.append([])
            # for j in xrange(col):
                # self.m[i].append(self.null_element)

    # def __str__(self):
        # s = ""
        # for row in self.m:
            # s += "%s\n" % row
        # return s

    # def __cmp__(self, other):
        # if not isinstance(other, Matrix):
            # raise TypeError("Cannot compare matrix with %s" % type(other))
        # return cmp(self.m, other.m)

    # def __getitem__(self, (row, col)):
        # """The value at (row, col)

        # For example, to get the value of element 1,3 say

        # m[(1,3)]
        # """
        # return self.m[row][col]

    # def __setitem__(self, (row, col), value):
        # """Sets the value at (row, col)

        # For example, to set the value of element 1,3 to 5 say

        # m[(1,3)] = 5
        # """
        # self.m[row][col] = value

    # def rows(self):
        # """The number of rows in the matrix"""
        # return len(self.m)

    # def cols(self):
        # """The number of columns in the matrix"""
        # return len(self.m[0])

    # def row(self, i):
        # """The ith row of the matrix"""
        # return self.m[i]

    # def col(self, j):
        # """The jth row of the matrix"""
        # r = []
        # for row in self.m:
            # r.append(row[j])
        # return r

    # def __add__(self, other):
        # """Add matrix self + other"""
        # if not isinstance(other, Matrix):
            # raise TypeError("Cannot add a matrix to type %s" % type(other))
        # if not (self.cols() == other.cols() and self.rows() == other.rows()):
            # raise MatrixAdditionError(self, other)
        # r = []
        # for row in xrange(self.rows()):
            # r.append([])
            # for col in xrange(self.cols()):
                # r[row].append(self[(row, col)] + other[(row, col)])
        # return Matrix(r)

    # def __neg__(self):
        # """Negate the current matrix"""
        # return self.inverse_element*self

    # def __sub__(self, other):
        # """Subtract matrix self - other"""
        # return self + -other

    # def __mul__(self, other):
        # """Multiply matrix self*other

        # other can be another matrix or a scalar.
        # """
        # if self.isScalarElement(other):
            # return self.scalarMultiply(other)
        # if not isinstance(other, Matrix):
            # raise TypeError("Cannot multiply matrix and type %s" % type(other))
        # if other.isRowVector():
            # raise MatrixMultiplicationError(self, other)
        # return self.matrixMultiply(other)

    # def __rmul__(self, other):
        # """Multiply other*self

        # This is only called if other.__add__ is not defined, so assume that
        # other is a scalar.
        # """
        # if not self.isScalarElement(other):
            # raise TypeError("Cannot right-multiply by %s" % type(other))
        # return self.scalarMultiply(other)

    # def scalarMultiply(self, scalar):
        # """Multiply the matrix by a scalar value.

        # This is a private function called by __mul__ and __rmul__.
        # """
        # r = []
        # for row in self.m:                
            # r.append(map(lambda x: x*scalar, row))
        # return Matrix(r)

    # def matrixMultiply(self, other):
        # """Multiply the matrix by another matrix.

        # This is a private function called by __mul__.
        # """
        # # Take the product of two matricies.
        # r = []
        # assert(isinstance(other, Matrix))
        # if not self.cols() == other.rows():
            # raise MatrixMultiplicationError(self, other)
        # for row in xrange(self.rows()):
            # r.append([])
            # for col in xrange(other.cols()):
                # r[row].append( self.vectorInnerProduct(self.row(row),
                                                       # other.col(col)))
        # if len(r) == 1 and len(r[0]) == 1:
            # # The result is a scalar.
            # return r[0][0]
        # else:
            # # The result is a matrix.
            # return Matrix(r)

    # def isRowVector(self):
        # """Is the matrix a row vector?"""
        # return self.rows() == 1 and self.cols() > 1

    # def isColumnVector(self):
        # """Is the matrix a column vector?"""
        # return self.cols() == 1 and self.rows() > 1

    # def isSquare(self):
        # """Is the matrix square?"""
        # return self.rows() == self.cols()

    # def transpose(self):
        # """The transpose of the matrix"""
        # r = []
        # for col in xrange(self.cols()):
            # r.append(self.col(col))
        # return Matrix(r)

    # def trace(self):
        # """The trace of the matrix"""
        # if not self.is_square():
            # raise MatrixTraceError()
        # t = 0
        # for i in xrange(self.rows()):
            # t += self[(i, i)]
        # return t

    # def determinant(self):
        # """The determinant of the matrix"""
        # if not self.isSquare():
            # raise MatrixDeterminantError()
        # # Calculate 2x2 determinants directly.
        # if self.rows() == 2:
            # return self[(0, 0)]*self[(1, 1)] - self[(0, 1)]*self[(1, 0)]
        # # Expand by minors for larger matricies.
        # return self.expandByMinorsOnRow(0)

    # def expandByMinorsOnRow(self, row):
        # """Calculates the determinant by expansion of minors

        # This function returns the determinant of the matrix by doing an
        # expansion of minors on the specified row.
        # """
        # assert(row < self.rows())
        # d = 0
        # for col in xrange(self.cols()):
            # # Note: the () around -1 are needed.  Otherwise you get -(1**col).
            # d += (-1)**(row+col)* \
                # self[(row, col)]*self.minor(row, col).determinant()
        # return d

    # def expandByMinorsOnColumn(self, col):
        # """Calculates the determinant by expansion of minors

        # This function returns the determinant of the matrix by doing an
        # expansion of minors on the specified column.
        # """
        # assert(col < self.cols())
        # d = 0
        # for row in xrange(self.rows()):
            # # Note: the () around -1 are needed.  Otherwise you get -(1**col).
            # d += (-1)**(row+col) \
                # *self[(row, col)]*self.minor(row, col).determinant()
        # return d

    # def minor(self, i, j):
        # """A minor of the matrix

        # This function returns the minor given by striking out row i and
        # column j of the matrix.
        # """
        # # Verify parameters.
        # if not self.isSquare():
            # raise MatrixMinorError()
        # if i<0 or i>=self.rows():
            # raise ValueError("Row value %d is out of range" % i)
        # if j<0 or j>=self.cols():
            # raise ValueError("Column value %d is out of range" % j)
        # # Create the output matrix.
        # m = Matrix(self.rows()-1, self.cols()-1)
        # # Loop through the matrix, skipping over the row and column specified
        # # by i and j.
        # minor_row = 0
        # minor_col = 0
        # for self_row in xrange(self.rows()):
            # if not self_row == i:    # Skip row i.
                # for self_col in xrange(self.cols()):
                    # if not self_col == j:    # Skip column j.
                        # m[(minor_row, minor_col)] = self[(self_row, self_col)]
                        # minor_col = minor_col + 1
                # minor_col = 0
                # minor_row = minor_col + 1
        # return m
        
    # def minorMatrix(self):
        # """
        # Calculates minor matrix
        # """
        # m = Matrix(self.rows(), self.cols())
        # for row in range(self.rows()):
            # for col in range(self.cols()):
                # minor_matrix = self.minor(row, col)
                # m[(row, col)] = minor_matrix.determinant()
        # return m

    # def adjoint(self):
        # """
        # Calculates adjoint matrix
        # """
        # m = Matrix(self.rows(), self.cols())
        # for row in range(self.rows()):
            # for col in range(self.cols()):
                # minor_matrix = self.minor(row, col)
                # det = minor_matrix.determinant()
                # m[(row, col)] = ((-1)**(row+col)) * det
        # return m

    # def inverse(self):
        # """
        # Calculates inverse matrix
        # """
        # det = float(self.determinant())
        # adj = self.adjoint()
        # return adj.scalarMultiply(1/det)
        
    # def vectorInnerProduct(self, a, b):
        # """Takes the inner product of vectors a and b

        # a and b are lists.
        # This is a private function called by matrix_multiply.
        # """
        # assert(isinstance(a, types.ListType))
        # assert(isinstance(b, types.ListType))
        # return reduce(operator.add, map(operator.mul, a, b))

    # def isScalarElement(self, x):
        # """Is x a scalar

        # By default a scalar is an element in the complex number field.
        # A class that wants to perform linear algebra on things other than
        # numbers may override this function.
        # """
        # return isinstance(x, types.IntType) or \
                # isinstance(x, types.FloatType) or \
                # isinstance(x, types.ComplexType)

# class SparseMatrix(dict):
    # """
    # A sparse matrix class based on a dictionary, supporting matrix (dot)
    # product and a conjugate gradient solver. 

    # In this version, the sparse class inherits from the dictionary; this
    # requires Python 2.2 or later.

    # Adapted from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52275
    # Original author: Alexander Pletzer

    # Dictionary storage format { (i,j): value, ... }
    # where (i,j) are the matrix indices
           # """

    # # no c'tor
    # def size(self):
        # " returns # of rows and columns "
        # nrow = 0
        # ncol = 0
        # for key in list(self.keys()):
            # nrow = max([nrow, key[0]+1])
            # ncol = max([ncol, key[1]+1])
        # return (nrow, ncol)

    # def __add__(self, other):
        # res = SparseMatrix(self.copy())
        # for ij in other:
            # res[ij] = self.get(ij, 0.) + other[ij]
        # return res
        
    # def __neg__(self):
        # return SparseMatrix(zip(list(self.keys()), 
                            # map(operator.neg, list(self.values()))))

    # def __sub__(self, other):
        # res = SparseMatrix(self.copy())
        # for ij in other:
            # res[ij] = self.get(ij, 0.) - other[ij]
        # return res
        
    # def __mul__(self, other):
        # " element by element multiplication: other can be scalar or sparse "
        # try:
            # # other is sparse
            # nval = len(other)
            # res = SparseMatrix()
            # if nval < len(self):
                # for ij in other:
                    # res[ij] = self.get(ij, 0.)*other[ij]
            # else:
                # for ij in self:
                    # res[ij] = self[ij]*other.get(ij, 0j)
            # return res
        # except:
            # # other is scalar
            # return SparseMatrix(zip(list(self.keys()), 
                                # map(lambda x: x*other, list(self.values()))))

    # def __rmul__(self, other):
        # return self.__mul__(other)

    # def __div__(self, other):
        # " element by element division self/other: other is scalar"
        # return SparseMatrix(zip(list(self.keys()), 
                            # map(lambda x: x/other, list(self.values()))))
        
    # def __rdiv__(self, other):
        # " element by element division other/self: other is scalar"
        # return SparseMatrix(zip(list(self.keys()), 
                            # map(lambda x: other/x, list(self.values()))))

    # def abs(self):
        # return SparseMatrix(zip(list(self.keys()), 
                            # map(operator.abs, list(self.values()))))

    # def out(self):
        # print('# (i, j) -- value')
        # for k in list(self.keys()):
            # print(k, self[k])

    # def plot(self, width_in=400, height_in=400):

        # import colormap
        # import Tkinter

        # cmax = max(self.values())
        # cmin = min(self.values())
        
        # offset = 0.05*min(width_in, height_in)
        # xmin, ymin, xmax, ymax = 0, 0, self.size()[0], self.size()[1]
        # scale = min(0.9*width_in, 0.9*height_in)/max(xmax-xmin, ymax-ymin)

        # root = Tkinter.Tk()
        # frame = Tkinter.Frame(root)
        # frame.pack()
        
        # text = Tkinter.Label(width=20, height=10, text='matrix sparsity')
        # text.pack()
        

        # canvas = Tkinter.Canvas(bg="black", width=width_in, height=height_in)
        # canvas.pack()

        # button = Tkinter.Button(frame, text="OK?", fg="red",
                                # command=frame.quit)
        # button.pack()

        # for index in list(self.keys()):
            # ix, iy = index[0], ymax-index[1]-1
            # ya, xa = offset+scale*(ix), height_in -offset-scale*(iy)
            # yb, xb = offset+scale*(ix+1), height_in -offset-scale*(iy)
            # yc, xc = offset+scale*(ix+1), height_in -offset-scale*(iy+1)
            # yd, xd = offset+scale*(ix), height_in -offset-scale*(iy+1)
            # color = colormap.strRgb(self[index], cmin, cmax)
            # canvas.create_polygon(xa, ya, xb, yb, xc, yc, xd, yd, fill=color)
        
        # root.mainloop()

    # def CGsolve(self, x0, b, tol=1.0e-10, nmax = 1000, verbose=1):
        # """
        # Solve self*x = b and return x using the conjugate gradient method
        # """
        # if not isVector(b):
            # raise TypeError, self.__class__, ' in solve '
        # else:
            # if self.size()[0] != len(b) or self.size()[1] != len(b):
                # print('**Incompatible sizes in solve')
                # print('**size()=', self.size()[0], self.size()[1])
                # print('**len=', len(b))
            # else:
                # kvec = diag(self) # preconditionner
                # n = len(b)
                # x = x0 # initial guess
                # r = b - sm_dot(self, x)
                # try:
                    # w = r/kvec
                # except: print('***singular kvec')
                # p = v_zeros(n)
                # beta = v_dot(r, w)
                # err = v_norm(dot(self, x) - b)
                # k = 0
                # if verbose: print(" conjugate gradient convergence (log error)")
                # while abs(err) > tol and k < nmax:
                    # p = w + beta*p
                    # z = sm_dot(self, p)
                    # alpha = rho/v_dot(p, z)
                    # r = r - alpha*z
                    # w = r/kvec
                    # rhoold = rho
                    # rho = v_dot(r, w)
                    # x = x + alpha*p
                    # beta = rho/rhoold
                    # err = v_norm(dot(self, x) - b)
                    # if verbose:
                        # print(k, ' %5.1f ' % math.log10(err))
                    # k = k+1
                # return x
                
    # def biCGsolve(self, x0, b, tol=1.0e-10, nmax = 1000):
        # """
        # Solve self*x = b and return x using the bi-conjugate gradient method
        # """

        # try:
            # if not isVector(b):
                # raise TypeError, self.__class__, ' in solve '
            # else:
                # if self.size()[0] != len(b) or self.size()[1] != len(b):
                    # print('**Incompatible sizes in solve')
                    # print('**size()=', self.size()[0], self.size()[1])
                    # print('**len=', len(b))
                # else:
                    # kvec = sm_diag(self) # preconditionner 
                    # n = len(b)
                    # x = x0 # initial guess
                    # r = b - sm_dot(self, x)
                    # rbar = r
                    # w = r/kvec
                    # wbar = rbar/kvec
                    # p = v_zeros(n)
                    # pbar = v_zeros(n)
                    # beta = 0.0
                    # rho = v_dot(rbar, w)
                    # err = v_norm(dot(self, x) - b)
                    # k = 0
                    # print(" bi-conjugate gradient convergence (log error)")
                    # while abs(err) > tol and k < nmax:
                        # p = w + beta*p
                        # pbar = wbar + beta*pbar
                        # z = dot(self, p)
                        # alpha = rho/v_dot(pbar, z)
                        # r = r - alpha*z
                        # rbar = rbar - alpha* sm_dot(pbar, self)
                        # w = r/kvec
                        # wbar = rbar/kvec
                        # rhoold = rho
                        # rho = v_dot(rbar, w)
                        # x = x + alpha*p
                        # beta = rho/rhoold
                        # err = v_norm(sm_dot(self, x) - b)
                        # print(k, ' %5.1f ' % math.log10(err))
                        # k = k+1
                    # return x
        # except:
            # print('ERROR ', self.__class__, '::biCGsolve')

    # def save(self, filename, OneBased=0):
        # """
        # Save matrix in file <filaname> using format
        # OneBased, nrow, ncol, nnonzeros
        # [ii, jj, data]
        # """
        # m = n = 0
        # nnz = len(self)
        # for ij in list(self.keys()):
            # m = max(ij[0], m)
            # n = max(ij[1], n)

        # f = open(filename, 'w')
        # f.write('%d %d %d %d\n' % (OneBased, m+1, n+1, nnz))
        # for ij in list(self.keys()):
            # i, j = ij
            # f.write('%d %d %20.17f \n'% \
                # (i+OneBased, j+OneBased, self[ij]))
        # f.close()
                
    
# def vDot(a, b):
    # """dot product of two vectors."""
    # try: return reduce(lambda x, y: x+y, a*b, 0.)
    # except: raise TypeError, 'Vector::FAILURE in dot'
    
# def vNorm(a):
    # """Computes the norm of vector a."""
    # try: return math.sqrt(abs(dot(a, a)))
    # except: raise TypeError, 'vector::FAILURE in norm'

# def vSum(a):
    # """Returns the sum of the elements of a."""
    # try: return reduce(lambda x, y: x+y, a, 0)
    # except: raise TypeError, 'vector::FAILURE in sum'


# def smTranspose(a):
    # """transpose"""
    # new = SparseMatrix({})
    # for ij in a:
        # new[(ij[1], ij[0])] = a[ij]
    # return new

# def smDotDot(y, a, x):
    # """double dot product y^+ *A*x """
    # if Vector.isVector(y) and isSparse(a) and Vector.isVector(x):
        # res = 0.
        # for ij in list(a.keys()):
            # i, j = ij
            # res += y[i]*a[ij]*x[j]
        # return res
    # else:
        # print('sparse::Error: dotDot takes vector, sparse , vector as args')

# def smDot(a, b):
    # """vector-matrix, matrix-vector or matrix-matrix product"""
    # if isSparse(a) and isVector(b):
        # new = v_zeros(a.size()[0])
        # for ij in list(a.keys()):
            # new[ij[0]] += a[ij]* b[ij[1]]
        # return new
    # elif isVector(a) and isSparse(b):
        # new = v_zeros(b.size()[1])
        # for ij in list(b.keys()):
            # new[ij[1]] += a[ij[0]]* b[ij]
        # return new
    # elif isSparse(a) and isSparse(b):
        # if a.size()[1] != b.size()[0]:
            # print('**Warning shapes do not match in dot(sparse, sparse)')
        # new = SparseMatrix({})
        # n = min([a.size()[1], b.size()[0]])
        # for i in range(a.size()[0]):
            # for j in range(b.size()[1]):
                # sum = 0.
                # for k in range(n):
                    # sum += a.get((i, k), 0.)*b.get((k, j), 0.)
                # if sum != 0.:
                    # new[(i, j)] = sum
        # return new
    # else:
        # raise TypeError, 'in dot'

# def smDiag(b):
    # # given a sparse matrix b return its diagonal
    # res = Vector.zeros(b.size()[0])
    # for i in range(b.size()[0]):
        # res[i] = b.get((i, i), 0.)
    # return res
        
# def smIdentity(n):
    # if type(n) != types.IntType:
        # raise TypeError, ' in identity: # must be integer'
    # else:
        # new = SparseMatrix({})
        # for i in range(n):
            # new[(i, i)] = 1+0.
        # return new
 
