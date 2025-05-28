# Marine eDNA Analysis System Build Plan

## Overview

This build plan provides a phase-based implementation guide for creating a comprehensive bioinformatics workflow that analyzes Oxford Nanopore marine eDNA sequences using HUMANn3. The system serves dual purposes: as a production-ready analysis pipeline and as an educational resource teaching marine bio-monitoring through literate programming.

### System Architecture Summary
- **Core Framework**: Jupytext-managed notebooks (`.py` source control, `.ipynb` runtime)
- **Analysis Engine**: HUMANn3 with marine-specific adaptations
- **Educational Layer**: Integrated tutorials and explanations throughout
- **Target Audiences**: Expert bioinformaticians, bright students, ocean stakeholders

### Key Design Principles
1. **Literate Programming**: Code and education interweaved
2. **Marine-First**: All algorithms adapted for ocean data
3. **Version Control**: Clean git history via Jupytext
4. **Modular Design**: Reusable components in `DAG-steps/`

## Prerequisites

### Software Requirements
```yaml
# Core Dependencies
python: ">=3.8,<3.11"
jupytext: ">=1.14.0"
jupyter: ">=1.0.0"
humann3: ">=3.6"
metaphlan: ">=4.0"
diamond: ">=2.0.15"
bowtie2: ">=2.4"

# Scientific Computing
numpy: ">=1.21.0"
pandas: ">=1.3.0"
scipy: ">=1.7.0"
scikit-learn: ">=1.0.0"

# Visualization
matplotlib: ">=3.5.0"
seaborn: ">=0.11.0"
plotly: ">=5.0.0"
altair: ">=4.2.0"

# Bioinformatics
biopython: ">=1.79"
pysam: ">=0.19.0"
```

### System Requirements
- **Memory**: 16GB minimum, 32GB recommended
- **Storage**: 100GB for reference databases
- **OS**: Linux (Ubuntu 20.04+ or CentOS 7+) or macOS 11+

### Reference Data Prerequisites
- Marine-adapted ChocoPhlAn database
- Ocean microbiome UniRef90 subset
- SILVA SSU Ref NR99 (marine subset)
- Custom marine metabolic pathways database

---

## Phase 1: Foundation and Infrastructure

### Objective
Establish repository structure, implement Jupytext workflow, and create core configuration system.

### 1.1 Repository Structure Creation

Create the following directory structure:
```bash
marine-edna-humann3/
├── README.md                    # (already created)
├── BUILD_PLAN.md               # (this file)
├── main_workflow.py            # Jupytext source
├── checkout_notebook.sh        # Notebook checkout script
├── environment.yml             # Conda environment
├── .gitignore                  # Git configuration
├── config/
├── DAG-steps/
├── reference_data/
├── example_data/
├── educational_resources/
└── tests/
```

### 1.2 Jupytext Workflow Implementation

#### checkout_notebook.sh
```bash
#!/bin/bash
# checkout_notebook.sh - Convert .py to .ipynb for analysis

set -e

echo "Creating Jupyter notebook from main_workflow.py..."

# Generate timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
NOTEBOOK_NAME="analysis_${TIMESTAMP}.ipynb"

# Convert using jupytext
jupytext --to notebook main_workflow.py -o "$NOTEBOOK_NAME"

echo "✅ Created $NOTEBOOK_NAME"
echo ""
echo "To start your analysis:"
echo "  jupyter notebook $NOTEBOOK_NAME"
echo ""
echo "Remember: Edit main_workflow.py for permanent changes!"
```

#### .gitignore Configuration
```gitignore
# Jupyter notebooks (except examples)
*.ipynb
!example_data/expected_outputs/*.ipynb

# Checkpoint files
.ipynb_checkpoints/

# Large data files
*.fastq
*.fastq.gz
*.fasta
*.fasta.gz

# Reference databases
reference_data/databases/

# Temporary files
tmp/
*.tmp
```

### 1.3 Core Configuration System

#### config/default_config.yaml
```yaml
# Marine eDNA Analysis Configuration
workflow:
  name: "marine_edna_metabolic_analysis"
  version: "1.0.0"
  
# Environment profile
marine_environment:
  type: "coastal"  # Options: coastal, pelagic, deep-sea, polar
  depth_range: [0, 200]  # meters
  salinity_expected: [30, 38]  # PSU
  
# Quality Control Parameters
quality_control:
  min_read_length: 1000
  max_read_length: 50000
  min_quality_score: 7
  remove_adapters: true
  detect_contamination: true
  contamination_db: "reference_data/marine_markers/terrestrial_markers.fasta"
  
# HUMANn3 Configuration
humann3:
  nucleotide_database: "marine_chocophlan"
  protein_database: "marine_uniref90"
  metaphlan_db: "mpa_v31_CHOCOPhlAn_201901"
  bypass_translated_search: false
  threads: 8
  
# Marine-specific parameters
marine_adaptations:
  normalize_by_salinity: true
  apply_depth_correction: true
  remove_terrestrial_taxa: true
  minimum_marine_confidence: 0.85
```

