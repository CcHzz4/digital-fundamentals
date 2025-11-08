#1/bin/bash

for i in $(ls $1)
do
  for j in $(cat $1$i)
  do
    age=$(echo $j | cut -d ":" -f2)
    if [ $age -ge 18 ]
    then
        teen=$((teen+1))
        #echo $teen
        #echo $age
    else
      noteen=$((noteen+1))
    fi
    #echo $teen
  done
  
done
echo $teen
echo $noteen
