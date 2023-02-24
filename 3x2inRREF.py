# Ellise Parnoff - 12/12/2022
# Check if 3x2 matrix is in RREF

# Create placeholder matrix
A = [[0,0],[0,0],[0,0]]
# True until proven false 
RREF = True

print("Enter a 3x2 matrix. I will tell you if it is in RREF or not!")
print()

# Input values one at a time into matrix
for i in range(3):
  for j in range(2):
    A[i][j] = int(input("Enter values for a 3x2 matrix, \
one entry at a time: "))

print("\nYour matrix: ")
print("([",A[0][0],"",A[0][1],"]")
print(" [",A[1][0],"",A[1][1],"]")
print(" [",A[2][0],"",A[2][1],"])\n")

# Brute force-- 

# Make sure all entries are 0 or 1 other than A[0][1]
for i in range(3):
  for j in range(2):
    if i != 0 or j != 1: 
      if (A[i][j] != 0) and (A[i][j] != 1):
        RREF = False  

# Bottom row must be all zeros 
if (A[2][0] != 0) or (A[2][1] != 0):                      
  RREF = False

# Middle row must be either [0 0] or [0 1]
if (A[1][0] or A[1][1]) != 0:                   
  if (A[1][0] != 0) or (A[1][1] != 1): 
    RREF = False
  else:
    if A[0][1] != 0:
      RREF = False

# First row must be [1 0], [0 0], or [1 n]
if (A[0][0] != 0) and (A[0][0] != 1):                    
  RREF = False

if A[0][1] != 0:
  if A[1][1] != 0:
    RREF = False 

# If first row is [0 0] the rest of the matrix must be zeros
if A[0][0] == 0 and A[0][1] == 0:
  if A[1][0] != 0:
    RREF = False
  elif A[1][1] != 0:
    RREF = False
  elif A[2][0] != 0:
    RREF = False
  elif A[2][1] != 0:
    RREF = False


if RREF == True:
  print("This matrix is in RREF.")
else:
  print("This matrix is not in RREF.")