### 1.4 Main Workflow Foundation

#### main_workflow.py (Initial Structure)
```python
# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
# ---

# %% [markdown]
# # Marine eDNA Metabolic Network Analysis
# 
# ## 🌊 Understanding Ocean Health Through Microbial Metabolism
# 
# This workflow analyzes environmental DNA (eDNA) from seawater samples to reveal
# the metabolic potential of marine microbial communities. By understanding what
# biochemical processes these microbes can perform, we gain insights into ocean
# health, nutrient cycling, and ecosystem function.

# %% [markdown]
# ## Learning Objectives
# 
# By completing this workflow, you will:
# 1. Understand how eDNA reveals microbial community function
# 2. Learn to process Oxford Nanopore long-read sequences
# 3. Master HUMANn3 for metabolic pathway analysis
# 4. Interpret metabolic profiles in marine ecological context
# 5. Create publication-ready visualizations of your findings

# %% [markdown]
# ## Workflow Overview
# 
# ```
# Raw Nanopore Reads → Quality Control → Taxonomic Profiling → 
# HUMANn3 Analysis → Marine Normalization → Time Series Analysis → 
# Interactive Visualizations
# ```

# %%
# Import core utilities
import sys
import yaml
from pathlib import Path

# Add our modules to path
sys.path.append(str(Path.cwd()))

# Load configuration
with open('config/default_config.yaml', 'r') as f:
    config = yaml.safe_load(f)

print(f"🌊 Marine eDNA Analysis Pipeline v{config['workflow']['version']}")
print(f"📍 Environment Profile: {config['marine_environment']['type']}")
```

### Phase 1 Validation Criteria
- [ ] Directory structure created successfully
- [ ] checkout_notebook.sh creates timestamped notebooks
- [ ] Jupytext conversion works both directions
- [ ] Configuration loads without errors
- [ ] Git ignores .ipynb files correctly
- [ ] main_workflow.py has proper percent format

---

## Phase 2: Data Processing Pipeline

### Objective
Implement quality control, denoising, and taxonomic profiling modules with full marine adaptations.

### 2.1 Quality Control Module

#### DAG-steps/01_quality_control.py
```python
"""
Marine eDNA Quality Control Module

This module implements Nanopore-specific quality control with marine
contamination detection. It ensures only high-quality marine sequences
proceed to analysis.

Scientific Rationale:
Marine eDNA samples often contain terrestrial contamination from
handling or atmospheric deposition. Long-read sequencing provides
unique opportunities to detect chimeric sequences that might indicate
contamination events.
"""

from typing import Dict, List, Tuple
import logging
from pathlib import Path
import numpy as np
from Bio import SeqIO
from Bio.Seq import Seq

logger = logging.getLogger(__name__)

def quality_filter_nanopore(
    input_fastq: Path,
    output_fastq: Path,
    config: Dict,
    educational_mode: bool = False
) -> Dict[str, any]:
    """
    Filter Nanopore reads for quality and length.
    
    This function implements marine-specific quality control including:
    - Length filtering optimized for marine genes
    - Quality score thresholds for Nanopore chemistry
    - Contamination detection using terrestrial markers
    
    Args:
        input_fastq: Path to input FASTQ file
        output_fastq: Path to filtered output
        config: Configuration dictionary
        educational_mode: Enable verbose educational output
        
    Returns:
        Dictionary with QC statistics and educational insights
    """
    if educational_mode:
        logger.info("🔬 Starting Quality Control...")
        logger.info("Did you know? Marine microbes have smaller genomes than soil microbes!")
    
    # Implementation here
    stats = {
        'total_reads': 0,
        'passed_reads': 0,
        'contamination_detected': 0,
        'length_distribution': []
    }
    
    return stats

def detect_terrestrial_contamination(
    sequence: Seq,
    markers_db: Path,
    threshold: float = 0.85
) -> bool:
    """
    Screen sequences for terrestrial contamination.
    
    Marine samples can contain DNA from:
    - Atmospheric deposition
    - River runoff
    - Sample handling
    
    We use curated terrestrial marker genes to identify
    likely contaminants.
    """
    # Implementation
    pass
