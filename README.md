
  
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
		*  $\\#operations \leq constant * n^2$ 
	+ **karatsuba multiplication**
		*  $\\#operations \leq constant * n^2$
	+ **base case**: a condition when algorithm cannot recurse
	
+ Merge Sort

	+ runing time
		* $\\#operations per recursion \leq 4m + 2 \leq 6m$
		* $\\#operations \leq 6nlogn + 6n$
		
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

### week2

#### Divide & Conquer Problem

+ **Counting Inversions**
	+ Count inversions while merge sorting
	+ If $left[i] > right[j]$, then  $(left[i::], right[j])$ are inversions
	+ Running time of subroutine: $O(n)$ 
	
+ **Matrix Multiplicaiton**
	+ **Straight-forward interative algorithm**
		+  $$z_{i,j}= \sum_{k=1}^{n}  x_{i,k} \times y_{k,j}$$
		+ Runing time: $O(n^3)$
	+ **Divide and Conquer**
		+ let $X =\left[ \begin{matrix} A & B\\ C & D \end{matrix} \right]$, $Y = \left[ \begin{matrix} E & F \\ G & H \end{matrix} \right]$, then 

		$X \cdot Y = \left[ \begin{matrix} A \cdot E + B \cdot G & A \cdot F + B \cdot H \\\\ C \cdot E + D \cdot G  & C \cdot F +D \cdot H \end{matrix} \right]$
		+ #Operations of subroutine: **8 multiplicaitons** + 4 additions
		+ Running time: $O(n^3)$
	
	+ **Strassen's Subcubic**
		+ $P_1 = A \cdot(F-H)$
		+ $P_2 = (A+B) \cdot H$
		+ $P_3 = (C+D) \cdot E$
		+ $P_4=D \cdot (G-E)$
		+ $P_5=(A +D) \cdot (E+H)$
		+ $P_6=(B-D) \cdot (G+H)$
		+ $P_7=(A-C) \cdot (E+F)$

		$X \cdot Y = \left[ \begin{matrix}  P_5 +P_4 - P_2 + P_6 & P_1 + P_2 \\\\ P_3+P4  & P_1+P_5-P_3-P_2 \end{matrix} \right]$
		+ #Operations of subroutine: **7 multiplications** + 18 additions
		+ Running time: $O(n^{2.81})$
+ **Closest Pairs**
	+ **Question:** find closest 2 points in a 2D points set
	+ **Brute-Force** : $O(n^2)$
	+ **Divide and Conquer:**
		1. **DIVIDE**
			+ $Q=$ left half of $P$, $R=$ right half of $P$
		2. **CONQUER**
			+ $(p_1,q_1)=Recurse(Q)$
			+ $(p_2,q_2)=Recurse(R)$
			+ $(p_3,q_3)=ClosestSplitPair(P)$
		3. **COMBINE**
			+ return $min \{ (p_1,q_1), (p_2,q_2), (p_3,q_3) \}$
		
		4. $ClosestSplitPair(P)$
			+ $\bar{x} = P[\frac{n}{2}]$, $\delta = minEuclideanDistance (Q,R)$
			+ $S_y = {(x,y)}$, where $(x,y) \in P$ and $x \in [\bar{x} - \delta, \bar{x} + \delta]$. Note that $S_y$ is sorted according to $y$ coordinate.
			+ Compare $S_y[i]$ with $S_y[i+1:i+7]$, return closest pair
		5. Running time: $O(n \cdot \log{n})$

#### The Master Method
+ **Master Theorom**
	+ Base case: $T(n) \leq$ a constant for all sufficiently small **n**
	+ $\forall$ larger n:
		+ $T(n) \leq a \cdot T(\frac{n}{b}) + O(n^d)$
		$a =$ #recursive calls
		$b=$ input size shrinking factor
		$d=$ exponent in running time of 'COMBINE' step
	+ $T(n)=\begin{cases} O(n^d \cdot \log{n}) & a=b^d \\\\ O(n^d) & a < b^d \\\\ O(n^{\log_b{a}}) & a > b^d \end{cases}$

