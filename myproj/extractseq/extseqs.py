def extseqs(seqs,ids):
    seqdicts = {}
    out_seqs = []
    for aa in seqs.split("\r\n"):
        if aa[0] == ">":
            seqid = aa.replace(">","")
            seqdicts[seqid] = []
        else:
            seqdicts[seqid].append(aa)
    seq_ids = ids.split("\r\n")
    for aa in seq_ids:
        out_seqs.append(">"+aa+"\r\n")
        out_seqs.append(''.join(seqdicts[aa]))
        out_seqs.append('\r\n')
    return out_seqs

