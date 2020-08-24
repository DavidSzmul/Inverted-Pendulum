import numpy as np
import matplotlib.pyplot as plt

from math import*
g=9.81

class Model_Segway:

    ### State 
    # state = [x˙; x; θ˙; θ]
    #
    ### Equations :
    # (M + 2m + 2J/h²).x¨ + M.h.θ¨ . (cos θ − θ˙²) = 2Γ/R
    #
    # (K + Mh²).θ¨ + M.h.x¨ . cos θ − Mgh . sin θ = −2Γ
    #
    # Simplify DC Motor without instantaneous response (L=0)
    # 
    # Γ = Ke.R.u_e
    # u_e = u_cons - u_bfem
    # u_bfem = Ke . (x˙/R - θ˙)

    
    state = []
    fig = []

    def __init__(self, x0=0, dx0=0, theta0=0, dtheta0=0, 
                       R_ohm=3, L=0.1, Ke=1.8,M=1,
                       m=0.05, J=0.04, K=0.00004,h=0.2, R=0.04,
                       Fs=100):

        self.x = x0
        self.dx = dx0
        self.theta = theta0
        self.dtheta = dtheta0
        self.get_state()

        self.dt = 1/Fs
        self.R_ohm=R_ohm
        self.L=L
        self.Ke=Ke

        self.M=M
        self.m=m
        self.J=J
        self.K=K

        self.h=h
        self.R=R

    def get_state(self):
        self.state = [self.x, self.dx, self.theta, self.dtheta]

    def update(self, u_cons):

        u_bfem = self.Ke * (self.dx/self.R - self.dtheta)
        ###DEBUG
        # u_e = u_cons-u_bfem
        u_e = u_cons
        torque = self.Ke*self.R_ohm*u_e

        ### Update Matrix 2 unknows 2 equations to determine x.. and theta..
        M_equation = np.array([[(self.M + 2*self.m + 2*self.J/pow(self.h,2)) , self.M * self.h * (cos(self.theta) - pow(self.dtheta,2))],
                                  [(self.K + self.M*pow(self.h,2))           , self.M*self.h*cos(self.theta) - self.M*g*self.h*sin(self.theta)]])

        Y_equation = np.array([[2*torque/self.R],[-2*torque]])

        X_equation = np.dot(np.linalg.inv(M_equation), Y_equation)

        ### Update state
        ddx = X_equation.item(0)
        ddtheta = X_equation.item(1)

        self.dx += ddx*self.dt
        self.dtheta += ddtheta*self.dt
        self.x += self.dx*self.dt
        self.theta += self.dtheta*self.dt
        self.get_state()

    def display(self):
        if self.fig is None:
            self.fig=plt.figure()

        plt.plot(self.x,self.dx)
        plt.draw()
        plt.pause(0.05)

if __name__ == "__main__":
    
    segway = Model_Segway()
    u_cons = 3
    for i in range(100):
        segway.update(u_cons)
        segway.display()
        print(segway.state)