```

### 2.2 Denoising Module

#### DAG-steps/02_denoising.py
```python
"""
Nanopore Denoising for Marine eDNA

Long-read sequencing has characteristic error patterns that must
be corrected before downstream analysis. Marine sequences pose
unique challenges due to high AT content in some organisms.
"""

def denoise_marine_nanopore(
    input_fastq: Path,
    output_fastq: Path,
    config: Dict
) -> Dict[str, any]:
    """
    Apply marine-optimized denoising to Nanopore reads.
    
    Key adaptations:
    - AT-rich region handling for marine bacteria
    - Homopolymer correction tuned for ocean samples
    - Preservation of natural sequence diversity
    """
    pass
```

### 2.3 Taxonomic Profiling Module

#### DAG-steps/03_taxonomic_profiling.py
```python
"""
Marine Taxonomic Profiling

Accurate taxonomic assignment in marine environments requires
specialized databases and depth-aware classification strategies.
"""

def profile_marine_taxa(
    input_sequences: Path,
    output_profile: Path,
    config: Dict,
    depth_meters: float = None
) -> Dict[str, any]:
    """
    Assign taxonomy with marine-specific optimizations.
    
    Depth-based adjustments:
    - Photic zone (0-200m): Expect phototrophs
    - Mesopelagic (200-1000m): Expect heterotrophs
    - Deep sea (>1000m): Expect pressure-adapted taxa
    """
    pass
```

### 2.4 Integration with Main Workflow

Update main_workflow.py to include:
```python
# %% [markdown]
# ## Step 1: Quality Control
# 
# ### 🧪 The Challenge of Ocean Sampling
# 
# When we collect seawater, we capture DNA from countless organisms:
# - Free-living bacteria and archaea
# - Phytoplankton and their associated microbes  
# - Viruses and mobile genetic elements
# - Unfortunately, sometimes terrestrial contamination!
# 
# Our first task is ensuring we analyze only true marine sequences.

# %%
from DAG_steps import quality_control as qc

# Configure QC for marine samples
qc_config = config['quality_control']
qc_config['educational_mode'] = True  # Enable teaching mode

# Process reads with educational output
qc_results = qc.quality_filter_nanopore(
    input_fastq=Path("data/raw_sequences.fastq"),
    output_fastq=Path("data/qc_passed.fastq"),
    config=qc_config
)

# %% [markdown]
# ### 📊 Understanding Your QC Results
# 
# The quality control step removed {qc_results['failed_percent']:.1f}% of reads.
# This might seem like a lot, but it ensures our downstream analysis is reliable.
# 
# Key insights from your data:
# - Average read length: {qc_results['avg_length']:.0f} bp
# - Contamination detected: {qc_results['contamination_percent']:.1f}%
# - Quality distribution: [visualization here]
```

### Phase 2 Validation Criteria
- [ ] QC module filters reads correctly
- [ ] Contamination detection identifies terrestrial sequences
- [ ] Denoising improves sequence quality metrics
- [ ] Taxonomic profiling assigns marine taxa accurately
- [ ] Educational outputs explain each step
- [ ] Main workflow integrates all modules

---

## Phase 3: HUMANn3 Integration

### Objective
Wrap HUMANn3 with marine-specific databases and implement ocean-adapted normalizations.

### 3.1 HUMANn3 Wrapper

#### DAG-steps/04_humann3_execution.py
```python
"""
Marine-Optimized HUMANn3 Execution

HUMANn3 quantifies metabolic pathways from metagenomic data.
For marine samples, we use specialized databases that better
represent ocean microbial diversity.
"""

def run_humann3_marine(
    input_sequences: Path,
    output_dir: Path,
    config: Dict,
    sample_metadata: Dict = None
) -> Dict[str, any]:
    """
    Execute HUMANn3 with marine adaptations.
    
    Marine-specific features:
    - Custom ocean pathway definitions
    - Salinity-adjusted abundance calculations
    - Integration of depth/temperature metadata
    
    Args:
        input_sequences: QC-passed sequences
        output_dir: Directory for HUMANn3 outputs
        config: HUMANn3 configuration
        sample_metadata: Environmental parameters
        
    Returns:
        Pathway abundance tables and statistics
    """
    # Set up marine databases
    # Run HUMANn3
    # Apply marine corrections
    pass
```

### 3.2 Marine Normalization Module

#### DAG-steps/05_marine_normalization.py
```python
"""
Marine-Specific Abundance Normalization

Ocean samples require special normalization due to:
- Variable biomass across depths
- Salinity effects on DNA recovery
- Temperature-dependent metabolic rates
"""

