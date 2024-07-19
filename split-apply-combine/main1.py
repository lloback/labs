# import pandas
import pandas as pd

# Creating the DataFrame
data = {
    'animal': ['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
    'class': ['bird', 'bird', 'mammal', 'mammal', 'mammal'],
    'order': [
        'Falconiformes', 'Psittaciformes', 'Carnivora',
        'Primates', 'Carnivora'
    ],
    'max_speed': [389.0, 24.0, 80.2, None, 58.09]
}
df = pd.DataFrame(data)
# print(df)

# Split-Apply-Combine
avg_speed = df.groupby('class')['max_speed'].mean().reset_index()

# Displaying the result
print(avg_speed)
