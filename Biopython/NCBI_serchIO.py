# blast の結果をsearchIOで解析する。

import sys
from Bio import SearchIO

blast_qresults = SearchIO.parse(sys.argv[1], "blast-xml")

for blast_qresult in blast_qresults:
    #結果全体を表示したい場合
    print(blast_qresult)

    # top 3 hits
    print(blast_qresult[:2])

    # hsp までblastの結果全体を表示
    for hit in blast_qresult:
        for hsp in hit:
            print(hsp)

    # accessionがNM_******となっているもののみ取り出す
    for hit in blast_qresult:
        if hit.accession.startswith("NM"):
            for hsp in hit:
                print(hsp)