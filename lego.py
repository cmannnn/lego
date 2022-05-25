# imports modules
import pandas as pd
import matplotlib.pyplot as plt
# read colors data
colors = pd.read_csv('colors.csv.gz')

# print the first few rows
print(colors.head())

# how many distinct colors are available?
num_colors = colors.shape[0]

# summarize colors based on transparacy
colors_summary = colors.groupby(['is_trans']).count()

# print summarization based on transparacy
# print(colors_summary)

# summarize of the average parts per year

# read sets data
sets = pd.read_csv('sets.csv.gz')

# summary of average number of parts by year
parts_by_year = sets[['year', 'num_parts']].\
groupby('year', as_index = False).sum()

# plot trends in average number of parts by year
parts_by_year.plot(x = 'year', y = 'num_parts')
plt.xlabel('year') 
plt.ylabel('number of parts')
plt.title('Lego Parts 1950-2020')

# show graph
# plt.show()

# summary of the number of themes shipped by year
themes_by_year = sets[['year', 'theme_id']].\
groupby('year', as_index = False).\
agg({'theme_id': pd.Series.count})

#print head
#print(themes_by_year.head())