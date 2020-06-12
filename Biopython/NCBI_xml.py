# blast で出力したxmlを表示する。
# serchIOを使った方が扱いやすいのでそちらを推奨。

# python NCBI_xml.py hoge.xml

import sys
from Bio.Blast import NCBIXML

result_handle = open(sys.argv[1])
blast_records = NCBIXML.parse(result_handle)

#e_valueの下限を決める
E_VALUE_THRESH = 1e-10

for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                print("****Alignment****")
                print("sequence:", alignment.title)
                print("length:", alignment.length)
                print("e value:", hsp.expect)
                print(hsp.query[0:75] + "...")
                print(hsp.match[0:75] + "...")
                print(hsp.sbjct[0:75] + "...")

result_handle.close()