+ **Proof**
	+ Recursion Tree
		+ input size n, $(\log_b{n} + 1)$ levels
		+ $j^{th}$ level: $a^j$ subproblems, each of size $\frac{n}{b^j}$
		+ work at level $j^{th} \leq a^j \cdot c \cdot (\frac{n}{b^j})^d=c \cdot n^d \cdot (\frac{a}{b^d})^j$
		+ total work $\ \ \ \ \ \ \ \ \leq c \cdot n^d \cdot \sum_{j = 0}^{\log_b{n}} (\frac{a}{b^d})^j$
	+ Understanding
		+ $a=$ rate of  subproblem proliferation(**RSP**)
		+ $b=$ rate of work shrinkage	(**RWS**)
		1. RSP = RWS$\rightarrow$ same amount of work at each level$\rightarrow O(n^d \cdot \log{n})$
		2. RSP <RWS$\rightarrow$ less work as goes deeper $\rightarrow$ most work at the root $\rightarrow O(n^d)$ 
		3. RSP>RWS$\rightarrow$ more work as goes deeper$\rightarrow$most work at the leaves$\rightarrow O(n^{\log_b{a}})$

### week3

#### Quicksort Algorithm

+  **2 Ways to Go**
	+	Extra memory: allocate $O(n)$ memory, use 1st element as pivot, smaller on left, larger on right, finally pivot.
	+ double pointers: exchange pivot with 1st element, swap on the original arrays.

+ **Choose a Good Pivot**
	+ $T(n)=\begin{cases} O(n^2) & smallest \ or \ largest \ elment \ as \ pivot \\\\ O(n\cdot logn) & median \ as \ pivot \ every \ time \end{cases}$
	+ **Random Pivot**
		+ $25\% - 75\%$ split is good enough for $O(n \cdot logn)$
#### Quicksort Analysis
+ A Decomposition Principle
	+ Master therom can't apply due to random size of subroutine
	+ Lemma: running time of Quicksort is dominated by number of comparisons
	+ $E[Comparisons] = \sum_{i = 1}^{n-1} \sum_{j=i+1}^{n} Pr(z_i, z_j \ get \ compared)$
+ The Key Insight
	+ $\forall i < j$, if pivot is $z_i$ or $z_j$, they get compared, otherwise, they don't.
	+ $Pr(z_i, z_j \ get \ compared) = \frac{2}{j-i+1}$
+ Running time
	+ $E[C] =\sum_{i = 1}^{n-1} \sum_{j=i+1}^{n} \frac{2}{j-i+1} \leq  \sum_{i = 1}^{n-1}  \sum_{k=2}^{n} \frac{1}{k} = 2 \cdot n \cdot \sum_{k=2}^{n} \frac{1}{k}$
	+ $\sum_{k=2}^{n} \frac{1}{k} \leq \int_2^n {\frac{1}{x}} \,{\rm d}x$
	+ $E[C] \leq 2 \cdot n \cdot \ln{n}$

### week3

#### Linear-Time Selection Algorithm
+ **Randomised Selection** 
	+ looking for *i*th smallest number in array
	+ $T(n) \leq T(\frac{n}{2}) + O(n)$
	+ $T(n) = O(n)$
+ **Deterministic Selection**
	+ 'median of medians'
	+ seprate array into n/5 groups, 5 element in each group, mergesort every group
	+ form a new array with medians of each group, and recurse the DS function to find its median. Use the median as partition pivot
	+ $T(n) = O(n)$
+ $O(n \cdot log n)$ is the lower bound of comparison-based sorting

#### Graphs and the Contraction Algorithm
+ **Minimum Cuts**
	+ for a connected undirected graph, allowed for parallel edges, find the cut with least crossing edges.
	+ Applications:
		+ **identify network weakness/bottleneck**: find the most efficient way to paralyse the enermy's transportation network
		+ **community detection in social networks**
		+ **image segmentation**
