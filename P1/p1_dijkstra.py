from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj):
	dist = {} #record the distance from source to source
	visited = {} #visited nodes
	dist[src] = 0 # set distance of first source to 0
	visited[src] = None #set that no node has been visited yet
	alt = 0 #shortest path record
	queue = [] #priority queue
	heappush(queue,src) #push first source to queue

	while queue: #while queue is not empty
		node = heappop(queue) #source node in first case
		
		if node == dst: # if the current node is the destination, then stop loop
			break
		
		neighbors = adj(graph, node) #check coor of all neighbors and if any exists
		
		for curNeighbor in neighbors: #starting from the bottom left neighbor
			x, y = node #current coordinate of current node
			dx, dy = curNeighbor # current coordinate of current neighbor
			alt = sqrt(((x-dx)*(x-dx))+((y-dy)*(y-dy))) + dist[node] #calculate distance from current node to current neighbor		
			if curNeighbor not in dist or alt < dist[curNeighbor]: #compare and records the shorter path
				dist[curNeighbor] = alt 
				visited[curNeighbor] = node
				heappush(queue, curNeighbor)

	if node == dst:
		path = []
		while node:
			path.append(node)
			node = visited[node]
		path.reverse()
		return path
	else:
		return []

#to return all the neighbors of current node
def navigation_edges(level, cell): 
	neighborNodes = [] #to record all the neighbor nodes
	x, y = cell
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			next_cell = (x + dx, y + dy)
			distance = sqrt(dx*dx+dy*dy)
			#if distance from current node to neighbor node is greater than 0
			#and is a dot/space, then append nextcell to neighbors[]
			if distance > 0 and next_cell in level['spaces']: 
				neighborNodes.append(next_cell)
			#if distance from current node to neighbor node is greater than 0
			#and is a way point, then append nextcell to neighbors[]
			elif distance > 0 and next_cell in level['waypoints']:
				neighborNodes.append(next_cell)
	return neighborNodes

def test_route(filename, src_waypoint, dst_waypoint):
	level = load_level(filename)

	show_level(level)

	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]

	path = dijkstras_shortest_path(src, dst, level, navigation_edges)

	if path:
		show_level(level, path)
	else:
		print "No path possible!"

if __name__ ==  '__main__':
	import sys
	_, filename, src_waypoint, dst_waypoint = sys.argv
	test_route(filename, src_waypoint, dst_waypoint)
