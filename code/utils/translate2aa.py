from Bio import SeqIO
from Bio.Seq import Seq
import re
import argparse


def main():
    parser = argparse.ArgumentParser(description="Translate nucleotide FASTA to amino acid FASTA, skipping specified IDs")
    parser.add_argument("input_fasta", help="Input nucleotide FASTA file")
    parser.add_argument("--out-nt", default="nt_seqs.fasta", help="Output file for cleaned nucleotide sequences")
    parser.add_argument("--out-aa", default="aa_seqs.fasta", help="Output file for translated amino acid sequences")
    parser.add_argument("--skip", nargs="*", default=[
        "ON932809.1", "MT512536.1", "LR760748.1", "PV883047.1", "PV626348.1", "PV626351.1",
        "PV626352.1", "PV626361.1", "PV626364.1", "PV626370.1", "PV626376.1", "PV626378.1",
        "PV626380.1", "PV626382.1", "PV626383.1", "PV626386.1", "PV626387.1", "PV626391.1",
        "PV626394.1", "PV626395.1", "PV626397.1", "PV626398.1", "PV626400.1", "PV626401.1",
        "ON811738.1", "MT799516.1", "MG655308.1", "HV202174.1", "HI516623.1", "A47690.1", "L49347.1"
    ], help="List of sequence IDs to skip (space-separated)")

    args = parser.parse_args()

    skip_set = set(args.skip)

    with open(args.input_fasta, "r") as handle, \
         open(args.out_nt, "w") as outfile_NT, \
         open(args.out_aa, "w") as outfile_AA:

        for record in SeqIO.parse(handle, "fasta"):
            if record.id in skip_set:
                continue
            cleaned = re.sub(r'[^ATCGN]', 'N', str(record.seq).upper())
            record.seq = Seq(cleaned)
            SeqIO.write(record, outfile_NT, "fasta")
            record.seq = record.seq.translate(table=1)
            SeqIO.write(record, outfile_AA, "fasta")

if __name__ == "__main__":
    main()