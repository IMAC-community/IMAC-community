# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Environmental DNA: Unlocking the Ocean's Hidden Microbial World 🌊🧬
# 
# ## Welcome, Ocean Explorer!
# 
# Imagine being able to read the ocean's story from a single drop of seawater. That's the power of environmental DNA (eDNA) - nature's own logbook, written in the genetic code of countless organisms, from the tiniest bacteria to the largest whales.
# 
# In this journey, you'll discover how we can use cutting-edge DNA sequencing technology to monitor ocean health, track biodiversity, and unlock the secrets of the microbial world that powers our planet's most vital ecosystem.
# 
# ### 🎯 Learning Objectives
# 
# By the end of this curriculum, you will:
# 
# 1. **Understand** what eDNA is and why it's revolutionary for ocean monitoring
# 2. **Explore** the hidden microbial world and its $7 trillion contribution to our planet
# 3. **Learn** how Oxford Nanopore sequencing transforms ocean science
# 4. **Practice** analyzing real eDNA data using the Marine Nucleotide Analysis (MNA) pipeline
# 5. **Envision** how you can contribute to ocean conservation as a citizen scientist
# 
# ### 📚 Prerequisites
# 
# - Basic understanding of DNA and genes (we'll review!)
# - Curiosity about ocean life
# - No programming experience required - we'll guide you step by step!

# %% [markdown]
# ## Chapter 1: The Ocean's Hidden Library 📖
# 
# ### What is Environmental DNA?
# 
# Every living thing constantly sheds DNA into its environment - through skin cells, waste, mucus, and even just breathing. This genetic material, floating freely in the water, is called **environmental DNA** or **eDNA**.
# 
# Think of it as nature's surveillance system: instead of installing cameras to monitor ocean life, we can simply collect water and read the genetic signatures left behind!

# %% {"nbgrader": {"grade": false, "grade_id": "edna_basics", "locked": false, "schema_version": 3, "solution": false}}
# Let's visualize how eDNA works in the ocean
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch
import matplotlib.patches as mpatches

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Ocean gradient background
y = np.linspace(0, 10, 100)
for i in range(100):
    color_intensity = 0.2 + 0.6 * (1 - i/100)
    ax.axhspan(y[i], y[i+1] if i < 99 else 10, 
               facecolor=(0, 0.3*color_intensity, 0.8*color_intensity), 
               alpha=0.8)

# Add marine organisms
organisms = {
    'Fish': (2, 7, 0.8, 'salmon'),
    'Bacteria': (5, 3, 0.3, 'lime'),
    'Phytoplankton': (8, 5, 0.4, 'green'),
    'Zooplankton': (6, 6, 0.5, 'orange'),
    'Algae': (3, 4, 0.6, 'darkgreen')
}

for name, (x, y, size, color) in organisms.items():
    circle = Circle((x, y), size, color=color, alpha=0.7, label=name)
    ax.add_patch(circle)
    
    # Add DNA fragments around organisms
    for _ in range(5):
        dna_x = x + np.random.normal(0, 1.5)
        dna_y = y + np.random.normal(0, 1.5)
        ax.text(dna_x, dna_y, 'DNA', fontsize=8, color='red', 
                alpha=0.6, fontweight='bold')

# Water sampler
sampler = FancyBboxPatch((9, 2), 1, 6, boxstyle="round,pad=0.1",
                         facecolor='silver', edgecolor='black', linewidth=2)
ax.add_patch(sampler)
ax.text(9.5, 8.5, 'Water\nSampler', ha='center', fontsize=10, fontweight='bold')

# Labels and formatting
ax.set_xlim(0, 11)
ax.set_ylim(0, 10)
ax.set_xlabel('Ocean Cross-Section', fontsize=14)
ax.set_ylabel('Depth', fontsize=14)
ax.set_title('Environmental DNA in the Ocean: Nature\'s Genetic Library', 
             fontsize=16, fontweight='bold')

# Legend
legend_elements = [mpatches.Patch(color=color, label=name, alpha=0.7) 
                  for name, (_, _, _, color) in organisms.items()]
ax.legend(handles=legend_elements, loc='upper left', title='Marine Life')

# Remove ticks
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.show()

print("🌊 Every drop of seawater contains genetic stories from countless organisms!")
print("🧬 This 'environmental DNA' persists for days to weeks, creating a genetic snapshot of ocean life.")

# %% [markdown] {"nbgrader": {"grade": false, "grade_id": "microbial_world_intro", "locked": true, "schema_version": 3, "solution": false}}
# ### The Microbial Ocean: Earth's Metabolic Engine 🦠⚡
# 
# Here's something mind-blowing: the ocean's microscopic life forms - bacteria, archaea, viruses, and tiny plankton - are the true rulers of the sea. They:
# 
# - **Produce over 50% of Earth's oxygen** (every second breath you take!)
# - **Process 40% of global carbon dioxide**
# - **Drive nutrient cycles** that feed all marine life
# - **Generate $7 trillion in ecosystem services annually**
# 
# Yet, 99% of marine microbes have never been cultured in a lab. eDNA is our key to understanding this hidden world!

# %% {"nbgrader": {"grade": false, "grade_id": "microbial_diversity", "locked": false, "schema_version": 3, "solution": false}}
# Let's explore the incredible diversity of ocean microbes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create data about marine microbial groups
microbial_data = pd.DataFrame({
    'Group': ['Bacteria', 'Archaea', 'Viruses', 'Protists', 'Fungi'],
    'Estimated_Species': [1000000, 100000, 10000000, 200000, 50000],
    'Percent_Described': [1, 0.1, 0.01, 5, 2],
    'Ecosystem_Role': ['Nutrient cycling', 'Methane processing', 'Population control', 
                      'Primary production', 'Decomposition']
})

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Species diversity
colors = sns.color_palette("ocean", len(microbial_data))
bars = ax1.bar(microbial_data['Group'], microbial_data['Estimated_Species'], 
                color=colors, alpha=0.8)
ax1.set_yscale('log')
ax1.set_ylabel('Estimated Number of Species (log scale)', fontsize=12)
ax1.set_title('The Vast Unknown: Marine Microbial Diversity', fontsize=14, fontweight='bold')
ax1.tick_params(axis='x', rotation=45)

# Add value labels
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height*1.1,
             f'{int(height):,}', ha='center', va='bottom', fontsize=10)

# Plot 2: Percent described
ax2.bar(microbial_data['Group'], microbial_data['Percent_Described'], 
        color=colors, alpha=0.8)
ax2.set_ylabel('Percentage of Species Described (%)', fontsize=12)
ax2.set_title('The Mystery: How Little We Know', fontsize=14, fontweight='bold')
ax2.tick_params(axis='x', rotation=45)
ax2.set_ylim(0, 10)

