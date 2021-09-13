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

![Image](http://www.sciweavers.org/upload/Tex2Img_1631528530/render.png)

**Data input:**

* We allow for 2-dimensional Euclidean data

* CSV files must list one pair of coordinates x,y on each row, with no header row

* CSV files must have extension ".txt" and be in the same directory

**Python Implementation:**

* To run (custom data set): python main.py filename z m
