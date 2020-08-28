import loompy

ds = loompy.connect("dev_all.loom")

ages = ds.ca["Age"] 
pseudoages = ds.ca["PseudoAge"]
tsne = ds.ca["TSNE"]
umap = ds.ca["UMAP"]

Cux1 = ds[ds.ra.Gene == 'Cux1', :]
Cux2 = ds[ds.ra.Gene == 'Cux2', :]
Brn2 = ds[ds.ra.Gene == 'Pou3f2', :]
Rorb = ds[ds.ra.Gene == 'Rorb', :]

ds.close()

output = open('200827_bioinfo.csv','w')

for i in range(0,len(ages)):
	print(ages[i],file=output,end=',')
	print(pseudoages[i],file=output,end=',')
	print(tsne[i],file=output,end=',')
	print(umap[i],file=output,end=',')
	print(Cux1[0][i],file=output,end=',')
	print(Cux2[0][i],file=output,end=',')
	print(Brn2[0][i],file=output,end=',')
	print(Rorb[0][i],file=output,end='\n')

output.close()
