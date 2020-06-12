# NCBI のEntrez からsra のデータを取り出す。


from Bio import Entrez
# https://biopython.org/
import xml.etree.ElementTree as ET
# xmlの操作モジュール

class SraData:

    # 引数: sra_no: sraの番号　srr, srx, srp など
    #      email: 使用者のemail address

    def __init__(self, sra_no, e_mail):
        # ncbi にemail address を伝える
        Entrez.email = e_mail

        self.sra_no = sra_no
        self.ids = []
        self.spots = dict()

        # sraの番号を Entrez 用の id に変換
        handle = Entrez.esearch(db="sra", term=self.sra_no, retmax=2000)
        record = Entrez.read(handle)
        self.ids = record["IdList"]

    def sra_spots(self):
        # id から　efetch してspot数を辞書に追加。辞書を return
        # 毎秒1ファイル程度。数が多いと時間がかかるので注意。
        for id in self.ids:
            handle = Entrez.efetch(db="sra", id=id)
            tree = ET.parse(handle)
            for node in tree.iter():
                if node.tag == "RUN":
                    self.spots[node.attrib['accession']] = node.attrib['total_spots']
        return self.spots


def main():
    # 使用例
    sra = "SRR*******"
    email = "example@email.com"
    sr1 = SraData(sra, email)
    print(sr1.sra_spots())


if __name__ == '__main__':
    main()