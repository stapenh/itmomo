import pandas as pd

data = {
    'Имя': ['Анна', 'Иван', 'Мария', 'Петр'],
    'Возраст': [25, 30, 22, 35],
    'Город': ['Москва', 'Санкт-Петербург', 'Киев', 'Минск']
}

df = pd.DataFrame(data)
print(df)
