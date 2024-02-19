import pandas as pd


import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


categories = sorted(set(data['whoAmI']))
one_hot_encoding = {category: [1 if value == category else 0 for value in categories] for category in categories}

one_hot_encoded_data = pd.DataFrame(data['whoAmI'].apply(lambda x: one_hot_encoding[x]).tolist(), columns=categories)


data_encoded = pd.concat([data, one_hot_encoded_data], axis=1)


data_encoded.drop('whoAmI', axis=1, inplace=True)

data_encoded.head()
