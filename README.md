# RobocupSS3D_Optimization_Scripts

This is an open-source optimization script (Test) authored by Tianjian Jiang (a member of the Apollo3D team from 2021 to 2022) with the assistance of Hannes Braun (magmaOffenburg). Developed based on magma OffenburgRelease, this script is governed by the GPL LICENSE. Optimization_PC.py is a script designed for executing Robocup3D parallel optimization on a single machine.

This is an LTS program, with additional features to be uploaded later, so please feel free to raise issues and submit pull requests without hesitation.

## Setup Instructions

1. Clone the repository into a workspace folder of your choice.

```bash
git clone <address from github>
```

2. Install the Python Environment:

```bash
sudo apt install python3-pip
pip3 install numpy cma
```

3. Set the parameters in the origin_params.txt.

4. Add the script's address after "ROBOVIZ_SCRIPT=" (Line 15 in start_training.sh)

5. Run the optimization

```bash
python3 optimization_PC.py
```
If you want to custom the parameters with intial sigma d, n populations per generation and run totally k times:

```bash
python3 optimization_PC.py --sigma d --popsize n --run_times k
```

6. Test the optimized parameters

**Step 1**: Copy the params with the highest the value to the test_params.txt

**Step 2**: run the script

```bash
./start_training.sh true test_params.txt
```

**Notice**

Voluntarily adhering to the GPL LICENSE, we have proactively uploaded the source code of the binary used in the script at the following location:

https://github.com/Jiangtianjian/magmaRelease

Contributers:

Tianjian Jiang (Team leader of Apollo3D from 2021 to 2022), Hannes Braun(magmaOffenburg)

