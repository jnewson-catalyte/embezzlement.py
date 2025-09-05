f_steal = 10000
k_steal= 1/4 * f_steal  
bb_steal = 1000 + k_steal 
j_steal = 8 * bb_steal  
ng_steal = 2 * j_steal 
g_steal = 7 * k_steal 
br_steal = 2000 - j_steal 
t_steal = 7000 - br_steal 
nic_steal = br_steal / 2  
p_steal = .1 * t_steal 


sum_of_stealing = f_steal + k_steal + bb_steal + j_steal + ng_steal+ g_steal + br_steal + t_steal + nic_steal + p_steal 


print(sum_of_stealing) 