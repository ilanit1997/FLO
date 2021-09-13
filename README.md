# FLO
Solve Facility location with m outliers, using IP (integer programming)

**Taken from ke-chen thesis (https://sarielhp.org/p/others/ke/kechen_phd_thesis.pdf):**

Let FLO(z, P, m) be an instance of facility location with m outliers, consisting of a parameter z ≥ 0, a set P of points, and an integer m ≥ 0.
The objective of FLO(z, P, m) is to compute a set C ⊆ P minimizing the cost Am(C, P) + z |C|. Let
OPTflo(z, P, m) denote the cost of the optimal solution.

The input to the algorithm is a set P of n points, a set F of facilities (we assume that F = P here),
the cost z for opening a facility, and the parameter m. 
There is a natural integer program (IP) for this problem. The IP has binary variables :
<img src="http://www.sciweavers.org/tex2img.php?eq=y_f%2C%20x_%7Bvf%7D%2C%20o_v&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="y_f, x_{vf}, o_v" width="83" height="18" />, where y indicate if facility f is open, x indiciated if client v is served by facility f, o indicates if v is outlier or not.

In addition, any client is either served by some facility, or it is considered to be an outlier. Finally, the total number of outliers cannot exceed m. In particular, the optimal solution for the IP with this objective function is the optimal solution for FLO.

**The LP relaxation of this IP is:**

<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cmin%20%5Csum_%7Bv%2Cf%7D%20d%28v%2C%20f%29%20%C2%B7%20x_%7Bvf%7D%20%2B%20z%20%5Csum_%7Bf%7D%20y_f%20s.t%20%5C%5C%0A%5Cforall%20v%20%5Cin%20P%2C%20f%20%5Cin%20F%3A%20y_%7Bf%7D%20%5Cge%20%20x_%7Bvf%7D%20%20%5C%5C%0A%5Cforall%20v%20%5Cin%20P%3A%20%5Csum_%7Bf%7D%20x_%7Bvf%7D%20%2B%20o_v%20%5Cge%201%20%5C%5C%20-%5Csum_%7Bv%7D%20o_v%20%5Cge%20-%20m%5C%5C%0A%5Cforall%20v%20%5Cin%20P%2C%20f%20%5Cin%20F%3A%20x_%7Bvf%7D%20%2C%20y_f%20%2C%20o_v%20%5Cge%200&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\min \sum_{v,f} d(v, f) · x_{vf} + z \sum_{f} y_f s.t \\\forall v \in P, f \in F: y_{f} \ge  x_{vf}  \\\forall v \in P: \sum_{f} x_{vf} + o_v \ge 1 \\ -\sum_{v} o_v \ge - m\\\forall v \in P, f \in F: x_{vf} , y_f , o_v \ge 0" width="240" height="181" />


**Data input:**

* We allow for 2-dimensional Euclidean data

* CSV files must list one pair of coordinates x,y on each row, with no header row

* CSV files must have extension ".txt" and be in the same directory

