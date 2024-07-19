# import pandas
import pandas as pd

data = {
    'animal': [
        'cheetah', 'elephant', 'giraffe', 'zebra', 'rhino',
        'falcon', 'parrot', 'lion', 'monkey', 'leopard'
    ],
    'class': [
        'mammal', 'mammal', 'mammal', 'mammal', 'mammal',
        'bird', 'bird', 'mammal', 'mammal', 'mammal'
    ],
    'order': [
        'Carnivora', 'Proboscidea', 'Artiodactyla',
        'Perissodactyla', 'Perissodactyla', 'Falconiformes',
        'Psittaciformes', 'Carnivora', 'Primates', 'Carnivora'
    ],
    'max_speed': [
        120.0, 40.0, 60.0, 65.0, 55.0,
        389.0, 24.0, 80.2, None, 58.09
    ]
}

# Creating the DataFrame
df = pd.DataFrame(data)
print(df)

# Split-Apply-Combine
# avg_speed = df.groupby('class')['max_speed'].mean().reset_index()
avg_speed = df.groupby('order')['max_speed'].mean(
).sort_values().reset_index()

# Displaying the result
print(avg_speed)
