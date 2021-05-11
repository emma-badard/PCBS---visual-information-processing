
#file=input("Give a name to your data file :")
#results = pandas.read_csv("data/final_code_{}.xpd".format(file), comment="#")

#results = pandas.read_csv("data/final_code_01_202105070005.xpd", comment ="#")
#print(resu

#Récupération des données
import pandas 
import glob
import matplotlib.pyplot as plt
import seaborn 

datas = []
for datafile in glob.glob('data/*.xpd'):
	datas.append(pandas.read_csv(datafile, comment='#'))
data = pandas.concat(datas)

#Suppression du training set 
test_set = data[data.Block == "Test set 1"]

#Calcul du RT moyen sur les essais corrects par condition
correct = test_set[test_set.Accuracy]
means_RT = correct.RT.groupby([correct.Condition]).mean()
print(means_RT)
seaborn.barplot(x = correct.Condition, y = correct.RT)
plt.show()

#Calcul du pourcentage de réponses correctes par condition
accuracy = test_set.Accuracy.groupby([test_set.Condition]).mean()
print(accuracy)

seaborn.barplot(x = test_set.Condition, y = test_set.Accuracy)
plt.show()

#files = glob.glob('data/*.xpd')
#df_from_each_file = (pandas.read_csv(f) for f in files)
#print (df_from_each_file)

#concatenated_df   = pandas.concat(df_from_each_file, ignore_index=True)
#print(concatenated_df)
#mean_RT_per_condition = data.groupby('Condition')['RT'].mean()
#print(mean_RT_per_condition)




