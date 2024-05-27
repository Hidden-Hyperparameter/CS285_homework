# # No baseline
# python cs285/scripts/run_hw2.py --env_name HalfCheetah-v4 \
#     -n 100 -b 5000 -rtg --discount 0.95 -lr 0.01 \
#     --exp_name cheetah \
#     > log_cheetah.log
# Baseline
# python cs285/scripts/run_hw2.py --env_name HalfCheetah-v4 \
#     -n 100 -b 5000 -rtg --discount 0.95 -lr 0.01 \
#     --use_baseline -blr 0.01 -bgs 5 --exp_name cheetah_baseline \
#     > log_cheetah_baseline.log

# Experiments
python cs285/scripts/run_hw2.py --env_name HalfCheetah-v4 \
    -n 100 -b 5000 -rtg --discount 0.95 -lr 0.01 \
    --use_baseline -blr 0.01 -bgs 2 --exp_name cheetah_baseline_lowgs \
    > log_cheetah_baseline_lowgs.log

python cs285/scripts/run_hw2.py --env_name HalfCheetah-v4 \
    -n 100 -b 5000 -rtg --discount 0.95 -lr 0.01 \
    --use_baseline -blr 0.004 -bgs 5 --exp_name cheetah_baseline_lowlr \
    > log_cheetah_baseline_lowlr.log