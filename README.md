# samcodes08/ALGO
# ALGO :
____________________________________________________________________________________________________________________________________________________________________
#Algorithm:

1.Ask user 3 unique questions from question set randomly.

2.The system assigns a minimum of 1 to maximum of 3
numbers ranging from 0-9 and symbols.

3.By taking answers from question as input ,system will randomly pick up answers and arrange them by considering step 2.

4.Additionally the password is also hashed using SHA 256.
(Complexity :O(n))
________________________________________________________________________________________________________________________________________________________________
Cracking the password using Brute force method

let the first answer be A1.
let the first answer be A2.
let the first answer be A3.
 
Since there are 10 numbers(0 to 9) there are 10 probable chances.
 
Since there are 8 symbols there are 8 probable chances.
 
Since there 52 letters including small letters and capital letters since our system is not case sensitive.There are 52 probable chances since each letters is considered  unique and repetitions are allowed.
 
 
By doing  permutations:
 
A1 A2 A3 N1 N2 P1
 
(52)A1  x  (52)A2  x  (52)A3  x  10  x  10  x  8
![image](https://user-images.githubusercontent.com/96153900/146282916-7c010225-5d8f-4ed8-a029-a8d0cc620047.png)

