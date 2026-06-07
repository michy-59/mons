import pandas as pd

def main(csv_path):
    df = pd.read_csv(csv_path)
    print(len(df))

if __name__=='__main__':
    csv_path = "prob.csv"
    main(csv_path)