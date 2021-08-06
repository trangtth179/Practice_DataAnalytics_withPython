#%% Import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import ssl
#%% - some configs
plt.rcParams['figure.figsize'] = (10,8)
plt.rcParams['figure.dpi'] = 200
plt.rcParams['font.size'] = 13
#%% Import data
df = pd.read_csv('./Data/NetProfit.csv')
dat = df[['Year','VIC']]
print(dat)
plt.plot('Year','VIC', data = dat, color = '#FF0000')
plt.show()

plt.plot('Year', 'VNM', data=df, color='b',linestyle='-', marker='o')
plt.plot('Year', 'PNJ', data=df, color='g',  linestyle='--', marker='s')
plt.plot('Year', 'VCB', data=df,  color='#FF0000', linestyle=':',  marker='+')
plt.plot('Year', 'VIC', data=df,  color='orange', linestyle='-.', marker='*')
plt.title("Lợi nhuận của VNM, PNJ, VCB,  VIC từ 2010 đến 2020", fontweight='bold')
plt.xlabel("Năm", fontweight='bold')
plt.ylabel("Lợi nhuận", fontweight='bold')
plt.legend()
plt.show()

#%% Scatter
df = pd.read_csv('./Data/Income.csv')
colors = np.random.rand(df.shape[0]) # random colors
area = df['Income'].values*50
plt.scatter('Income','Expenditure', data = df, c = colors, s = area, alpha= 0.8)
plt.xlabel("Income")
plt.ylabel("Expenditure")
plt.show()

#%%
dat = np.random.normal(12, 2, 400)
plt.hist (dat, color = 'darkgreen', edgecolor = 'orange')
plt.show()

#%%
lbls = ['Chuyển nhượng BĐS', 'Cho thuê  BĐS', 'DV khách sạn', 'Bệnh viện', 'Giáo  dục', 'Sản xuất', 'Hoạt động khác']
income = [71.576, 6.788, 4.869, 2.675,2.244, 18.007, 4.304]
explode = [0.1, 0.1,0.2, 0.2, 0.1, 0.1, 0.2]
plt.pie(income, labels=lbls, explode = explode, autopct= '%1.1f%%', pctdistance=1.1, labeldistance=1.2)
plt.title("Cơ cấu doanh thu VinGroup- 2020", fontweight = 'bold')
plt.show()

#%% Biểu đồ Boxplot
df = pd.read_csv('./Data/Salary_of_Developer.csv')
orange_square = dict(markerfacecolor = 'orange', marker = 's')
plt.boxplot(df, vert =False, flierprops=orange_square)
plt.xlabel("Lương")
plt.title ("Biểu đồ thể hiện phân bổ mức lương lập trình viên")
plt.show()

#%% Biểu đồ kết hợp
plt.figure(figsize=(18, 12), dpi=200)
#Biểu đồ cột
plt.subplot(2,2,1)
df = pd.read_csv('./Data/NetProfit.csv')
dat = df[['Year','VIC']]
plt.plot('Year', 'VNM', data=df, color='b',linestyle='-', marker='o')
plt.plot('Year', 'PNJ', data=df, color='g',  linestyle='--', marker='s')
plt.plot('Year', 'VCB', data=df,  color='#FF0000', linestyle=':',  marker='+')
plt.plot('Year', 'VIC', data=df,  color='orange', linestyle='-.', marker='*')
plt.title("Lợi nhuận của VNM, PNJ, VCB,  VIC từ 2010 đến 2020", fontweight='bold')
plt.xlabel("Năm", fontweight='bold')
plt.ylabel("Lợi nhuận", fontweight='bold')
plt.legend()
#Biểu đồ scatter
plt.subplot(2,2,2)
df = pd.read_csv('./Data/Income.csv')
colors = np.random.rand(df.shape[0]) # random colors
area = df['Income'].values*50
plt.scatter('Income','Expenditure', data = df, c = colors, s = area, alpha= 0.8)
plt.xlabel("Income")
plt.ylabel("Expenditure")

#Biểu đồ
plt.subplot(2,2,3)
dat = np.random.normal(12, 2, 400)
plt.hist (dat, color = 'darkgreen', edgecolor = 'orange')

#Biểu đồ
plt.subplot(2,2,4)
lbls = ['Chuyển nhượng BĐS', 'Cho thuê  BĐS', 'DV khách sạn', 'Bệnh viện', 'Giáo  dục', 'Sản xuất', 'Hoạt động khác']
income = [71.576, 6.788, 4.869, 2.675,2.244, 18.007, 4.304]
explode = [0.1, 0.1,0.2, 0.2, 0.1, 0.1, 0.2]
plt.pie(income, labels=lbls, explode = explode, autopct= '%1.1f%%', pctdistance=1.1, labeldistance=1.2)
plt.title("Cơ cấu doanh thu VinGroup- 2020", fontweight = 'bold')
plt.show()

#%% Thư viện seaborn
ssl._create_default_https_context = ssl._create_unverified_context


