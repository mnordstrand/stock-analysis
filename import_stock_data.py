# Instructions used from https://www.youtube.com/watch?v=momk1LLABPT
import datetime
import matplotlib.pyplot as plt
import quandl
from api_quandl import api

# Below two statements (line 7 and 8) were added as PyCharm warned that converters for Datetime was needed for Pandas.
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

start = datetime.datetime(2016, 1, 1)
end = datetime.date.today()

quandl_data = quandl.get("EOD/AAPL", start_date = '2001-01-01', end_date = '2019-05-10', paginate = True)

plt.plot(quandl_data)
plt.show()
print(quandl_data)