#Calculate pdf and cdf by using scipy 
from scipy.stats import norm

print(norm.rvs(loc=0,scale=1,size=20))

#cdf of 10 random variables
print(norm.cdf(10,loc=1,scale=3))

#pdf of 14 random variables
print(norm.pdf(14,loc=1,scale=1))

