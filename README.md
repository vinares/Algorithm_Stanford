
# Algorithm_Stanford

+ Algorithm specialization
+ provided by Tim Roughgarden, Stanford Univ, on Coursera
+ https://www.coursera.org/specializations/algorithms

## Chpater 1	Divide and Conquer, Sorting and Searching, and Randomized Algorithms

### week1

#### Introduction

+ Integer Multiplication

	+ **'primitive operations'** : add or multiply 2 single-digit numbers
	+ **3rd-grade multiplication**
		*  $\#operations \leq constant * n^2$ 
	+ **karatsuba multiplication**
		*  $\#operations \leq constant * n^2$
	+ **base case**: a condition when algorithm cannot recurse
	
+ Merge Sort

	+ runing time
		* $\#operations per recursion \leq 4m + 2 \leq 6m$
		* $\#operations \leq 6nlogn + 6n$
		
+ Guiding Principles for Analysis of Algorithms

	+ **'worst-case analysis'**
		* general-purpose, easier to calculate
		* instead of 'average-case' or benchmarks, which requires domain knowledge
	+ **won't pay much attention to constant and lower-order terms**
		* way much easier
		* constants depend on architecture/compiler/language
		* lose very little predicative power
	+ **asympototic analysis**
		* only big problems are interesting
		* when scale becomes small, we can shift to other algorithm
		* **'sweet spot'**: mathmetical tractability & predicative power

#### Asymptotic Analysis

+ **Big-O**		
	* $T(n) = O(f(n))$
	* $\exists c, n_0 > 0, \forall n \geq n_0,  s.t. T(n) \leq c \times f(n)$
	* $T(n)$ is upper bounded by $c \times f(n)$
+ **Big-Omega**
	* $T(n) = \Omega(f(n))$
	* $\exists c, n_0 > 0,  \forall n \geq n_0,  s.t. T(n) \geq c \times f(n)$
	* $T(n)$ is lower bounded by $c \times f(n)$
+ **Big-Theta**
	* $T(n) = \Theta(f(n))$
	* $\exists c_1, c_2 , n_0 > 0,  \forall n \geq n_0,  s.t. c_1 \times f(n) \leq T(n) \leq c_2 \times f(n)$
	* $T(n)$ is sandwiched by $c_1 \times f(n)$ and 	 $c_2 \times f(n)$
+ **Little-O**
	* $T(n) = o(f(n))$
	* $\exists n_0 > 0, s.t. \forall c >0, \forall n > n_0,  T(n) \leq c \times f(n)$
	* $T(n)$ is eventually upper bounded by $c \times f(n)$, no matter how c is close to zero
