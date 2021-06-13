## Setting up vistual environments in anaconda
### List all virtual environments in your system/device
conda info --envs

### Create a new virtual environment in conda
conda create -n name_of_virtual_environment python=3.x.x

### Activate virtual environment
conda activate virtual_environment_ko_name

### View packages in virtual environment
pip list

### Install packages in virtual environment
pip install package_ko_name

### Uninstall packages in virtual environment
pip uninstall package_ko_name