# CMPS 6610 Problem Set 02

**Name:** Keith J. Mitchell

In this assignment we'll work on applying the methods we've learned to
analyze recurrences, and also see their behavior in practice. As with
previous assignments, some of of your answers will go in
`main.py`. Please add your written answers to `answers.md` which you can convert
to a PDF using `convert.sh`. Alternatively, you may scan and upload written answers
to a file named `answers.pdf`. 


1. Prove that $\log n! \in \Theta(n \log n).$

This can be proven using the brick method to bound sums of $\log n!$. As seen below:

$$\log n! = \log 1 + \log 2 + \log 3 + \ldots + \log n$$

This is equal to:
$$\sum_{i=1}^{n} \log i$$

Using that logic, we can approximate the sum $\sum_{i=1}^{n} \log i$ using inequalities and direct bounds.

Using the fact that for $k \geq 1$:
$$\log k! \geq k \log k - k$$

This gives us:
$$\log n! \geq n \log n - n$$

Since $n \log n$ grows faster than $n$, we have:
$$\log n! \geq n \log n - n = \Omega(n \log n)$$

This satisfies the lower bound, now to solve for the upper bound. This can be satisfied by the fact that every term in the sum is at most $\log n$:

$$\log n! = \sum_{i=1}^{n} \log i \leq \sum_{i=1}^{n} \log n = n \log n$$

Therefore: $\log n! \leq O(n \log n)$

From these direct bounds, it can be seen that:
- The lower bound: $\log n! \geq \Omega(n \log n)$
- The upper bound: $\log n! \leq O(n \log n)$

Therefore: $\log n! \in \Theta(n \log n)$ is proven true

---
 
2. Derive asymptotic upper bounds for each recurrence below, using a
   method of your choice.

This can be done by using the brick method to expand the recurrence relations level by level. Then just sum up all levels to get the total cost.
   
### $T(n)=2T(n/6)+1$

**Expansion:**
- Level 0: $T(n) = 2T(n/6) + 1$
- Level 1: $T(n) = 2[2T(n/36) + 1] + 2 = 4T(n/36) + 3$
- Level 2: $T(n) = 4[2T(n/216) + 3] + 4 = 8T(n/216) + 7$
- Level $k$: $T(n) = 2^k T(n/6^k) + (2^k - 1)$

This means that at any level $k$, we have $2^k$ subproblems of size $n/6^k$. The base case is reached when $n/6^k = 1$, so $k = \log_6 n$. The total cost is then : $\sum_{i=0}^{\log_6 n - 1} 2^i + 2^{\log_6 n} \cdot T(1)$. This results in $T(n) = O(n^{\log_6 2})$. Which can be simplified down to $T(n) = O(n^{0.387})$

### $T(n)=6T(n/4)+n$

**Expansion:**
- Level 0: $T(n) = 6T(n/4) + n$
- Level 1: $T(n) = 6[6T(n/16) + n/4] + n = 36T(n/16) + 6n/4 + n = 36T(n/16) + 2.5n$
- Level 2: $T(n) = 36[6T(n/64) + n/16] + 2.5n = 216T(n/64) + 36n/16 + 2.5n = 216T(n/64) + 4.75n$
- Level $k$: $T(n) = 6^k T(n/4^k) + n \sum_{i=0}^{k-1} (6/4)^i$

This means that at any level $k$, we have $6^k$ subproblems of size $n/4^k$. The base case is reached when $n/4^k = 1$, so $k = \log_4 n$. Since $6/4 = 1.5 > 1$, the geometric series is dominated by its last term. The total cost is: $O(n^{\log_4 6})$. This results in $T(n) = O(n^{1.29})$.

### $T(n)=7T(n/7)+n$

**Expansion:**
- Level 0: $T(n) = 7T(n/7) + n$
- Level 1: $T(n) = 7[7T(n/49) + n/7] + n = 49T(n/49) + n + n = 49T(n/49) + 2n$
- Level 2: $T(n) = 49[7T(n/343) + n/49] + 2n = 343T(n/343) + n + 2n = 343T(n/343) + 3n$
- Level $k$: $T(n) = 7^k T(n/7^k) + (k+1)n$

