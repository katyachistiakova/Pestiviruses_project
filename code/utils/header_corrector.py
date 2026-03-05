from Bio import SeqIO
import re
import argparse


# ── для fasta-выравниваний ───────────────────────────────────────

def clean_header(header):
    header = header.split(",")[0]
    header = re.split(r"polyprotein", header, flags=re.IGNORECASE)[0]
    return header.strip()


def load_name_map(full_fasta):
    name_map = {}
    for rec in SeqIO.parse(full_fasta, "fasta"):
        full_header = rec.description
        full_id = full_header.split()[0]
        cleaned = clean_header(full_header)
        name_map[full_id] = cleaned
        name_map[full_id.split(".")[0]] = cleaned
    return name_map


def rename_alignment_headers(alignment_in, alignment_out, name_map):
    out_records = []
    for rec in SeqIO.parse(alignment_in, "fasta"):
        old_id = rec.id
        base_id = old_id.split("/")[0]
        base_no_ver = base_id.split(".")[0]
        if base_id in name_map:
            new_header = name_map[base_id]
        elif base_no_ver in name_map:
            new_header = name_map[base_no_ver]
        else:
            new_header = base_id
        rec.id = new_header
        rec.description = ""
        out_records.append(rec)
    SeqIO.write(out_records, alignment_out, "fasta")


# ── для файлов с деревьями (newick) ───────────────────────────────

def sanitize_name(name):
    name = re.sub(r"[:,;\\(\\)\\[\\]]", "", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def load_name_map_tree(fasta_file):
    name_map = {}
    with open(fasta_file, encoding="utf-8") as f:
        for line in f:
            if not line.startswith(">"):
                continue
            header = line[1:].strip()
            seq_id = header.split()[0]
            clean = re.split(r"\bpolyprotein\b", header, flags=re.IGNORECASE)[0].strip()
            clean = re.sub(r"\bcomplete genome\b", "", clean, flags=re.IGNORECASE).strip()
            clean = sanitize_name(clean)
            name_map[seq_id] = clean
    return name_map


def replace_ids_in_tree(treefile_in, treefile_out, name_map):
    with open(treefile_in, encoding="utf-8") as f:
        tree = f.read()

    for seq_id, full_name in name_map.items():
        pattern = r'\b' + re.escape(seq_id) + r'[^,():;]*'
        tree = re.sub(pattern, full_name, tree)

    with open(treefile_out, "w", encoding="utf-8") as f:
        f.write(tree)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    # Команда для переименования заголовков в fasta-выравнивании
    p1 = subparsers.add_parser("headers-fasta")
    p1.add_argument("--fasta-full",   required=True)
    p1.add_argument("--alignment-in",  required=True)
    p1.add_argument("--alignment-out", required=True)

    # Команда для замены идентификаторов в файле дерева
    p2 = subparsers.add_parser("headers-tree")
    p2.add_argument("--fasta-names", required=True)
    p2.add_argument("--tree-in",     required=True)
    p2.add_argument("--tree-out",    required=True)

    args = parser.parse_args()

    if args.cmd == "headers-fasta":
        name_map = load_name_map(args.fasta_full)
        rename_alignment_headers(args.alignment_in, args.alignment_out, name_map)

    elif args.cmd == "headers-tree":
        name_map = load_name_map_tree(args.fasta_names)
        replace_ids_in_tree(args.tree_in, args.tree_out, name_map)