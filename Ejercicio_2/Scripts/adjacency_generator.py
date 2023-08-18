def generate_complete_graph_adjacency_list(num_vertices):
    adjacency_list = []
    for i in range(0, num_vertices):
        for j in range(i + 1, num_vertices):
            adjacency_list.append((i, j))
    return adjacency_list

def generate_list_to_file(adjacency_list, file_path):
    with open(file_path, 'w') as file:
        for edge in adjacency_list:
            file.write(f"{edge[0]} {edge[1]}\n")

if __name__ == "__main__":
    num_vertices = int(input("Ingrese el número de vértices: "))
    adjacency_list = generate_complete_graph_adjacency_list(num_vertices)
    file_path = "..\Data\ADJACENCY_LIST_"+ str(num_vertices)+".txt"
    generate_list_to_file(adjacency_list, file_path)
    print(f"La lista de adyacencias se ha guardado en '{file_path}'.")
