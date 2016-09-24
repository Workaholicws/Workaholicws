# -*- coding: utf-8 -*-
"""
    Created on Tue Sep 15 14:36:26 2015
    
    @author: genius
    """

import matplotlib.pyplot as plt
import numpy as np


#------------------Define model------------------------------
#@custom_model_1d
def Tb_theory(vs, dv, tau_m=1.0,v0=0.,Tex=30,osg1=0.,isg1=0.,mg=0.,isg2=0.,osg2=0.):
    
    v_0,v_1=-19.84514,-19.31960
    v_2,v_3,v_4=-7.88632,-7.46920,-7.35005
    v_5,v_6,v_7,v_8,v_9,v_10,v_11,v_12=-0.46227,-0.32312,-0.30864,-0.18950,0.07399,0.13304,0.21316,0.25219
    v_13,v_14,v_15=7.23455,7.37370,7.81539
    v_16,v_17=19.40943,19.54859
    
    a0,a1=1.0/27,2.0/27
    a2,a3,a4=5.0/108,1.0/12,1.0/108
    a5,a6,a7,a8,a9,a10,a11,a12=1.0/54,1.0/108,1.0/60,3.0/20,1.0/108,7.0/30,5.0/108,1.0/60
    a13,a14,a15=5.0/108,1.0/108,1.0/12
    a16,a17=1.0/27,2.0/27
    
    profile1 =a0 * np.exp(-4*np.log(2)*((vs-v0-v_0)/dv)**2)+ \
              a1 * np.exp(-4*np.log(2)*((vs-v0-v_1)/dv)**2)  #osg_1
    profile2 =a2 * np.exp(-4*np.log(2)*((vs-v0-v_2)/dv)**2)+ \
              a3 * np.exp(-4*np.log(2)*((vs-v0-v_3)/dv)**2)+ \
              a4 * np.exp(-4*np.log(2)*((vs-v0-v_4)/dv)**2)  #isg_1
    profile3 =a5 * np.exp(-4*np.log(2)*((vs-v0-v_5)/dv)**2)+ \
              a6 * np.exp(-4*np.log(2)*((vs-v0-v_6)/dv)**2)+ \
              a7 * np.exp(-4*np.log(2)*((vs-v0-v_7)/dv)**2)+ \
              a8 * np.exp(-4*np.log(2)*((vs-v0-v_8)/dv)**2)+ \
              a9 * np.exp(-4*np.log(2)*((vs-v0-v_9)/dv)**2)+ \
              a10 * np.exp(-4*np.log(2)*((vs-v0-v_10)/dv)**2)+ \
              a11 * np.exp(-4*np.log(2)*((vs-v0-v_11)/dv)**2)+ \
              a12 * np.exp(-4*np.log(2)*((vs-v0-v_12)/dv)**2)  #mg
    profile4 =a13 * np.exp(-4*np.log(2)*((vs-v0-v_13)/dv)**2)+ \
              a14 * np.exp(-4*np.log(2)*((vs-v0-v_14)/dv)**2)+ \
              a15 * np.exp(-4*np.log(2)*((vs-v0-v_15)/dv)**2)  #osg_2
    profile5 =a16 * np.exp(-4*np.log(2)*((vs-v0-v_16)/dv)**2)+ \
              a17 * np.exp(-4*np.log(2)*((vs-v0-v_17)/dv)**2)  #osg_2

    tau_m = 3.0/dv;
    tau_v = tau_m * (osg1*profile1+isg1*profile2+mg*profile3+isg2*profile4+osg2*profile5)
    
    Tb_theory = (1.137/(-1+np.exp(1.137/Tex))-2.201) * (1-np.exp(-tau_v))
    return Tb_theory

vs_theory=np.arange(-30.0,30.0,0.1)
dv_theory=np.arange(0.0,20.0,0.4)

Tb_summg_theory=0.0*dv_theory
Tb_sumisg_theory=0.0*dv_theory

R_sm_theory=0.0*dv_theory
Trand=0.0
Tb=0.0
for i in range(10):
    dv_theory=0.4*(i+1)
    plt.figure()
#    vsrand = vs_theory+np.random.randn(len(vs_theory))
#    Trand = Tb_theory(vsrand, dv_theory ,osg1=1,osg2=1,mg=1,isg1=1,isg2=1)
#    Tb = Tb_theory(vs_theory, dv_theory ,osg1=1,osg2=1,mg=1,isg1=1,isg2=1)+1.0*Trand
#    上面加随机误差的方法效果不好
    Tb = Tb_theory(vs_theory, dv_theory ,osg1=1,osg2=1,mg=1,isg1=1,isg2=1)+np.random.randn(len(vs_theory))

    plt.plot(vs_theory,Tb,color='k')
    plt.plot(vs_theory,Tb_theory(vs_theory, dv_theory ,osg1=1,osg2=1,mg=1,isg1=1,isg2=1),color='red')
    plt.xlim([-25,25])
    plt.ylim([0,21])
    plt.xlabel("Velocity(km/s)")
    plt.ylabel("Temperature(K)")
    plt.savefig('/Users/genius/Desktop/work/NH3witherr_gif/NH3_'+str(dv_theory)+'.eps',dpi=100)
    plt.show()