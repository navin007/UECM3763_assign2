
import pylab as p
import numpy as np


alpha = 1
theta = 0.064
sigma = 0.27
R0 = 3
time = 1
npath = 1000
n = 1000

dt = time / n
t =p.linspace (0,time ,n+1)
dB = p.randn(npath,n+1) * p.sqrt(dt) ; dB[:,0] = 0
B = dB.cumsum(axis = 1)

R = p.zeros_like(B)
R[:,0]=R0

for col in range(n):
    R[:,col+1] = R[:,col] + (theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]
    
R_sample=R[0:5]
p.plot(t,R_sample.transpose())

label = 'Time , $t$' ; p.xlabel(label)
label = '$R_t$' ; p.ylabel(label)
para1 = '\n with $\\alpha$ = ' + str(alpha)
para2 = ', $\\theta$ = ' + str(theta)
para3 = ', and $\sigma$ = ' + str(sigma) + '\n'
p.title(str(5) + ' runs of Mean reversal process for ' + label + para1 + para2 + para3)
p.show();
R1=p.array(R[:,-1])
E_R1=np.mean(R1)
print('E(R1) = ' + str(E_R1))
mask = R[:,-1] > 2
P_R1 = sum(mask)/npath
print('P(R1 > 2) = ' + str(P_R1))


