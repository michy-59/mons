import pandas as pd

def align_prob(csv_path):
    df = pd.read_csv(csv_path)
    df = df.sort_values(['year', 'no'])
    df = make_blank(df)
    df.to_csv(csv_path,index=0)
    return df

def make_blank(df):
    df['prob'] = df['prob'].apply(lambda x: x.replace('**', '（    ）'))
    return df

def check_duplication(df):
    df_u = df.groupby(['year', 'no'])['prob'].count().reset_index()
    df_u = df_u.rename(columns={'prob': 'cnt'})
    df_u = df_u[df_u['cnt'] > 1].reset_index(drop=True)

    if len(df_u) == 0:
        print('OK')
        print(len(df))
    else:
        print(df_u)

def main(csv_path):
    df = align_prob(csv_path)
    check_duplication(df)

if __name__=='__main__':
    csv_path = 'prob.csv'
    main(csv_path)