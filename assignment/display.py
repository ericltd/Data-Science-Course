import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pandas as pd
import json

x = np.array([1,8])
y=np.array([3,12])



gamestop = yf.Ticker("GME")





gamestop_info = gamestop.info

history=gamestop.history(period="max")


gs_df = pd.DataFrame(history)
#print(gs_df.tail())
#print(tesla_df.tail())

#print(tesla_info.keys())
#print(gamestop_info["displayName"])


plt.plot(history)
plt.title("GameStop Stock History")
plt.show()


"""

tesla = yf.Ticker("TSLA")




#print(tesla)
tesla_info = tesla.info

history=tesla.history(period="max")


tesla_df = pd.DataFrame(history)
print(history)
#print(tesla_df)
history_head = tesla_df.head()
#print(tesla_df.tail())

#print(tesla_info.keys())
#print(tesla_info["displayName"])




plt.plot(history)
plt.title("Tesla Stock History")
plt.show()

"""









