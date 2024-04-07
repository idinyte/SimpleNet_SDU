datapath="$DATASET_DIR"
datasets=('screw')
dataset_flags=($(for dataset in "${datasets[@]}"; do echo '-d '"${dataset}"; done))

$CONDA_PREFIX/bin/python3.8 "$WORK_DIR"/SimpleNet_SDU/main.py
