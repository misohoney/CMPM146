from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj):

	dist = [] #record the distance from source to source
	prev = []
	distance = 0
	dist[src] = 0
	prev[src] = None
	queue = [src]

	while queue:
		node = heappop(queue) #source node in first case

		if node == dst: # if the current node is the destination, then stop loop
			break

		neighbors = adj(graph, node)
		for curNeighor in neighbors:
			x, y = node #current coordinate of current node
			dx, dy = curNeighbor # current coordinate of current neighbor
			if curNeighbor not in prev: #make sure we're not going backward
				#calculate distance from current node to current neighbor
				alt = sqrt((x+dx)*(x+dx)+(y+dy)*(y+dy)) + dist[node] 
				if curNeighbor not in dist or alt < dist(curNeighbor)
					or alt < dist.get(curNeighbor, alt+1)

					dist[curNeighbor] = alt
					




					#prev[next_node] = node






				#prev[next_node] = node
				#stack.append(next_node)

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
    neighbors = [] #to record all the neighbor nodes
	x, y = cell
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			next_cell = (x + dx, y + dy)
			distance = sqrt(dx*dx+dy*dy)
			#if distance from current node to neighbor node is greater than 0
			#and is a dot/space, then append nextcell to neighbors[]
			if distance > 0 and next_cell in level['spaces']: 
				neighbors.append(next_cell)
			#if distance from current node to neighbor node is greater than 0
			#and is a way point, then append nextcell to neighbors[]
			elif distance > 0 and next_cell in level['waypoints']:
				neighbors.append(next_cell)
	return neighbors

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
