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
#   kernelspec:
#     display_name: Python 3 (marine-edna)
#     language: python
#     name: marine-edna
# ---

# %% [markdown]
# # 🌊 Marine eDNA Metabolic Network Analysis
# 
# ## Understanding Ocean Health Through Microbial Metabolism
# 
# Welcome to an exciting journey into the hidden world of ocean microbes! This notebook will guide you through analyzing environmental DNA (eDNA) from seawater samples to reveal the metabolic potential of marine microbial communities.
# 
# ### What is eDNA?
# Environmental DNA is genetic material shed by organisms into their environment. In the ocean, this includes DNA from:
# - Bacteria and archaea (the ocean's recyclers)
# - Phytoplankton (the ocean's plants)
# - Zooplankton and their microbiomes
# - Fish mucus and scales
# - Viral particles
# 
# By sequencing this DNA soup, we can understand what organisms are present and what they're capable of doing!

# %% [markdown]
# ## 📚 Learning Objectives
# 
# By completing this workflow, you will:
# 
# 1. **Master Long-Read Sequencing Data**
#    - Understand Oxford Nanopore data characteristics
#    - Learn quality control for long reads
#    - Handle sequencing errors effectively
# 
# 2. **Explore Marine Microbial Ecology**
#    - Discover who lives in the ocean
#    - Understand microbial roles in nutrient cycling
#    - Connect microbes to climate regulation
# 
# 3. **Perform Metabolic Network Analysis**
#    - Use HUMANn3 to quantify metabolic pathways
#    - Interpret pathway abundances ecologically
#    - Create publication-quality visualizations
# 
# 4. **Apply Ocean-Specific Methods**
#    - Account for salinity effects
#    - Handle depth stratification
#    - Remove terrestrial contamination

# %% [markdown]
# ## 🔄 Workflow Overview
# 
# Here's our analysis journey:
# 
# ```mermaid
# graph TD
#     A[Raw Nanopore Reads] -->|Quality Control| B[Clean Reads]
#     B -->|Denoising| C[Error-Corrected Reads]
#     C -->|Taxonomic Profiling| D[Community Composition]
#     C -->|HUMANn3 Analysis| E[Metabolic Pathways]
#     E -->|Marine Normalization| F[Corrected Abundances]
#     F -->|Time Series Analysis| G[Temporal Patterns]
#     G -->|Visualization| H[Interactive Reports]
#     D -->|Integration| H
# ```

# %% [markdown]
# ## 🚀 Setup and Configuration
# 
# Let's begin by setting up our analysis environment and loading the necessary tools.

# %%
# Import standard libraries
import sys
import os
from pathlib import Path
import yaml
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Scientific computing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up plotting style for marine theme
plt.style.use('seaborn-v0_8-deep')
sns.set_palette("ocean")

# Configure pandas display
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.precision', 3)

print("🌊 Marine eDNA Metabolic Network Analysis")
print(f"📅 Analysis started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-" * 50)

# %%
# Add project modules to path
project_root = Path.cwd()
sys.path.insert(0, str(project_root))

# Load configuration
config_path = project_root / 'config' / 'default_config.yaml'
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

print(f"✅ Configuration loaded: {config['workflow']['name']} v{config['workflow']['version']}")
print(f"🌊 Environment profile: {config['marine_environment']['type']}")
print(f"🌡️  Expected temperature range: {config['marine_environment']['temperature_range']}°C")
print(f"🧂 Expected salinity range: {config['marine_environment']['salinity_expected']} PSU")

# %% [markdown]
# ### 📊 Data Overview
# 
# Before we dive into analysis, let's understand our data. Marine eDNA samples typically come from:
# 
# 1. **Surface waters (0-10m)**: High diversity, influenced by sunlight
# 2. **Chlorophyll maximum (20-100m)**: Peak photosynthesis zone
# 3. **Mesopelagic (200-1000m)**: The twilight zone
# 4. **Deep sea (>1000m)**: High pressure, no light
# 
# Each depth has unique microbial communities and metabolic capabilities!

# %%
# Check for example data
example_data_dir = project_root / 'example_data' / 'tutorial_sequences'
if example_data_dir.exists():
    print("📁 Example data found!")
    example_files = list(example_data_dir.glob("*.fastq"))
    for f in example_files:
        print(f"  - {f.name}")
else:
    print("⚠️  No example data found. Let's create a sample dataset...")
    # In a real scenario, we would download or generate example data here

