# DAG-steps: Modular Analysis Functions

This directory contains the modular functions that implement each step of the marine eDNA metabolic network analysis workflow. Each module is designed to be self-contained, testable, and reusable.

## Module Overview

### 01_quality_control.py
**Purpose:** Nanopore-specific quality control with marine contamination detection

**Key Functions:**
- `quality_filter_nanopore()` - Main QC filtering function
- `detect_terrestrial_contamination()` - Identify non-marine sequences
- `calculate_read_quality_metrics()` - Compute quality statistics
- `filter_by_marine_characteristics()` - Apply marine-specific filters

**Marine Adaptations:**
- Detects terrestrial contamination (soil, freshwater, human)
- Handles AT-rich marine bacterial sequences
- Optimized length thresholds for marine genes

### 02_denoising.py
**Purpose:** Error correction optimized for marine Nanopore data

**Key Functions:**
- `denoise_marine_nanopore()` - Main denoising function
- `correct_homopolymers()` - Fix homopolymer errors
- `correct_at_rich_regions()` - Special handling for AT-rich sequences
- `preserve_marine_diversity()` - Avoid over-correction

**Marine Adaptations:**
- Preserves natural AT-richness in marine bacteria
- Tuned for high-diversity marine communities
- Handles low-coverage deep-sea samples

### 03_taxonomic_profiling.py
**Purpose:** Assign taxonomy with marine-specific optimizations

**Key Functions:**
- `profile_marine_taxa()` - Main profiling function
- `apply_depth_priors()` - Use depth to improve assignments
- `remove_terrestrial_contamination()` - Clean taxonomic profile
- `calculate_marine_diversity()` - Compute diversity metrics

**Marine Adaptations:**
- Depth-aware classification (phototrophs in photic zone)
- Marine-specific reference databases
- Identifies key marine clades (SAR11, Prochlorococcus, etc.)

### 04_humann3_execution.py
**Purpose:** Run HUMANn3 with marine-optimized parameters

**Key Functions:**
- `run_humann3_marine()` - Execute HUMANn3 pipeline
- `extract_marine_pathways()` - Focus on ocean-relevant pathways
- `apply_environmental_corrections()` - Adjust for temperature/depth
- `calculate_biogeochemical_indices()` - Compute ocean health metrics

**Marine Adaptations:**
- Custom marine pathway definitions (DMSP, CCM, etc.)
- Environmental corrections for abundance
- Focus on biogeochemically important pathways

### 05_marine_normalization.py (Placeholder)
**Purpose:** Apply marine-specific abundance corrections

**Planned Functions:**
- `normalize_by_biomass()` - Account for depth-dependent biomass
- `salinity_correction()` - Adjust for DNA recovery efficiency
- `temperature_scaling()` - Metabolic rate corrections

### 06_timeseries_analysis.py (Placeholder)
**Purpose:** Analyze temporal patterns in metabolic data

**Planned Functions:**
- `detect_seasonal_patterns()` - Find recurring cycles
- `identify_anomalies()` - Detect unusual metabolic signatures
- `correlate_with_environment()` - Link to oceanographic variables

### 07_visualization.py (Placeholder)
**Purpose:** Create publication-quality visualizations

**Planned Functions:**
- `create_metabolic_heatmap()` - Interactive pathway abundance heatmap
- `plot_diversity_depth_profile()` - Vertical diversity patterns
- `generate_network_diagram()` - Metabolic network visualization

## Usage Pattern

All modules follow a consistent pattern:

```python
from DAG_steps import quality_control as qc

# Run with configuration
results = qc.quality_filter_nanopore(
    input_fastq=Path("input.fastq"),
    output_fastq=Path("output.fastq"),
    config=config_dict,
    educational_mode=True  # Enable teaching outputs
)

# Results always include statistics and metrics
print(f"Processed {results['total_reads']} reads")
print(f"Passed QC: {results['passed_reads']}")
```

## Educational Features

Each module includes:
- Comprehensive docstrings explaining the science
- Educational mode with verbose outputs
- Example usage in docstrings
- Standalone educational functions

Example:
```python
# At the end of each module
if __name__ == "__main__":
    explain_quality_scores()
    demonstrate_example_analysis()
```

## Testing

Each module has associated tests in `../tests/`:
```bash
pytest tests/test_quality_control.py
pytest tests/test_workflow_integrity.py
```

## Configuration

Modules read configuration from YAML files:
- `config/default_config.yaml` - Main parameters
- `config/marine_databases.yaml` - Database paths
- `config/compute_resources.yaml` - Resource allocation

## Marine-Specific Design Decisions

1. **Contamination Detection:** Critical for marine samples due to sampling challenges
2. **Depth Awareness:** Many functions accept depth parameters for ecological context
3. **Diversity Preservation:** Avoid over-correcting natural variation
4. **Biogeochemical Focus:** Emphasize pathways important for ocean health
5. **Environmental Integration:** Always consider temperature, salinity, depth

## Future Development

To add new functionality:
1. Create new module following naming convention
2. Include comprehensive docstrings
3. Add educational examples
4. Implement marine-specific adaptations
5. Write associated tests

## Support

For questions about specific modules:
- Check module docstrings
- Run educational examples
- Consult the troubleshooting guide
- Open an issue on GitHub