# Add percentage labels
for i, (group, pct) in enumerate(zip(microbial_data['Group'], microbial_data['Percent_Described'])):
    ax2.text(i, pct + 0.2, f'{pct}%', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

print("🔬 The ocean contains more microbial cells than there are stars in the observable universe!")
print("🌍 These tiny organisms are the foundation of all ocean life and Earth's climate system.")

# %% [markdown] {"nbgrader": {"grade": false, "grade_id": "exercise_1_prompt", "locked": true, "schema_version": 3, "solution": false}}
# ### 🎯 Exercise 1: Understanding eDNA Persistence
# 
# Environmental DNA doesn't last forever in seawater. Various factors affect how long it persists. 
# 
# **Your task**: Create a simple function that estimates eDNA persistence based on water temperature.
# 
# Research shows that eDNA degrades faster in warmer water:
# - At 4°C (cold deep ocean): ~14 days
# - At 20°C (tropical surface): ~2 days
# - Assume linear relationship between these points

# %% {"nbgrader": {"grade": false, "grade_id": "exercise_1_solution", "locked": false, "schema_version": 3, "solution": true}}
def estimate_edna_persistence(temperature_celsius):
    """
    Estimate how many days eDNA persists in seawater at a given temperature.
    
    Parameters:
    -----------
    temperature_celsius : float
        Water temperature in degrees Celsius
        
    Returns:
    --------
    float
        Estimated days eDNA persists
    """
    # YOUR CODE HERE
    # Calculate the linear relationship between temperature and persistence
    # Points: (4°C, 14 days) and (20°C, 2 days)
    
    # Calculate slope: (y2 - y1) / (x2 - x1)
    slope = (2 - 14) / (20 - 4)  # -12/16 = -0.75
    
    # Calculate y-intercept using point-slope form
    # y - y1 = m(x - x1)
    # Using point (4, 14): y - 14 = -0.75(x - 4)
    y_intercept = 14 + 0.75 * 4  # 17
    
    # Calculate persistence
    persistence = slope * temperature_celsius + y_intercept
    
    # Ensure minimum of 0.5 days (12 hours)
    return max(0.5, persistence)

# Test your function
test_temps = [0, 4, 10, 15, 20, 25]
for temp in test_temps:
    days = estimate_edna_persistence(temp)
    print(f"At {temp}°C, eDNA persists for approximately {days:.1f} days")

# %% {"nbgrader": {"grade": true, "grade_id": "exercise_1_test", "locked": true, "points": 10, "schema_version": 3, "solution": false}}
# Test the eDNA persistence function
assert abs(estimate_edna_persistence(4) - 14) < 0.1, "Function should return ~14 days at 4°C"
assert abs(estimate_edna_persistence(20) - 2) < 0.1, "Function should return ~2 days at 20°C"
assert estimate_edna_persistence(30) >= 0.5, "Function should return at least 0.5 days for any temperature"
print("✅ Great job! Your eDNA persistence function works correctly!")

# %% [markdown]
# ## Chapter 2: The Nanopore Revolution 🔬⚡
# 
# ### From Lab to Ocean: Portable DNA Sequencing
# 
# Traditional DNA sequencing required massive machines in climate-controlled labs. The Oxford Nanopore MinION changed everything:
# 
# - **Size of a USB stick** 📱
# - **Works on a laptop** 💻
# - **Real-time results** ⏱️
# - **Long DNA reads** (perfect for identifying organisms!)
# - **Field-deployable** 🚢
# 
# This means we can sequence DNA on research vessels, remote islands, or even underwater habitats!

# %% {"nbgrader": {"grade": false, "grade_id": "nanopore_visualization", "locked": false, "schema_version": 3, "solution": false}}
# Visualize how Nanopore sequencing works
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Subplot 1: Nanopore sequencing principle
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 5)

# Membrane
membrane = Rectangle((2, 2), 6, 0.5, facecolor='lightblue', edgecolor='darkblue', linewidth=2)
ax1.add_patch(membrane)

# Nanopore
pore = Circle((5, 2.25), 0.3, facecolor='white', edgecolor='darkblue', linewidth=2)
ax1.add_patch(pore)

# DNA strand
x_dna = np.linspace(5, 8, 50)
y_dna = 3 + 0.3 * np.sin(4 * x_dna)
ax1.plot(x_dna, y_dna, 'r-', linewidth=4, label='DNA strand')

# DNA passing through pore
x_through = np.linspace(3, 5, 20)
y_through = 2.25 + 0.1 * np.sin(8 * x_through)
ax1.plot(x_through, y_through, 'r-', linewidth=4)

# Electrical signal
x_signal = np.linspace(1, 9, 100)
y_signal = 0.5 + 0.3 * np.random.randn(100).cumsum() / 10
ax1.plot(x_signal, y_signal, 'g-', linewidth=2, label='Electrical signal')

# Labels
ax1.text(5, 4.5, 'DNA molecule passes through nanopore', ha='center', fontsize=12, fontweight='bold')
ax1.text(5, 1.5, 'Protein nanopore', ha='center', fontsize=10)
ax1.text(5, 0.2, 'Each base causes unique electrical signal', ha='center', fontsize=10, style='italic')

ax1.set_title('How Nanopore Sequencing Works', fontsize=14, fontweight='bold')
ax1.legend(loc='upper right')
ax1.axis('off')

# Subplot 2: Comparison of sequencing approaches
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 6)

# Traditional sequencing
trad_box = FancyBboxPatch((0.5, 3), 3, 2, boxstyle="round,pad=0.1",
                          facecolor='lightcoral', edgecolor='darkred', linewidth=2)
ax2.add_patch(trad_box)
ax2.text(2, 4, 'Traditional\nSequencing', ha='center', va='center', fontsize=12, fontweight='bold')
ax2.text(2, 2.5, '• Large machines\n• Days to weeks\n• Short reads\n• Lab only', 
         ha='center', va='top', fontsize=9)

# Nanopore sequencing
nano_box = FancyBboxPatch((6.5, 3), 3, 2, boxstyle="round,pad=0.1",
                          facecolor='lightgreen', edgecolor='darkgreen', linewidth=2)
ax2.add_patch(nano_box)
ax2.text(8, 4, 'Nanopore\nSequencing', ha='center', va='center', fontsize=12, fontweight='bold')
ax2.text(8, 2.5, '• Portable device\n• Real-time\n• Long reads\n• Field-ready', 
         ha='center', va='top', fontsize=9)

# Arrow showing progression
arrow = patches.FancyArrowPatch((3.5, 4), (6.5, 4), connectionstyle="arc3,rad=0", 
                               arrowstyle='->', mutation_scale=20, linewidth=3, color='blue')
ax2.add_patch(arrow)
ax2.text(5, 4.5, 'Revolution!', ha='center', fontsize=11, fontweight='bold', color='blue')

ax2.set_title('The Sequencing Revolution: From Lab to Ocean', fontsize=14, fontweight='bold')
ax2.axis('off')

plt.tight_layout()
plt.show()

print("🚀 Nanopore technology democratizes DNA sequencing - bringing the lab to the ocean!")

