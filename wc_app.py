import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv("text.csv")

df.columns = df.columns.str.strip()  # remove unwanted spaces

print(df.columns)  # debug

text = " ".join(df.iloc[:, 0].dropna().astype(str))

wc = WordCloud().generate(text)

plt.imshow(wc)
plt.axis("off")
plt.show()
