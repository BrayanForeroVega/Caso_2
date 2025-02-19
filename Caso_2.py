from collections import deque  
import heapq  

# Definición del grafo (ciudades y rutas con distancias)  
graph = {  
    'Tunja': {'Bogotá': 150, 'Duitama': 50},  
    'Bogotá': {'Tunja': 150, 'Manizales': 300, 'Medellín': 250},  
    'Duitama': {'Tunja': 50, 'Sogamoso': 30},  
    'Sogamoso': {'Duitama': 30, 'Manizales': 200},  
    'Medellín': {'Bogotá': 250, 'Manizales': 100},  
    'Manizales': {'Bogotá': 300, 'Medellín': 100, 'Sogamoso': 200}   
   
}  

# Heurística: Distancia en línea recta estimada a Manizales (valores ficticios)  
heuristic = {  
    'Tunja': 250,  
    'Bogotá': 200,  
    'Duitama': 220,  
    'Sogamoso': 180,  
    'Medellín': 50,  
    'Manizales': 0   
}  

# Algoritmo A*  
def a_star(graph, start, goal, heuristic):  
    open_set = []  
    heapq.heappush(open_set, (0, start))  
    came_from = {}  
    g_score = {city: float('inf') for city in graph}  
    g_score[start] = 0  
    f_score = {city: float('inf') for city in graph}  
    f_score[start] = heuristic[start]  

    while open_set:  
        _, current = heapq.heappop(open_set)  

        if current == goal:  
            path = []  
            while current in came_from:  
                path.append(current)  
                current = came_from[current]  
            path.append(start)  
            return path[::-1]  

        for neighbor, distance in graph[current].items():  
            tentative_g_score = g_score[current] + distance  
            if tentative_g_score < g_score[neighbor]:  
                came_from[neighbor] = current  
                g_score[neighbor] = tentative_g_score  
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]  
                heapq.heappush(open_set, (f_score[neighbor], neighbor))  

    return None  

# Ejecución del algoritmo  
start = 'Tunja'  
goal = 'Manizales'  
path = a_star(graph, start, goal, heuristic)  
print(f"Ruta más corta: {path}")
