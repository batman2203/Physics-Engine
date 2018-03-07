import matplotlib.pyplot as p

import math
#import simulation_hajime

import numpy as np
class move_able_particle:
	def __init__(self,mass,x,y,i):
		self.m=mass
		self.co_ordinate=np.array([float(x),float(y)])
		self.velocity=np.array([float(0), float(0)])
		self.particle_no=i
	def __repr__(self):
		return 'Move able particle- ' + str(self.particle_no)
class fixed_particle:
	def __init__(self,mass,x,y,i):
		self.m=mass
		self.co_ordinate =np.array([x, y])
		self.particle_no=i
	def __repr__(self):
		return 'fixed particle- ' + str(self.particle_no)
def each_particle_force(mov_list,fixed_list,i):
	G=6.67*10**(-11)
	acc=np.array([float(0),float(0)])

	for j in mov_list :
		r=math.sqrt((i.co_ordinate[0]-j.co_ordinate[0])**2+(i.co_ordinate[1]-j.co_ordinate[1])**2)

		if abs(r)>0.1:
			temp=np.array(j.co_ordinate-i.co_ordinate)*(G*(j.m)/(r**3))

			acc += temp[0]
		elif j == i:
			pass
		else:
			'''Write code for collision of particles'''
			print "Un written code"
	for j in fixed_list :
		r=math.sqrt((i.co_ordinate[0]-j.co_ordinate[0])**2+(i.co_ordinate[1]-j.co_ordinate[1])**2)
		if abs(r)>0.1:
			temp = np.array(j.co_ordinate-i.co_ordinate)*(G*(j.m)/(r**3))

			acc += temp
		elif j == i:
			pass
		else:
			'''Write code for collision of particles'''
			print 'unwritten code'
	return acc
def step(list_of_fixed,list_of_move_able,no_of_fixed,no_of_move_able,time_step):
	acc_list=[]
	for i in list_of_move_able:
		acc_list.append(each_particle_force(list_of_move_able,list_of_fixed,i))
	for i in range(len(list_of_move_able)):
		(list_of_move_able[i]).velocity+=((acc_list[i])*time_step)
		(list_of_move_able[i]).co_ordinate+=((list_of_move_able[i].velocity)*time_step)

def main():

	no_of_fixed_particle,no_of_move_able_particle=map(int,raw_input('Enter no of fixed particles and moveable particles').split())

	if not no_of_fixed_particle==0:
		print "enter detalis regarding fixed particles"

	list_of_fixed=[]
	list_of_move_able=[]
	for i in xrange(no_of_fixed_particle):
		temp=map(int,raw_input('Enter mass , x, y ').split())
		list_of_fixed.append(fixed_particle(temp[0],temp[1],temp[2],i+1))
	if not no_of_move_able_particle==0:
		print "enter detalis abt movable"
	for i in xrange(no_of_move_able_particle):
		temp=map(int,raw_input('Enter mass , x, y ').split())
		list_of_move_able.append(move_able_particle(temp[0],temp[1],temp[2],i+1))
	p.ion()
	for a in range(100000):
		step(list_of_fixed,list_of_move_able,no_of_fixed_particle,no_of_move_able_particle,0.1)
		print a
		for i in list_of_move_able:
			p.scatter(i.co_ordinate[0],i.co_ordinate[1])
			print i.co_ordinate
		p.pause(0.1)


if __name__ == '__main__':
	main()
