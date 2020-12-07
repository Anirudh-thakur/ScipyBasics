# https://lms.simplilearn.com/courses/3814/PG-DS---Data-Science-with-Python/syllabus
import numpy as np
from scipy import linalg

"""equation: 
x + y = 30
4x + 9y = 150
"""
Variables = np.array([[1,1],[4,9]])
Values = np.array([30,150])

print(linalg.solve(Variables,Values))
