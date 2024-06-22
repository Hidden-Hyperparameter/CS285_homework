for i in 0 2 4 6 8 10
do
   python ./cs285/scripts/run_hw5_offline.py \
    -cfg experiments/offline/pointmass_medium_cql_alpha$i.yaml \
    --dataset_dir datasets \
    --which_gpu 1 \
    > ./exp_alpha$i.log 2>&1
done