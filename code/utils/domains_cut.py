from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import argparse


def extract_hmmer_domains_domtblout(fasta_file, domtblout_file, output_file):
    seqs = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))
    extracted = []

    with open(domtblout_file) as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue

            parts = line.split()
            seq_id = parts[3]
            env_from = int(parts[-4])
            env_to = int(parts[-3])

            if seq_id not in seqs:
                continue

            nt_start = env_from - 1
            nt_end = env_to

            subseq = seqs[seq_id].seq[nt_start:nt_end]

            record = SeqRecord(
                subseq,
                id=f"{seq_id}_{env_from}_{env_to}",
                description="RdRp_env_coords_nt"
            )

            extracted.append(record)

    SeqIO.write(extracted, output_file, "fasta")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fasta", required=True)
    parser.add_argument("-d", "--domtblout", required=True)
    parser.add_argument("-o", "--output", required=True)

    args = parser.parse_args()

    extract_hmmer_domains_domtblout(
        args.fasta,
        args.domtblout,
        args.output
    )