
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\User\Documents\Pandas Practice\analyst_ratings_processed.csv")


class mnp_dataframe:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def grouped(self):
        df_stock = self.dataframe[['stock','date']].groupby('stock').min()
        return(df_stock)
    
    def printed(self):
        return print(self.dataframe)


#stocked = mnp_dataframe(df)
#stocked.printed()

#print(stocked.grouped())



class dataframe_with_cols:

    def __init__(self, dataframe):
        self.dataframe = dataframe



    def out(self,stock_col, date_col):

        out = self.dataframe[[stock_col, date_col]].groupby(stock_col).min()
        return print(out)
    
    def print_dataframe_after(self):
        return print(len(self.dataframe))
    
    def str_test(self, col):
        return(self.dataframe[col].str[1:])
    
    def if_then(self, col):
        conditional = self.dataframe[col].apply(lambda x: 1 if x =='A' else 0 )
        return(print(conditional))
    
    def if_then_multiple(self,col):
        conditional =self.dataframe[col].apply(lambda x: np.where(x == 'A', 1, np.where(x =='AAMC',2,np.where(x == 'AAME',3,np.where(x =='ZX',10,4)))))
        return(print(conditional))
    
    def print_dataframe(self):
        return(print(self.dataframe))
    
    def date_format(self, col):
        return self.dataframe['date'].str[:10]
    


class ChangeDataFrame():
    def __init__(self, dataframe):
        self.dataframe =dataframe
    
    def apply_if_statement(self, col_name):
        return self.dataframe[col_name].apply(lambda x: x[5:] if x.startswith('ABC') else x[4:] if x.startswith('AB') else x)


import pandas as pd

list_ = ['ABC::1234545432', 'AB23423432']

df =pd.DataFrame(data = list_,columns = ['Account'])


modifier = ChangeDataFrame(df)
df['modified'] =modifier.apply_if_statement(col_name= 'Account')



df['mod'] = df['Account'].apply(lambda x: x[5:] if x.startswith('ABC') else x)
print(df)


    
stocked1 = dataframe_with_cols(df)
stocked1.out(stock_col='stock',date_col= 'date')
stocked1.print_dataframe_after()
print(stocked1.str_test('date'))
stocked1.print_dataframe()
stocked1.if_then_multiple('stock')

stocked2 =mnp_dataframe(df)
stocked2.grouped()

stocked1.if_then_multiple(col ='stock')
    
    