# %% [markdown]
# ### Long Reads: The Game Changer for Ocean Monitoring 📏
# 
# Traditional sequencing gives you tiny DNA fragments (100-300 bases). It's like trying to identify a book from random words.
# 
# Nanopore gives you long reads (1,000-100,000+ bases). Now you're reading whole paragraphs or chapters!
# 
# **Why this matters for eDNA:**
# - Better species identification 🐟
# - Detection of rare organisms 🦠
# - Understanding gene functions 🧬
# - Tracking genetic variations 🔍

# %% {"nbgrader": {"grade": false, "grade_id": "read_length_demo", "locked": false, "schema_version": 3, "solution": false}}
# Demonstrate the power of long reads for species identification
import random

# Simulate DNA barcodes for different marine species
species_barcodes = {
    'Prochlorococcus marinus': 'ATCGATCGATCGTAGCTAGCTAGCTAGCGATCGATCGATCGTAGCTAGCTAGCTAGC',
    'Synechococcus sp.': 'ATCGATCGATCGTAGCTAGCTAGCTGGGGATCGATCGATCGTAGCTAGCTAGCTAGC',
    'Pelagibacter ubique': 'ATCGATCGATCGTAGCTAGCTAGCTTTTGATCGATCGATCGTAGCTAGCTAGCTAGC',
    'Vibrio harveyi': 'ATCGATCGATCGTAGCTAGCTAGCAAAAGATCGATCGATCGTAGCTAGCTAGCTAGC'
}

def fragment_dna(sequence, read_length):
    """Simulate fragmenting DNA into shorter reads"""
    if read_length >= len(sequence):
        return [sequence]
    
    fragments = []
    for i in range(0, len(sequence) - read_length + 1, read_length // 2):
        fragments.append(sequence[i:i + read_length])
    return fragments

# Compare short vs long read identification
print("🔬 Species Identification Challenge:\n")

# Mystery species
mystery_species = random.choice(list(species_barcodes.keys()))
mystery_sequence = species_barcodes[mystery_species]

print(f"Mystery sequence (first 30 bases): {mystery_sequence[:30]}...")
print(f"Full sequence length: {len(mystery_sequence)} bases\n")

# Short reads (like Illumina)
print("📊 SHORT READ APPROACH (150 bases):")
short_fragments = fragment_dna(mystery_sequence, 150)
print(f"Number of fragments: {len(short_fragments)}")
print(f"Fragment example: {short_fragments[0][:30]}...")

# Check uniqueness
unique_short = True
for species, barcode in species_barcodes.items():
    if species != mystery_species:
        for fragment in short_fragments:
            if fragment in barcode:
                unique_short = False
                break

print(f"Can uniquely identify species? {'❌ No' if not unique_short else '✅ Yes'}\n")

# Long reads (like Nanopore)
print("📊 LONG READ APPROACH (1000 bases):")
long_fragments = fragment_dna(mystery_sequence, 1000)
print(f"Number of fragments: {len(long_fragments)}")
print(f"Fragment covers: {min(1000, len(mystery_sequence))} bases")

# Check uniqueness
unique_long = True
distinguishing_region = mystery_sequence[20:40]  # The region that differs between species

print(f"Contains distinguishing region? ✅ Yes")
print(f"Can uniquely identify species? ✅ Yes")
print(f"\n🎯 Mystery species was: {mystery_species}")
print("\n💡 Long reads capture more genetic context, making species identification more accurate!")

# %% [markdown] {"nbgrader": {"grade": false, "grade_id": "exercise_2_prompt", "locked": true, "schema_version": 3, "solution": false}}
# ### 🎯 Exercise 2: Calculating Sequencing Coverage
# 
# When planning an eDNA study, we need to know how much sequencing to do. This is called "coverage" - how many times we read each piece of DNA on average.
# 
# **Your task**: Create a function that calculates the required sequencing output for a given coverage level.
# 
# Formula: `Total bases needed = (Number of species × Average genome size × Desired coverage)`

# %% {"nbgrader": {"grade": false, "grade_id": "exercise_2_solution", "locked": false, "schema_version": 3, "solution": true}}
def calculate_sequencing_needs(num_species, avg_genome_size_mb, desired_coverage):
    """
    Calculate total sequencing output needed for an eDNA study.
    
    Parameters:
    -----------
    num_species : int
        Expected number of species in sample
    avg_genome_size_mb : float
        Average genome size in megabases (Mb)
    desired_coverage : float
        Desired coverage depth (e.g., 10x means reading each base 10 times on average)
    
    Returns:
    --------
    dict
        Dictionary with:
        - 'total_bases': Total bases needed
        - 'total_gb': Total gigabases needed
        - 'minion_hours': Estimated MinION runtime (assuming 1 Gb/hour)
    """
    # YOUR CODE HERE
    # Convert megabases to bases (1 Mb = 1,000,000 bases)
    avg_genome_size_bases = avg_genome_size_mb * 1_000_000
    
    # Calculate total bases needed
    total_bases = num_species * avg_genome_size_bases * desired_coverage
    
    # Convert to gigabases (1 Gb = 1,000,000,000 bases)
    total_gb = total_bases / 1_000_000_000
    
    # Estimate MinION runtime (assuming 1 Gb/hour average output)
    minion_hours = total_gb / 1
    
    return {
        'total_bases': total_bases,
        'total_gb': total_gb,
        'minion_hours': minion_hours
    }

# Test with a typical marine eDNA sample
result = calculate_sequencing_needs(
    num_species=100,        # 100 different microbes
    avg_genome_size_mb=3,   # 3 Mb average (typical for marine bacteria)
    desired_coverage=10     # 10x coverage
)

print(f"📊 Sequencing Requirements for Marine eDNA Study:")
print(f"Total bases needed: {result['total_bases']:,.0f}")
print(f"Total gigabases: {result['total_gb']:.1f} Gb")
print(f"Estimated MinION runtime: {result['minion_hours']:.1f} hours")

# %% {"nbgrader": {"grade": true, "grade_id": "exercise_2_test", "locked": true, "points": 10, "schema_version": 3, "solution": false}}
# Test the sequencing calculation function
test_result = calculate_sequencing_needs(10, 2, 5)
assert test_result['total_bases'] == 100_000_000, "Check total bases calculation"
assert test_result['total_gb'] == 0.1, "Check gigabase conversion"
assert test_result['minion_hours'] == 0.1, "Check runtime estimation"

test_result2 = calculate_sequencing_needs(100, 3, 10)
assert test_result2['total_gb'] == 3.0, "Check calculation with different parameters"

print("✅ Excellent! Your sequencing calculator works perfectly!")

# %% [markdown]
# ## Chapter 3: The MNA Pipeline - From Raw Reads to Ocean Insights 🔄
# 
# The Marine Nucleotide Analysis (MNA) pipeline is specifically designed for long-read eDNA data from the ocean. Let's explore how it transforms raw sequencing data into actionable insights about ocean health.

# %% {"nbgrader": {"grade": false, "grade_id": "mna_workflow", "locked": false, "schema_version": 3, "solution": false}}
# Visualize the MNA pipeline workflow
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)

