from collections import defaultdict
import networkx as nx


def load_data():
    with open('./input/day07.txt', 'r') as f:
        return [(line[5], line[36]) for line in f.read().strip().split('\n')]


def create_graph(data):
    G = nx.DiGraph()
    for line in data:
        G.add_edge(line[0], line[1])
    return G


def part_one(G):
    return ''.join(nx.lexicographical_topological_sort(G))


def part_two(G):
    task_times = []
    tasks = []
    time = 0
    while task_times or G:
        available_tasks = [
            t for t in G if t not in tasks and G.in_degree(t) == 0]
        if available_tasks and len(task_times) < 5:
            # min gets smallest task alphabetically
            task = min(available_tasks)
            task_times.append(ord(task) - 4)
            tasks.append(task)
        else:
            min_time = min(task_times)
            completed = [tasks[i] for i, v in enumerate(task_times) if v == min_time]
            task_times = [v - min_time for v in task_times if v > min_time]
            tasks = [t for t in tasks if t not in completed]
            time += min_time
            G.remove_nodes_from(completed)
    return time


if __name__ == '__main__':
    data = load_data()
    G = create_graph(data)
    print(part_one(G))
    print(part_two(G))
