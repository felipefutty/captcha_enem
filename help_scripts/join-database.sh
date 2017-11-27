#cononfig
outdir="captcha-joined"
max=1000
auxdir="captcha-"
outcsv="dataset-joined.csv"
csv="dataset-"

read -p 'What is your fucking name, bitch (3 letters only)?' bitch1
read -p 'What is your fucking name, bitch (3 letters only)?' bitch2
read -p 'What is your fucking name, bitch (3 letters only)?' bitch3
read -p 'What is your fucking name, bitch (3 letters only)?' bitch4


# Verify existence of dataset
if [ -d "$outdir" ]; then
        echo "The $outdir already exists. Remove it (maybe backup?)."
        exit
fi

mkdir $outdir

# Move to dataset bitch1
for i in `seq 1 $max`
do
	cp "$auxdir$bitch1/$i-$bitch1.png" "$outdir/$i.png"
	txt=$(awk "NR==$i" "$csv$bitch1.csv" | sed "s/.*,//g" | awk '{print tolower($0)}')
	echo "$i,$txt"  >> $outcsv
done

# Move to dataset bitch2
st=1000
for i in `seq 1 $max`
do
	sum=$((i+st))
	cp "$auxdir$bitch2/$i-$bitch2.png" "$outdir/$sum.png"
	txt=$(awk "NR==$i" "$csv$bitch2.csv" | sed "s/.*,//g" | awk '{print tolower($0)}')
	echo "$sum,$txt"  >> $outcsv
done

# Move to dataset bitch3
st=2000
for i in `seq 1 $max`
do
	sum=$((i+st))
	cp "$auxdir$bitch3/$i-$bitch3.png" "$outdir/$sum.png"
	txt=$(awk "NR==$i" "$csv$bitch3.csv" | sed "s/.*,//g" | awk '{print tolower($0)}')
	echo "$sum,$txt"  >> $outcsv
done

# Move to dataset bitch4
st=3000
for i in `seq 1 $max`
do
	sum=$((i+st))
	cp "$auxdir$bitch4/$i-$bitch4.png" "$outdir/$sum.png"
	txt=$(awk "NR==$i" "$csv$bitch4.csv" | sed "s/.*,//g" | awk '{print tolower($0)}')
	echo "$sum,$txt"  >> $outcsv
done
