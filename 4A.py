def get_genetic_code_codons():
    genetic_code = {
        "AAA": "K",
        "AAC": "N",
        "AAG": "K",
        "AAU": "N",
        "ACA": "T",
        "ACC": "T",
        "ACG": "T",
        "ACU": "T",
        "AGA": "R",
        "AGC": "S",
        "AGG": "R",
        "AGU": "S",
        "AUA": "I",
        "AUC": "I",
        "AUG": "M",
        "AUU": "I",
        "CAA": "Q",
        "CAC": "H",
        "CAG": "Q",
        "CAU": "H",
        "CCA": "P",
        "CCC": "P",
        "CCG": "P",
        "CCU": "P",
        "CGA": "R",
        "CGC": "R",
        "CGG": "R",
        "CGU": "R",
        "CUA": "L",
        "CUC": "L",
        "CUG": "L",
        "CUU": "L",
        "GAA": "E",
        "GAC": "D",
        "GAG": "E",
        "GAU": "D",
        "GCA": "A",
        "GCC": "A",
        "GCG": "A",
        "GCU": "A",
        "GGA": "G",
        "GGC": "G",
        "GGG": "G",
        "GGU": "G",
        "GUA": "V",
        "GUC": "V",
        "GUG": "V",
        "GUU": "V",
        "UAA": "*",
        "UAC": "Y",
        "UAG": "*",
        "UAU": "Y",
        "UCA": "S",
        "UCC": "S",
        "UCG": "S",
        "UCU": "S",
        "UGA": "*",
        "UGC": "C",
        "UGG": "W",
        "UGU": "C",
        "UUA": "L",
        "UUC": "F",
        "UUG": "L",
        "UUU": "F",
    }

    return genetic_code

def Translation(dna):
    D=get_genetic_code_codons()
    amino=[]
    for i in range(0,len(dna),3):
        codon=dna[i:i+3]
        am=D[codon]
        if am=="*":
            break
        amino.append(am)
    return "".join(amino)

