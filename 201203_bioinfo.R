
#201203 bioinfo (advanced)

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

DimPlot(cortex, reduction = "umap", group.by = "seurat_clusters",label=T,pt.size=0.01)

markers <- FindAllMarkers(cortex, only.pos = TRUE, min.pct = 0.25, logfc.threshold = 0.25)
write.csv(markers,"cortex_markers.txt")
