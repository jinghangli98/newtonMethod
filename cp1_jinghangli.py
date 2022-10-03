import numpy as np

def f(theta_t, theta_i, gamma): #np.sin or np.cos takes in radians instead of degrees
    return (gamma + 1)/(1 - gamma) * (np.cos(theta_i)*np.sin(theta_i)) - np.sin(theta_t)*np.cos(theta_t)

itr = 0

def newtonMethod(x1, x2, alpha, y1, y2, theta, g, itr):
    if np.abs(y1) <= alpha: 
        return x1
    elif np.abs(y2) <= alpha : 
        return x2
    else:
        itr = itr + 1
        slope = (y2-y1)/(x2-x1)
        x3 = x1 - y1/slope
        if np.abs(f(x3, theta, g)) <= alpha: 
            return x3
        else: #recursive case, iteratively find the next solution
            x1_new = x2
            x2_new = x3
            y1_new = f(x1_new, theta, g)
            y2_new = f(x2_new, theta, g)
            x3 = newtonMethod(x1_new, x2_new, alpha, y1_new, y2_new, theta, g, itr)
            #print("Iterations took to calculate the relative permitivity:", itr, "theta_i:", theta, "alpha:", alpha, "gamma:",g)
            return x3
    

GAMMA = [-0.1, -0.5, -0.9]
THETA_I = [20, 40, 60, 80]
theta_i = np.divide(THETA_I, 180) * np.pi #turn THETA_I into radian
ALPHA = [0.1, 0.0001]

x2 = 6 #radian
x1 = 6.05

counter = 0
r_perm = []
for g in GAMMA:
    for theta in theta_i:
        for a in ALPHA:
            y1 = f(x1, theta, g)
            y2 = f(x2, theta, g)
            theta_t = newtonMethod(x1, x2, a, y1, y2, theta, g, 0)
            r_perm.append(np.power(np.sin(theta)/np.sin(theta_t), 2))
            #print(a,",", "%0.2f" % theta, ",", g,",", "%0.2f \n" % r_perm[counter])
            print("alpha is", a, "theta_i is %0.2f" % theta, "Gamma is ", g, "\nThe calculated relative permitivity is: %0.2f \n" % r_perm[counter])
            #print("alpha: ", a, "theta_i: ", theta, "Gamma: ", g, "\nThe calculated relative permitivity is: ", r_perm[counter], "\nThe calculated theta_t is:", theta_t, "(radian)")
            counter += 1