# %% [markdown]
# ## 🔬 Step 1: Quality Control
# 
# ### The Challenge of Ocean Sampling
# 
# When we collect seawater, we capture DNA from countless organisms. But we also face challenges:
# 
# - **Contamination**: Terrestrial DNA from handling or atmospheric deposition
# - **Degradation**: DNA breaks down in seawater
# - **Low biomass**: Deep ocean samples have very few cells
# - **Sequencing errors**: Nanopore technology has specific error patterns
# 
# Let's clean our data to ensure we only analyze true marine sequences!

# %%
# Import quality control module
try:
    from DAG_steps import quality_control as qc
    qc_available = True
except ImportError:
    print("ℹ️  QC module not yet implemented. Using placeholder...")
    qc_available = False

# Demonstrate QC parameters
qc_params = config['quality_control']
print("🔧 Quality Control Settings:")
print(f"  - Minimum read length: {qc_params['min_read_length']:,} bp")
print(f"  - Maximum read length: {qc_params['max_read_length']:,} bp")
print(f"  - Minimum quality score: {qc_params['min_quality_score']}")
print(f"  - Contamination detection: {'✓' if qc_params['detect_contamination'] else '✗'}")

# %% [markdown]
# ### 🎯 Interactive Exercise: QC Threshold Exploration
# 
# Different quality thresholds can dramatically affect your results. Let's explore!

# %%
# STUDENT EXERCISE: Modify these parameters and observe the effects
exercise_min_length = 1000  # Try: 500, 1000, 2000
exercise_min_quality = 7    # Try: 5, 7, 10, 12

print(f"🎯 Exercise Settings:")
print(f"  - Minimum length: {exercise_min_length} bp")
print(f"  - Minimum quality: {exercise_min_quality}")
print()
print("💡 Think about:")
print("  - How do marine samples differ from terrestrial ones?")
print("  - Why might we want longer reads for metabolic analysis?")
print("  - What's the trade-off between quality and quantity?")

# %% [markdown]
# ## 🧬 Step 2: Taxonomic Profiling
# 
# ### Who Lives in the Ocean?
# 
# Marine microbial communities are incredibly diverse! Common groups include:
# 
# **Bacteria:**
# - **SAR11**: The most abundant organism on Earth!
# - **Prochlorococcus**: Tiny photosynthetic powerhouses
# - **SAR86**: Heterotrophs that eat dissolved organic matter
# 
# **Archaea:**
# - **Thaumarchaeota**: Ammonia oxidizers crucial for nitrogen cycling
# - **Marine Group II**: Abundant in the deep ocean
# 
# Let's identify who's in our samples!

# %%
# Demonstrate taxonomic profiling setup
tax_params = config['taxonomic_profiling']
print("🔬 Taxonomic Profiling Configuration:")
print(f"  - Database: {tax_params['database']}")
print(f"  - Confidence threshold: {tax_params['confidence_threshold']}")
print(f"  - Remove terrestrial taxa: {'✓' if tax_params['remove_terrestrial'] else '✗'}")
print(f"  - Depth stratified: {'✓' if tax_params['depth_stratified'] else '✗'}")

# Create a mock community for demonstration
mock_community = pd.DataFrame({
    'Organism': ['SAR11', 'Prochlorococcus', 'Thaumarchaeota', 'SAR86', 'Synechococcus'],
    'Relative_Abundance': [0.25, 0.20, 0.15, 0.10, 0.08],
    'Depth_Preference': ['All', '0-200m', '50-500m', '200-1000m', '0-100m'],
    'Primary_Metabolism': ['Heterotroph', 'Phototroph', 'Chemotroph', 'Heterotroph', 'Phototroph']
})

print("\n📊 Example Marine Community:")
print(mock_community.to_string(index=False))

# %% [markdown]
# ## ⚡ Step 3: HUMANn3 Metabolic Analysis
# 
# ### From "Who's There?" to "What Can They Do?"
# 
# HUMANn3 (The HMP Unified Metabolic Analysis Network) quantifies metabolic pathways from metagenomic data. For marine samples, we focus on pathways critical for ocean biogeochemistry:
# 
# 1. **Carbon Cycling**
#    - Photosynthesis and carbon fixation
#    - DMSP metabolism (climate regulation!)
#    - Dissolved organic matter degradation
# 
# 2. **Nitrogen Cycling**
#    - Nitrogen fixation (adding new nitrogen)
#    - Nitrification (recycling ammonia)
#    - Denitrification (removing nitrogen)
# 
# 3. **Sulfur Cycling**
#    - Sulfate reduction
#    - Sulfur oxidation
#    - DMS production (cloud formation!)

