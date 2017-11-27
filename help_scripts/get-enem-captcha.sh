#Config
outdir="captcha-"
max=1000

# Get user name (used as unique id)
read -p 'What is your fucking name, bitch (3 letters only)?' bitch

outdir=$outdir$bitch

# Verify existence of dataset
if [ -d "$outdir" ]; then
        echo "The $outdir already exists. Remove it (maybe backup?)."
        exit
fi

# Download dataset
mkdir $outdir
for i in `seq 1 $max`
do
	curl "http://sistemasenem2.inep.gov.br/resultadosenem/seam/resource/captcha" -o "$outdir/$i-$bitch.png"
	echo "$i-$bitch," >> "dataset-$bitch.csv"
done
