# Inverted-Pendulum

## Table of contents
* [General info](#general-info)
* [Steps](#steps)

## General info
This is a personnal project in progress in order to build from scratch an entire embedded system.
The final goal is to build a small segway controlled with a Raspberry-pi (Choice in Python for the moment) that can send information with user via a websocket Server (for IHM)
The purpose is to use no pre-built system in order to be the most educational and instructive
	
## Steps
The steps necessary to make the system reality are:

* Choice of Actuators/Sensors/Mechanical Pieces
* CAD : Conception of 3D-printed pieces
* Caracterisation of Actuators/Sensors
* Control Loop of system (1rst example with a PID. Can be improved with a LQR for improvement)
* Websocket Server in order to have an IHM for the user from any device
