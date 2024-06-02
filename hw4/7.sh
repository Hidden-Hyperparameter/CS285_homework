cd CS285_homework/hw4
export i=$1
python cs285/scripts/run_hw4.py -cfg experiments/mpc/reacher_ablation$i.yaml --my > log_task4_my_$i.log