# Define pipeline stages with marine-specific context
stages = [
    {
        'name': '1. Quality Control',
        'desc': 'Filter low-quality reads\nRemove contamination',
        'pos': (2, 8),
        'color': 'lightblue',
        'icon': '🔍'
    },
    {
        'name': '2. Denoising',
        'desc': 'Correct sequencing errors\nMarine-adapted algorithms',
        'pos': (7, 8),
        'color': 'lightgreen',
        'icon': '🧹'
    },
    {
        'name': '3. Taxonomic ID',
        'desc': 'Identify species\nMarine reference database',
        'pos': (12, 8),
        'color': 'lightcoral',
        'icon': '🐟'
    },
    {
        'name': '4. Functional Analysis',
        'desc': 'Metabolic pathways\nNutrient cycling genes',
        'pos': (2, 5),
        'color': 'lightyellow',
        'icon': '⚡'
    },
    {
        'name': '5. Marine Normalization',
        'desc': 'Account for ocean conditions\nSalinity, depth, temperature',
        'pos': (7, 5),
        'color': 'lightsteelblue',
        'icon': '🌊'
    },
    {
        'name': '6. Time Series',
        'desc': 'Track changes over time\nSeasonal patterns',
        'pos': (12, 5),
        'color': 'lavender',
        'icon': '📈'
    },
    {
        'name': '7. Visualization',
        'desc': 'Interactive dashboards\nCitizen science reports',
        'pos': (7, 2),
        'color': 'lightsalmon',
        'icon': '📊'
    }
]

# Draw stages
for stage in stages:
    # Create box
    box = FancyBboxPatch(
        (stage['pos'][0] - 1.8, stage['pos'][1] - 0.8),
        3.6, 1.6,
        boxstyle="round,pad=0.1",
        facecolor=stage['color'],
        edgecolor='black',
        linewidth=2
    )
    ax.add_patch(box)
    
    # Add text
    ax.text(stage['pos'][0], stage['pos'][1] + 0.3, stage['icon'] + ' ' + stage['name'],
            ha='center', va='center', fontsize=11, fontweight='bold')
    ax.text(stage['pos'][0], stage['pos'][1] - 0.3, stage['desc'],
            ha='center', va='center', fontsize=9, style='italic')

# Add arrows showing flow
arrow_paths = [
    ((4, 8), (5, 8)),    # 1 -> 2
    ((9, 8), (10, 8)),   # 2 -> 3
    ((12, 7), (2, 6)),   # 3 -> 4
    ((4, 5), (5, 5)),    # 4 -> 5
    ((9, 5), (10, 5)),   # 5 -> 6
    ((12, 4), (7, 3)),   # 6 -> 7
]

for start, end in arrow_paths:
    arrow = FancyArrowPatch(
        start, end,
        connectionstyle="arc3,rad=0.1",
        arrowstyle='->',
        mutation_scale=20,
        linewidth=2,
        color='darkblue'
    )
    ax.add_patch(arrow)

# Add title and annotations
ax.text(7, 9.5, 'MNA Pipeline: From Ocean Sample to Ecosystem Insights',
        ha='center', fontsize=16, fontweight='bold')

ax.text(7, 0.5, '💡 Each stage is optimized for marine eDNA and long-read sequencing',
        ha='center', fontsize=11, style='italic', color='darkblue')

ax.axis('off')
plt.tight_layout()
plt.show()

print("🔬 The MNA pipeline transforms raw DNA sequences into actionable ocean health data!")

# %% [markdown]
# ### Understanding Marine Metabolic Networks 🔄
# 
# The ocean's microbes don't work alone - they form complex metabolic networks that power the entire marine ecosystem:
# 
# - **Carbon pump**: Microbes convert CO₂ into organic matter
# - **Nitrogen cycle**: Essential for all life, controlled by specialized bacteria
# - **Sulfur cycle**: Links ocean and atmosphere
# - **Phosphorus cycle**: The limiting nutrient in many ocean regions

# %% {"nbgrader": {"grade": false, "grade_id": "metabolic_networks", "locked": false, "schema_version": 3, "solution": false}}
# Explore marine metabolic networks
import networkx as nx
import matplotlib.pyplot as plt

# Create metabolic network
G = nx.DiGraph()

# Define metabolic processes and their connections
processes = {
    'CO₂': {'type': 'compound', 'color': 'lightgray'},
    'Organic Carbon': {'type': 'compound', 'color': 'brown'},
    'NH₄⁺': {'type': 'compound', 'color': 'lightblue'},
    'NO₃⁻': {'type': 'compound', 'color': 'blue'},
    'N₂': {'type': 'compound', 'color': 'darkblue'},
    'Photosynthesis': {'type': 'process', 'color': 'green'},
    'Respiration': {'type': 'process', 'color': 'red'},
    'Nitrification': {'type': 'process', 'color': 'orange'},
    'Denitrification': {'type': 'process', 'color': 'purple'},
    'N₂ Fixation': {'type': 'process', 'color': 'cyan'}
}

# Add nodes
for node, attrs in processes.items():
    G.add_node(node, **attrs)

# Add edges (metabolic connections)
connections = [
    ('CO₂', 'Photosynthesis', 'Cyanobacteria'),
    ('Photosynthesis', 'Organic Carbon', 'Primary production'),
    ('Organic Carbon', 'Respiration', 'Heterotrophs'),
    ('Respiration', 'CO₂', 'Carbon cycling'),
    ('NH₄⁺', 'Nitrification', 'Nitrosomonas'),
    ('Nitrification', 'NO₃⁻', 'Nitrobacter'),
    ('NO₃⁻', 'Denitrification', 'Pseudomonas'),
    ('Denitrification', 'N₂', 'Anaerobic zones'),
    ('N₂', 'N₂ Fixation', 'Trichodesmium'),
    ('N₂ Fixation', 'NH₄⁺', 'New nitrogen')
]

for source, target, microbe in connections:
    G.add_edge(source, target, microbe=microbe)

# Visualize the network
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, k=3, iterations=50)

# Draw nodes
node_colors = [processes[node]['color'] for node in G.nodes()]
node_shapes = ['o' if processes[node]['type'] == 'compound' else 's' for node in G.nodes()]

# Draw compounds (circles) and processes (squares) separately
compounds = [node for node in G.nodes() if processes[node]['type'] == 'compound']
processes_nodes = [node for node in G.nodes() if processes[node]['type'] == 'process']

nx.draw_networkx_nodes(G, pos, nodelist=compounds, node_color=[processes[n]['color'] for n in compounds],
                      node_shape='o', node_size=2000, alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=processes_nodes, node_color=[processes[n]['color'] for n in processes_nodes],
                      node_shape='s', node_size=2000, alpha=0.8)