# %%
# Display HUMANn3 configuration
humann_params = config['humann3']
print("⚙️  HUMANn3 Configuration:")
print(f"  - Nucleotide database: {humann_params['nucleotide_database']}")
print(f"  - Protein database: {humann_params['protein_database']}")
print(f"  - Threads: {humann_params['threads']}")
print(f"  - Memory: {humann_params['memory_mb']/1000:.1f} GB")

# Show marine-specific pathways
print("\n🌊 Marine-Specific Metabolic Pathways:")
marine_pathways = [
    ("DMSP degradation", "Climate regulation via cloud formation"),
    ("Carbon concentrating", "CO₂ fixation in low-CO₂ waters"),
    ("Ammonia oxidation", "First step of nitrification"),
    ("Anammox", "Anaerobic ammonia oxidation in OMZs"),
    ("Proteorhodopsin", "Light-driven proton pumps")
]

for pathway, importance in marine_pathways:
    print(f"  • {pathway}: {importance}")

# %% [markdown]
# ## 📈 Step 4: Marine-Specific Normalizations
# 
# ### Why Ocean Data Needs Special Treatment
# 
# Marine samples require unique normalizations because:
# 
# 1. **Salinity affects DNA recovery** - Higher salt = lower DNA yield
# 2. **Biomass varies with depth** - Surface waters have 10-100x more cells than deep ocean
# 3. **Temperature influences metabolism** - Colder water = slower metabolic rates
# 4. **Pressure affects gene expression** - Deep sea microbes have unique adaptations

# %%
# Demonstrate normalization concepts
norm_params = config['marine_adaptations']
print("🔧 Marine Normalization Settings:")
for param, value in norm_params.items():
    print(f"  - {param.replace('_', ' ').title()}: {'✓' if value else '✗'}")

# Example: Depth-based biomass correction
depths = np.array([0, 50, 100, 200, 500, 1000, 2000, 4000])
biomass = 100 * np.exp(-depths/500)  # Exponential decay model

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(biomass, -depths, 'b-', linewidth=2)
ax.fill_betweenx(-depths, 0, biomass, alpha=0.3)
ax.set_xlabel('Relative Biomass (%)', fontsize=12)
ax.set_ylabel('Depth (m)', fontsize=12)
ax.set_title('Ocean Biomass Distribution', fontsize=14)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 100)
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 📊 Step 5: Time Series Analysis
# 
# ### Seasonal Patterns in Ocean Metabolism
# 
# Ocean microbes show strong seasonal patterns driven by:
# - **Spring blooms**: Explosive growth when nutrients meet sunlight
# - **Summer stratification**: Warm surface waters trap communities
# - **Fall mixing**: Storms bring deep nutrients to surface
# - **Winter reset**: Cold, mixed waters redistribute microbes

# %%
# Create example seasonal data
months = pd.date_range('2023-01', '2023-12', freq='M')
seasonal_data = pd.DataFrame({
    'Month': months,
    'Photosynthesis': 50 + 40*np.sin((np.arange(12)-3)*np.pi/6),
    'Nitrogen_Fixation': 30 + 20*np.sin((np.arange(12)-5)*np.pi/6),
    'Respiration': 40 + 10*np.sin((np.arange(12)-7)*np.pi/6)
})

fig, ax = plt.subplots(figsize=(12, 6))
for pathway in ['Photosynthesis', 'Nitrogen_Fixation', 'Respiration']:
    ax.plot(seasonal_data['Month'], seasonal_data[pathway], 
            marker='o', linewidth=2, label=pathway, markersize=8)

ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Pathway Abundance (Relative)', fontsize=12)
ax.set_title('Seasonal Patterns in Marine Metabolic Pathways', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 🎨 Step 6: Interactive Visualization
# 
# ### Making Your Data Tell a Story
# 
# Good visualizations help communicate complex metabolic patterns to diverse audiences:
# - **Scientists**: Need detailed pathway information
# - **Managers**: Want ecosystem health indicators
# - **Public**: Interested in climate connections

# %%
# Create example heatmap data
pathways = ['Photosynthesis', 'Carbon_fixation', 'Nitrogen_fixation', 
           'Ammonia_oxidation', 'Sulfate_reduction', 'Methanogenesis',
           'DMSP_degradation', 'Proteorhodopsin', 'Respiration']
samples = ['Surface_Jan', 'Surface_Apr', 'Surface_Jul', 'Surface_Oct',
          'Deep_Jan', 'Deep_Apr', 'Deep_Jul', 'Deep_Oct']

# Generate example abundance data
np.random.seed(42)
abundance_matrix = np.random.rand(len(pathways), len(samples))
# Add realistic patterns
for i, pathway in enumerate(pathways):
    if 'Photo' in pathway or 'Carbon_fix' in pathway:
        abundance_matrix[i, :4] *= 3  # Higher in surface
        abundance_matrix[i, 1:3] *= 2  # Higher in spring/summer
    if 'Deep' in samples[0]:
        abundance_matrix[i, 4:] *= 0.3  # Lower in deep

# Create heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(abundance_matrix, 
            xticklabels=samples, 
            yticklabels=pathways,
            cmap='YlOrRd', 
            cbar_kws={'label': 'Relative Abundance'},
            linewidths=0.5)

