import pandas as pd


df = pd.read_csv('data.csv').set_index('Id')


set_test_data = df.sample(frac=0.2)
set_train_data = df.drop(set_test_data.index)
set_data = pd.concat([set_train_data, set_test_data])


__all__ = ['set_data', 'set_test_data', 'set_train_data']