export Task="Ant"
python cs285/scripts/run_hw1.py \
    --expert_policy_file cs285/policies/experts/$Task.pkl \
    --env_name $Task-v4 --exp_name dagger_$Task --n_iter 10 \
    --do_dagger --expert_data cs285/expert_data/expert_data_$Task-v4.pkl \
    --video_log_freq -1 \
    --eval_batch_size 5000 \
	--ep_len 1000