
# BidsValidatorA

# Table of Contents
1. [ General usage](#General-usage-)
2. [Specific usage](#Specific-usage-)
3. [Testing usage](#Testing-usage-)
4. [Details](#Details-)


## General usage :
```
usage: BidsValidatorA.py [-h] [-v] path

positional arguments:
  path           Path to your folder

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity

```

## Specific usage :

```
$Python resources/BidsValidatorA.py Tests/DataSets/FirstDataSet/Data
```
OR verbose usage  :
```
$Python resources/BidsValidatorA.py Tests/DataSets/FirstDataSet/Data
```

## Testing usage :

```
$cd Bids-validator-web/
$python3.5 -m unittest discover -v
```
## Details :

In resources folder  :

 - file BidsValidatorA.py is the main file 
 - file Error.py is the custom error exception file
 - file BidsEngine.py is the file that verify  with the rules 

In the Rules folder :

 - data_rules.json regex for data rules
 - date_rules.json regex for date rules
 - subject_rules.json regex for subject rules
 - source_rules.json  regex for source rules

 

