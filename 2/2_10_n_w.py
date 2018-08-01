# -*- coding: utf-8 -*-
"""
2.10
nrwade0
Feb 20, 2018
"""

from numpy import array, zeros

# declare constant coefficients
a1,a2,a3,a4=15.8,18.3,0.714,23.2

# what part do you want to do?
part=str(input("Enter the part of the problem, a, b, c, d: "))



if part in ['a']:
    
    # input mass number and atomic number
    a=int(input("Enter the mass number (A): "))
    z=int(input("Enter the atomic number (Z): "))
    
    # find the value for a5
    if a % 2 != 0: # if A is odd...
        a5=0
        
    elif z % 2 == 0: # if A and Z are even 
        a5=12.0
        
    else: # if A is even and Z is odd
        a5=-12.0
    
    # caclulate total nuclear binding energy
    B=a1*a-a2*a**(2/3)-a3*z*z/a**(1/3)-a4*(a-2*z)**2/a+a5/a**(1/2)
    
    # output
    print("Total binding energy (B) is ",B,"MeV")
    
    
    
if part in ['b']:
    
    # input mass number and atomic number
    a=int(input("Enter the mass number (A): "))
    z=int(input("Enter the atomic number (Z): "))
    
    # find the value for a5
    if a % 2 != 0: # if A is odd...
        a5=0
        
    elif z % 2 == 0: # if A and Z are even 
        a5=12.0
        
    else: # if A is even and Z is odd
        a5=-12.0
    
    # calculate total nuclear binding energy
    B=a1*a-a2*a**(2/3)-a3*z*z/a**(1/3)-a4*(a-2*z)**2/a+a5/a**(1/2)
    
    Bpn=B/a
    # output binding energy per nucleon
    print("Binding energy per nucleon (B/A) is ",Bpn,"MeV")



if part in ['c']:
    
    # input only the atomic number
    z=int(input("Enter the atomic number (Z): "))
    
    # array of a from z to 3z
    a=array(list(range(z,3*z+1)))
    
    # length of a
    n=len(a)
    
    # array of zeros of float type and size n
    a5=zeros(n,float)
    
    # go thru n and calculate each a5 coefficient
    for i in range(n):
        # find the value for a5 for each mass number
        if a[i] % 2 != 0: # if A is odd...
            a5[i]=0
            
        elif z % 2 == 0: # if A and Z are even 
            a5[i]=12.0
            
        else: # if A is even and Z is odd
            a5[i]=-12.0
        
        # make it happen
        B=a1*a-a2*a**(2/3)-a3*z*z/a**(1/3)-a4*(a-2*z)**2/a+a5/a**(1/2)        
        Bpn=B/a
        
        # calculate binding energies per nucleon
        Bmax=Bpn[0]        
        
        # find the largest binding energy per nucleon
    for j in range(1,n):
        Bcompare=Bpn[j]
        if Bcompare > Bmax:
            Bmax=Bcompare
            index=j
        
    # print Bmas and the apporpriate mass number
    print("Highest binding energy per nucleon:",Bmax,"MeV")
    print("This occurs at A =",a[index],"nucleons")



if part in ['d']:
    
    n1=100
    a_stable=zeros(n1,float)
    B_stable=zeros(n1,float)
    
    z=array(list(range(1,n1+1)))
    
    for k in range(n1):
        
        # array of a from z to 3z for each iteration of k
        a=array(list(range(z[k],3*z[k]+1)))
        
        # length of a
        n2=len(a)
        
        # array of zeros of float type and size n
        a5=zeros(n2,float)
        
        # go thru n and calculate each a5 coefficient
        for i in range(n2):
            # find the value for a5 for each mass number
            if a[i] % 2 != 0: # if A is odd...
                a5[i]=0
                
            elif z[k] % 2 == 0: # if A and Z are even 
                a5[i]=12.0
                
            else: # if A is even and Z is odd
                a5[i]=-12.0
            
            # open wide
            B=a1*a-a2*a**(2/3)-a3*z[k]*z[k]/a**(1/3)-a4*(a-2*z[k])**2/a+a5/a**(1/2)        
            Bpn=B/a
            
            # calculate binding energies per nucleon
            Bmax=Bpn[0]        
            
            # find the largest binding energy per nucleon
        for i in range(1,n2):
            Bcompare=Bpn[i]
            if Bcompare > Bmax:
                Bmax=Bcompare
                index=i
        
        a_stable[k]=a[index]
        B_stable[k]=Bmax
        
        if k == 0:
            print("Z A")
            
        print(z[k],a_stable[k])
        
    Bmax=B_stable[0]
    
    for h in range(1,n1):
        Bcompare=B_stable[h]
        if Bcompare > Bmax:
            Bmax = Bcompare
            index=h
            
    print("The maximum binding energy occurs at z =",z[index])
            





