#!/usr/bin/env python

###################
#Dev Note for what Params are used
#

############################
# Imports
############################

from __future__ import print_function
from scipy.optimize import linear_sum_assignment
import numpy as np
import time
import sys
import rospy
from behaviour.srv import *
from behaviour.msg import members
from behaviour.msg import drone_state
from behaviour.srv import areareq
import geopy.distance


############################
# Global Params
############################
global memberlist
global pub

############################
# Inits
############################
meID = rospy.get_param("thisdroneID")

def members_callback(data):
    global memberlist
    memberlist = data
    return

def swarm_state_client():
    rospy.wait_for_service('swarm_state')
    swarmreq = rospy.ServiceProxy('swarm_state', swarmstatereq)
    resp = swarmreq(1)
    return resp

def handle_area_req(a):
    lats = []
    lons = []
    npoints = swarm_state_client()
    n_points = npoints.a
    #####################################
    # Uncomment this block for final build
    #lats = rospy.get_param("mission_points_lats")
    #lons = rospy.get_param("mission_points_lons")
    #alts = rospy.get_param("mission_points_alts")
    #####################################

    #####################################
    # Comment out this block when not testing
    lats.append  (52.06688046891671)
    lats.append  (52.06670194104023)
    lats.append  (52.06669981570283)
    lats.append  (52.06688049328314)
    lons.append (-0.6336844349831279)
    lons.append (-0.6336786728635458)
    lons.append (-0.6329491885016963)
    lons.append (-0.6329496307356894)
    #####################################

    diflat = max(lats) - min(lats)
    diflon = max(lons) - min(lons)
    if not n_points == 0:
        dellon = diflon / n_points
    else:
        print("None Available")
        return(1)
    dellat = diflat/ 2 # this is a simplification due to the simple shape and size of our area
    # please see the segmenter algorithm for a more complex implementation (ommited here as overkill)
    points = []
    i = 1
    while i <= n_points:

        points.append(  (min(lats) +  dellat, min(lons) + ((i * dellon) - (dellon / 2)) , i )  )
        i = i + 1

    #########
    # take the points and allocate them
    #########
    available = []
    costs = []
    num_mon = 0
    i = 0
    while i < len(memberlist.drone_states):
        drone_type = memberlist.drone_states[i].type
        drone_mode = memberlist.drone_states[i].mode
        if drone_type == 2:
            if drone_mode == 1:
                available.append((memberlist.drone_states[i].drone_id, memberlist.drone_states[i].drone_geometry.lat, memberlist.drone_states[i].drone_geometry.lon, memberlist.drone_states[i].battery))
        i = i + 1

    # avialable format: id,lat,lon.bat
    # Calcualte their costs for each task
    diction = []
    array = []
    i = 0
    while i < len(points):
        w = 0
        while w < len(available):
            coordpoint = (points[i][0], points[i][1])
            coorddrone = (available[w][1], available[w][2])
            distance = (geopy.distance.vincenty(coordpoint, coorddrone).km) * 1000
            score = 1/distance * available[w][3]    
            diction.append (score)
            w = w + 1
        array.append(diction)
        diction = []
        i = i +1
    array = np.array(array)
    try:
        x, y = linear_sum_assignment(array)
    except:
        print("No Trackers Available")
        return(1)    
    # Order of the allocation preserved from available
    i = 0
    try:
        while i < len(y):
            hb_msg = drone_state()
            hb_msg.drone_id = available[i][0]
            hb_msg.task.task_geometry.lat = float(points[y[i]][0])
            hb_msg.task.task_geometry.lon = float(points[y[i]][1])
            hb_msg.task.task_geometry.alt = 0
            hb_msg.task.allocated = int( y[i])
            hb_msg.task.type = 1
            i = i + 1
            pub.publish(hb_msg)
            rospy.sleep(0.1)
    except:
        print ("Failed to set Areas")
        return(1)
    return(1)

def area_allocation_server():
    global pub
    rospy.init_node('area_allocation_server')
    rospy.Subscriber("Members", members, members_callback)
    pub = rospy.Publisher('Heartbeat_Internal', drone_state, queue_size=10, latch = True)
    s = rospy.Service('area_allocation', areareq, handle_area_req)
    rospy.spin()

if __name__ == '__main__':
    area_allocation_server()