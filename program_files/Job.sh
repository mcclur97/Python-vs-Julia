#!/bin/bash --login
########## SBATCH Lines for Resource Request ##########

#SBATCH --time=99:59:00             # limit of wall clock time - how long the job will run (same as -t)
#SBATCH --nodes=1                 # number of different nodes - could be an exact number or a range of nodes (same as -N)
#SBATCH --ntasks=1                  # number of tasks - how many tasks (nodes) that you require (same as -n)
#SBATCH --cpus-per-task=1           # number of CPUs (or cores) per task (same as -c)
#SBATCH --mem-per-cpu=20G            # memory required per allocated CPU (or core) - amount of memory (in bytes)
#SBATCH --job-name julia         # you can give your job a name for easier identification (same as -J)
#SBATCH -q normal

######### Command Lines to Run #########
module load julia/1.5.2

julia julia_matrix.jl

scontrol show job $SLURM_JOB_ID     ### write job information to output file#
