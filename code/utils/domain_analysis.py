import argparse
from collections import Counter
from Bio import SeqIO

def analyze_domains(domains_file):
    results = {
        'has_jiv90': [],
        'has_ubiquitin': [], 
        'domain_duplications': [],
        'all_proteins': []
    }
    
    with open(domains_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
                
            parts = line.split('\t')
            if len(parts) < 4:
                continue
                
            protein_id = parts[0]
            domain_formula = parts[3]
            
            results['all_proteins'].append(protein_id)
            
            if 'Jiv90' in domain_formula:
                results['has_jiv90'].append(protein_id)

            if any(ub in domain_formula for ub in ['ubiquitin', 'Ubiquitin', 'UBQ']):
                results['has_ubiquitin'].append(protein_id)

            domains = domain_formula.split()
            domain_counts = Counter(domains)
            
            duplicated_domains = [dom for dom, count in domain_counts.items() if count > 1]
            if duplicated_domains:
                results['domain_duplications'].append({
                    'protein_id': protein_id,
                    'duplicated_domains': duplicated_domains})
    
    return results

def print_results(results):
    print("=== RESULTS ===\n")
    
    print(f"1. Jiv90 ({len(results['has_jiv90'])}):")
    for pid in results['has_jiv90']:
        print(f"   - {pid}")
    
    print(f"\n2. ubiquitin ({len(results['has_ubiquitin'])}):")
    for pid in results['has_ubiquitin']:
        print(f"   - {pid}")
    
    print(f"\n3. duplications ({len(results['domain_duplications'])}):")
    for item in results['domain_duplications']:
        print(f"   - {item['protein_id']}: {item['duplicated_domains']}")

def reorder_fasta(fasta_in, fasta_out, order_file):
    with open(order_file) as f:
        desired_order = [x.strip() for x in f if x.strip()]
    fasta_dict = {}
    for record in SeqIO.parse(fasta_in, "fasta"):
        key = record.id.split(".")[0]  
        fasta_dict[key] = record

    missing = [x for x in desired_order if x not in fasta_dict]
    if missing:
        print(f"IDs missing in FASTA: {missing}")

    with open(fasta_out, "w") as out:
        for seq_id in desired_order:
            if seq_id in fasta_dict:
                SeqIO.write(fasta_dict[seq_id], out, "fasta")

    print(f"All done{fasta_out}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script for domain analysis and FASTA reordering.")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Subparser for analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze domains from a file.')
    analyze_parser.add_argument('-i', '--domains_file', type=str, required=True, help='Path to the domains file.')

    # Subparser for reorder command
    reorder_parser = subparsers.add_parser('reorder', help='Reorder FASTA file based on order file.')
    reorder_parser.add_argument('-i', '--fasta_in', type=str, required=True, help='Path to input FASTA file.')
    reorder_parser.add_argument('--fasta_out', type=str, required=True, help='Path to output FASTA file.')
    reorder_parser.add_argument('--order_file', type=str, required=True, help='Path to order file.')

    args = parser.parse_args()

    if args.command == 'analyze':
        results = analyze_domains(args.domains_file)
        print_results(results)
    elif args.command == 'reorder':
        reorder_fasta(args.fasta_in, args.fasta_out, args.order_file)