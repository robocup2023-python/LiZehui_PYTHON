import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--path', help='Path to the CSV file')
parser.add_argument('--number', type=int, help='Column number to be deleted')
args = parser.parse_args()
df = pd.read_csv(args.path)
df = df.drop(df.columns[args.number], axis=1)
df['sum_column'] = df['column1'] + df['column2']
print(df)