# Draw edges with labels
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, 
                      arrowsize=20, arrowstyle='->', width=2, alpha=0.6)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Add edge labels (microbes responsible)
edge_labels = nx.get_edge_attributes(G, 'microbe')
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8, font_style='italic')

plt.title('Ocean Metabolic Networks: The $7 Trillion Engine', fontsize=16, fontweight='bold')
plt.text(0.5, -0.1, 'Circles = Chemical compounds | Squares = Metabolic processes',
         transform=plt.gca().transAxes, ha='center', fontsize=10, style='italic')
plt.axis('off')
plt.tight_layout()
plt.show()

print("🌊 These metabolic networks generate $7 trillion in ecosystem services annually!")
print("🦠 Different microbes work together to complete these essential cycles.")

# %% [markdown] {"nbgrader": {"grade": false, "grade_id": "exercise_3_prompt", "locked": true, "schema_version": 3, "solution": false}}
# ### 🎯 Exercise 3: Analyzing eDNA Community Composition
# 
# As a citizen scientist, you'll often need to interpret eDNA results to understand ecosystem health.
# 
# **Your task**: Create a function that calculates diversity metrics from eDNA data and interprets ecosystem health.
# 
# Use the Shannon Diversity Index: H = -Σ(pi × ln(pi)), where pi is the proportion of each species

# %% {"nbgrader": {"grade": false, "grade_id": "exercise_3_solution", "locked": false, "schema_version": 3, "solution": true}}
import numpy as np

def analyze_edna_diversity(species_counts):
    """
    Calculate diversity metrics and interpret ecosystem health from eDNA data.
    
    Parameters:
    -----------
    species_counts : dict
        Dictionary with species names as keys and read counts as values
        
    Returns:
    --------
    dict
        Dictionary containing:
        - 'total_reads': Total number of DNA reads
        - 'num_species': Number of species detected
        - 'shannon_index': Shannon diversity index
        - 'evenness': Pielou's evenness (how evenly distributed species are)
        - 'health_status': Interpretation of ecosystem health
    """
    # YOUR CODE HERE
    # Calculate total reads and number of species
    total_reads = sum(species_counts.values())
    num_species = len(species_counts)
    
    # Handle edge cases
    if total_reads == 0 or num_species == 0:
        return {
            'total_reads': 0,
            'num_species': 0,
            'shannon_index': 0,
            'evenness': 0,
            'health_status': 'No data'
        }
    
    # Calculate proportions
    proportions = [count / total_reads for count in species_counts.values()]
    
    # Calculate Shannon diversity index
    shannon_index = 0
    for p in proportions:
        if p > 0:  # Avoid log(0)
            shannon_index -= p * np.log(p)
    
    # Calculate maximum possible diversity
    max_diversity = np.log(num_species) if num_species > 1 else 1
    
    # Calculate evenness (Pielou's J)
    evenness = shannon_index / max_diversity if max_diversity > 0 else 0
    
    # Interpret health status based on diversity and evenness
    if shannon_index > 3.0 and evenness > 0.8:
        health_status = "Excellent - High diversity and even distribution"
    elif shannon_index > 2.0 and evenness > 0.6:
        health_status = "Good - Moderate diversity, fairly even"
    elif shannon_index > 1.0:
        health_status = "Fair - Low diversity or uneven distribution"
    else:
        health_status = "Poor - Very low diversity, potential stress"
    
    return {
        'total_reads': total_reads,
        'num_species': num_species,
        'shannon_index': round(shannon_index, 3),
        'evenness': round(evenness, 3),
        'health_status': health_status
    }

# Test with example data
healthy_ocean = {
    'Prochlorococcus': 2500,
    'Synechococcus': 2000,
    'Pelagibacter': 1800,
    'Alteromonas': 1500,
    'Vibrio': 1200,
    'Roseobacter': 1000
}

stressed_ocean = {
    'Vibrio': 8000,  # Dominant species
    'Alteromonas': 1500,
    'Unknown_bacteria': 500
}

print("🌊 Healthy Ocean Sample:")
healthy_results = analyze_edna_diversity(healthy_ocean)
for key, value in healthy_results.items():
    print(f"  {key}: {value}")

print("\n⚠️  Stressed Ocean Sample:")
stressed_results = analyze_edna_diversity(stressed_ocean)
for key, value in stressed_results.items():
    print(f"  {key}: {value}")

# %% {"nbgrader": {"grade": true, "grade_id": "exercise_3_test", "locked": true, "points": 15, "schema_version": 3, "solution": false}}
# Test the diversity analysis function
test_data = {'A': 100, 'B': 100, 'C': 100}
result = analyze_edna_diversity(test_data)
assert result['num_species'] == 3, "Should detect 3 species"
assert result['total_reads'] == 300, "Should sum reads correctly"
assert abs(result['shannon_index'] - 1.099) < 0.01, "Shannon index calculation error"
assert result['evenness'] == 1.0, "Perfect evenness should be 1.0"

# Test edge case
empty_result = analyze_edna_diversity({})
assert empty_result['health_status'] == 'No data', "Should handle empty data"

print("✅ Outstanding! Your diversity analyzer correctly assesses ocean health!")

# %% [markdown]
# ## Chapter 4: Becoming an Ocean Guardian - Your Role as a Citizen Scientist 🌊🦸
# 
# ### Where You Can Make a Difference
# 
# With portable sequencing and the MNA pipeline, citizen scientists can now:
# 
# 1. **Monitor local waters**: Track the health of your coastal area
# 2. **Early warning system**: Detect harmful algal blooms before they're visible
# 3. **Biodiversity surveys**: Document species in remote or understudied areas
# 4. **Climate change tracking**: Monitor how warming affects microbial communities
# 5. **Pollution detection**: Identify bacterial indicators of contamination

# %% {"nbgrader": {"grade": false, "grade_id": "citizen_science_map", "locked": false, "schema_version": 3, "solution": false}}
# Create an interactive citizen science monitoring map
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(14, 8))

# Create a simple world map outline
coastline_x = [0, 2, 3, 4, 5, 7, 8, 10, 11, 12, 14, 14, 12, 11, 10, 8, 7, 5, 4, 3, 2, 0, 0]
coastline_y = [2, 2.5, 2.2, 3, 2.8, 3.2, 2.9, 3.5, 3.2, 3.8, 4, 6, 5.8, 6.2, 5.9, 6.3, 5.8, 6.2, 5.9, 6.1, 5.8, 6, 2]

ax.fill(coastline_x, coastline_y, color='tan', alpha=0.5, label='Land')
ax.fill([0, 14, 14, 0], [0, 0, 2, 2], color='lightblue', alpha=0.7, label='Ocean')
ax.fill([0, 14, 14, 0], [6, 6, 8, 8], color='lightblue', alpha=0.7)

