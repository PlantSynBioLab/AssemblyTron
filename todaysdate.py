from datetime import date
import pandas as pd

today = date.today()

date = str(today.strftime('%Y%m%d'))

datedf = pd.DataFrame(data = [date],columns = ['Date'])

datedf.to_csv('todaysdate.csv')