rna="AUGCUCACCCAUCAGAAGUGUCCUAUUCCUCACCAAUAUCGGUCCCUAUUACAACGAAAUGUGCGGGUGCGUUGGAUGCGUACUUAUUGGGAGUCCUUCCGGUAUAGUAUUGCUGGUCCAACUGCUUCGUUUAUCCUAUACAGGGCGCAUAGGCUGGUGUUAAUAUUACCUCACUGUAAGCUCGGCCAUAUAGGAUCCUUUAAGUCAACAUGCGUCGUUGGUGCCAUGCUCGCUUCGGAUGAUCUUGUGACGGCCGAAUCCGCGACGGGAAGUGGAACACAUCGCGCAGUUACCCGUUUAUCCCAUCUUGAAAGGCCCUAUACGGCCCGGGGUGCAACCAAGCAAAAGUUUGUGAUACGGGGCUCCAUGUGGUGGCCACUUUUCGAUCCUCCCAUAGUGUACCAAUCGAUUAAGGAAGUACCCAUAGUCGGACACGGGUUCAUCAGGAUGCGCACUAAAUUCCUUAUGCUCACCCCCACUACGGGUAAGUCCACAUACCUAAAUUUCCUUAGCUCUCUGCUGAUUAAUAGUGAUGAUCACUUUUUAGCAUACGAGAUCGGUCCGCAAUCAACAUUACUGGCGGGGACUUUUGCCGAUGCUCCCAUAUCGACAAUCCACCAAUCGCGAUCACCGGUUCUGUCAUUCGUCUACAAUCACGCGGCACACCUCCAACUAUCGCAAUUCGUGAUUGAGUUUAUUGACUCUAGUGAACGUAAUGCGUGCGGUAGGUUAAUAUCUGAGAAGCACCGUCAAAGUAGGCUCGGAAUACCGGUUGUCAAGAAACUAACCGGACACCACAUUCAUACGAUGAGCUACUUCGACGCAGCUUGUGUUUGUAUUGGCUUUCGGUCCGAAGCGCCCCCCCAUGCACACAGUCAAGGGUAUGUGAGUAUGUGUGUGGAUGCUGGUCCGCUUGCUAACGUCGUAGAGACGCCGCAGUCCUUGUUACUACACGGUCUCUUGGGCGGCACGCUACCUCGGGACGCCGGACACAUGGAUAGCAUUGAGAAAAUAGUCAGCUUAAUAAGCGCCGUCAGAUGGCGGUAUAUGUCAAAGCUUUCCAUGGCAAAUGAUUCGCUGUGCGUAGCAUCUAUCUCUCCCAUGACCUUUAAUGCUAGAGUUUGCGAGAUUAGAAAGAGCCCUCUGCUUUACGGAUUCUCCCUCCACCUGGGGACCUCUAGAUACUUGCAAUUUAAUGUGCACGAACUAUACCACCACCGUGAAAUCGGACAAAUAAGACUAUUGGCAGAAUCUGGUACCGCACGGUUUACGUAUAUUUCAUUGCAGCCACUAGGAACCGUGCAAAAUUUAAUACUCACACCUCUAUAUCUGCAUGCACAUUCUUUACCAAAGCACAAUGUGCGGUUUUGCUUCCUCGCUCAGUUAUGUAACCGGCCGACGAAACGUCACAGCCAGUUGAGCAAGAUAUAUGCUGACGGGCUGGAUGGGACUACCGUCGGACACCACGCGAGUUCACAGCUAUGUCUCGCCGAAUAUACGCUUCGUUUAGAUCCUCUUUUCAGCAGAGUAACGAAUCGUCGGCUCGAGAAGGAAUGGUCAUGUUUCGGAGGCAGGCAAAAGUAUACUUUUACGCCCCGUAAAAUCCAGUGGUCAAUCGACGUGGUUGCCCUAGACGCAAAAGCUGGCAUGUUAGGUCGAAGUCCUUGCCACGAAUGUUACCCAUGGACAUUUUUGAUGCCUAAACCGAACUGUGAUCUCCAGCAGCUGGUUACUGCAACAAUCCAGGCUUGCGCGAUCGCGGCCUCCCCUUUAAUGGAGUUCUCUGCCGUCAGGAUCGGUCAUGGGAGUAACUUGCCUCUAGCCGCCCUGAUGAAGCGGAGGGAUGUUUCCACAGAAGCGUCUCGACUAGUUAGUCAACGAGACAAGAGUGCGCUCGCAUCUUCCGUAAGAAAGCACAGAAGGUCCUCUGGAGCUACCCGACCGCAGAGACGUGGUACUAUGCUCCUCAGCAAAACUAGGUUGUCUAACUACUACUGCCGAGUCCAGUACUCAGGAUCUCUUAACGGAAAGGAGAGCAGUCAAGGAAAGCCUCAUCCUCUUCAGACGGAAACCUGCUACUGUAACCGCACGGGUUCUAACGUGUACCUGGUGACUGCUUUCUUUAGGCUCCCUACUCUGCCAAGAGAGCAUGGAGGUUUGGUGCGAUGGCUGCCGUCAAACCCUUGCCACUCGGCAGGGGGAUACCAGGGGUCGUUUCUCACAAAGCAUUAUCCCGUAGGGGCUUGUAACAAGGCCCCAUGUAAAACAGCUAGUAAUGAUAUCUUAUCCGGGCGUAUCUGUGUGCUGCCUGACCUAUGGGUCCUGCCCGUCCCGACUAGAGUCGACCGAACCCAUGAAGGCCUGGAUAGUCUGGGGGCAUCAAAGCGGUUGAACUUCACUGACGACCAGUCACAGAUACCAACUCGUGAAAAGGCGCUCUCGGCGACCGGGAGUUUUAGGGGUAACCAUUUCCGACUAUUUUGUACCGCGGAGAUUAUGAAGAAAUUUUCUGCUACUCCGACCGCAAGGCAACUUGACCAUGGGCGGAGAGUCGUCGCGAAGUCCUCGCCAAGAAGGAUUUCGGACUGGCGAGGGCUGAUCACAGCGAGGACUAGCAUGCUACCCGGAGCCUACCGUCGGUCUGGACACGUGGGUCCGCGUUGUACGCAUGAUUGGAUUGGGGGCUGUUUAGUGAUGGGGAACUCCUCAUUGUCGCGUUGUACGGAAAAAAUUACAAAGUCAUCGCCAGACCAGGCACGGCAUAUGAGCUUAUCUGUCUUCCGACGGCCGGCGGCGAGAACCCACCAGCACCCUCGUAGCCUGAUUGUUAUGAUUAAAGCCAGCAUUCUGCAGCGUGUCACUUGCACAUUUCUUAAAUUGCUAUCCCCGCGCUCUCCAUUCCGUCUCCGGUCGGAAUUGACGAGGUGUGAAAUAUUCAAAUACUCGAUACUUGCCAGAUCCCACGUGCGUCAGCCGCUCCCAACCAAACACACUCUGACAUCUCGAGAACGCGAAUCUGCACUAAUUGGGCCAAGCGGUACAGGGUCCAGUCAUCCAUGCAUGGGUUUAUUUACGGAGUUGCGACCUAUAGUUAAGGAUCACUUAGAGAUAAUGGUUCUCGGAUUAAGCUGUCCCAUGGGCCGUGUAAGCGAUAACCAGCUGAUAACAAUCACGUGGACCGUUAUAGACGAACCGGUCCCAUGUCCACUCUUCAAUCGAUUCCGCGACGUGACUUCGCGAACCACCAUGCGACGUGGUCUCGCAUUUCAGCGGUGUGGCUGCAUUAUCACCACGAAGGUUCCCGGCCGCUAUUCGGAAAUUUCCGGUUUUCCUGGGUUAGUGGCAUCCGGCCCAGAUCUGGGUUCGGAUAGCGCUGUCGGAACAAUGAGGCCGGGAAACAAUUUAAGCUCUUUCGACGUUCAUAUACAAUUCUACGGAUACCCCGACUUGCGACCCGGGGCUGUGUUUGGAGCAAUCAUCUACGAAGUGCUCCUAGGAUACCGUGGCAUUAGCAAAGUGCAAGAAUUAUUGUCUGUUCCUCAGCCUCUAGUUAUCAUCCGCCCUGUUCUUGAAAGAUCGCCCUGGAGCUGCCCGUCACUUCCUGAUAUCCUGAGCCACCAAACUGCAUUCGCUGAAGCUGCAAAUAUCUCGAAACGGCCUACGCUACAGGCCGACAGUAGAGAGUAUCGCAGCUGGGACGUCUUUAAGGCAGGUGACAAUCGGGGAAGGCGUGAUCCGAGCCUUGUCCCUAAGAUGCAUGCCGUUUACUCGCCCUGGCCGCAUCGUGCCUCAUUCUUAGGGCCGGAACGCACUGCCAGACGCUUUUACAUUUUGUUGCUGCUCGAACGGUUUUCUUCAAGGCGCAGCCUCACGGUAAAGAUUAUUGCCAAUGGUUCUUUGACACAGUGCUUUUUUGUCAUGACAUUCUGGGAAACAGCGGGCCGGAGUUCGUUACUUGGUCAGCUGACCGAUUGUGGUACUCCCGCACUCCGGUAUAUGACCGAGAUCUGGGUAACAGCAAACCAUCCGGGGUGGAGGCUUCCCCAAGGGGCAUACGUUGACCGUCUUCCAGCCUUGAGUAGAGCAGUGCCUGGAAAUAUAAUACCCCGGUGCCACCACCGUUUUUGUUUUAGUCCGAAGUCACCCUGCACUUAUCGUUCACCGAAGAUGAAGUUGAUACUCUCAUCUGAUAUUGCGACGCACGUAGCCGACCGACUGUUUUACCGCGAGAGGAUCCGAGACGCGCAUUACAGGGAAGCGAAUCUCCAGGGUCCAAACCAGGCAUUGCGUGGCUGUACCUGUUGUAGUCUUUGGGGAAAAUUUUUCUUUGCCCUGGCCUACACUGAAUCUAUGGAGUCUCUCGUGCGUGUCUCGAUCAAGUAUUCCUGCUCAGAUAGCAAUUCAAGUCUUGUAGUUCAAUUUCAUACAUUGCAGCCGUGCGGGGUGGUCUAUCGGAAGGAGGGGGGCCUACUCCAUCCAGAGUCAUGGGAGAGUCUAGUAGAGAAGUCCCGCGCAAGCAUUUUAGUCUGCUUCAUUUUCUCCUCAACUUGUACUCUGUCGUCUGCUAACUCGGGAUCCAGGUAUCCGCACGUUUAUCGACUUCCAAUCGAUCGACCGGUAGAUAAAGUCUGGCCGUUCGCCGAGUGCUCAAAAAGCUUGCCUCAAUAUGUUGAAUACAACACAACACAGCCGUCGGUAAUAACAACUCCCAUUAGUUCACAUGUCGCGAAGAACCGCUGCCGUUUCGGCUUUGCGAAAAUUUCGGAUAAAUUGUUCUGCGCGACUUCGUGUGGUGGUGCCCACGGUAACGAGAUGACCGCUGUUUGUCUGGCCAUUUUAUCUUCCCCUUUUAACCACUGCGUACACAGUCUGCCCGAGACGGACAAGAAUUCCGAAAUCAAGGAGACGGGCAGUAUGCCUCUGGGGAAGAGCAAUAAUUGGUCCUGCGUAGAUCACGACGAGUAUGCUCUCGUUGGUACGUACCACAAACAGCUUACUUACGCGAUCGGUGUCCGCCACCAAUUAACAACUUGUGGGGAUGCAUGGGAAGCUAGCAUCAAUUUGGGAGUCGCGUAUCGCAUCCUCCUGCAUCGUUGUCCAGAUUGUUCCCUUGGAGCUUCGAACGAUGAAGACAUUCCUGAAGUACCCAGGUCAAAUAAACCCCGUGUAGAGGUAAAUACGCUACUCAGAUAUCCGUGGCCCUUUGAUAUGGGAUUCGAAAUCGCGCCUUGUAUCAAUACCUCCCACUCUGUCAGCAACAGCAUCAUGGUGAGAAUGUCACGUCGAUGUAAGCCUUUGAUUCGAGGUGUUAAAAGUGAGAACCCUAGCGUACAGCAACAAUGGUUAACGGGUGAUUUCAAGCGGCGGCAAAGUGGCAGCAACAGAGCCCAAACACUCUUCAUGGCUAGCUGUUUGGGGGAUUGGAACGGGUCUUUAAAAAGCCAGCAGGAACUUGAUUGGUCAUCUGCCACAUACAUCAUAACUCAAGCUCCUAGCCGCAGCUCUGCUGGACACUUCGGUCACAUGCCUCCUGCGCCGAAAACGGCGGAUCCCGUUAGGCUGGGCUCGGCAGGCGAUGCAAAACUGUCGUCUUCGGAGAGAACUCCCGGCCAGAGUCUUAGACGCGGUCCGAGGAUACAGUUUCCCGCUCGAUGUCGCGGGCGUCUUGGUAAACAUACAAAUCCAGAAGGAAAACAAGCUGCUUGGUUCCCACUCACUAAUUUCUCCGCCUUAAACUUAAUGUCAGAAGACUGCUGCGGUUCUUUAUCGUUAGUAUUCCUAUCCACACUAAGACAGGGAAUCGCUAGCUCCGAGGAGUUAAAGUACCAGCCGUCGCUUAAGCGUACUCGCACAGCCGUAGAAGGCCGAGGCAUUUCGAGCCCACUGGCAGCAUCUCUACCAGGAAUCGGUUUUGCUUGGGCGUUUGCCAAUAGGGGAAAUCGGCUCCAUACUUUCUAUCCUCGGAUUCGCACGUGGUCCAGCGGUACCGAACGCGACUGGUGGCGCAGAUUAAAAGCCGCCUGGAAUACGUCCGGAUGGGGGUAUGUGUCCGCGUUCCAACGGCGAUUACUUGGUAAUGUGGCAGGGGUUUUGACACCGGUGGAUAUGGUUCCGGUUCCGGGAGGACCAAAAUCGGCGAUCAGCCCCUACGGCCUGCAUAAUAUUAUUACCCCUUUUAGUAUUUGUUUCCCACUUCCGCUCCUGAUGAGCUCGCGAAAAUUCUGCAGUGGCCUUAACUUUAAUCAUAAAAUCCAUAGGCUCAAUCCCAGGAGAUUCAUGCAAUUACCACCUCACAAUACGUAUGGCAUCUUAAAAGCAGUUGUGUACAAUACGAUGUCUAUCUCGACCCAAGUAGAGAAGGAUAAGAGCUGGCGCGGUAGUGUCCGGAAAAGACGAUGUCAGAGGUGGUUGGCUCGUGACCGGCUAGUUCCCACUGGGCGAGUAGAAUGCUUUCCUACAACGACAGGUGUAUGUGACGUCCCUGGAACACCACCCGAUAAAACACGAGUGGGACAGAACCAUCAGUAUAGUAUAUACCUCUGUGUAUAUUCAGCACAAGGGAGACCGUGGUAUCAGAUCCACUACACAACGAUUCAGCUCAAAGCGUACUUCCGUUGUUCACGUGCUGACGGUCUGCAGUCUCCGAGAUAUAGAAUAGCUGAAUGUAUUCUCGAUACUGACUCAAGGGCUCUGAUUAUAAUACCAAAGACCCAAGGGUUAGGAGUAAUUGAUUUGAUGAUUGGAUGCCCACUCCGUUUGCCUACUAUUUCCGGAAGGAGUGUUCUCACAUCUGCGGCGCAGACGGACCAAUCAUCUCGCUUCAACGGGCGGUUCUCUCCCGCUGCUUCGGCUCCCAGCUUCCUUCCGCGUGCGGGACAGCAGAGCAGUUACAAUUGCUUGUGCCAGCUAAAAAUCGUGCCACUGAACUUACGCGCAUGUAUAGCUCCGGCUACUCAUUGUCGUAGCAGUUCACGCACGUCCUGCUUGGCACAAUCGGGGGUUUUAUGGCCCACCUACCAUUUCUAUUGUCAUUUGCGCGUACUCGUUUGUGCACAGACGGGGUACGCGCUCGCUAAAGGGGCCUGGCGCCCCCAAGACUCCAAGACAAACUGGUAUGUCACACCCCCACCCGACAUCCGCCAUAGCAGCAAGUGGGAUAGUUCCUGUAGGUGCGAAAAUAAACCCCAUCAGUCCCCAACAUCGCUGUUACGCUGCAAUAAUACCUUGCCCCCCCCGGAUAGGAGCAGACACGGUUCUGGAAUUUCCUGCAAGCGUCCCAUAAGGACUAGAACGAGGAGGGGUGGACACAUGUGCAACAAGUUUUGCAUGGCAGCCGGACCGAGGGGAGGAAGCAGUAAAAGCUACCGCCAUCUACAUUCCCCACAAGAAUGCCAGCAAGCGCACAUAAUAAUGCUAGAUGGCUCCUUCGUAAACGUCGCUAACGACAUACAACAGAUUACUGGUGACUCCAGUCCAUCCUCUCUUUGCUGUUCCCACCCCACUGCCGGGAAGAUAUGUAGAUACGUAAAGGUUCCGGAGAAUUUUUGUGAAAGCUGGAUGUCUGUGGGACCUCGCGGUGAUCAAAUAGGCUUGACUACCGCGGACACAGAGGCGGAUGCUGACCUGCAUAGCCUGGAUUGGGGAAACAAAGUCGCCGCCCCAAUGACAGGUUUCAUCUUUUUCACAGAUCCAAAGAUAUCUCUGCUAGGGUUUUCGUUGAGCUGCCUCAGUCGUCACUCCGGCCCGGACGUCUGCAAAGGAACGAGCACGCCGAAAGCCCUUCUGUCGCUGGUAGGCUACGUUUUAACAUUAGUUAUACCUGGACAGAGCAAUCCUGUUAUGCGCAGGUCAAUGAUCAGAGCUCAGGCGACGACCGGCCCCAAGCUGCUGAAAGACUCGCCAGAUAGGACUCUAACCAGAAGACCUCAACACCAGGCAGCCGAACACUCAAACGAGUUCUCCAGAGCCAACAGACAACAGGGUUACAGCUUUAAGCCGCUGGCAGGGAGGGGACUUCAAGCACUACUUGCAGACAGUACGAGCCCAGUAGCUUUUCGAUGUACGUUUCUUGCGUCUAUUUACACAGAAAGACAGUGUAUCAAACAAUUAACGAUUGUCCACGAUAGGUACUCGAGCCUGGCCGUUCCGACGAGAGGAAUGUGUCAGGCACUUCAAAGUAACAGAACACAGACCGACAAAUGCGGUACCGCUCCAGGCAUCCUUUACAAAAGAUCGUUUUUUAAUGGGACUGCUUCACCGAACGAUCUUGAACGUGGUAUGCAAGGAAGAUUCCGCUUAUUUGGUCCGCCGACCCUAUGGUCCGCUGCUACAGAGACCAGUUCUGACGCUAUCACACUCUUCGAGCAACAUUCCGUCCCGUCACGAUCGUUAUCUGGCUCUUACAGCAUACCCAUAAGCGGCGCAGCGGAGCGUCUUGGAGUUACGAACUAUGGGAAGCUUGCUAUUGUUAUCAGUACUGUUCUUAAACUCGUUAAUGCGGGCUUCAUUUUUACAUUUUAUGCCAGUAGGCGACCUAAACAAACCCGGUUACGCCUACACACGGCCUUACGAGCGCGUCCAGUCCCACUGUCUAUCGCUCCGCCUAGCACCUGGUCGUCAGUGCUAAGCGCCUGCAAUCCAGCUAACCUGUAUUUAGAUACCAGCUCGCCCAUGAAAUUCAACAUCAACGGAGAAUCUAGGACAAGAUAUUUAGAUCAUGCUCAUAUAGUUCCCAGAACUUACGCCGCACAGGACAAUGAAGUGUGUAGAAUUCUAGCACGCUUGGUCUCGCGCAAGGUGUCGGAGUUUACGAUCUCCAGUGAUAAUACGGGACUCCCCAAUUCUCCGCACAACAAGGUUAAGCCCGCAUCCUGCCCUAUCCUACUUGCUCAUCUCAUGGCAGAGCACCAUCAUACAGCACAUUUUGUCAUCGCAGCUUACCUAGGAACAGGAUCUCACCGUCAGCAUGCAUGCUGUCACAAAACAUUCCGGGAACCUUGUGUAGACACCUUCAUGCCUGCUCGUAUCGACUGCAACAGAAUCGUUCAUUUACACAAGUUGGAGGAGAAGCUAACAAAACAUUGCUGUCAUCUCUCUACGUUUCUCCUAUCCCCUGCAGAGCAGCAUGGUAUAGUUCGCGGGAAGUGGCUUGAUUGGGAGCCGUCUGGCGGCAGCCAAGGUCGCGUAUGCUACCAGGAUCGUAGAGUAAAUAUUUCCCGAUCUCCCUAUAGUCUGAGUAACAAUCCGACAACACUAGGCAAUCAACUUGUCGCAGGGCGGCCUAUAAGCCUAUUGCCAGGGCUCAGUAGCUUUCGCACUCAGUCAUCCGAUAAUUCCGUCCGUACUCCAAAGAACGACUCGACAUAUCUUCUAAUUGAUCAUAGUAAUAGCUCGAUACCAUCGGAGGUGGGCCGCUCAUUUCGCCCGACCCCUGGCCGGAUGGGGUUGGUCCGGACCUUCUGCCCCCCCAAAUCGGCUACACCUGUCUGCGUACAUACUUUAGAGCAUUUGUAUAGAAUUACAGGAGCCAGGCGUCAGUUGCAUACGCUCUGUCCUGGGUUAGUGUGCAGAGACGUAUUAGGCCUUAUUGGCAAACUCAAUGAUCCCUGUUCUAAGUUGGGGCCAGAUGCAUGCAUCCAAGCUCUGCAUAAUUUCUCGAUGGGCAAACGGUCGUCUGCUGCAAUGUACUGCAUCCAAGUUGAUAGUAGGUAUGAAUGA"
print(Translation(rna))
