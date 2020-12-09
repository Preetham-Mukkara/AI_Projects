# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Author:- Preetham Mukkara
Class:- CS 540 in Spring 2020
Name of file:- ten_hundred.py

"""
import numpy as np
from scipy.spatial.distance import pdist,squareform
import math
import csv

def load_data(filepath):
    data = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row.pop("Long")
            row.pop("Lat")
            data.append(dict(row))
    return data

def calculate_x_y(time_series):
    temp = list(time_series.values())
    del temp[0]
    del temp[0]
    temp = list(map(lambda x: int(x),temp)) 
    n = len(temp)
    x = 0
    y = 0
    z = n - 1
    index1 = 0
    index2 = 0
    
    
    if temp[z] <= 0:
        x = math.nan
        y = math.nan
        return (x,y)
    
    for i in range(n):
        if temp[i] <= (temp[z]/10) and i == z :
            index1 = i
            break
        elif temp[i] <= (temp[z]/10) and temp[i+1] > (temp[z]/10):
            index1 = i
            break
             
    for j in range(n):
        if temp[j] <= (temp[z]/100) and j == z :
            index2 = j
            break
        elif temp[j] <= (temp[z]/100) and temp[j+1] > (temp[z]/100):
            index2 = j
            break    
    
    if index2 == 0 and temp[z]/100 < temp[index2]:
        y = math.nan
    else:
        y = index1 - index2
        
    x = z - index1    
    return (x,y)

def hac(dataset):
     # dataset in mxn array
     # m is number of regions ,n is x and y features
     temp = []
     for x in range(len(dataset)):
         if not((math.isnan(dataset[x][0])) or (math.isnan(dataset[x][1]))):
                   temp.append(dataset[x])      
     # dataset has filtered out NaN values
     dataset = temp
     # number of clusters possible
     numClusters = len(dataset)-1
     # numPy array to be returned
     Z = [[0]*4]*(len(dataset)-1) 
     # distance matrix based on given datapoints
     matrix = squareform(pdist(dataset))
     # array for storing cluster index values
     index = [[]]*len(dataset)
     # initializing cluster index array
     for i in range(len(index)):
         index[i] = i
     # traverses distnace matrix until number of clusters is singular
     while numClusters > 1 :
         # sets min value to infinity 
         minimum = math.inf
         # counter for number of cluster points
         counter = 0
         # list to cross check clustering
         check = []
         idx = len(dataset)-1-numClusters
         for i in range(len(matrix)):
             for j in range(len(matrix)):
                 # finds minimum 
                 if (matrix[i][j] < minimum) and (i != j):
                     minimum = matrix[i][j]
                     t1 = i
                     t2 = j
                 # tie breaking algorithm
                 if matrix[i][j] == minimum and (i != j):
                     if index[t1] > index[i]:
                         minimum = matrix[i][j]
                         t1 = i
                         t2 = j 
         # set Z[i, 0] and  Z[i,1] accordingly                
         if index[t1] < index[t2]:
             Z[idx][0] = index[t1]
             Z[idx][1] = index[t2]
         if index[t2] < index[t1]:
             Z[idx][0] = index[t2]
             Z[idx][1] = index[t1]
         # set minimum as Z[i,2]    
         Z[idx][2] =  minimum
         # set values such that won't get caught as minimum again
         matrix[t1][t2] = math.inf
         matrix[t2][t1] = math.inf
         # update cluster index values
         index[t1] =  len(dataset) + idx  
         index[t2] =  len(dataset) + idx
         # update check list
         for i in range(len(matrix)):
             if matrix[t1][i] == math.inf:
                 check.append(i)
         for i in range(len(matrix[0])):
             if matrix[i][t2] == math.inf:
                 check.append(i)
         # filter duplicate values from check list        
         check = list(set(check))
         # does necessary corrections according to check list
         for i in range(len(check)):
             if (matrix[t1][check[i]] != math.inf) or (matrix[check[i]][t1] != math.inf):
                 matrix[t1][check[i]] = math.inf
                 matrix[check[i]][t1] = math.inf
             if (matrix[check[i]][t2] != math.inf) or (matrix[t2][check[i]] != math.inf):
                 matrix[t2][check[i]] = math.inf
                 matrix[check[i]][t2] = math.inf  
         # checks for number of cluster points        
         for i in range(len(matrix)):
             if matrix[t1][i] == math.inf:
                 counter = counter + 1
         # sets Z[i,3] as number of cluster points
         Z[idx][3] =  counter  
         # updates numClusters
         numClusters = numClusters - 1 
         # converts to numPy array
         Z = np.array(Z)
     return Z

