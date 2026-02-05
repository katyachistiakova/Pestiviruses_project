# Pestiviruses_project
🗂<strong>full_data</strong>\
<strong>full_record.csv</strong> - таблица с аннотацией ко всем последовательностям\
<strong>full_sequences.acc</strong> - accessions для всех последовательностей\
<strong>deduplicated_no_cds_orfs.fasta</strong> - предсказанные ORFs последовательностей, для которых не была найдена CDS\
<strong>full_CDS_sequences.fasta</strong> - последовательности CDS и ORF\
<strong>aa_full_seqs.fasta</strong> - аминокислотные последовательности, полученные после кластеризации с порогом идентичности 99, очищенные и транслированные кодом translate2aa.ipynb\
<strong>nt_ful_seqs.fasta</strong> - нуклеотидные последовательности, полученные после кластеризации с порогом идентичности 99, очищенные кодом translate2aa.ipynb\
<strong>all_filtered_clusters.fasta</strong> - последовательности после кластеризации с порогом 99% идентичности, послученные с помощью CD-HIT
<strong>all_filtered_clusters.fasta.clstr</strong> - кластеры с порогом 99% идентичности, послученные с помощью CD-HIT\

🗂<strong>new_data</strong>\
<strong>new_pestivirus_records.csv</strong> - таблица с аннотацией к новым последовательностям\
<strong>new_sequences.acc</strong> - accessions для новых последовательностей

🗂<strong>code</strong>\
<strong>CDS_search.ipynb</strong> - код для скачивания CDS\
<strong>translate2aa.ipynb</strong> - код для очистки и трансляции последовательностей\
<strong>NS5_cut.ipynb</strong> - код для вырезания доменов RDRP_ из последовательстей по координатам в белке\
<strong>insertions_search.ipynb</strong> - код для поиска неаннотированных вставок

🗂<strong>alignments</strong>\
<strong>aa_mafft_alignment.fasta</strong> - аминокислотное выравнивание mafft\
<strong>aa_muscle_alignment.fasta</strong> - аминокислотное выравнивание muscle\
<strong>nt_pal_mafft_alignment.fasta</strong> - нуклеотидное выравнивание, полученное с помощью pal2nal из выравнивания mafft\
<strong>nt_pal_muscle_alignment.fasta</strong> - нуклеотидное выравнивание, полученное с помощью pal2nal из выравнивания muscle

🗂<strong>domains</strong>\
<strong>domresults.tbl</strong> - результат поиска доменов по отобранным последовательностям с помощью hmmscan\
<strong>unannotated_insertions.fasta</strong> - неаннотированные вставки, найденные кодом insertions_search.ipynb

🗂<strong>NS5_small</strong>\
<strong>NS5_mafft.fasta</strong> - выравнивание mafft аминокислотных последовтельностей полимеразы
<strong>aa_NS5_for_tree.fasta</strong> - аминокислотные последовательности полимеразы
<strong>nt_NS5_for_tree.fasta</strong> - нуклеотидные последовательности полимеразы
<strong>pal_NS5.fasta</strong> - нуклеотидное выравнивание полимеразы
<strong>pal_NS5.fasta.treefile</strong> - дерево, построенное iqtree

🗂<strong>short_data</strong>\
<strong>nt_pal_small_mafft.fasta</strong> - нуклеотидное выравнивание pal2nal, полученное из выравнивания mafft\
<strong>nt_pal_small_muscle.fasta</strong> - нуклеотидное выравнивание pal2nal, полученное из выравнивания muscle\
<strong>small_search_pfam.domains</strong> - результаты поиска доменов DomainAnalyser\
<strong>small_clusters.fasta</strong> - нуклеотидные последовательности\
<strong>small_clusters.fasta.clstr</strong> - кластеры, получнные cd-hit\
<strong>small_mafft.fasta</strong> - аминокислотное выравнивание mafft\
<strong>small_muscle.fasta</strong> - аминокислотное выравнивание muscle\
<strong>small_pfam_search.svg</strong> - карта доменов с DomainAnalyser\

🗂🗂<strong>rdrp</strong>\
<strong>BVDV_RDRP.fasta</strong> - аминокислотные последовательности RDRP группы BVDV \
<strong>BVDV_RDRP_mafft_named.fasta</strong> - выравнивание аминокислотных последовательностей RDRP группы BVDV\
<strong>BVDV_RDRP_mafft_named.fasta.treefile</strong> - дерево RDRP группы BVDV о аминокислотному выравниванию\
<strong>RDRP_LONG_ONLY.fasta</strong> - аминокислотные последовательности RDRP подвыборки из 97 последовательностей\
<strong>RDRP_mafft_named</strong> - выравнивание аминокислотных последовательностей RDRP подвыборки из 97 последовательностей\
<strong>RDRP_mafft_named.fasta.treefile</strong> - дерево RDRP подвыборки из 97 последовательностей по аминокислотному выравниванию\

🗂<strong>BVDV_sample</strong>\
<strong>BVDV_alignment.jvp</strong> - проект выравнивания полипротеинов BVDV c размеченными доменами\
<strong>insertions_overview.xlsx</strong> - результаты BLASTp для выделенных в выраванивании полипротеинов BVDV вставок\

🗂<strong>reference</strong>\
Домены, найденные для геномов родов Hepacivirus и Pegivirus
<strong>.fasta</strong> - CDS translated sequences
<strong>.domains</strong> - Domain Analyser 2.0 output, contains domain coords
<strong>.svg</strong> - visualization
