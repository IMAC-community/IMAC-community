# 🌊 Marine eDNA Metabolic Analysis Glossary

## Quick Navigation
- [Sequencing Terms](#sequencing-terms)
- [Marine Biology Terms](#marine-biology-terms)
- [Metabolic Pathways](#metabolic-pathways)
- [Bioinformatics Terms](#bioinformatics-terms)
- [Oceanographic Terms](#oceanographic-terms)
- [Statistical Terms](#statistical-terms)

---

## Sequencing Terms

### eDNA (Environmental DNA)
DNA that organisms shed into their environment through mucus, feces, scales, or cell death. In the ocean, eDNA provides a snapshot of all organisms present without needing to catch them.

### Oxford Nanopore Sequencing
A long-read sequencing technology that passes DNA through protein pores and measures electrical current changes. Produces reads typically 1-100kb long with ~90-95% accuracy.

### Long Reads
DNA sequences >1000 base pairs. Advantages include better genome assembly and detection of structural variants. Disadvantages include higher error rates than short reads.

### Homopolymer
A DNA sequence of identical bases (e.g., AAAAA). Nanopore sequencing struggles with these because the electrical signal doesn't change as identical bases pass through the pore.

### Quality Score (Phred Score)
A measure of base-calling accuracy. Q10 = 90% accurate, Q20 = 99% accurate. Nanopore typically produces Q7-Q15.

### Adapter Sequences
Short DNA sequences added during library preparation. Must be removed before analysis as they're not from the organism.

---

## Marine Biology Terms

### SAR11 (Pelagibacterales)
The most abundant organism on Earth, comprising ~25% of ocean bacteria. These tiny heterotrophs eat dissolved organic matter and have streamlined genomes.

### Prochlorococcus
The smallest photosynthetic organism and most abundant phototroph in tropical oceans. Different ecotypes live at different depths based on light adaptation.

### Synechococcus
A cyanobacterium closely related to Prochlorococcus but larger and more widespread, including in colder waters.

### Thaumarchaeota
Marine archaea that oxidize ammonia to nitrite (first step of nitrification). Abundant below the photic zone.

### DMSP (Dimethylsulfoniopropionate)
An organic sulfur compound produced by phytoplankton as an osmolyte and cryoprotectant. When degraded, produces DMS which affects climate.

### DMS (Dimethyl Sulfide)
A gas produced from DMSP breakdown. Released to atmosphere where it forms cloud condensation nuclei, potentially cooling climate.

### Photic Zone (Euphotic Zone)
Ocean layer where enough sunlight penetrates for photosynthesis (0-200m). Home to phytoplankton and highest productivity.

### Mesopelagic Zone (Twilight Zone)
Ocean layer from 200-1000m. Too dark for photosynthesis but some light penetrates. Many organisms migrate here daily.

### OMZ (Oxygen Minimum Zone)
Ocean regions with dissolved oxygen <20 μM. Important for anaerobic processes like denitrification and anammox.

---

## Metabolic Pathways

### Carbon Fixation
Converting inorganic CO₂ into organic compounds. Marine organisms use various pathways including Calvin cycle and 3-hydroxypropionate bicycle.

### Nitrogen Fixation
Converting atmospheric N₂ gas into ammonia (NH₃). Only certain bacteria/archaea can do this, adding "new" nitrogen to the ocean.

### Nitrification
Two-step process converting ammonia to nitrite (by ammonia-oxidizers) then nitrite to nitrate (by nitrite-oxidizers).

### Denitrification
Converting nitrate back to N₂ gas under low oxygen conditions. Removes bioavailable nitrogen from the ocean.

### Anammox (Anaerobic Ammonia Oxidation)
Process where specialized bacteria convert ammonia and nitrite directly to N₂ gas. Important in OMZs.

### Proteorhodopsin
A light-driven proton pump found in many marine bacteria. Provides supplemental energy from sunlight without true photosynthesis.

### Carbon Concentrating Mechanism (CCM)
System that concentrates CO₂ around RuBisCO enzyme. Essential for marine phototrophs because ocean CO₂ is low.

---

## Bioinformatics Terms

### HUMANn3
Software that profiles metabolic pathways from metagenomic data. Works by identifying genes and mapping them to pathways.

### MetaPhlAn
Software that identifies which microbes are present using marker genes. Often run before HUMANn3.

### ChocoPhlAn
Database of microbial pangenomes used by HUMANn3 for nucleotide-level gene search.

### UniRef
Protein database clustered by similarity. UniRef90 means sequences clustered at 90% identity.

### Metagenome
All genetic material in an environmental sample. Represents the collective genomes of a microbial community.

### Pathway Abundance
The sum of gene abundances for all genes in a metabolic pathway. Indicates metabolic potential.

### Pathway Coverage
Fraction of pathway steps for which genes are detected. High coverage suggests complete pathway.

---

## Oceanographic Terms

### CTD
Conductivity, Temperature, Depth sensor. Standard oceanographic instrument providing environmental context.

### Chlorophyll Maximum
Depth with highest chlorophyll concentration, usually 50-150m in open ocean. Peak phytoplankton biomass.

### Thermocline
Sharp temperature gradient separating warm surface from cold deep water. Often coincides with nutrient changes.

### Upwelling
Process bringing nutrient-rich deep water to surface. Supports high productivity and unique communities.

### PSU (Practical Salinity Units)
Standard measure of ocean salinity. Open ocean typically 34-36 PSU, coastal can vary more.

### Mixed Layer
Upper ocean layer mixed by wind and waves. Uniform temperature and well-oxygenated.

---

## Statistical Terms

### Shannon Diversity
Measure accounting for both species richness and evenness. Higher values indicate more diverse communities.

### Rarefaction
Subsampling to equal depth to fairly compare diversity between samples with different sequencing depths.

### Normalization
Adjusting data to account for technical biases (sequencing depth) or environmental factors (biomass differences).

### PCoA (Principal Coordinates Analysis)
Ordination method showing similarity between samples in reduced dimensional space.

### Differential Abundance
Statistical test identifying features (taxa, pathways) that differ significantly between conditions.

### Time Series Decomposition
Separating temporal data into trend, seasonal, and random components to understand patterns.

---

## Common Acronyms

- **eDNA**: Environmental DNA
- **OMZ**: Oxygen Minimum Zone  
- **DMS**: Dimethyl Sulfide
- **DMSP**: Dimethylsulfoniopropionate
- **CCM**: Carbon Concentrating Mechanism
- **QC**: Quality Control
- **PSU**: Practical Salinity Units
- **CTD**: Conductivity, Temperature, Depth
- **bp**: Base Pairs
- **DOC**: Dissolved Organic Carbon
- **NPP**: Net Primary Production

---

## Need More Help?

- Check the [Troubleshooting Guide](troubleshooting_guide.md)
- Review example notebooks in `example_data/`
- Consult the main workflow documentation
- Visit ocean microbiome resources at [Ocean Biomolecular Observing Network](https://www.oceanbestpractices.net/)