from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj):

	dist = {} #record the distance from source to source
	prev = {}
	alt = 0
	dist[src] = alt
	prev[src] = None
	queue = []
	heappush(queue, src)

	while queue:
		node = heappop(queue) #source node in first case

		if node == dst: # if the current node is the destination, then stop loop
			break

		neighbors = adj(graph, node)
		for curNeighbor in neighbors:
			x, y = node #current coordinate of current node
			dx, dy = curNeighbor # current coordinate of current neighbor
		
			#calculate distance from current node to current neighbor
			alt = sqrt(((x-dx)*(x-dx))+((y-dy)*(y-dy))) + dist[node] 
			if curNeighbor not in dist or alt < dist[curNeighbor]:
				dist[curNeighbor] = alt
				prev[curNeighbor] = node
				heappush(queue, curNeighbor)
					
	if node == dst:
		path = []
		while node:
			path.append(node)
			node = prev[node]
		path.reverse()
		return path
	else:
		return []

#to return all the neighbors of current node
def navigation_edges(level, cell): 
	adj = [] #to record all the neighbor nodes
	x, y = cell
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			next_cell = (x + dx, y + dy)
			distance = sqrt(dx*dx+dy*dy)
			#if distance from current node to neighbor node is greater than 0
			#and is a dot/space, then append nextcell to neighbors[]
			if distance > 0 and next_cell in level['spaces']: 
				adj.append(next_cell)
			#if distance from current node to neighbor node is greater than 0
			#and is a way point, then append nextcell to neighbors[]
			elif distance > 0 and next_cell in level['waypoints']:
				adj.append(next_cell)
	return adj

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
