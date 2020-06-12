# biopythonでblast検索
# ターミナルで python NCBI_blast.py hoge.fa(sta)　で実行。 hoge.xmlを出力。

import sys
import re
from Bio.Blast import NCBIWWW

fasta = open(sys.argv[1]).read()

# qblast("手法","データベース",fasta)　
# help(NCBIWWW.qblast)
result_handle = NCBIWWW.qblast("blastn", "nt", fasta)

with open(re.sub(r'\.fa(|sta)$', '.xml', sys.argv[1]), "w") as out_handle:
    out_handle.write(result_handle.read())

result_handle.close()

