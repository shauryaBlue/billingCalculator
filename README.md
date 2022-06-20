# Billing Calculator

Implement a bill calculator provided the number of units consumed and the slab information.


## Example Slabs

```
1 to 100 units charged at Rs.1 per unit
101 to 200 units charged at Rs.2 per unit
201 to 300 units charged at Rs.3 per unit
300 and above unit charged at Rs5 per unit
 
Sample bill calculation formula for an input of 250 units
(100 units * Rs.1) + (100 units * Rs.2) + (50 units * Rs.3) = Rs.450
```

## How to Run

Enter values in billingInput with format: lowest unit value, highest unit value, slab cost per unit  
For highest slab, mention -1 as highest unit value  
  
Use last line to input total number of units  
  
  
Ensure that billingInput.txt is in the same folder as billingCalculator.py  
Use python3 to run billingCalculator.py  

```
Example 1: 
1, 100, 1
101, 200, 2
201, 300, 3
300, -1, 5
Total Units: 250

Expected Soln 1:
(100 units * Rs.1) + (100 units * Rs.2) + (50 units * Rs.3) = Rs.450
```

```
Example 2: 
1, 100, 10
101, 200, 15
201, 300, 20
300, -1, 25
Total Units: 250

Expected Soln 2:
(100 units * Rs.10) + (100 units * Rs.15) + (50 units * Rs.20) = Rs.3500
```

```
Example 3: 
1, 100, 10
101, 200, 15
201, 300, 20
300, -1, 25
Total Units: 95

Expected Soln 2:
(95 units * Rs.10) = Rs.950
```