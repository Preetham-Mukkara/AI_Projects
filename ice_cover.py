#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:54:49 2020

@author: Preetham Mukkara
"""
import random
import math

def get_dataset():
    # cleaned dataset
    dataset = [[1855,118],[1856,151],[1857,121],[1858,96],[1859,110],[1860,117],[1861,132],[1862,104],[1863,125],[1864,118],[1865,125],[1866,123],[1867,110],[1868,127],[1869,131],[1870,99],
               [1871,126],[1872,144],[1873,136],[1874,126],[1875,91],[1876,130],[1877,62],[1878,112],[1879,99],[1880,161],[1881,78],[1882,124],[1883,119],[1884,124],[1885,128],[1886,131],[1887,113],[1888,88],[1889,75],[1890,111],
               [1891,97],[1892,112],[1893,101],[1894,101],[1895,91],[1896,110],[1897,100],[1898,130],[1899,111],[1900,107],[1901,105],[1902,89],[1903,126],[1904,108],[1905,97],[1906,94],[1907,83],[1908,106],[1909,98],[1910,101],
               [1911,108],[1912,99],[1913,88],[1914,115],[1915,102],[1916,116],[1917,115],[1918,82],[1919,110],[1920,81],[1921,96],[1922,125],[1923,104],[1924,105],[1925,124],[1926,103],[1927,106],[1928,96],[1929,107],[1930,98],
               [1931,65],[1932,115],[1933,91],[1934,94],[1935,101],[1936,121],[1937,105],[1938,97],[1939,105],[1940,96],[1941,82],[1942,116],[1943,114],[1944,92],[1945,98],[1946,101],[1947,104],[1948,96],[1949,109],[1950,122],
               [1951,114],[1952,81],[1953,85],[1954,92],[1955,114],[1956,111],[1957,95],[1958,126],[1959,105],[1960,108],[1961,117],[1962,112],[1963,113],[1964,120],[1965,65],[1966,98],[1967,91],[1968,108],[1969,113],[1970,110],
               [1971,105],[1972,97],[1973,105],[1974,107],[1975,88],[1976,115],[1977,123],[1978,118],[1979,99],[1980,93],[1981,96],[1982,54],[1983,111],[1984,85],[1985,107],[1986,89],[1987,87],[1988,97],[1989,93],[1990,88],
               [1991,99],[1992,108],[1993,94],[1994,74],[1995,119],[1996,102],[1997,47],[1998,82],[1999,53],[2000,115],[2001,21],[2002,89],[2003,80],[2004,101],[2005,95],[2006,66],[2007,106],[2008,97],[2009,87],[2010,109],
               [2011,57],[2012,87],[2013,117],[2014,91],[2015,62],[2016,65],[2017,94],[2018,86],[2019,70]]
    return dataset

def print_stats(dataset):
    data = dataset
    counter = len(data)
    mean = 0
    sd = 0
    print(counter)
    # for loop to calculate mean
    for i in range(counter):
        mean = mean + data[i][1]
    mean = mean/counter
    print("%.2f" % mean)
    # for loop to calculate standard deviation
    for i in range(counter):
        sd = sd + math.pow((mean - data[i][1]),2)    
    sd = sd/(counter - 1)
    sd = math.sqrt(sd)       
    print("%.2f" % sd)   

def regression(beta_0,beta_1):
    data = get_dataset()
    b0 = beta_0
    b1 = beta_1
    mse = 0
    n = len(data)
    # for loop to calculate mse
    for i in range(n):
        mse = mse + math.pow(b0+b1*data[i][0]-data[i][1],2)
    mse = mse/n
    return mse    

def gradient_descent(beta_0,beta_1):
    b0 = beta_0
    b1 = beta_1
    data = get_dataset()
    gd = []
    gd0 = 0
    gd1 = 0
    n = len(data)
    #for loop to calculate gradient descent
    for i in range(n):
        gd0 = gd0 + (b0+b1*data[i][0]-data[i][1])
    gd0 = (2*gd0)/n
    for i in range(n):
        gd1 = gd1 + data[i][0]*(b0+b1*data[i][0]-data[i][1])
    gd1 = (2*gd1)/n
    gd = ((gd0,gd1))
    return gd 

def iterate_gradient(T,eta):
    T = T
    eta = eta
    b0 = 0 #beta_0 at time t - 1
    bc0 = 0 #current beta_0
    b1 = 0 #beta_1 at time t - 1
    bc1 = 0 #current beta_1
    counter = 1 
    # while loop for iterating T times    
    while counter < T+1:
        bc0 = b0 - eta*(gradient_descent(b0,b1)[0])
        bc1 = b1 - eta*(gradient_descent(b0,b1)[1])
        b0 = bc0
        b1 = bc1
        print(counter, "%.2f" % bc0,"%.2f" % bc1,"%.2f" % regression(bc0,bc1))
        counter = counter + 1

def compute_betas():
    b0 = 0 
    b1 = 0
    temp1 = 0  
    temp2 = 0
    mse = 0
    mx = 0
    my = 0
    result = []
    data = get_dataset()
    n = len(data)
    # calculates mean 
    for i in range(n):
        my = my + data[i][1]
    my = my/n
    for i in range(n):
        mx = mx + data[i][0]
    mx = mx/n
    # calculates closed form solution using formula   
    for i in range(n):
            temp1 = temp1 + (data[i][0] - mx)*(data[i][1] - my) 
    for i in range(n):
            temp2 = temp2 + math.pow((data[i][0] - mx), 2)
    b1 = temp1/temp2        
    b0 = my - b1*mx
    mse = regression(b0,b1)
    result = ((b0,b1,mse))
    return result

def predict(year):
    # calls compute beta and returns prediction
    b0 = float(compute_betas()[0])
    b1 = float(compute_betas()[1])
    prediction = b0 + b1*year
    return prediction
              
def iterate_normalized(T,eta):
    data = get_dataset()
    n = len(data)
    mx = 0
    stdx = 0
    T = T
    eta = eta
    b0 = 0 #beta_0 at time t - 1
    bc0 = 0 #current beta_0
    b1 = 0 #beta_1 at time t - 1
    bc1 = 0 #current beta_1
    counter = 1 
    #calculates mean
    for i in range(n):
        mx = mx + data[i][0]
    mx = mx/n 
    # calculates stdx for normalization
    for i in range(n):
        stdx = stdx + math.pow((data[i][0] - mx),2)
    stdx = stdx/(n-1)
    stdx = math.sqrt(stdx)
    # normalizes dataset
    for i in range(n):
        data[i][0] = ((data[i][0] - mx)/stdx) 
    # iterates T times      
    while counter < T+1:        
        # makes sure values are reset at every iteration
        gd0 = 0 
        gd1 = 0
        mse = 0
        for i in range(n):
            gd0 = gd0 + (b0+b1*data[i][0]-data[i][1])
        gd0 = (2*gd0)/n
        for i in range(n):
            gd1 = gd1 + data[i][0]*(b0+b1*data[i][0]-data[i][1])
        gd1 = (2*gd1)/n        
        bc0 = b0 - eta*(gd0)
        bc1 = b1 - eta*(gd1)
        b0 = bc0
        b1 = bc1
        for i in range(n):
            mse = mse + math.pow(b0+b1*data[i][0]-data[i][1],2)
        mse = mse/n
        print(counter, "%.2f" % bc0,"%.2f" % bc1,"%.2f" % mse)
        counter = counter + 1
    
def sgd(T,eta):
    data = get_dataset()
    n = len(data)
    mx = 0
    stdx = 0
    T = T
    eta = eta
    b0 = 0 #beta_0 at time t - 1
    bc0 = 0 #current beta_0
    b1 = 0 #beta_1 at time t - 1
    bc1 = 0 #current beta_1
    rand = 0
    counter = 1    
    #calculates mean 
    for i in range(n):
        mx = mx + data[i][0]
    mx = mx/n 
    # calculates stdx for normalization
    for i in range(n):
        stdx = stdx + math.pow((data[i][0] - mx),2)
    stdx = stdx/(n-1)
    stdx = math.sqrt(stdx)
    # normalizes dataset
    for i in range(n):
        data[i][0] = ((data[i][0] - mx)/stdx)     
    # iterates T times
    while counter < T+1:
        # chooses random integer betweem 0 and n-1 (both inclusive)
        rand = random.randint(0,n-1)        
        temp = data[rand]
        gd0 = 2*(b0+b1*temp[0]-temp[1])
        gd1 = 2*(b0+b1*temp[0]-temp[1])*temp[0]       
        bc0 = b0 - eta*(gd0)
        bc1 = b1 - eta*(gd1)
        b0 = bc0
        b1 = bc1
        mse = math.pow(b0+b1*temp[0]-temp[1],2)
        print(counter, "%.2f" % bc0,"%.2f" % bc1,"%.2f" % mse)
        counter = counter + 1
    