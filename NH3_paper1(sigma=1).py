# -*- coding: utf-8 -*-
"""
    Created on Sun Sep  6 08:31:51 2015
    
    @author: genius
    """

import matplotlib.pyplot as plt
import numpy as np

##--------------load the theory spectra--------------
sigma=1
Cc=2.99792458*10**5
Pi=3.1415926
vs_theory,inten_theory = np.array([]),np.array([])
spf_theory = open('nh3_11_theory.txt')
line = spf_theory.readline()
words = line.split()
while (words[0] != 'end'):
    vs_theory = np.append(vs_theory, float(words[0]))
    inten_theory = np.append(inten_theory, float(words[1]))
    line = spf_theory.readline()
    words = line.split()

spf_theory.close()
#print 'spectra point:',np.size(vs_theory)

vel=vs_theory/23694495.487*Cc   #将频率转换成速度

##--------------18 Gauss----------------------------

x=np.arange(-25,25,0.05)
y=np.arange(-25,25,0.05)*0.0

gf=0.0
ggf=0.0
for i in range(18):
    gf = inten_theory[i]*(1/(np.sqrt(2*Pi)*sigma)*np.exp(-(x-vel[i])**2/(2*sigma**2)))
    ggf = ggf + gf
    plt.plot(x,100*gf,linestyle='steps')

plt.plot(x,100*ggf,"k--",label="Coalition",linewidth=2)
#plt.title("18 Gauss")
plt.xlabel("Velocity(km/s)")
plt.ylabel("Relative Intensity(%)")

plt.xlim([-25,25])
plt.ylim([0,21])

plt.text(-19, 5, "osg", fontsize=12 )
plt.text(-7, 6, "isg", fontsize=12 )
plt.text(1, 19, "mg", fontsize=12 )
plt.text(8, 6, "isg", fontsize=12 )
plt.text(20, 5, "osg", fontsize=12 )
plt.legend()

plt.savefig('/Users/genius/Desktop/work/NH3_paper1.eps',dpi=100)
plt.show()