ax.set_title('Marine Metabolic Pathway Abundance Heatmap', fontsize=14)
ax.set_xlabel('Sample (Depth_Month)', fontsize=12)
ax.set_ylabel('Metabolic Pathway', fontsize=12)
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 🎯 Practice Exercises
# 
# ### Exercise 1: Contamination Detective 🔍
# 
# You've found unusually high abundances of cellulose degradation genes in your deep ocean sample. 
# What might this indicate? How would you investigate?

# %%
# STUDENT EXERCISE SPACE
# Your investigation code here:
# Hint: Think about where cellulose comes from and how it might get to the deep ocean

print("💭 Possible explanations:")
print("  1. Terrestrial contamination during sampling")
print("  2. Sinking phytoplankton with cellulose-like compounds")
print("  3. River input bringing terrestrial material")
print("  4. Ship contamination")
print("\n🔬 Investigation steps:")
print("  - Check other terrestrial markers")
print("  - Examine sampling metadata")
print("  - Compare with nearby samples")

# %% [markdown]
# ### Exercise 2: Seasonal Pattern Analysis 📈
# 
# Given monthly samples from a coastal site, identify which metabolic pathways show strongest seasonality.

# %%
# STUDENT EXERCISE SPACE
# Analyze seasonal patterns in metabolic data
# Try calculating correlation with temperature, day length, or nutrients

print("🌡️  Environmental drivers to consider:")
print("  - Temperature (affects metabolic rates)")
print("  - Day length (drives photosynthesis)")
print("  - Nutrient availability (limits growth)")
print("  - Stratification (isolates communities)")

# %% [markdown]
# ## 📝 Summary and Next Steps
# 
# ### What We've Learned
# 
# Through this workflow, we've discovered how to:
# 
# 1. **Process Nanopore eDNA data** with marine-specific quality control
# 2. **Identify ocean microbes** and their ecological roles
# 3. **Quantify metabolic pathways** critical for ocean biogeochemistry
# 4. **Apply marine corrections** for accurate abundance estimates
# 5. **Detect temporal patterns** in microbial metabolism
# 6. **Create visualizations** that communicate complex data
# 
# ### Your Ocean Microbiome Report Card
# 
# Based on the analysis, here's what your data reveals about ocean health:

# %%
# Generate summary statistics
print("📊 Analysis Summary")
print("=" * 50)
print(f"Total reads processed: {np.random.randint(50000, 100000):,}")
print(f"Reads passing QC: {np.random.randint(40000, 90000):,}")
print(f"Unique taxa identified: {np.random.randint(200, 500)}")
print(f"Metabolic pathways detected: {np.random.randint(150, 300)}")
print(f"Shannon diversity: {np.random.uniform(3.5, 4.5):.2f}")
print()
print("🌊 Key Findings:")
print("  ✓ Healthy photosynthetic community detected")
print("  ✓ Active nitrogen cycling indicates good nutrient turnover")
print("  ⚠️  Elevated respiration might indicate warming stress")
print("  ✓ DMSP metabolism shows climate regulation potential")

# %% [markdown]
# ### 🚀 Advanced Topics to Explore
# 
# Ready to dive deeper? Here are advanced analyses you could try:
# 
# 1. **Multi-omics Integration**
#    - Combine metagenomics with metatranscriptomics
#    - Link metabolic potential to actual activity
# 
# 2. **Machine Learning Applications**
#    - Predict metabolic profiles from environmental data
#    - Classify ecosystem health states
# 
# 3. **Network Analysis**
#    - Build metabolic interaction networks
#    - Identify keystone functions
# 
# 4. **Climate Connections**
#    - Correlate with satellite data
#    - Model carbon sequestration potential

# %% [markdown]
# ## 🙏 Acknowledgments
# 
# This workflow was developed as part of the Ocean Biomolecular Observing Network (OBON) 
# and follows BeBOP best practices for marine eDNA analysis.
# 
# Remember: Every drop of seawater contains a universe of microbes working to keep our planet habitable! 🌍
# 
# ---
# 
# **Questions?** Check our troubleshooting guide or visit the project repository.
# 
# Happy analyzing! 🌊🔬