def normalize_marine_abundances(
    pathway_abundances: Path,
    sample_metadata: Dict,
    normalization_method: str = "marine_biomass_adjusted"
) -> pd.DataFrame:
    """
    Apply oceanographic normalizations to pathway abundances.
    
    Methods available:
    - marine_biomass_adjusted: Correct for depth-dependent biomass
    - salinity_corrected: Adjust for DNA recovery efficiency
    - temperature_scaled: Account for metabolic rate differences
    """
    pass
```

### 3.3 Marine Pathway Definitions

#### reference_data/ocean_metabolic_pathways/marine_pathways.yaml
```yaml
# Custom Marine Metabolic Pathways
marine_carbon_pathways:
  DMS_degradation:
    name: "Dimethylsulfoniopropionate degradation"
    importance: "Climate regulation through cloud formation"
    key_genes: ["dmdA", "dddP", "dddD"]
    
  carbon_concentration:
    name: "Carbon concentrating mechanisms"
    importance: "CO2 fixation in low-CO2 ocean waters"
    key_genes: ["ccmK", "ccmL", "ccmM"]
```

### Phase 3 Validation Criteria
- [ ] HUMANn3 runs successfully with marine databases
- [ ] Pathway abundances are generated
- [ ] Marine normalizations apply correctly
- [ ] Custom pathways are detected
- [ ] Output formats are correct
- [ ] Integration with workflow is smooth

---

## Phase 4: Analysis and Visualization

### Objective
Implement time series analysis and create interactive visualizations for metabolic profiles.

### 4.1 Time Series Analysis Module

#### DAG-steps/06_timeseries_analysis.py
```python
"""
Temporal Analysis of Marine Metabolic Functions

Ocean systems show strong seasonal patterns. This module
detects trends and anomalies in metabolic potential over time.
"""

def analyze_metabolic_timeseries(
    abundance_table: pd.DataFrame,
    time_points: List[str],
    config: Dict
) -> Dict[str, any]:
    """
    Perform temporal analysis on metabolic profiles.
    
    Analyses include:
    - Seasonal decomposition
    - Trend detection
    - Anomaly identification
    - Correlation with environmental variables
    """
    pass
```

### 4.2 Visualization Module

#### DAG-steps/07_visualization.py
```python
"""
Interactive Visualizations for Marine Metabolic Data

Create publication-ready figures that tell the story
of ocean microbial metabolism.
"""

def create_metabolic_heatmap(
    abundance_data: pd.DataFrame,
    metadata: pd.DataFrame,
    output_path: Path,
    interactive: bool = True
) -> None:
    """
    Generate interactive heatmap of metabolic pathways.
    
    Features:
    - Hierarchical clustering
    - Time slider for temporal exploration
    - Environmental parameter overlay
    - Export to static formats
    """
    pass
```

### 4.3 Workflow Integration

```python
# %% [markdown]
# ## Step 5: Visualizing Ocean Metabolism
# 
# ### 🎨 Making Data Tell a Story
# 
# Our final step transforms complex metabolic data into
# intuitive visualizations that reveal patterns in ocean health.

# %%
from DAG_steps import visualization as viz

# Create interactive heatmap
viz.create_metabolic_heatmap(
    abundance_data=normalized_abundances,
    metadata=sample_metadata,
    output_path=Path("results/metabolic_heatmap.html"),
    interactive=True
)

# %% [markdown]
# ### 🔍 What Do These Patterns Mean?
# 
# The heatmap reveals several important patterns:
# 
# 1. **Seasonal Cycling**: Notice how photosynthesis pathways peak in summer
# 2. **Depth Stratification**: Deep samples lack photosynthesis but show
#    enhanced genes for pressure adaptation
# 3. **Nutrient Indicators**: Nitrogen cycling genes indicate nutrient availability
```

### Phase 4 Validation Criteria
- [ ] Time series analysis detects known seasonal patterns
- [ ] Visualizations render correctly
- [ ] Interactive features work
- [ ] Export formats are publication-ready
- [ ] Workflow produces complete analysis

---

## Phase 5: Educational Enhancement

### Objective
Add comprehensive educational materials, exercises, and assessments.

### 5.1 Tutorial Dataset Creation

#### example_data/generate_tutorial_data.py
```python
"""
Generate small tutorial datasets that demonstrate key concepts
while running quickly on student laptops.
"""

def create_tutorial_dataset():
    """
    Generate tutorial data with known properties:
    - Mix of marine and terrestrial sequences (for QC demo)
    - Multiple time points (for time series)
    - Clear metabolic signatures (for interpretation)
    """
    pass
