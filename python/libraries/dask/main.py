import csv
import dask.dataframe as dd


"""
Here you can see some methods of dask library
"""
df = dd.read_csv('simplef.csv').compute()
    df = df.dropna(subset=['title1'])
    df = df.drop_duplicates(subset=['title1'], keep=False)
    df1 = df['title1'].isin(listma)
    df_people = df[df1].drop_duplicates(subset=['title1']) 

    df_people['title1'] = df_people['national_code'].replace(listma, listma1)
    df_people['title2'] = df_people['title2'].replace(dp_reas_code_list, dp_reas_id_list)
    df_people['title3'] = df_people['title3'].replace(susp_reas_code_list, susp_reas_id_list)

    df_people = df_people.rename(columns={"title1": "title1_id", "title2": "title2_id", "title3": "title3_id"})
    df_people.to_csv('answer.csv')