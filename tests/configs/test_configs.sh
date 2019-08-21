#/bin/sh

# Test all *.tf.json files

if [ ! -e test_configs.sh ]; then
    echo "This script must be executed form within the tools/ folder"
    exit 1
fi

TF=`which terraform`
if [ -z "$TF" ]; then
    TF=`pwd`/../../tools/terraform
fi

for config in *.tf.json; do
    echo $config
    tmpdir=`mktemp -d`
    cp $config $tmpdir/
    cd $tmpdir/
    $TF init || exit 1
    $TF validate || exit 1
    cd -
done
