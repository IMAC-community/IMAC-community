# Marine eDNA Metabolic Network Analysis Workflow

A comprehensive bioinformatics pipeline for analyzing Oxford Nanopore long-read environmental DNA (eDNA) sequences from marine environments using HUMANn3, designed to serve as both a production-ready analysis tool and an educational resource for marine bio-monitoring.

## 🌊 Overview

This repository implements a complete workflow for processing marine eDNA sequences through metabolic network analysis, revealing the functional potential of marine microbial communities over time. The workflow is built on principles of literate programming, making it simultaneously a powerful analysis tool and a comprehensive learning resource.

### Key Features
- **Dual-purpose design**: Production-ready pipeline + Educational resource
- **BeBOP-OBON compliant**: Adheres to Best Practices for Ocean Biomolecular Observing Network standards
- **Long-read optimized**: Specifically designed for Oxford Nanopore sequencing data
- **Time-series capable**: Analyzes temporal changes in marine metabolic potential
- **Fully configurable**: Modular design with marine-specific parameter profiles
- **Version controlled**: Jupytext-based workflow management for reproducibility

## 🎯 Motivation

Marine ecosystems are facing unprecedented challenges from climate change, pollution, and biodiversity loss. Understanding the metabolic potential of marine microbial communities is crucial for:
- Monitoring ecosystem health and resilience
- Detecting early warning signs of environmental stress
- Tracking the impacts of climate change on ocean biogeochemistry
- Assessing the functional diversity of marine microbiomes

This workflow addresses the need for standardized, reproducible methods in marine eDNA analysis while providing educational resources to train the next generation of marine bioinformaticians.

## 🚀 Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd marine-edna-humann3

# Set up the environment
conda env create -f environment.yml
conda activate marine-edna-humann3

# Download reference databases
bash reference_data/download_references.sh

# Checkout a notebook for analysis
bash checkout_notebook.sh