This means that at any level $k$, we have $7^k$ subproblems of size $n/7^k$. The base case is reached when $n/7^k = 1$, so $k = \log_7 n$. Each level contributes exactly $n$ to the total cost. The total cost is: $7^{\log_7 n} \cdot T(1) + n \log_7 n = n \cdot T(1) + n \log_7 n$. This results in $T(n) = O(n \log n)$.

### $T(n)=9T(n/4)+n^2$

**Expansion:**
- Level 0: $T(n) = 9T(n/4) + n^2$
- Level 1: $T(n) = 9[9T(n/16) + (n/4)^2] + n^2 = 81T(n/16) + 9n^2/16 + n^2 = 81T(n/16) + 1.5625n^2$
- Level 2: $T(n) = 81[9T(n/64) + (n/16)^2] + 1.5625n^2 = 729T(n/64) + 81n^2/256 + 1.5625n^2 ≈ 729T(n/64) + 1.879n^2$
- Level $k$: $T(n) = 9^k T(n/4^k) + n^2 \sum_{i=0}^{k-1} (9/16)^i$

This means that at any level $k$, we have $9^k$ subproblems of size $n/4^k$. The base case is reached when $n/4^k = 1$, so $k = \log_4 n$. Since $9/16 < 1$, the geometric series is dominated by its first term. The total cost is: $9^{\log_4 n} \cdot T(1) + n^2 \cdot \frac{1}{1 - 9/16}$. This results in $T(n) = O(n^2)$.

### $T(n)=4T(n/2)+n^3$

**Expansion:**
- Level 0: $T(n) = 4T(n/2) + n^3$
- Level 1: $T(n) = 4[4T(n/4) + (n/2)^3] + n^3 = 16T(n/4) + 4n^3/8 + n^3 = 16T(n/4) + 1.5n^3$
- Level 2: $T(n) = 16[4T(n/8) + (n/4)^3] + 1.5n^3 = 64T(n/8) + 16n^3/64 + 1.5n^3 = 64T(n/8) + 1.75n^3$
- Level $k$: $T(n) = 4^k T(n/2^k) + n^3 \sum_{i=0}^{k-1} (4/8)^i = 4^k T(n/2^k) + n^3 \sum_{i=0}^{k-1} (1/2)^i$

This means that at any level $k$, we have $4^k$ subproblems of size $n/2^k$. The base case is reached when $n/2^k = 1$, so $k = \log_2 n$. Since $1/2 < 1$, the geometric series is dominated by its first term. The total cost is: $n^2 \cdot T(1) + 2n^3$. This results in $T(n) = O(n^3)$.

### $T(n)=49T(n/25)+n^{3/2}\log n$

**Expansion:**
- Level 0: $T(n) = 49T(n/25) + n^{3/2}\log n$
- Level 1: $T(n) = 49[49T(n/625) + (n/25)^{3/2}\log(n/25)] + n^{3/2}\log n$
- Level $k$: $T(n) = 49^k T(n/25^k) + n^{3/2} \sum_{i=0}^{k-1} (49/25^{3/2})^i \cdot \log(n/25^i)$

This means that at any level $k$, we have $49^k$ subproblems of size $n/25^k$. The base case is reached when $n/25^k = 1$, so $k = \log_{25} n$. The logarithmic terms don't change the asymptotic behavior significantly. This results in $T(n) = O(n^{3/2}\log n)$.

### $T(n)=T(n-1)+2$

**Expansion:**
- Level 0: $T(n) = T(n-1) + 2$
- Level 1: $T(n) = [T(n-2) + 2] + 2 = T(n-2) + 4$
- Level 2: $T(n) = [T(n-3) + 2] + 4 = T(n-3) + 6$
- Level $k$: $T(n) = T(n-k) + 2k$

This means that at any level $k$, we have 1 subproblem of size $n-k$. The base case is reached when $n-k = 1$, so $k = n-1$. The total cost is: $T(1) + 2(n-1) = T(1) + 2n - 2$. This results in $T(n) = O(n)$.

