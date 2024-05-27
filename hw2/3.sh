# lambdas=(0 0.95 0.98 0.99 1)
lambdas=(0.99)

for lmd in "${lambdas[@]}"
do
    python cs285/scripts/run_hw2.py \
        --env_name LunarLander-v2 --ep_len 1000 \
        --discount 0.99 -n 300 -l 3 -s 128 -b 2000 -lr 0.001 \
        --use_reward_to_go --use_baseline --gae_lambda $lmd \
        --exp_name lunar_lander_lambda_$lmd \
        # > log_lunar_lander_lambda_$lmd.log
done