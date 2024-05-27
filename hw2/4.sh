export NAME=discount0.99_smallbatch_gae0.98
for seed in $(seq 1 5); do
    python cs285/scripts/run_hw2.py --env_name InvertedPendulum-v4 -n 150 \
        --exp_name pendulum_${NAME}_s$seed \
        -rtg --use_baseline -na \
        --batch_size 2000 \
        --seed $seed \
        --discount 0.99 \
        --gae_lambda 0.98 \
        > log_pendulum_${NAME}_s$seed.log
done

python report/merge_4.py --name $NAME