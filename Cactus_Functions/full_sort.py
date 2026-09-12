#Alteration of checker formation, Ignores parity
#It should stop at each position and run a while loop to check for two conditions
#First condition is that the current spot (when not on a corner or edge) should be the minimum of itself, the value north, and the value east
#The second condition is that it should be the maximum value of itself, the value south and the value west
#Sides should not search for parity match
#tracker variables need to be implemented to prevent scanning over an entire area multiple times
from funcs import *
def full_sort():
	#Create list of integers to check for the correct coordinate cases
	
	initial_tracker = 0
	coords_ls = []

	for y in range(get_world_size()):
		for x in range(get_world_size()):
		
			if initial_tracker == 0:
				till()
				plant(Entities.Cactus)
			move(East)
		move(North)	
	initial_tracker = 1
	#Above should include the cactus planting code
	tracker = 0
	while tracker != 1:
		for y in range(get_world_size()):

			for x in range(get_world_size()):
				#Set up encoding
				encoded_x = get_pos_x() * 100
				encoded_y = get_pos_y()
				encoded = encoded_x + encoded_y
				#Here, we should begin case checks, start with bottom-left as it will always be the first case
				if get_pos_x() == 0 and get_pos_y() == 0 :
					#Ignore South and West cases
					while measure() != min([measure(),measure(North),measure(East)]):
						if measure() > measure(North):
							swap(North)
							if encoded + 1 not in coords_ls:
								coords_ls.append(encoded+1)
						elif measure() > measure(East):
							swap(East)
							if encoded + 100 not in coords_ls:
								coords_ls.append(encoded+100)
						tracker += 1
						if encoded not in coords_ls:
							coords_ls.append(encoded)
					#Move East should ideally only be needed once, after all cases are ran
				
				#Check case for bottom row not corner as this will always be the second case encountered
				elif get_pos_y() == 0 and get_pos_x() % 2 == 0 and get_pos_x() != get_world_size() -1:
					#Ignore South Case
					while measure() != min([measure(),measure(North),measure(East)]) or measure() != max([measure(), measure(West)]):
						if measure() > measure(North):
							swap(North)
							if encoded + 1 not in coords_ls:
								coords_ls.append(encoded+1)
						elif measure() > measure(East):
							swap(East)
							if encoded + 100 not in coords_ls:
								coords_ls.append(encoded+100)
						elif measure() < measure(West):
							swap(West)
							if encoded - 100 not in coords_ls:
								coords_ls.append(encoded-100)
						if encoded not in coords_ls:
							coords_ls.append(encoded)
							
				#Check case for bottom right, should always be third case, should pass if world size is odd
				elif get_pos_y() == 0 and get_pos_x() == get_world_size() - 1 and get_pos_x() % 2 == 0:
					#Ignore South, Ignore East
					while measure() != min([measure(),measure(North)]) or measure() != max([measure(), measure(West)]):
						if measure() > measure(North):
							swap(North)
							if encoded + 1 not in coords_ls:
								coords_ls.append(encoded+1)
						elif measure() < measure(West):
							swap(West)
							if encoded - 100 not in coords_ls:
								coords_ls.append(encoded-100)
						if encoded not in coords_ls:
							coords_ls.append(encoded)

				#Next is case left hand side
				elif (get_pos_y() != 0 and get_pos_y() != get_world_size() - 1) and get_pos_x() == 0 :
					#Ignore West
					while measure() != min([measure(),measure(North),measure(East)]) or measure() != max([measure(), measure(South)]):
						if measure() > measure(North):
							swap(North)
							if encoded + 1 not in coords_ls:
								coords_ls.append(encoded+1)
						elif measure() > measure(East):
							swap(East)
							if encoded + 100 not in coords_ls:
								coords_ls.append(encoded+100)
						elif measure() < measure(South):
							swap(South)
							if encoded - 1 not in coords_ls:
								coords_ls.append(encoded-1)
						if encoded not in coords_ls:
							coords_ls.append(encoded)

				#Next is body case, nothing ignored parity matching should work here
				elif (get_pos_y() != 0 and get_pos_y() != get_world_size() - 1) and get_pos_x() != get_world_size() - 1 and get_pos_x() != 0 :
								#Ignore Nothing
					while measure() != min([measure(),measure(North),measure(East)]) or measure() != max([measure(), measure(South), measure(West)]):
						if measure() > measure(North):
							swap(North)
							if encoded + 1 not in coords_ls:
								coords_ls.append(encoded+1)
						elif measure() > measure(East):
							swap(East)
							if encoded + 100 not in coords_ls:
								coords_ls.append(encoded+100)
						elif measure() < measure(South):
							swap(South)
							if encoded - 1 not in coords_ls:
								coords_ls.append(encoded-1)
						elif measure() < measure(West):
							swap(West)
							if encoded - 100 not in coords_ls:
								coords_ls.append(encoded-100)
						if encoded not in coords_ls:
							coords_ls.append(encoded)

				#Next case is the right wall 
				elif (get_pos_y() != 0 and get_pos_y() != get_world_size() - 1) and get_pos_x() == get_world_size() - 1:
								#Ignore East
					while measure() != min([measure(),measure(North)]) or measure() != max([measure(), measure(South), measure(West)]):
						if measure() > measure(North):
							swap(North)
							if encoded + 1 not in coords_ls:
								coords_ls.append(encoded+1)
						elif measure() < measure(South):
							swap(South)
							if encoded - 1 not in coords_ls:
								coords_ls.append(encoded-1)
						elif measure() < measure(West):
							swap(West)
							if encoded - 100 not in coords_ls:
								coords_ls.append(encoded-100)
						if encoded not in coords_ls:
							coords_ls.append(encoded)

				#Next is top left corner
				elif get_pos_y() == get_world_size() - 1 and get_pos_x() == 0 and ((get_pos_y() % 2 == 0 and get_pos_x() % 2 == 0) or (get_pos_y() % 2 != 0 and get_pos_x() % 2 != 0)):
								#Ignore North, West
					while measure() != min([measure(),measure(East)]) or measure() != max([measure(), measure(South)]):
						if measure() > measure(East):
							swap(East)
							if encoded + 100 not in coords_ls:
								coords_ls.append(encoded+100)
						elif measure() < measure(South):
							swap(South)
							if encoded - 1 not in coords_ls:
								coords_ls.append(encoded-1)
						if encoded not in coords_ls:
							coords_ls.append(encoded)

				#Next is top row
				elif get_pos_x() != get_world_size() -1 and get_pos_x() != 0 and get_pos_y() == get_world_size() - 1  :
					#Ignore North
					while measure() != min([measure(),measure(East)]) or measure() != max([measure(), measure(South), measure(West)]):
						if measure() > measure(East):
							swap(East)
							if encoded + 100 not in coords_ls:
								coords_ls.append(encoded+100)
						elif measure() < measure(South):
							swap(South)
							if encoded - 1 not in coords_ls:
								coords_ls.append(encoded-1)
						elif measure() < measure(West):
							swap(West)
							if encoded - 100 not in coords_ls:
								coords_ls.append(encoded-100)
						if encoded not in coords_ls:
							coords_ls.append(encoded)
				#Final case should be top right corner
				elif get_pos_y() == get_world_size() - 1  and get_pos_x() == get_world_size() - 1 and ((get_pos_y() % 2 == 0 and get_pos_x() % 2 == 0) or (get_pos_y() % 2 != 0 and get_pos_x() % 2 != 0)):
								#Ignore North and East cases
					while measure() != max([measure(),measure(South),measure(West)]):
						if measure() < measure(South):
							swap(South) 
							if encoded - 1 not in coords_ls:
								coords_ls.append(encoded-1)
						elif measure() < measure(West):
							swap(West)
							if encoded - 100 not in coords_ls:
								coords_ls.append(encoded-100)
						if encoded not in coords_ls:
							coords_ls.append(encoded)
				move(East)

		#This should be linked to for y in range
			move(North)	

	tracker = 1	
	quick_print(coords_ls)
		#All the coordinates of all potential change candidates is now included
		#We must run all checks again as in the previous block but this time remove from the list if it passes all checks, only can remove the exact encoded value, not any surrounding
		#sometimes new values will need to be added, make sure the append part still runs
	for coord in coords_ls:
		go_to(coord // 100 , coord % 100)

	harvest()
set_world_size(8)
full_sort()