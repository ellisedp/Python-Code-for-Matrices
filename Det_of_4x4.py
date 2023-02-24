# Ellise Parnoff - 12/12/2022
# Determinant of 4x4 matrix 

"""
STRATEGY: To calculate the determinant I used the formula for finding the 
determinant of a 4x4 matrix. To do this, I had to also find the determinants of 
2x2 and 3x3 matrices. I used functions to find these values to make my code 
more comprehensible.

Note: I understand using the 4x4 determinant formula in this program is not
computationally efficient. However, since we aren't dealing with too many 
numbers, I decided to use it to make my program simpler and more accurate.
"""

def det_2x2(listt):
  """Takes a 2x2 matrix as a list and returns determinant."""
  a = listt[0]
  b = listt[1]
  c = listt[2]
  d = listt[3]
  det = (a * d) - (b * c)
  return det


def det_3x3(listt):
  """Takes a 3x3 matrix in list form and returns determinant."""
  a = listt[0]
  b = listt[1]
  c = listt[2]
  d = listt[3]
  e = listt[4]
  f = listt[5]
  g = listt[6]
  h = listt[7]
  i = listt[8]

  det = (a * det_2x2([e,f,h,i])) - (b * det_2x2([d,f,g,i])) 
  det += (c * det_2x2([d,e,g,h]))
  return det

# Create placeholder matrix
A = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# Input values one at a time into matrix
for i in range(4):
  for j in range(4):
    A[i][j] = int(input("Enter values for a 4x4 matrix, \
one entry at a time: "))

print("\nYour matrix: ", A, "\n")

# Rename variables for simplicity 
a = A[0][0]
b = A[0][1]
c = A[0][2]
d = A[0][3]
e = A[1][0]
f = A[1][1]
g = A[1][2]
h = A[1][3]
i = A[2][0]
j = A[2][1]
k = A[2][2]
l = A[2][3]
m = A[3][0]
n = A[3][1]
o = A[3][2]
p = A[3][3]

# Calculate det of 4x4 matrix
det = a * det_3x3([f,g,h,j,k,l,n,o,p])
det -= b * det_3x3([e,g,h,i,k,l,m,o,p])
det += c * det_3x3([e,f,h,i,j,l,m,n,p])
det -= d * det_3x3([e,f,g,i,j,k,m,n,o])

print("The determinant of your matrix is: ",det)