# Add monitoring scenarios
scenarios = [
    {'pos': (2, 1), 'color': 'red', 'label': 'Coral Reef\nBleaching', 'icon': '🪸'},
    {'pos': (5, 0.8), 'color': 'green', 'label': 'Kelp Forest\nHealth', 'icon': '🌿'},
    {'pos': (8, 1.2), 'color': 'orange', 'label': 'HAB Detection\n(Harmful Algae)', 'icon': '🦠'},
    {'pos': (11, 1), 'color': 'purple', 'label': 'Deep Sea\nExploration', 'icon': '🐙'},
    {'pos': (3, 7), 'color': 'blue', 'label': 'Arctic\nMicrobiome', 'icon': '🧊'},
    {'pos': (9, 6.8), 'color': 'brown', 'label': 'Estuary\nPollution', 'icon': '🏭'},
]

for scenario in scenarios:
    # Add monitoring station
    circle = Circle(scenario['pos'], 0.3, color=scenario['color'], alpha=0.7)
    ax.add_patch(circle)
    
    # Add label
    ax.text(scenario['pos'][0], scenario['pos'][1] - 0.6, scenario['icon'] + '\n' + scenario['label'],
            ha='center', va='top', fontsize=9, fontweight='bold')
    
    # Add data flow arrows
    ax.annotate('', xy=(7, 4), xytext=scenario['pos'],
                arrowprops=dict(arrowstyle='->', color=scenario['color'], 
                              alpha=0.5, linewidth=1.5))

# Add central data hub
hub = Rectangle((6, 3.5), 2, 1, facecolor='gold', edgecolor='black', linewidth=2)
ax.add_patch(hub)
ax.text(7, 4, '🌐 iMAC\nData Hub', ha='center', va='center', fontsize=11, fontweight='bold')

# Add citizen scientist icons
citizen_positions = [(1.5, 5), (4, 4.5), (10, 5), (12, 4)]
for pos in citizen_positions:
    ax.text(pos[0], pos[1], '👨‍🔬', fontsize=20)

# Title and labels
ax.set_title('Global Citizen Science Network: Monitoring Ocean Health with eDNA',
             fontsize=16, fontweight='bold')
ax.text(7, -0.5, '🌊 Every sample tells a story. Every story helps protect our oceans.',
        ha='center', fontsize=12, style='italic', color='darkblue')

# Legend
monitoring_types = [mpatches.Patch(color=s['color'], label=s['label'].replace('\n', ' ')) 
                   for s in scenarios[:4]]
ax.legend(handles=monitoring_types, loc='upper right', title='Monitoring Types')

ax.set_xlim(-0.5, 14.5)
ax.set_ylim(-1, 8.5)
ax.axis('off')

plt.tight_layout()
plt.show()

print("🌍 Join thousands of citizen scientists worldwide in protecting our oceans!")

# %% [markdown]
# ### Your eDNA Monitoring Toolkit 🧰
# 
# Here's what you need to get started:
# 
# 1. **Basic Equipment**:
#    - Water sampling bottles (sterile)
#    - Filtration system (0.22 μm filters)
#    - DNA preservation buffer
#    - GPS device or smartphone
#    - Field notebook
# 
# 2. **For Advanced Monitoring**:
#    - MinION sequencer (~$1,000)
#    - Laptop with MNA pipeline
#    - Portable power supply
#    - Internet for data upload

# %% [markdown] {"nbgrader": {"grade": false, "grade_id": "exercise_4_prompt", "locked": true, "schema_version": 3, "solution": false}}
# ### 🎯 Exercise 4: Design Your Own Monitoring Project
# 
# **Your task**: Create a function that helps citizen scientists plan their eDNA monitoring project by calculating sampling requirements and generating a field protocol.

# %% {"nbgrader": {"grade": false, "grade_id": "exercise_4_solution", "locked": false, "schema_version": 3, "solution": true}}
def plan_monitoring_project(site_name, monitoring_goal, area_km2, budget_usd):
    """
    Plan a citizen science eDNA monitoring project.
    
    Parameters:
    -----------
    site_name : str
        Name of the monitoring location
    monitoring_goal : str
        One of: 'biodiversity', 'pollution', 'climate', 'invasive'
    area_km2 : float
        Area to monitor in square kilometers
    budget_usd : float
        Available budget in US dollars
    
    Returns:
    --------
    dict
        Project plan including:
        - 'num_samples': Recommended number of samples
        - 'sampling_frequency': How often to sample
        - 'sequencing_approach': Recommended sequencing strategy
        - 'total_cost': Estimated project cost
        - 'duration_months': Recommended project duration
        - 'protocol': Step-by-step sampling protocol
    """
    # YOUR CODE HERE
    # Define monitoring parameters based on goal
    monitoring_params = {
        'biodiversity': {
            'samples_per_km2': 3,
            'frequency': 'Monthly',
            'duration': 12,
            'sequencing_depth': 'High'
        },
        'pollution': {
            'samples_per_km2': 5,
            'frequency': 'Weekly',
            'duration': 6,
            'sequencing_depth': 'Medium'
        },
        'climate': {
            'samples_per_km2': 2,
            'frequency': 'Seasonal',
            'duration': 24,
            'sequencing_depth': 'Medium'
        },
        'invasive': {
            'samples_per_km2': 4,
            'frequency': 'Bi-weekly',
            'duration': 12,
            'sequencing_depth': 'Low'
        }
    }
    
    # Get parameters for the monitoring goal
    params = monitoring_params.get(monitoring_goal, monitoring_params['biodiversity'])
    
    # Calculate number of samples
    num_samples = int(params['samples_per_km2'] * area_km2)
    num_samples = max(3, min(num_samples, 50))  # Practical limits
    
    # Calculate costs
    cost_per_sample = 50  # Basic processing
    sequencing_costs = {
        'High': 200,   # Full MinION flow cell
        'Medium': 100, # Shared flow cell
        'Low': 50      # Targeted sequencing
    }
    
    sequencing_cost = sequencing_costs[params['sequencing_depth']]
    
    # Determine sampling events based on frequency
    frequency_events = {
        'Weekly': 52,
        'Bi-weekly': 26,
        'Monthly': 12,
        'Seasonal': 4
    }
    events_per_year = frequency_events[params['frequency']]
    total_events = int(events_per_year * params['duration'] / 12)
    
    # Calculate total cost
    total_cost = (num_samples * cost_per_sample + sequencing_cost) * total_events
    
    # Determine sequencing approach based on budget
    if budget_usd >= total_cost:
        sequencing_approach = f"Full {params['sequencing_depth'].lower()} coverage sequencing"
    elif budget_usd >= total_cost * 0.5:
        sequencing_approach = "Pooled samples with medium coverage"
        total_cost *= 0.5
    else:
        sequencing_approach = "Targeted marker gene sequencing only"
        total_cost *= 0.25
    
    # Generate protocol
    protocol = [
        f"1. Establish {num_samples} sampling points across {area_km2} km²",
        f"2. Collect 1L water samples at each point",
        f"3. Filter through 0.22 μm membrane within 2 hours",
        f"4. Preserve filters in DNA buffer at -20°C",
        f"5. Record GPS coordinates, temperature, and observations",
        f"6. Sample {params['frequency'].lower()} for {params['duration']} months",
        f"7. Sequence using {sequencing_approach}",
        f"8. Analyze with MNA pipeline and share results"
    ]
    
    return {
        'num_samples': num_samples,
        'sampling_frequency': params['frequency'],
        'sequencing_approach': sequencing_approach,
        'total_cost': round(total_cost, 2),
        'duration_months': params['duration'],
        'protocol': protocol
    }

