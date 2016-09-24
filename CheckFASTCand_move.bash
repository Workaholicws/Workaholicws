#/bin/bash

#input
#bash CheckFASTCand.bash (file list)
#file list format:
#filename list, all filenames

#0, must have a input file, or, tell the usage
if [ ! "$#" -eq "2" ]; then
  echo "Usage: bash CheckFASTCand.bash (filelist) (destination)"
  exit 0
fi


#1, check if file list exist
if [ ! -f "${1}" ]; then
  echo "No file list ${1}."
  exit 1
fi

#2, loop to check each

#echo "Checking results:" > ${1}_check.txt

lines=`cat ${1} | wc -l`
echo "$lines file(s) in the filelist ${1}."
list_file=${1}
for((i=1;i<=lines;i++))
do
  #PM0xxx_0xxx1_ACCEL_50_aaa_ACCEL_Cand_bbb.pfd.yyy
  cand_file=`cat $list_file | sed -n "$i p"`
  ps_file=${cand_file%.pfd*}
  #ps_file=${ps_file%.*}
  ps_file=$ps_file".pfd.png"
  #PM0xxx_0xxx1_ACCEL_50_aaa_ACCEL_Cand_bbb
  #cand_name=${cand_file%.pfd*}
  #need PM0xxx_0xxx1 and aaa

  #PM0xxx_0xxx1
  #datafile=${cand_name%_ACCEL_50*}

  #aaa
  #PM0xxx_0xxx1_ACCEL_50_aaa
  #tmp1=${cand_name%_ACCEL_Cand*}
  #aaa
  #cand_no=${tmp1#*ACCEL_50_}

  #echo "Datafile $datafile, candidate number $cand_no, $i in $lines candidate(s)."

  #get Ra, Dec, p0 and DM
  #pmps_path=${datafile%_*}
  #ra=`readfile $PMPS/$pmps_path/$datafile.sf | grep RA | grep deg | awk '{print $5}'`
  #dec=`readfile $PMPS/$pmps_path/$datafile.sf | grep Dec | grep deg | awk '{print $5}'`

  #((cand_lines=cand_no+cand_no+cand_no+1))
  #p0=`cat /home/pzc/pulsar_search/searches/$datafile/log.txt | sed -n "$cand_lines p" | awk '{print $6*1000.0}'`
  #dm=`cat /home/pzc/pulsar_search/searches/$datafile/log.txt | sed -n "$cand_lines p" | awk '{print $9}'`
  #dm_int=${dm%.*}

  #echo "Candidate RA $ra, DEC $dec, p0 $p0, DM $dm."
  #echo "Checking......"
  #echo
  #echo $cand_file >> ${1}_check.txt
  #echo "RA $ra, Dec $dec, p0 $p0 ms, DM $dm" >> ${1}_check.txt
  #python $RPPPS_DIR/CandCheck.py $ra $dec $p0 $dm_int >> ${1}_check.txt
  echo "Moving $ps_file to ${2}, $i in $lines files."
  #mv /home/pzc/pulsar_search/searches/$datafile/$ps_file ${2} -f
  mv /Users/genius/Desktop/2607/$ps_file ${2}
  #echo >> ${1}_check.txt
  #echo
  #echo "Done."
  #echo

done

#return 0

