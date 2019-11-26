"""
Consider the experiment of throwing a die n times, 
and let X_k = "score in the k-th trow".
Then the sequence of RVs X_1, X_2, ... is IID, 
each with a given probability distribution, 
with common mean mu and variance sigma^2.
(For example, P(X=k) = 1/6 for k=1,...,6 if the die is fair.)

By the CLT, the sample sum S_n := X_1+...+X_n approximately 
follows a normal distribution with mean n\mu and variance 
n\sigma^2.

This program computes the pmf of S_n exactly using the convolution 
formula, and plots the distribution of S_n for different values of n."""

import matplotlib.pyplot as plt

n=10 # Number of throws of the die

# pmf of X="score in one throw".
probs = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

def pmf(n, k):
    """This function computes recursively the pmf of the RV
    S_n="sum of scores in n throws", computed exactly thanks to 
    convolution formula.
     
    Parameters:
        n=number of throws
        k=value at which to evaluate the pmf
     
    Return value:
        pmf(n,k) = P(S_n = k)."""
    if k<n or k>6*n:
        # In this case P(S_n=k) = 0 
        return 0    
    if n==1:
        # Just one die
        return probs[k-1]

    # More than one die. Use recursive convolution formula.
    s = 0
    for j in range(1,7):
        s += probs[j-1]*pmf(n-1, k-j)
    return s

scores = range(1, 6*n+1) # Possible values of S_n: [1,2, ..., 6n].

# Compute the pmf of S_n.
fun = []
for i in range(len(scores)):
    fun.append(pmf(n,scores[i]))

# Plot the pmf of S_n.
print(fun)
plt.bar(scores,fun)
plt.show()