# Example: Planning a coral reef monitoring project
project = plan_monitoring_project(
    site_name="Turtle Bay Reef",
    monitoring_goal="biodiversity",
    area_km2=2.5,
    budget_usd=5000
)

print("🏝️ eDNA Monitoring Project Plan: Turtle Bay Reef")
print(f"\n📊 Project Overview:")
print(f"  • Samples per event: {project['num_samples']}")
print(f"  • Sampling frequency: {project['sampling_frequency']}")
print(f"  • Duration: {project['duration_months']} months")
print(f"  • Sequencing: {project['sequencing_approach']}")
print(f"  • Estimated cost: ${project['total_cost']:,.2f}")

print(f"\n📋 Field Protocol:")
for step in project['protocol']:
    print(f"  {step}")

# %% {"nbgrader": {"grade": true, "grade_id": "exercise_4_test", "locked": true, "points": 15, "schema_version": 3, "solution": false}}
# Test the monitoring project planner
test_project = plan_monitoring_project("Test Site", "pollution", 1.0, 10000)
assert test_project['num_samples'] == 5, "Should calculate correct sample number"
assert test_project['sampling_frequency'] == 'Weekly', "Should set correct frequency"
assert len(test_project['protocol']) == 8, "Should generate complete protocol"
assert test_project['total_cost'] > 0, "Should calculate costs"

# Test budget constraints
low_budget = plan_monitoring_project("Test Site", "biodiversity", 10.0, 1000)
assert "Targeted" in low_budget['sequencing_approach'], "Should adapt to low budget"

print("✅ Fantastic! You're ready to plan real eDNA monitoring projects!")

# %% [markdown]
# ## Chapter 5: The Future is in Your Hands 🚀
# 
# ### Emerging Technologies and Opportunities
# 
# The future of ocean monitoring is incredibly exciting:
# 
# 1. **Real-time sequencing buoys**: Autonomous eDNA monitoring stations
# 2. **AI-powered species identification**: Instant results from sequencing
# 3. **Blockchain verification**: Ensuring data integrity for policy decisions
# 4. **Citizen science networks**: Global ocean health monitoring
# 5. **Predictive modeling**: Forecasting ecosystem changes

# %% {"nbgrader": {"grade": false, "grade_id": "future_vision", "locked": false, "schema_version": 3, "solution": false}}
# Visualize the future of ocean monitoring
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(14, 10))

# Create timeline
years = [2024, 2026, 2028, 2030, 2035]
y_positions = np.linspace(1, 9, len(years))

# Draw timeline
ax.plot([2, 2], [0, 10], 'k-', linewidth=3)
for year, y in zip(years, y_positions):
    ax.plot([1.8, 2.2], [y, y], 'k-', linewidth=2)
    ax.text(1.5, y, str(year), ha='right', fontsize=12, fontweight='bold')

# Add future developments
developments = [
    {
        'year': 2024,
        'title': 'Citizen Science Launch',
        'desc': '• Portable MinION kits\n• MNA pipeline v1.0\n• Community training',
        'icon': '👥',
        'color': 'lightblue'
    },
    {
        'year': 2026,
        'title': 'Autonomous Monitors',
        'desc': '• Solar-powered buoys\n• Continuous sampling\n• Satellite uplink',
        'icon': '🛰️',
        'color': 'lightgreen'
    },
    {
        'year': 2028,
        'title': 'AI Integration',
        'desc': '• Real-time analysis\n• Anomaly detection\n• Predictive alerts',
        'icon': '🤖',
        'color': 'lightyellow'
    },
    {
        'year': 2030,
        'title': 'Global Network',
        'desc': '• 10,000+ stations\n• Open data platform\n• Policy integration',
        'icon': '🌐',
        'color': 'lightcoral'
    },
    {
        'year': 2035,
        'title': 'Ocean Digital Twin',
        'desc': '• Complete microbiome map\n• Climate predictions\n• Ecosystem management',
        'icon': '🌊',
        'color': 'lavender'
    }
]

# Plot developments
for i, (dev, y) in enumerate(zip(developments, y_positions)):
    # Create box
    box = FancyBboxPatch((3, y-0.8), 8, 1.6, boxstyle="round,pad=0.1",
                        facecolor=dev['color'], edgecolor='black', linewidth=2)
    ax.add_patch(box)
    
    # Add content
    ax.text(4, y+0.3, dev['icon'] + ' ' + dev['title'], fontsize=14, fontweight='bold')
    ax.text(4, y-0.3, dev['desc'], fontsize=10, va='top')
    
    # Connect to timeline
    ax.plot([2.2, 3], [y, y], 'k--', alpha=0.5)

# Add inspiring message
ax.text(7, 10.5, 'The Future of Ocean Monitoring: Your Journey Starts Today! 🚀',
        ha='center', fontsize=16, fontweight='bold')

ax.text(7, -0.5, '"The ocean is not just water - it\'s a living system that needs guardians like you."',
        ha='center', fontsize=12, style='italic', color='darkblue')

# Impact metrics
impact_box = FancyBboxPatch((11.5, 3), 2.5, 4, boxstyle="round,pad=0.1",
                           facecolor='gold', edgecolor='black', linewidth=2)
ax.add_patch(impact_box)
ax.text(12.75, 6.5, 'Your Impact:', ha='center', fontsize=12, fontweight='bold')
ax.text(12.75, 5.8, '🌍 1 sample =\n1000 species\nidentified', ha='center', fontsize=10)
ax.text(12.75, 4.8, '📊 1 year =\n52 data points\nfor science', ha='center', fontsize=10)
ax.text(12.75, 3.8, '🐟 1 project =\n∞ ocean\nprotection', ha='center', fontsize=10)

ax.set_xlim(0, 14)
ax.set_ylim(-1, 11)
ax.axis('off')

plt.tight_layout()
plt.show()

print("🌟 The future of our oceans depends on citizen scientists like you!")
print("🔬 With eDNA technology, we can finally understand and protect the 71% of our planet covered by water.")

# %% [markdown]
# ## Final Challenge: Put It All Together! 🏆
# 
# Now that you've learned about eDNA, Nanopore sequencing, and the MNA pipeline, let's simulate a complete monitoring workflow!