```

### 5.2 Interactive Exercises

Add to main_workflow.py:
```python
# %% [markdown]
# ## 🎯 Exercise 1: Exploring Quality Thresholds
# 
# How does changing the quality threshold affect your results?
# 
# Try modifying the minimum quality score below and re-running:

# %%
# STUDENT EXERCISE: Try values between 5 and 15
exercise_qc_config = config['quality_control'].copy()
exercise_qc_config['min_quality_score'] = 7  # <-- Change this!

# Run QC with your threshold
exercise_results = qc.quality_filter_nanopore(
    input_fastq=Path("example_data/tutorial_sequences/coastal_sample_01.fastq"),
    output_fastq=Path("tmp/exercise_output.fastq"),
    config=exercise_qc_config
)

print(f"Reads passing QC: {exercise_results['passed_reads']}")
print(f"Think about: Why might marine samples have different quality distributions?")
```

### 5.3 Assessment Materials

#### educational_resources/assessments.md
```markdown
# Self-Assessment Questions

## Module 1: Quality Control
1. Why is terrestrial contamination a particular concern for marine samples?
2. How do Nanopore error patterns affect downstream analysis?
3. What read length range is optimal for marine metabolic analysis?

## Module 2: Metabolic Analysis
1. Which metabolic pathways are unique to marine environments?
2. How does depth affect microbial metabolic potential?
3. Why normalize by salinity?

[Include answer key with explanations]
```

### Phase 5 Validation Criteria
- [ ] Tutorial dataset runs in <5 minutes
- [ ] Exercises have clear learning objectives
- [ ] Assessment questions cover key concepts
- [ ] Educational narratives are engaging
- [ ] Difficulty progression is appropriate

---

## Phase 6: Testing and Documentation

### Objective
Ensure robustness through comprehensive testing and create complete documentation.

### 6.1 Test Suite

#### tests/test_workflow_integrity.py
```python
"""
End-to-end workflow testing
"""

def test_complete_workflow():
    """Run full pipeline on test data"""
    pass

def test_marine_adaptations():
    """Verify marine-specific features work correctly"""
    pass
```

### 6.2 API Documentation

#### docs/api_reference.md
```markdown
# API Reference

## Quality Control Module

### quality_filter_nanopore
Filter Nanopore reads with marine-specific QC.

**Parameters:**
- input_fastq (Path): Input FASTQ file
- output_fastq (Path): Output path
- config (Dict): Configuration dictionary

**Returns:**
- Dict: QC statistics including contamination metrics
```

### 6.3 Troubleshooting Guide

#### educational_resources/troubleshooting_guide.md
```markdown
# Troubleshooting Common Issues

## Problem: High contamination rates
**Symptoms:** >10% sequences flagged as terrestrial
**Causes:** 
- Sample collection near shore
- Atmospheric deposition
- Lab contamination

**Solutions:**
1. Review sampling protocols
2. Check blank controls
3. Adjust contamination thresholds for coastal samples
```

### Phase 6 Validation Criteria
- [ ] All tests pass
- [ ] Documentation is complete
- [ ] Troubleshooting covers common issues
- [ ] Examples run successfully
- [ ] System is ready for release

---

## Integration Instructions

### Connecting Components
Each phase builds on the previous, but modules communicate through well-defined interfaces:

1. **File Formats**: 
   - FASTQ for sequences
   - TSV for abundance tables
   - YAML for configuration
   - JSON for metadata

2. **Data Flow**:
   ```
   Raw FASTQ → QC Module → Cleaned FASTQ → 
   Taxonomic Module → Profile TSV → HUMANn3 → 
   Abundance TSV → Normalization → Analysis → 
   Visualizations
   ```

3. **Configuration Propagation**:
   - Central config in `config/default_config.yaml`
   - Each module reads relevant sections
   - Override with command-line arguments

### Final System Validation

Complete system is ready when:
- [ ] Tutorial completes without errors
- [ ] Expert bioinformaticians approve methods
- [ ] Students successfully complete exercises
- [ ] Visualizations effectively communicate results
- [ ] Git history is clean with .py files only
- [ ] Documentation enables independent use

---

## Success Metrics

The build succeeds when:
1. **Technical Excellence**: Pipeline processes real data accurately
2. **Educational Impact**: Students gain deep understanding
3. **Scientific Rigor**: Methods meet publication standards
4. **Accessibility**: Stakeholders understand ocean health implications
5. **Maintainability**: Clear code enables future development

Each phase should be implemented incrementally, with validation before proceeding to the next phase.