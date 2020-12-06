
setwd('~/Desktop/201203_bioinfo')

library(dplyr)
library(Seurat)
library(patchwork)
library(ggplot2)
library(cowplot)
library(data.table)

#mat <- fread("zcat < exprMatrix.tsv.gz")
mat <- fread("exprMatrix.tsv")
meta <- read.table("meta.tsv", header=T, sep="\t", as.is=T, row.names=1)
genes = mat[,1][[1]]
genes = gsub(".+[|]", "", genes)
mat = data.frame(mat[,-1], row.names=genes)

cortex <- CreateSeuratObject(counts = mat, project = "cortex", meta.data=meta)

cortex <- NormalizeData(cortex, normalization.method = "LogNormalize", scale.factor = 10000)
cortex <- FindVariableFeatures(cortex, selection.method = "vst", nfeatures = 1000, verbose = FALSE)

all.genes <- rownames(cortex)
cortex <- ScaleData(cortex,features = all.genes)
cortex <- RunPCA(cortex,features = VariableFeatures(object = cortex))
cortex <- FindNeighbors(cortex,dims=1:10)
cortex <- FindClusters(cortex,resolution = 0.5)
cortex <- RunUMAP(cortex,dims = 1:10)

#201008 DimPlot
DimPlot(cortex, reduction = "umap", group.by = "orig.ident",label=T,pt.size=0.01)
DimPlot(cortex, reduction = "umap", group.by = "Age_in_Weeks",label=T,pt.size=0.01)
DimPlot(cortex, reduction = "umap", group.by = "Area",label=T,pt.size=0.01)
DimPlot(cortex, reduction = "umap", group.by = "RegionName",label=T,pt.size=0.01)
#DimPlot(cortex, reduction = "umap", group.by = "WGCNAcluster",label=T,pt.size=0.01)
DimPlot(cortex, reduction = "umap", group.by = "seurat_clusters",　label=T,　pt.size=0.01)

#201008 FeaturePlot
FeaturePlot(cortex,features = "DAB1",reduction = "umap")
FeaturePlot(cortex,features = "RELN",reduction = "umap")
FeaturePlot(cortex,features = c("DAB1", "RELN"),reduction = "umap")

#201008 write.table
cortex.umap<-as.matrix(cortex@reductions$umap@cell.embeddings)
cortex.seurat_clusters<-as.matrix(cortex@meta.data$seurat_clusters)

write.table(cortex.umap, file="cortex_umap.txt",sep="\t")
write.table(cortex.seurat_clusters,file="cortex_seurat_clusters.txt",sep="\t")

#201022 VariableFeatures
write.csv(VariableFeatures(cortex),"cortex_VariableFeatures.txt")

#201022 png
png(filename="cortex_top9.png", width=1000, height=1000)
FeaturePlot(cortex,features = c('SPP1', 'COL1A2', 'RGS1', 'CCL3L3', 'COL1A1', 'SPARC', 'COL3A1', 'CXCL8', 'TTR'),reduction = "umap")
dev.off()

#201029 FindAllMarkers
markers <- FindAllMarkers(cortex, only.pos = TRUE, min.pct = 0.25, logfc.threshold = 0.25)
write.csv(markers,"cortex_markers.txt")

#201029 DoHeatmap
top10 <- markers %>% group_by(cluster) %>% top_n(n = 10, wt = avg_logFC)
DoHeatmap(cortex, features = top10$gene) + NoLegend()

#201029 VlnPlot
VlnPlot(cortex, features = c("DAB1","RELN"), slot = "counts", log = TRUE)

#201126 subset by seurat_cluster
cortex_c3 <- subset(cortex, idents = c("3"))
cortex_c9 <- subset(cortex, idents = c("9"))

#201126 subset by an expressed gene
cortex_DAB1 = subset(x = cortex, subset = DAB1 > 0, slot = 'counts')
cortex_RELN = subset(x = cortex, subset = RELN > 0, slot = 'counts')
