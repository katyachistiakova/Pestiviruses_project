# Pestiviruses_project
🗂<strong>NS5_small</strong>\
<strong>NS5_mafft.fasta</strong> - выравнивание mafft аминокислотных последовтельностей полимеразы\
<strong>aa_NS5_for_tree.fasta</strong> - аминокислотные последовательности полимеразы\
<strong>nt_NS5_for_tree.fasta</strong> - нуклеотидные последовательности полимеразы\
<strong>pal_NS5.fasta</strong> - нуклеотидное выравнивание полимеразы\
<strong>pal_NS5.fasta.treefile</strong> - дерево, построенное iqtree

🗂<strong>alignments</strong>\
<strong>aa_mafft_alignment.fasta</strong> - аминокислотное выравнивание mafft\
<strong>aa_muscle_alignment.fasta</strong> - аминокислотное выравнивание muscle\
<strong>nt_pal_mafft_alignment.fasta</strong> - нуклеотидное выравнивание, полученное с помощью pal2nal из выравнивания mafft\
<strong>nt_pal_muscle_alignment.fasta</strong> - нуклеотидное выравнивание, полученное с помощью pal2nal из выравнивания muscle

🗂<strong>code</strong>\
<strong>CDS_search.ipynb</strong> - код для скачивания CDS\
<strong>translate2aa.ipynb</strong> - код для очистки и трансляции последовательностей\
<strong>NS5_cut.ipynb</strong> - код для вырезания доменов RDRP_ из последовательстей по координатам в белке\
<strong>insertions_search.ipynb</strong> - код для поиска неаннотированных вставок

🗂<strong>domains</strong>\
<strong>domresults.tbl</strong> - результат поиска доменов по отобранным последовательностям с помощью hmmscan\
<strong>unannotated_insertions.fasta</strong> - неаннотированные вставки, найденные кодом insertions_search.ipynb

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

🗂<strong>reference</strong>\
Домены, найденные для геномов родов Hepacivirus и Pegivirus\
<strong>.fasta</strong> - CDS translated sequences\
<strong>.domains</strong> - Domain Analyser 2.0 output, contains domain coords\
<strong>.svg</strong> - visualization

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

🗂<strong>species</strong>\

🗂🗂<strong>BVDV_sample</strong>\
<strong>BVDV_alignment.jvp</strong> - проект выравнивания полипротеинов BVDV c размеченными доменами\
<strong>insertions_overview.xlsx</strong> - результаты BLASTp для выделенных в выраванивании полипротеинов BVDV вставок\
<strong>BVDV_pic.png</strong> - визуализация дерево + домены BVDV

🗂🗂🗂<strong>BVDV_tree</strong>\
<strong>aa_BVDV_RDRP.fasta</strong> - аминокислотные последовательности BVDV RDRP\
<strong>mafft_BVDV_R.fasta</strong> - выравнивание mafft аминокислотных последовательностей BVDV RDRP\
<strong>nt_BVDV_RDRP.fasta</strong> - нуклеотидные последовательности BVDV RDRP\
<strong>pal2nal_BVDV_RDRP.fasta</strong> - выравнивание pal2nal нуклеотидных последовательностей BVDV RDRP\
<strong>tree_BVDV_RDRP.treefile</strong> - newick файл дерева RDRP BVDV по нуклеотидному выравниванию\
<strong>tree_l.rdf</strong> - дерево ао нуклеотидному выравниванию с bootstrap

🗂🗂<strong>atypical_porcine</strong>\
<strong>aa_porcine.fasta</strong> - аминокислотные последовательности apv\
<strong>nt_porcine.fasta</strong> - нуклеотидные последовательности apv\
<strong>porcine_dom.tbl</strong> - домены, найденные по профилю PPHMMDB.hmm\
<strong>porcine_mafft.fasta</strong> - аминокислотное выравнивание mafft apv\
<strong>porcine_pal.fasta</strong> - нуклеотидное выранвиание pal2nal apv

🗂🗂<strong>border_desease</strong>\
<strong>aa_rdrp_border.fasta</strong> - аминокислотные последовательности bd\
<strong>nt_rdrp_border.fasta</strong> - нуклеотидные последовательности bd\
<strong>rdrp_bd_mafft.fasta</strong> - аминокислотное выравнивание mafft bd\
<strong>rdrp_bd_pal.fasta</strong> - нуклеотидное выранвиание pal2nal bd\
<strong>rdrp_bd_tree.treefile</strong> - newick дерева по нуклеотидным последовательностям RDRP bd\
<strong>tree_bd.pdf</strong> - дерево по нуклеотидным последовательностям RDRP bd\
<strong>bd_small_colored_alignment.jvp</strong> - аминокислотное выравнивание маленькой выборки bd (с дерева) с разметкой доменов\
<strong>pic_bd.png</strong> - визуализация дерево + домены bd

🗂🗂<strong>swine_fever</strong>\
<strong>aa_swine.fasta</strong> - аминокислотные последовательности swine fever virus\
<strong>nt_swine.fasta</strong> - нуклеотидные последовательности swine fever virus\
<strong>swine_99_clusters.clstr</strong> - кластеры с порогом идентичночти 99 sfv\
<strong>swine_dom.tdl</strong> - домены, найденные по профилю PPHMMDB.hmm\
<strong>swine_mafft.fasta</strong> - аминокислотное выравнивание mafft sfv \
<strong>swine_pal.fasta</strong> - нуклеотидное выранвиание pal2nal sfv
