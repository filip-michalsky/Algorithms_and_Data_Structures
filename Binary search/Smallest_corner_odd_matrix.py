# -*- coding: utf-8 -*-
"""
Let a two-dimensional array of integers be corner-odd if the values in the four corners of the array
sum to an odd number. We want you to write efficient code to find the smallest corner-odd subarray
(i.e. contains the fewest elements) contained in an input array that is also corner-odd.

@author: Filip Michalsky
"""
def test_corner_odd(my_array,r):
    (px, py), (qx, qy) = r
    sum_corners=my_array[px][py]+my_array[px][qy]+my_array[qx][py]+my_array[qx][qy]
    ##order of corners##
    #beginning
    #top right corner
    #bottom left corner
    #bottom right corner
    #print(sum_corners)
    if sum_corners%2 !=0:
        return True
    else:
        return False
    
def smallest_corner_odd(A, r = None):
    '''
    Input: 2D array A, subarray indices ((px, py), (qx, qy))
    Output: a smallest corner-odd subarray if the input
        subarray is corner-odd, else return None.
        Your output should be a tuple of tuples
        representing the indices of the upper left
        and lower right corners of the subarray.
    '''
   
 
    
    m,n = len(A), len(A[0]) #len(A[0] is number of columns! len(A) is a number of rows!!)
    
    if r is None:
        r = ((0, 0), (m - 1, n - 1))
    (px, py), (qx, qy) = r # (upper left), (lower right)
    #print("Initial r")
    #print(r)
    #print("px and py")
    #print(px,py)
    #print("qx and qy")
    #print(qx,qy)
    
    if test_corner_odd(A,r)==False:
        return None
    else:
        if qx-px==1 and qy-py==1:
            #print("We are finished!",r)
            r=(py, px), (qy, qx)

        else:
            if qx-px==1 and qy-py>=1: #rows and columns

                r=((px,py),(qx,int(round((py+qy)/2)))) #cutting number of columns in half

                if test_corner_odd(A,r) == True: #tests the first half is even

                    r=smallest_corner_odd(A,r)
                else:
                    r=((px,int(round((py+qy)/2))),(qx,qy)) #switched to the lower half

                    r=smallest_corner_odd(A,r)
                    
            else: #start cutting horizontally, does not need to modify the array, just the index!
                r=((px,py),(int(round((px+qx)/2)),qy)) #add first and last index and divide by 2

                if test_corner_odd(A,r) == True: #tests the first half is even

                    r= smallest_corner_odd(A,r)
                else:
                    r=((int(round((px+qx)/2)),py),(qx,qy)) #switched to the lower half

                    r = smallest_corner_odd(A,r)
                    
    return r
    ##################
    return None

##################
# Test your code #
##################
def parse_2D_int_array(s):
    return [[int(v) for v in line.split()] for line in s.split('\n')[:-1]]

def test():
    with open('cases/1.in', 'r') as f:
        A = parse_2D_int_array(f.read())
        print("Case 1")
        print(smallest_corner_odd(A),"\n")
        # [[4, 2], [5, 3]] would be a correct output for test case 1.in
    
    with open('cases/2.in', 'r') as f:
        A = parse_2D_int_array(f.read())
        print("Case 2")
        print(smallest_corner_odd(A))
        # --None-- would be a correct output for test case 2.in
    
if __name__ == '__main__':
    test()


