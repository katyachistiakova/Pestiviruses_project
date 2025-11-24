# Pestiviruses_project
🗂<strong>full_data</strong>\
<strong>full_record.csv</strong> - таблица с аннотацией ко всем последовательностям\
<strong>full_sequences.acc</strong> - accessions для всех последовательностей\
<strong>deduplicated_no_cds_orfs.fasta</strong> - предсказанные ORFs последовательностей, для которых не была найдена CDS\
<strong>full_CDS_sequences.fasta</strong> - последовательности CDS и ORF\
<strong>aa_full_seqs.fasta</strong> - аминокислотные последовательности, очищенные и транслированные кодом translate2aa.ipynb\
<strong>nt_ful_seqs.fasta</strong> - нуклеотидные последовательности, очищенные кодом translate2aa.ipynb\
<strong>all_filtered_clusters.fasta</strong> - кластеры с порогом 99% идентичности, послученные с помощью CD-HIT

🗂<strong>new_data</strong>\
<strong>new_pestivirus_records.csv</strong> - таблица с аннотацией к новым последовательностям\
<strong>new_sequences.acc</strong> - accessions для новых последовательностей

🗂<strong>code</strong>\
<strong>CDS_search.ipynb</strong> - код для скачивания CDS\
<strong>translate2aa.ipynb</strong> - код для очистки и трансляции последовательностей

🗂<strong>alignments</strong>\
<strong>aa_mafft_alignment.fasta</strong> - аминокислотное выравнивание mafft\
<strong>aa_muscle_alignment.fasta</strong> - аминокислотное выравнивание muscle\
<strong>nt_pal_mafft_alignment.fasta</strong> - нуклеотидное выравнивание, полученное с помощью pal2nal из выравнивания mafft\
<strong>nt_pal_muscle_alignment.fasta</strong> - нуклеотидное выравнивание, полученное с помощью pal2nal из выравнивания muscle

🗂<strong>domains</strong>\
<strong>domresults.tbl</strong> - результат поиска доменов по отобранным последовательностям с помощью hmmscan
