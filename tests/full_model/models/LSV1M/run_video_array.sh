#!/bin/bash
#SBATCH --job-name=video
#SBATCH --output=/home/fleiscl/video_runs/logs/video_%A_%a.out
#SBATCH --error=/home/fleiscl/video_runs/logs/video_%A_%a.err
#SBATCH --array=0-0
#SBATCH --partition=debug
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G

source /home/fleiscl/venvs/mozaik/bin/activate

BASE_DIR=/home/fleiscl/src/mozaik/tests/full_model/models/LSV1M
VIDEO_LIST="/home/fleiscl/video_runs/input/video_list.txt"
RESULTS_ROOT=/home/fleiscl/video_runs

mkdir -p "$RESULTS_ROOT/logs"

VIDEO_PATH=$(sed -n "$((SLURM_ARRAY_TASK_ID+1))p" "$VIDEO_LIST")

if [ -z "$VIDEO_PATH" ]; then
    echo "No video found for task $SLURM_ARRAY_TASK_ID"
    exit 1
fi

VIDEO_NAME=$(basename "$VIDEO_PATH" .npy)

export VIDEO_PATH
export VIDEO_NAME

echo "Running task $SLURM_ARRAY_TASK_ID"
echo "VIDEO_PATH=$VIDEO_PATH"
echo "VIDEO_NAME=$VIDEO_NAME"

cd "$BASE_DIR" || exit 1

python run_parameter_search_video.py run_video.py nest param/defaults