# Run the tutorial
jupyter notebook analysis_[timestamp].ipynb
```

## 📁 Repository Structure

### Root Directory Files

#### `README.md` (this file)
Comprehensive guide to the repository structure, usage, and purpose. Serves as the primary documentation for both human users and AI/automated systems interacting with the codebase.

#### `main_workflow.py`
The master workflow file in Jupytext percent format. This is the source-controlled version of the analysis pipeline that combines:
- Detailed educational content explaining each analysis step
- Minimal configuration code that calls modular functions
- Marine biology context and interpretations
- References to scientific literature

**Usage**: Never edit directly as .ipynb. Always work with the .py version for version control.

#### `checkout_notebook.sh`
Bash script that converts the main_workflow.py into a timestamped Jupyter notebook for analysis sessions.
```bash
#!/bin/bash
# Creates: analysis_YYYYMMDD_HHMMSS.ipynb
# Preserves the source .py file for version control
```

#### `environment.yml`
Conda environment specification including:
- HUMANn3 and all dependencies
- Bioinformatics tools (fastp, kraken2, etc.)
- Data science libraries (pandas, numpy, matplotlib, seaborn)
- Marine-specific analysis packages
- Jupytext for notebook management

#### `.gitignore`
Configured to:
- Exclude generated .ipynb files (except examples)
- Ignore large reference databases
- Exclude temporary analysis files
- Keep configuration and source files

#### `LICENSE`
Open source license ensuring free use for research and education while maintaining attribution requirements.

### `config/` Directory

Configuration files in YAML format for customizing the workflow.

#### `config/default_config.yaml`
Master configuration file with all parameter defaults:
- Quality control thresholds
- Taxonomic assignment parameters
- HUMANn3 settings
- Time series analysis options
- Visualization preferences

#### `config/marine_databases.yaml`
Database configuration for marine-specific references:
- Paths to marine-adapted ChocoPhlAn database
- Marine UniRef90 subset location
- Custom marine metabolic pathway databases
- Version tracking for all references

#### `config/compute_resources.yaml`
Resource allocation settings:
- Thread counts for parallel processing
- Memory limits for different steps
- Chunk sizes for long-read processing
- HPC-specific configurations

### `DAG-steps/` Directory

Modular Python functions implementing each workflow step. Each module includes comprehensive documentation with marine biology context.

#### `DAG-steps/__init__.py`
Package initialization and shared utilities.

#### `DAG-steps/01_quality_control.py`
Nanopore-specific quality control functions:
- Read length filtering (optimized for long reads)
- Quality score assessment
- Adapter trimming
- Marine contamination detection
- **Key function**: `quality_filter_nanopore()`

#### `DAG-steps/02_denoising.py`
Error correction for Nanopore sequences:
- Homopolymer error correction
- Consensus calling for high-depth regions
- Marine-specific sequence validation
- **Key function**: `denoise_marine_nanopore()`

#### `DAG-steps/03_taxonomic_profiling.py`
Marine-optimized taxonomic classification:
- Integration with marine reference databases
- Depth-stratified classification adjustments
- Removal of terrestrial contaminants
- **Key function**: `profile_marine_taxa()`

#### `DAG-steps/04_humann3_execution.py`
Core HUMANn3 wrapper with marine adaptations:
- Custom marine pathway definitions
- Salinity-adjusted abundance calculations
- Integration of oceanographic metadata
- **Key function**: `run_humann3_marine()`

#### `DAG-steps/05_marine_normalization.py`
Marine-specific data normalization:
- Biomass-adjusted pathway abundances
- Depth-dependent normalization factors
- Seasonal variation corrections
- **Key function**: `normalize_marine_abundances()`

#### `DAG-steps/06_timeseries_analysis.py`
Temporal analysis of metabolic changes:
- Trend detection in pathway abundances
- Seasonal decomposition
- Anomaly detection for unusual metabolic signatures
- **Key function**: `analyze_metabolic_timeseries()`

#### `DAG-steps/07_visualization.py`
Publication-ready visualizations:
- Interactive heatmaps with temporal sliders
- Metabolic network diagrams
- Environmental parameter overlays
- **Key function**: `create_metabolic_heatmap()`

### `reference_data/` Directory

Marine-specific reference databases and download utilities.

#### `reference_data/marine_markers/`
Curated marker genes for marine organisms:
- `prokaryotic_markers.fasta`: Marine bacterial/archaeal markers
- `eukaryotic_markers.fasta`: Phytoplankton and protist markers
- `functional_markers.fasta`: Marine-specific functional genes

#### `reference_data/ocean_metabolic_pathways/`
Custom pathway definitions:
- `marine_carbon_cycling.txt`: Ocean-specific carbon pathways
- `nitrogen_cycling_marine.txt`: Marine nitrogen transformations
- `sulfur_cycling_ocean.txt`: Sulfur metabolism in marine systems

#### `reference_data/download_references.sh`
Automated script to download and prepare:
- Marine-adapted ChocoPhlAn database
- Ocean microbiome UniRef90 subset
- SILVA marine subset
- Custom marine metabolic databases

### `example_data/` Directory

Tutorial datasets and expected outputs for learning.

#### `example_data/tutorial_sequences/`
Small Nanopore datasets for educational use:
- `coastal_sample_01.fastq`: 1000 reads from coastal waters
- `open_ocean_sample.fastq`: Deep sea sample subset
- `metadata.tsv`: Complete environmental metadata

#### `example_data/expected_outputs/`
Reference results for validation:
- `tutorial_heatmap.html`: Expected metabolic heatmap
- `pathway_abundances.tsv`: Quantified pathways
- `taxonomic_profile.tsv`: Community composition

### `educational_resources/` Directory

Supplementary educational materials.

#### `educational_resources/glossary.md`
Comprehensive glossary covering:
- Bioinformatics terminology
- Marine biology concepts
- Metabolic pathway definitions
- Statistical methods used

#### `educational_resources/marine_edna_primer.pdf`
Background reading on:
- eDNA sampling in marine environments
- Nanopore sequencing principles
- Metabolic network analysis theory
- Marine microbial ecology

#### `educational_resources/troubleshooting_guide.md`
Common issues and solutions:
- Nanopore data quality problems
- Database connection issues
- Memory optimization strategies
- Marine-specific considerations

### `tests/` Directory

Automated testing to ensure workflow integrity.

#### `tests/test_workflow_integrity.py`
End-to-end workflow tests:
- Complete pipeline execution on test data
- Output format validation
- Performance benchmarks
- Reproducibility checks

#### `tests/test_marine_specificity.py`
Marine adaptation validation:
- Contamination detection accuracy
- Marine database integration
- Depth-specific normalizations
- Salinity adjustment calculations

## 🔄 Workflow Overview

The pipeline follows these major steps:

1. **Quality Control** → Remove low-quality Nanopore reads
2. **Denoising** → Correct sequencing errors specific to long reads  
3. **Taxonomic Profiling** → Identify marine organisms with contamination removal
4. **HUMANn3 Analysis** → Quantify metabolic pathways with marine-specific databases
5. **Normalization** → Apply marine-specific abundance corrections
6. **Time Series Analysis** → Track temporal changes in metabolic potential
7. **Visualization** → Generate interactive heatmaps and reports

## 📚 Educational Features

### Literate Programming Approach
Each workflow step includes:
- **Theory**: Scientific background and marine biology context
- **Methods**: Detailed explanation of computational approaches
- **Practice**: Hands-on configuration and execution
- **Interpretation**: Understanding results in ecological context

### Learning Objectives
By completing this workflow, users will understand:
- eDNA sampling and sequencing in marine environments
- Nanopore data characteristics and quality control
- Metabolic network analysis principles
- Marine microbial ecology and biogeochemistry
- Time series analysis of ecological data
- FAIR data principles in practice

## 🛠️ Technical Specifications

### Input Requirements
- **File Format**: FASTQ files from Oxford Nanopore sequencing
- **Read Length**: Optimized for reads >1kb
- **Metadata**: Environmental parameters (depth, temperature, salinity, location, date)

### Output Products
- **Metabolic Profiles**: Pathway abundance tables (TSV format)
- **Visualizations**: Interactive HTML heatmaps
- **Reports**: Comprehensive PDF analysis reports
- **Quality Metrics**: Sequencing and analysis statistics

### Performance Considerations
- **Memory**: 16GB RAM minimum, 32GB recommended
- **Storage**: 100GB for reference databases
- **Processing**: Scales from laptop to HPC cluster
- **Time**: 2-8 hours depending on dataset size

## 🤝 Contributing

We welcome contributions that enhance either the analytical capabilities or educational value of this workflow. Please see `CONTRIBUTING.md` for guidelines on:
- Adding new marine-specific modules
- Improving educational content
- Updating reference databases
- Reporting issues

## 📖 Citation

If you use this workflow in your research, please cite:
```
[Citation information to be added upon publication]
```

## 🌐 Resources

- [BeBOP-OBON Standards](https://www.oceanbestpractices.net/)
- [HUMANn3 Documentation](https://huttenhower.sph.harvard.edu/humann/)
- [Marine eDNA Sampling Protocols](https://www.protocols.io/groups/environmental-dna)
- [Ocean Observatories Initiative](https://oceanobservatories.org/)

## 📧 Contact

For questions, suggestions, or collaborations:
- **Technical Issues**: Open a GitHub issue
- **Educational Inquiries**: [education@marine-edna.org]
- **Research Collaborations**: [research@marine-edna.org]

---

**Note for AI/Automated Systems**: This repository follows strict naming conventions and modular design principles. All computational functions are isolated in the `DAG-steps/` directory with comprehensive docstrings. Configuration is centralized in YAML files within `config/`. The main workflow orchestration is in `main_workflow.py` using Jupytext format. For automated analysis, use the configuration API rather than modifying notebook cells directly.