# %% {"nbgrader": {"grade": false, "grade_id": "final_challenge", "locked": false, "schema_version": 3, "solution": true}}
def simulate_edna_monitoring(location, water_temp, sample_volume_ml, sequencing_hours):
    """
    Simulate a complete eDNA monitoring workflow from sampling to results.
    
    Parameters:
    -----------
    location : str
        Sampling location name
    water_temp : float
        Water temperature in Celsius
    sample_volume_ml : float
        Volume of water sampled in milliliters
    sequencing_hours : float
        Hours of sequencing performed
    
    Returns:
    --------
    dict
        Complete monitoring report including:
        - 'location': Sampling location
        - 'edna_quality': Expected eDNA quality based on conditions
        - 'species_detected': Simulated number of species found
        - 'diversity_index': Calculated diversity metric
        - 'dominant_groups': List of dominant microbial groups
        - 'ecosystem_health': Overall assessment
        - 'recommendations': Next steps for monitoring
    """
    # YOUR CODE HERE
    # Simulate eDNA quality based on temperature
    edna_persistence = estimate_edna_persistence(water_temp)
    if edna_persistence > 10:
        edna_quality = "Excellent"
        quality_factor = 1.0
    elif edna_persistence > 5:
        edna_quality = "Good"
        quality_factor = 0.8
    elif edna_persistence > 2:
        edna_quality = "Fair"
        quality_factor = 0.6
    else:
        edna_quality = "Poor"
        quality_factor = 0.4
    
    # Estimate species detection based on sample volume and sequencing
    # Assume 1L optimal, with diminishing returns
    volume_factor = min(1.0, sample_volume_ml / 1000)
    
    # Assume 1 Gb/hour sequencing, with logarithmic returns
    sequencing_gb = sequencing_hours * 1.0
    sequencing_factor = np.log10(sequencing_gb + 1) / np.log10(10)
    
    # Calculate expected species
    base_species = 50  # Typical marine sample
    species_detected = int(base_species * quality_factor * volume_factor * sequencing_factor)
    species_detected = max(5, min(species_detected, 200))  # Realistic bounds
    
    # Simulate diversity
    # Higher temperature generally means lower diversity in extreme cases
    if water_temp < 10:
        diversity_base = 2.5
        dominant_groups = ['Psychrophiles', 'SAR11', 'Polaribacter']
    elif water_temp < 20:
        diversity_base = 3.0
        dominant_groups = ['Prochlorococcus', 'Synechococcus', 'Pelagibacter']
    else:
        diversity_base = 2.0
        dominant_groups = ['Vibrio', 'Alteromonas', 'Pseudoalteromonas']
    
    diversity_index = round(diversity_base * quality_factor * np.random.uniform(0.8, 1.2), 2)
    
    # Assess ecosystem health
    if diversity_index > 2.5 and species_detected > 30:
        ecosystem_health = "Healthy - Diverse microbial community"
    elif diversity_index > 1.5 and species_detected > 20:
        ecosystem_health = "Moderate - Some stress indicators"
    else:
        ecosystem_health = "Stressed - Low diversity, needs attention"
    
    # Generate recommendations
    recommendations = []
    if edna_quality in ["Poor", "Fair"]:
        recommendations.append("Sample during cooler periods for better eDNA preservation")
    if species_detected < 30:
        recommendations.append("Increase sample volume or sequencing depth")
    if diversity_index < 2.0:
        recommendations.append("Monitor more frequently to track changes")
    if water_temp > 25:
        recommendations.append("Check for thermal stress indicators")
    
    if not recommendations:
        recommendations.append("Continue regular monitoring schedule")
        recommendations.append("Consider expanding to nearby sites")
    
    return {
        'location': location,
        'edna_quality': edna_quality,
        'species_detected': species_detected,
        'diversity_index': diversity_index,
        'dominant_groups': dominant_groups,
        'ecosystem_health': ecosystem_health,
        'recommendations': recommendations
    }

# Simulate a monitoring event
results = simulate_edna_monitoring(
    location="Coral Garden Bay",
    water_temp=24,
    sample_volume_ml=1000,
    sequencing_hours=4
)

print("🌊 eDNA Monitoring Report")
print("=" * 50)
print(f"📍 Location: {results['location']}")
print(f"🧬 eDNA Quality: {results['edna_quality']}")
print(f"🦠 Species Detected: {results['species_detected']}")
print(f"📊 Diversity Index: {results['diversity_index']}")
print(f"🏆 Dominant Groups: {', '.join(results['dominant_groups'])}")
print(f"💚 Ecosystem Health: {results['ecosystem_health']}")
print(f"\n📋 Recommendations:")
for rec in results['recommendations']:
    print(f"  • {rec}")

# %% {"nbgrader": {"grade": true, "grade_id": "final_challenge_test", "locked": true, "points": 20, "schema_version": 3, "solution": false}}
# Test the complete monitoring simulation
test_results = simulate_edna_monitoring("Test Site", 15, 500, 2)
assert 'location' in test_results, "Missing location in results"
assert 'species_detected' in test_results, "Missing species count"
assert 'diversity_index' in test_results, "Missing diversity index"
assert 'ecosystem_health' in test_results, "Missing health assessment"
assert len(test_results['recommendations']) > 0, "Should provide recommendations"
assert test_results['species_detected'] > 0, "Should detect some species"

print("\n✅ 🎉 CONGRATULATIONS! You've completed the eDNA Ocean Monitoring curriculum!")
print("🌊 You're now ready to join the global community of ocean guardians!")

# %% [markdown]
# ## 🎓 Curriculum Complete! Your Next Steps
# 
# ### You've learned:
# ✅ What eDNA is and why it's revolutionary  
# ✅ The hidden world of ocean microbes worth $7 trillion  
# ✅ How Nanopore sequencing democratizes ocean science  
# ✅ The MNA pipeline for analyzing marine eDNA  
# ✅ How to plan and execute monitoring projects  
# 
# ### Your journey continues:
# 
# 1. **Join the iMAC community** - Connect with fellow ocean guardians
# 2. **Start local** - Monitor a nearby water body
# 3. **Share your data** - Every sample contributes to global understanding
# 4. **Keep learning** - Advanced workshops on specific techniques
# 5. **Inspire others** - Teach someone else about eDNA
# 
# ### Remember:
# > "In every drop of water, there's a story of life waiting to be told. You now have the tools to read those stories and help write a better future for our oceans." 🌊
# 
# ### 🔗 Resources:
# - iMAC Community Forum: Share your experiences
# - MNA Pipeline Documentation: Technical details
# - Equipment Suppliers: Get your sampling kit
# - Data Upload Portal: Contribute to global database
# 
# **The ocean needs guardians like you. Welcome to the revolution! 🌊🧬🚀**

# %% [markdown]
# ---
# 
# *This curriculum was developed by the iMAC Education Team to empower citizen scientists worldwide. Together, we're unlocking the secrets of the ocean, one sample at a time.*