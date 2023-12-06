import pandas as pd

pesos = {
    "Organic Impressions" : 0.1,
    "Paid Impressions" : 0.1,
    "Organic reach" : 0.1,
    "Paid Reach" : 0.1,
    "TOP2 Social Media" : 0.2,
    "Interacions per Follwers" : 0.1,
    "Interacions per Impressions" : 0.1,
    "Comments health" : 0.08,
    "Content Retention rate" :0.06 ,
    "Social NPS" : 0.06
}

#df = pd.read_excel("SCOREs.xlsx")

def calculateTotal(df):
    aux_list = []
    df2 = pd.DataFrame()
    for peso in pesos:
        aux_list = []
        for index, value in  df[peso].items():                
            aux_list.append(float(value) * float(pesos[peso]))
        df2[peso] = aux_list
        
    df2["Total"] = df2.sum(axis=1)
    return df2


def getTest(a, b):
    
    data  = {"col1": [a], "col2":[b]}
    df = pd.DataFrame(data=data)
    
    return df