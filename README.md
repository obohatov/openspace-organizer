# OpenSpace Organizer

## Description
OpenSpace Organizer is a Python script designed to automate the seat allocation process in an open plan office or shared workspace. This script is especially useful for companies with flexible seating arrangements, as it can assign employees to seats on a daily basis.

## Installation
To install the script, you'll need to have Python installed on your machine. You can clone the repository to your local machine using the following commands:
```bash
git clone https://github.com/obohatov/openspace-organizer.git
cd openspace-organizer
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

## Usage
To run the script, you can execute the main.py file from your command line:
```
python main.py
```
The script reads an Excel file containing the names of the employees, which is by default named colleagues.xlsx. It then assigns each employee to an available seat and prints the assignments in your terminal. 

The resulting seating plan is output to your console and also saved to an Excel file named "output.xlsx".

## Visuals
![How it works in practice](./assets/Bu2A.gif)
