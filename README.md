# RobocupSS3D_Optimization_Scripts


This is the open-source optimization scripts(Test) written by Tianjian Jiang(Apollo3D team member from 2021 to 2023) under the help of Hannes Braun(magmaOffenburg). Also as a code developed based on magma OffenburgRelease, this script is based on the GPL LICENSE. The Optimization_PC.py is a script that allows you to run Robocup3D parallel optimization on a single machine.
This is a LTS program and more function would be upload later, so please do not hesitate to set up issues and pull requests.

## Setup Instructions

1. Clone the repository into a workspace folder of your choice.

```bash
git clone <address from github>
```

2. Install the Python Environment:

```bash
pip install numpy cma
```

3. Set the parameters in the origin_params.txt.

4. Run the optimization

```bash
python3 optimization_PC.py
```
If you want to custom the parameters with intial sigma d, n populations per generation and run totally k times:

```bash
python3 optimization_PC.py --sigma d --popsize n --run_times k
```

