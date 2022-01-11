# NLI_macrophage_iron_regulation

This NLI_macrophage_iron_regulation repository contains all resources pertaining to the mathematical model of iron control in macrophages during invasive pulmonary aspergillosis (IPA). This model will allow us to study iron regulation within a macrophage and its effect on iron level in the local environment in the context of IPA.

Files in this repository are arranged as such:

```bash
├── Macrophage_model.py
├── README.md
├── LICENSE.md
└── .gitignore
```

## macrophage_model_3state.py
This script contains a discrete dynamical system model that converts a static network into a dynamical model and computes steady state for the model. The model consists of generalized Boolean functions of how nodes (molecules) in the static network interact with each other and evolve with time.  The nodes in the model takes  0, 1 or 2 state representing low, medium or high expression level, respectively. 

This static network is available [here](https://github.com/NutritionalLungImmunity/NLI_macrophage_iron_regulation/blob/master/Wiring_diagram_macModel.png)

The static network and the dynamic model is constructed by inferring relationships based on bioinformatics analysis, functional enrichment analysis and literature.

* Bioinformatics analysis is [here](https://github.com/NutritionalLungImmunity/NLI_response_to_Aspergillus_fumigatus_omics_data_analysis/tree/master/Macrophage_Data_Analysis)

#### Prerequisites

Running the code depends on the following packages.
* [Python 3.0 or newer](https://www.python.org/downloads/)

#### Run command
The code can be run on terminal using the following command. Before running the model, the states of external parameters (fungal, iron levels - FE2, FE3, EHEME) need to fixed to the desired state.

```bash
python Macrophage_model.py outputfile.txt number_of_iterations
```
#### Code output
A text file with 
1. steady state - fixed and cyclic - of the systems
2. the number of basins that converge to a steady state
3. Intermediate steps to converge to a steady state

## Authors
* Bandita Adhikari
-PhD student, UConn Health, Farmington, CT
* Joseph Masison
-MD/PhD student, UConn Health, Farmington, CT
* Luis Sordo Vieira
-Postdoctoral Associate, The University of Florida, Geinesville, CT
* Reinhard Laubenbacher
-Professor, The University of Florida, Geinesville, CT

## License
This project is licensed under the MIT License - see LICENSE.md file for details.
