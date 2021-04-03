from matplotlib import pyplot as plt
import math

#Question 2
time=list(range(10))
i=[1,6,30,60,42,24,12,7,1.5,1]
k=1
x=0.2


def outflow():
    q_0=1
    e=0
    q_li=[1]
    while e <len(time)-1:
    
        c1=(1-(2*k*x))/((2*k*(1-x))+1)
        c2=(1+(2*k*x))/((2*k*(1-x))+1)
        c3=((2*k*(1-x))-1)/(((2*k)*(1-x))+1)
        
        qj1=(c1*i[e+1])+(c2*i[e])+(c3*q_0)
        q_li.append(qj1)
        
        q_0=qj1
        e+=1
    
    return q_li

def plot_outflow():
    q_li=outflow()
    outflow_plot=plt.plot(time,q_li)
    plt.xlabel("Time [hr]")
    plt.ylabel("Outflow [$m^3$/hr]")
    plt.title("Outflow Hydrograph with K={} and X={}".format(k,x))
    
    return outflow_plot

def plot_inflow():
    inflow_plot=plt.plot(time,i,"Orange")
    plt.xlabel("Time [hr]")
    plt.ylabel("Inflow [$m^3$/hr]")
    plt.title("Inflow Hydrograph with K={} and X={}".format(k,x))
    return inflow_plot
    
def combined_plot():
    Outflow=outflow()
    plt.plot(time,Outflow,label="Outflow")
    plt.plot(time,i,label="Inflow")
    plt.xlabel("Time [hr]")
    plt.ylabel("[$m^3$/hr]")
    plt.title("Inflow & Outflow Hydrographs with K={} and X={}".format(k,x))
    plt.legend()
    
    plt.show()
    
def storage_change():
    q_li=outflow()
    dS=0
    dS_li=[]
    for inf,outf in zip(i,q_li):
        diff=inf-outf
        dS+=diff
        dS_li.append(diff)
    
    return (dS,dS_li)

def cumulative_storage_change():
    dS_li=storage_change()[1]
    sum_li=[]
    tot=0
    for i in dS_li:
        tot+=i
        sum_li.append(tot)
    return tot,sum_li

def plot_cumulative_storage_change():
    sum_li=cumulative_storage_change()[1]
    plt.plot(time,sum_li)
    plt.xlabel("Time [hr]")
    plt.ylabel("Cumulative Storage Change [$m^3$]")
    plt.title("Cumulative Storage Change with K={} and X={}".format(k,x))
    plt.show()
 
    
#Question 3 Below
def precip():
    k=1
    i=4
    t=0
    t_0=20
    q_li=[]
    t_li=[]
    while t <=t_0:
        q=k*i*(1-math.exp(-k*t))
        q_li.append(q)
        t_li.append(t)
        t+=0.1
    return (t_li,q_li)

def no_precip():
    k=1
    i=4
    t=precip()[0][-1]
    t_i=precip()[0][-1]
    t_0=40
    q_li=[]
    t_li=[]
       
    while t <=t_0:
        first_term= -k*t
        second_term = math.log((k*i)*(1-math.exp(-k*t_i)))
        third_term= k*t_i
        q=math.exp(first_term+second_term+third_term)
        q_li.append(q)
        t_li.append(t)
        t+=0.1
    return (t_li,q_li)

def plot_precip():
    i=4
    k=1
    t=precip()[0]
    q=precip()[1]
    plot=plt.plot(t,q,label="Outflow During Precipitation [Volume/time]")
    plt.xlabel("Time")
    plt.ylabel("Outflow [Volume/time]")
    plt.title("Outflow vs. Time During Precipitation with K={} and I={} [Volume/time]".format(k,i))
    return plot

def plot_aft_precip():
    i=4
    k=1
    t=no_precip()[0]
    q=no_precip()[1]
    plot=plt.plot(t,q,"Orange",label="Outflow After Precipitation [Volume/time]")
    plt.xlabel("Time")
    plt.ylabel("Outflow [Volume/time]")
    plt.title("Outflow vs. Time After Precipitation with K={} and I={} [Volume/time]".format(k,i))
    return plot

def thru_precip():
    prec=precip()
    aft_precip=no_precip()
    i=4
    k=1
    
    t_precip=prec[0]
    t_aft_precip=aft_precip[0]
    t_total=t_precip+t_aft_precip
    
    
    q_precip=prec[1]
    q_aft_precip=aft_precip[1]
    q_total=q_precip+q_aft_precip
    
    plot=plt.plot(t_total,q_total)
    plt.xlabel("Time")
    plt.ylabel("Outflow [Volume/time]")
    plt.title("Outflow vs. Time During & After Precipitation with K={} and I={} [Volume/time]".format(k,i))
    return plot