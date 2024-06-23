for steps in {1,5,10,20}; do
    echo "Running $steps steps"
    python cs285/scripts/run_hw5_explore.py \
        -cfg experiments/exploration/pointmass_medium_rnd_step$steps.yaml \
        --dataset_dir datasets_ablation
    python ./cs285/scripts/run_hw5_offline.py \
        -cfg experiments/offline/pointmass_medium_cql_step$steps.yaml \
        --dataset_dir datasets_ablation \
        > 4.3-step$steps.log
done