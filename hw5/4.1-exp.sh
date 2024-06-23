for i in {0,2,4,6,8,10}
do
    echo Doing $i
    python ./cs285/scripts/run_hw5_offline.py \
        -cfg experiments/offline/pointmass_medium_cql_alpha$i.yaml \
        --dataset_dir datasets \
        > ./exp_alpha$i.log
done