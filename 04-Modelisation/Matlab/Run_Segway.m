clear; close all;

%% Parameters
Fs = 200;
Ts = 1/Fs;
T_final = 10;

m_wheel = 2;
m_body = 3.5;
R_wheel = 0.32;
L_body = 0.4;
J_wheel = 0.32;
J_body = 0.0065;
b = 1e-3;

R_ohm = 4.7;
Ke = 0.684;

%% Initial State
theta_body_init = 0;
dtheta_body_init = 0;
theta_wheel_init = 0;
dtheta_wheel_init = 0;

torque=0;

H1 = (m_wheel+m_body)*R_wheel^2 + J_wheel;
H2 = m_body*R_wheel*cos(theta2);
H3 = m_body*L_body^2 + J_body;