#!/usr/bin/env python

# Copyright (c) 2019 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

"""Spawn NPCs into the simulation"""

import glob
import os
import sys
import time
import random

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

actor_list = [];

try:
	client = carla.Client("localhost",2000)
	client.set_timeout(10.0)
	world = client.load_world('Town01')
	blueprint_library = world.get_blueprint_library()


	#create model 3
	bp = blueprint_library.filter("model3")[0]
	spawn_point = random.choice(world.get_map().get_spawn_points())
	
	model3 = world.spawn_actor(bp,spawn_point)
	model3.set_autopilot(True)
	actor_list.append(model3)
	print("spawned model3")


	#create bmw
	bp = blueprint_library.filter("bmw")[0]
	spawn_point = random.choice(world.get_map().get_spawn_points())
	print(blueprint_library.filter("bmw"))
	bmw = world.spawn_actor(bp,spawn_point)
	bmw.set_autopilot(True)
	actor_list.append(bmw)
	print("spawned bmw")
	
	print(client.get_available_maps())


	time.sleep(35)
	
finally:

	for actor in actor_list:
		print(actor)
		actor.destroy()
	print("cleaned up")