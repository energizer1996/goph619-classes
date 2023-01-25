# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 08:12:25 2023

pathlib packages

@author: jesus.parra
"""
def exp_num(x):
    """
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    s : TYPE
        DESCRIPTION.

    """
    k=0
    error = 1.0
    tolerance = 1e-16
    s = 1.0
    fact_k = 1
    counter = 0
    while error > tolerance:
        k += 1
        fact_k *= k
        t = (x**k)/fact_k
        s+=t
        error = abs(t/s)
        counter += 1
    return (s,counter)

if __name__ == '__main__':
    print(f'exp_num(0): {exp_num(0)}')
    print(f'exp_num(1): {exp_num(1)}')