### $T(n)= T(n-1)+n^c$, with $c\geq 1$

**Expansion:**
- Level 0: $T(n) = T(n-1) + n^c$
- Level 1: $T(n) = [T(n-2) + (n-1)^c] + n^c = T(n-2) + (n-1)^c + n^c$
- Level 2: $T(n) = [T(n-3) + (n-2)^c] + (n-1)^c + n^c = T(n-3) + (n-2)^c + (n-1)^c + n^c$
- Level $k$: $T(n) = T(n-k) + \sum_{i=0}^{k-1} (n-i)^c$

This means that at any level $k$, we have 1 subproblem of size $n-k$. The base case is reached when $n-k = 1$, so $k = n-1$. The total cost is: $T(1) + \sum_{i=1}^{n} i^c$. Since $\sum_{i=1}^{n} i^c = \Theta(n^{c+1})$, this results in $T(n) = O(n^{c+1})$.

### $T(n)=T(\sqrt{n})+1$

**Expansion:**
- Level 0: $T(n) = T(\sqrt{n}) + 1 = T(n^{1/2}) + 1$
- Level 1: $T(n) = [T((n^{1/2})^{1/2}) + 1] + 1 = T(n^{1/4}) + 2$
- Level 2: $T(n) = [T((n^{1/4})^{1/2}) + 2] + 1 = T(n^{1/8}) + 3$
- Level $k$: $T(n) = T(n^{1/2^k}) + k$

This means that at any level $k$, we have 1 subproblem of size $n^{1/2^k}$. The base case is reached when $n^{1/2^k} = 2$ (or some constant), which gives us $1/2^k = \log_n 2$, so $2^k = \log n / \log 2 = \log n$, and therefore $k = \log \log n$. The total cost is: $T(2) + \log \log n$. This results in $T(n) = O(\log \log n)$.



3. Suppose that for a given task you are choosing between the following three algorithms:

	* Algorithm $\mathcal{A}$ solves problems by dividing them into
      two subproblems of one fifth of the input size, recursively
      solving each subproblem, and then combining the solutions in quadratic time.
	  
	* Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively one subproblems of size $n-1$ and then
      combining the solutions in logarithmic time.
		
	* Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into a subproblems of size $n/3$ and a subproblem of size
      $2n/3$, recursively solving each subproblem, and then combining
      the solutions in $O(n^{1.1})$ time.

    What is the work and span of these algorithms? For the span, just
    assume that it is the same as the work to combine solutions
    (i.e. the non-recursive quantity).
    Which algorithm would you choose? Why?

- Algorithm $\mathcal{A}$ has a recurrence of $T(n) = 2T(n/5) + O(n^2)$. This would mean level 0 is of size $n$ where work = $n^2$. Level 1 is 2 problems of size $n/5$ where work = $2 \cdot (n/5)^2 = 2n^2/25$. This would continue to be dominated by the first term leading to work being $O(n^2)$ and the span is $O(n^2)$.
- Algorithm $\mathcal{B}$ has a recurrence of $T(n) = T(n-1) + O(\log n)$. Level 0 of the recursion tree is 1 problem of size $n$ where work = $\log n$. Level 1 is 1 problem of size $n-1$, work = $\log(n-1)$. This would lead to the work being $O(n \log n)$ and the span also being $O(n \log n)$.
- Algorithm $\mathcal{C}$ has a recurrence of $T(n) = T(n/3) + T(2n/3) + O(n^{1.1})$. Level 0 for this is 1 problem of size $n$ where work = $n^{1.1}$. Level 1 would be 2 problems of sizes $n/3$ and $2n/3$ with work = $(n/3)^{1.1} + (2n/3)^{1.1} \approx 0.613n^{1.1}$. Since this decreases, the work would be $O(n^{1.1} \log n)$ and span = $O(n^{1.1})$.

- Algorithm $\mathcal{B}$ with its $O(n \log n)$ work complexity is the best choice for most scenarios, offering the best overall time complexity despite having no parallelization benefits.

