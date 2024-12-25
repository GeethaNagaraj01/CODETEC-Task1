import pandas as pd
data = {
    'Name': ['Arthi', 'Rethu', 'Boomi', 'Dhanya', 'Kavi', 'Sree', 'Deepi', 'Hema', 'Vanu', 'Jeevasri', 'Jeevi'],
    'Age': [20, 22, 21, 19, 24, 23, 18, 25, 22, 26, 27],
    'City': ['Pollachi', 'Coimbatore', 'Kodaikanal', 'Ooty', 'Delhi', 'Newyork', 'Goa', 'Mysore', 'Kochin', 'Madurai', 'Dindukal'],
    'Salary': [20000, 24000, 23000, 25000, 19000, 26000, 23700, 34000, 29000, 34000, 27000]
}
df = pd.DataFrame(data)
df.to_csv('my_dataset.csv', index=False)
print("Dataset created and saved as 'my_dataset.csv'")
