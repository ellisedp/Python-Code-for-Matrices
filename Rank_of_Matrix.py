# Ellise Parnoff - 12/12/2022
# Output rank of matrix 

"""
STRATEGY: To find the rank of the matrix, first I check if the matrix is a zero 
matrix. If so, the rank must be 0. I also check the determinant of the matrix. 
If the det is non-zero, then the matrix must be invertible and it's rank must be 
3. Then, I check the linear dependence between rows in the matrix. If only two 
rows are linearly dependent, then the rank is 2. If all three rows are linearly 
dependent, then the rank is 1. 

This method comes from the fact that you can cancel out linearly dependent 
rows using elementary row opperations to make zero rows. Since the rank of a 
matrix is the number of non-zero rows it has, this information is very useful. 
"""

def det_2x2(listt):
  """Takes a 2x2 matrix in list form and returns determinant."""
  det = (listt[0] * listt[3]) - (listt[1] * listt[2])
  return det


def row_mult(listt, scalar):
  """Multiplies list by scalar."""
  # Create a new list as to not change origninal matrix during this process
  newlist= [0,0,0]
  for i in range(len(listt)):
    newlist[i] = listt[i]
  for i in range(len(listt)):
    newlist[i] = newlist[i] * scalar
  return newlist


def row_add(list1, list2):
  """Adds together two lists."""
  newlist = [0,0,0]
  for i in range(len(list1)):
    newlist[i] = list1[i] + list2[i]
  return newlist 


def check_lin_dep(row1, row2):
  """Check if two rows are linearly dependent."""
  temp1 = row_mult(row1, -(row2[0]))
  temp2 = row_mult(row2, row1[0])
  temp3 = row_add(temp1, temp2)
  # See if temp 3 is all zeros
  # If so, row1 and row2 are linearly dependent
  sum = 0
  for i in range(len(temp3)):
    sum += abs(temp3[i])
  
  if sum == 0:
    lin_dep = True
  else:
    lin_dep = False

  return lin_dep


# Create placeholder matrix
A = [[0,0,0],[0,0,0],[0,0,0]]
end = False

# Input values one at a time into matrix
for i in range(3):
  for j in range(3):
    A[i][j] = int(input("Enter values for a 3x3 matrix, \
one entry at a time: "))
print("\nYour matrix: ") 
print("([",A[0][0]," ",A[0][1]," ",A[0][2],"]")
print(" [",A[1][0]," ",A[1][1]," ",A[1][2],"]")
print(" [",A[2][0]," ",A[2][1]," ",A[2][2],"])")
print()

a = A[0][0] 
b = A[0][1] 
c = A[0][2]
d = A[1][0] 
e = A[1][1] 
f = A[1][2] 
g = A[2][0]
h = A[2][1]
i = A[2][2]

# Calculate determinant for use later
det = (a * det_2x2([e,f,h,i])) - (b * det_2x2([d,f,g,i])) 
det += (c * det_2x2([d,e,g,h]))

# Check if matrix is the zero matrix. If so, rank = 0.
sum = 0
for i in range(3):
  for j in range(3):
    sum += abs(A[i][j])
if sum == 0: 
  print("The rank of your matrix is 0.")
  end = True

# Check the determinant of the matrix. If it is nonzero, this means the matrix
# is invertible and its rank is automatically n (3).
if end == False:
  if det != 0:
    print("The rank of your matrix is 3.")
    end = True

# Check linear dependence between rows to find rank 
if end == False: 
  if check_lin_dep(A[0], A[1]) == True:
    if check_lin_dep(A[0], A[2]) == True:
      print("The rank of your matrix is 1.")
    else: 
      print("The rank of your matrix is 2.")
  else: 
    if check_lin_dep(A[0], A[2]) == True:
      print("The rank of your matrix is 2.")
    else:
      print("The rank of your matrix is 2.")