4. Suppose that for a given task you are choosing between the following three algorithms:

	* Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
	  
	* Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
		
	* Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What is the work and span of these algorithms? For the span, just
    assume that it is the same as the work to combine solutions (i.e.,
    the non-recursive quantity). Which algorithm would you choose? Why?

- Algorithm $\mathcal{A}$ has a recurrence of $T(n) = 5T(n/2) + O(n)$. Level 0 would be 1 problem of size $n$ where work = $n$. Level 1 is then 5 problems of size $n/2$ with work = $5n/2$. This leads to work being $O(n^{\log_2 5})$ OR $O(n^{2.32})$ and span being $O(n)$.
- Algorithm $\mathcal{B}$ has a recurrence of $T(n) = 2T(n-1) + O(1)$. Level 0 is 1 problem of size $n$ where work = $1$. Level 1 is 2 problems of size $n-1$ where work = $2$. This continues with work being $O(2^n)$ and span being $O(1)$.
- Algorithm $\mathcal{C}$ has a recurrence of $T(n) = 9T(n/3) + O(n^2)$. Level 0 is 1 problem of size $n$ with work = $n^2$. Level 1 is 9 problems of size $n/3$ with work = $n^2$. Work would then be $O(n^2 \log n)$ and span would be $O(n^2)$. 
- Algorithm $\mathcal{C}$ is the best option as it has $O(n^2 \log n)$ work, offering polynomial rather than exponential growth.


5. In Module 2 we discussed two algorithms for integer multiplication. The first algorithm was simply a recapitulation of the "grade school"
  algorithm for integer multiplication, while the second was the
  Karatsaba-Ofman algorithm. For this problem, you will use the stub
  functions in `main.py` to implement these two algorithms for integer
  multiplication. Once you've correctly implemented them, test the
  empirical running times across a variety of inputs to test whether
  your code scales in the manner predicted by our analyses of the
  asymptotic work.


6. A "white hat" conducts hacking activities for the common good, while a
"black hat" hacker does so for nefarious reasons. Let's consider a
computer security class with $n$ students who are all either white hat
or black hat hackers. You're the instructor, and you don't know who is
a white hat or a black hat, but all of the student do. 

Your goal is to identify the white hats and you're allowed to ask a
pair of students about one another. White hats will always tell the
truth, but you cannot trust a black hat's response. For a pair of students $A$ and
$B$ then there are several possible outcomes:


|$A$ says | $B$ says | Conclusion |
|---------|----------|------------|
|$B$ is a white hat | $A$ is a white hat | both are good, or both are bad |
|$B$ is a white hat | $A$ is a black hat | at least one is bad |
|$B$ is a black hat | $A$ is a white hat | at least one is bad |
|$B$ is a black hat | $A$ is a black hat | at least one is bad |

*6a.* Show that if more than $n/2$ students are black hats, you cannot determine which students are white hats based on a pairwise test. Note that you must assume the black hats are conspiring to fool you.

- If black hats are more than half the class, it is impossible to identify the white hats. Since black hats lie and can coordinate, they can always produce answers that are consistent with multiple possible assignments of who is white or black. This makes it impossible for the instructor to determine the true identities.

*6b.* Consider the problem of finding a single white hat, assuming strictly more than $n/2$ of the students are white hats. Show that $n/2$ pairwise interviews is enough to reduce the problem size by a constant fraction. 

- If white hats are in the majority, pairing students and asking them about each other allows progress. Only a white–white pair will both say the other is white, so keeping one student from such pairs and discarding all others reduces the problem size by a constant fraction. This step requires only about $n/2$ interviews.

*6c.* Using the above show that all white hats can be identified using $\Theta(n)$ pairwise interviews.

- Repeating the reduction shrinks the group geometrically, and after a few rounds a single white hat can be identified. Once one white hat is known, their truthful answers can be used to test all remaining students. Since each round uses at most linear work and the costs form a geometric series, all white hats can be identified in $\Theta(n)$ pairwise interviews.