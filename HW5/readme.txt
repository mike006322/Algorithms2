Traveling Salesman problem

tsp_v1.py is correct but with 25 points it takes a long time to complete (>1 hour) and uses a lot of memory (>30 gigs). 

tsp_v2 is optimized and can run with 25 points using about 500 mb memory and ~ 30 mins of compute time.

Optimizations include:
- cached distance calculations
- representations of subsets as numbers in n-digit binary where 1 means the subset contains the element in the n-th position and 0 means it doesn't contains

Alternatively I could have shortened the number of points by identifying clusters and assuming that they must connect to each other. 
In that case I would delete a member of the cluster and leave a cluster representative. 
Then I would customize the distance formula to detect if the input is a cluster representative in which case the output of the distance formula 
would be the distance to the deleted point or the sum of the distance to the representative and the distance from the representative to the delted point. 