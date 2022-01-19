#!/usr/bin/python 
import serial 
import time 
from track import * 
from libCompass import * 
from rrb2 import * 
import math 

def move_angle(angle): 
	if angle < 0: 
		angle = angle + 360 
	bearing = readDirection() 
	move angle = bearing - angle 
	if move_angle > 180: 
		turn_right() 
	elif move_angle < -180: 
		turn_left() 
	elif (move_angle) < 180 and move_angle > 0: 
		turn left() 
	elif move_angle > -180 and move_angle < 0: 
		turn_right() 
	while(abs(angle - bearing)) > 5: 
		time.sleep(.2) 
		print abs(angle-bearing) 
		bearing = readDirection() 
	stop() 
	print("angle", bearing)
	
	
def positionRobot(xpos, ypos, xpos_goal, ypos_goal): 
	print xpos, ypos, xpos_goal, ypos_goal 
	distance = math.sqrt((xpos_goal - ypos_robot)**2 + (ypos_goal - ypos_robot)**2) 
	angle = round(math.degrees(math.atan2((ypos_goal - ypos_robot), xpos_goal - xpos_robot)))) 
	print("angle",angle)
	move_angle(angle) 
	print(distance)
	return distance, angle 

xpos_robot = int(raw_input("Robot X Position: ")) 
ypos_robot = int(raw_input("Robot Y Position: ")) 
xpos_goal = int(raw_input("Goal X Position: ")) 
ypos_goal = int(raw_input("Goal Y Position: ")) 

distance, angle = positionRobot(xpos_robot, ypos_robot, xpos_goal, ypos_goal) 

start time = time.time() 
forward() 
barrier = rr.get_distance() 
elapsed_time = 0 
while barrier > 10 and elapsed_time < distance: 
	elapsed_time = time.time() - start_time 
	barrier = rr.get_distance() 
	if barrier > 0 and barrier < 10: 
		print("barrier", barrier) 
		distance_traveled = elapsed time 
		new_distance = 1 
		ypos_robot = ypos_robot + distance_traveled * math.sin(math.radians(angle)) 
		ypos_goal_barrier = ypos_robot + new_distance * math.sin(math.radians(angle + 90)) 
		xpos_robot = xpos_robot + distance_traveled * math.cos(math.radians(angle)) 
		xpos_goal_barrier = xpos_robot + new_distance * math.cos(math.radians(angle + 90)) 
		distance = positionRobot(xpos_robot, ypos_robot, xpos_goal_barrier, ypos_goal_barrier) 
		start_time = time.time() 
		forward() 
		elapsed_time = 0 
		while elapsed_time < new distance: 
			elapsed_time = time.time() - start_time 
		print "Done moving around barrier" 
		ypos_robot = ypos_goal barrier 
		xpos_robot = xpos_goal barrier 
		distance = positionRobot(xpos_robot, ypos_robot, xpos_goal, ypos_goal) 
		start time = time.time() 
		forward() 
		barrier = rr.get_distance() 
		elapsed_time = 0 
stop() 
print ("Goal Reached") 

