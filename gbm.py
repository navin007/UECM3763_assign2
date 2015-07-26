# coding: utf-8
import pylab as p
import numpy as np
mu=0.1;
sigma=0.26;
S0=39;
npath=1000;
n=npartition=1000;
period=3
t=p.linspace(0,period,n+1)
dB = p.randn(npath,n+1) / p.sqrt(n/period) ; dB[:,0]=0
B = dB.cumsum(axis = 1)
nu = mu - sigma * sigma / 2.0
S = p.zeros_like(B) ; S[:,0] = S0
S[:,1:] = S0 * p.exp(nu * t[1:] + sigma * B[:,1:])
S_sample = S[0:5]
p.plot(t,S_sample.transpose());
label = 'Time , $t$' ; p.xlabel(label)
label = 'stock prices , $S_t$' ; p.ylabel(label)
p.title('GBM of ' + label + '\n with $\mu$ = ' + str(mu) + ' and $\sigma$ = ' + str(sigma))
p.show();
p.show();
p.show()
S3 = p.array(S[:,-1])
E_S3 = np.mean(S3)
Var_S3 = np.var(S3)
S3 = p.array(S[:,-1])
E_S3 = np.mean(S3)
print('E(S3) = ' + str(E_S3) , '\nVar(S3) = ' + str(Var_S3))
mask = S3 > 39
P_S3 = sum(mask) / len(mask)
S3_39 = S3 * mask
E_S3_39 = sum(S3_39) / sum(mask)
print('P(S3 > 39) = ' +str(P_S3), '\nE(S3 | S3 > 39) = ' +str(E_S3_39))
print('\nTheoritical expectation and variance:')
E = S0 * p.exp(mu*period)
Var = (S0**2)*(np.exp(2*mu*period))*(np.exp(sigma*sigma*period)-1)
print('E('+ str(period) + ') = ' + str(E) , '\nVar('+str(period) + ') = ' + str(Var))
