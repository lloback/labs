# Creating the data
from collections import defaultdict

data = [
    {'animal': 'falcon', 'class': 'bird',
        'order': 'Falconiformes', 'max_speed': 389.0},
    {'animal': 'parrot', 'class': 'bird',
        'order': 'Psittaciformes', 'max_speed': 24.0},
    {'animal': 'lion', 'class': 'mammal', 'order': 'Carnivora', 'max_speed': 80.2},
    {'animal': 'monkey', 'class': 'mammal', 'order': 'Primates', 'max_speed': None},
    {'animal': 'leopard', 'class': 'mammal',
        'order': 'Carnivora', 'max_speed': 58.09}
]

# Grouping by class and calculating average speed
grouped_data = defaultdict(lambda: {'total_speed': 0, 'count': 0})

for entry in data:
    class_name = entry['class']
    max_speed = entry['max_speed']
    if max_speed is not None:
        grouped_data[class_name]['total_speed'] += max_speed
        grouped_data[class_name]['count'] += 1

avg_speed = [{'class': class_name, 'avg_speed': (info['total_speed'] / info['count'])}
             for class_name, info in grouped_data.items()]

# Displaying the result
print(avg_speed)
