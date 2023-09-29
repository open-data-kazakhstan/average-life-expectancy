# Average life expecrancy and Amount of hospital facilities


## Installation

Clone the repository
```shell
$ git clone https://github.com/open-data-kazakhstan/inflation-and-avg-salary-with-projections.git
```

Requires Python 3.11.3 

Create a virtual environment and activate it 
```bash
pip install venv
python -m venv /path/to/localrepo
```

Swicth to venv directory by using cd comand
```bash
cd /path/to/localrepo
Scripts/activate
```

Install dependecies in venv by using pip
```bash
pip install -r requirements.txt
```

Run the project:
```bash
python scripts/main.py
```

## Data 

Salary data collected by hand from stat.gov stats: https://stat.gov.kz/

We downoladed data from this source and placed it in the data folders 

We have processed the source data to make it normalized and derived  several aggregated datasets from it:

* `data/Hosp_piv.csv` - sourсe data for amount of hospital facilities
* `data/life_X_piv.csv` - sourсe data for average life expectancy
* `data/Hosp_fin.csv` - expanded main dataset which predicts hospital facilities from 2023 to 2050
* `data/life_X_fin.csv` - expanded main dataset which predicts sourсe data for average life expectancy from 2023 to 2050
* `datapackage.json` - conatins all of the key information about our dataset

## Scripts

* `expand.py` - uses main dataset and expands it to 8 steps to make animation smoother
* `anim.py` - uses matplotlib to create an infographic about life expectancy 
* `Hosp_anim.py` - uses matplotlib to create an infographic about amount of hospital facilities
* `datapack.py` - creating datapckage.json file that conatinsall meatadata

## License

This dataset is licensed under the Open Data Commons [Public Domain and Dedication License][pddl].

[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/
