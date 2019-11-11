# NLI_macrophage_iron_regulation

This NLI_macrophage_iron_regulation repository contains all resources pertaining to the mathematical model of iron control in macrophages during invasive pulmonary aspergillosis (IPA). This model will allow us to study iron regulation within a macrophage and its effect on iron level in the local environment in the context of IPA.

Files in this repository are arranged as such:

```bash
├── Macrophage_model.py
├── README.md
├── LICENSE.md
└── .gitignore
```

## Macrophage_model.py
This script contains a discrete dynamical system model that converts a static network into a dynamical model and computes steady state for the model. The model consists of generalized Boolean functions of how nodes (molecules) in the static network interact with each other and evolve with time.  The nodes in the model takes  0, 1 or 2 state representing low, medium or high expression level, respectively.

This static network is available [here](https://data.nutritionallungimmunity.org/#item/5dc05722ef2e2603553c5a0c)

The static network and the dynamic model is constructed by inferring relationships based on bioinformatics analysis, functional enrichment analysis and literature.

* Experimental data/results is [here](https://data.nutritionallungimmunity.org/#collection/5d41dcf7ef2e26236e2bb3ef)

* Bioinformatics analysis is [here](https://github.com/NutritionalLungImmunity/NLI_response_to_Aspergillus_fumigatus_omics_data_analysis/tree/master/Macrophage_Data_Analysis)

#### Prerequisites

Running the code depends on the following packages.
* [Python 2.7.16](https://www.python.org/downloads/release/python-2716/)
* [Python Library itertools](https://docs.python.org/2/library/itertools.html)
* [Python Library random](https://docs.python.org/3/library/random.html)

#### Run command
The code can be run on terminal using the following command.

```bash
python Macrophage_model.py outputfile.txt number_of_iterations
```
#### Code output
A text file with steady state - fixed and cyclic - of the systems and the number of basins that converge to a steady state.

## Authors
* Bandita Adhikari
-PhD student, UConn Health, Farmington, CT
* Joseph Masison
-MD/PhD student, UConn Health, Farmington, CT
* Luis Sordo Vieira
-Postdoctoral Associate, The Jackson Laboratory, Farmington, CT
* Reinhard Laubenbacher
-Professor, Center for Quantitative Medicine, UConn Health, Farmington, CT
-Professor, The Jackson Laboratory for Genomic Medicine, Farmington, CT

## License
This project is licensed under the MIT License - see LICENSE.md file for details.
