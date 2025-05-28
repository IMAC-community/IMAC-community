#!/bin/bash
# download_references.sh - Download marine-specific reference databases
#
# This script downloads and prepares reference databases optimized for
# marine eDNA analysis, including marine-adapted versions of ChocoPhlAn,
# UniRef, and custom marine metabolic pathway databases.

set -e  # Exit on error

# Configuration
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DB_DIR="${SCRIPT_DIR}/databases"
LOG_FILE="${SCRIPT_DIR}/download.log"

# Color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Create directories
mkdir -p "${DB_DIR}"
mkdir -p "${SCRIPT_DIR}/marine_markers"
mkdir -p "${SCRIPT_DIR}/ocean_metabolic_pathways"

# Logging function
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "${LOG_FILE}"
}

# Progress bar function
progress_bar() {
    local duration=$1
    local width=50
    local progress=0
    
    while [ $progress -le $width ]; do
        printf "\r["
        printf "%${progress}s" | tr ' ' '='
        printf "%$((width-progress))s" | tr ' ' ' '
        printf "] %d%%" $((progress*100/width))
        progress=$((progress+1))
        sleep $(echo "scale=3; $duration/$width" | bc)
    done
    printf "\n"
}

echo -e "${BLUE}"
echo "======================================"
echo "  Marine eDNA Reference Downloader"
echo "  🌊 Optimized for Ocean Microbiomes"
echo "======================================"
echo -e "${NC}"

log "Starting reference database downloads..."

# Function to download with progress
download_with_progress() {
    local url=$1
    local output=$2
    local description=$3
    
    echo -e "${YELLOW}Downloading ${description}...${NC}"
    if command -v wget &> /dev/null; then
        wget -c --progress=bar:force -O "${output}" "${url}" 2>&1 | \
            grep --line-buffered "%" | \
            sed -u -e "s,.*\([0-9]\+\)%.*,\1," | \
            while read percent; do
                printf "\rProgress: [%-50s] %d%%" \
                    "$(printf '#%.0s' $(seq 1 $((percent/2))))" \
                    "$percent"
            done
        printf "\n"
    else
        curl -L -# -o "${output}" "${url}"
    fi
}

# 1. Download HUMANn3 databases
echo -e "${GREEN}1. HUMANn3 Databases${NC}"
echo "Note: Full downloads require ~50GB space and may take hours."
echo "For testing, we'll create placeholder files."

# Create placeholder database structure
log "Creating placeholder database structure for testing..."

# ChocoPhlAn placeholder
mkdir -p "${DB_DIR}/marine_chocophlan"
echo "Marine ChocoPhlAn v202212 - Placeholder" > "${DB_DIR}/marine_chocophlan/README.txt"
log "Created marine_chocophlan placeholder"

# UniRef placeholder  
mkdir -p "${DB_DIR}/marine_uniref90"
echo "Marine UniRef90 2023_01 - Placeholder" > "${DB_DIR}/marine_uniref90/README.txt"
log "Created marine_uniref90 placeholder"

# To download real databases (commented out for quick setup):
# echo "humann3_databases --download chocophlan full ${DB_DIR}"
# echo "humann3_databases --download uniref uniref90_diamond ${DB_DIR}"

# 2. Create marine marker databases
echo -e "${GREEN}2. Marine Marker Genes${NC}"

# Prokaryotic markers
cat > "${SCRIPT_DIR}/marine_markers/prokaryotic_markers.fasta" << 'EOF'
>amoA_marine_AOA_1 Ammonia monooxygenase alpha subunit - Marine Thaumarchaeota
ATGGACATGCTGACGGAAACCTGGCATTACGACCCGGAGTTCGTGAAGCACGAG
>nifH_Trichodesmium_1 Nitrogenase iron protein - Trichodesmium
ATGAGCGAAACCCTGAAGCTGGTGATCCTGAAGCAGATCGAGATCGGCATCGCG
>dsrA_marine_SRB_1 Dissimilatory sulfite reductase - Marine sulfate reducer
ATGGCGGATCAGCTGACCGAAGTGAAGGCGATCGAGACCCGCGAGGTGCTGCTG
>pmoA_marine_methanotroph_1 Methane monooxygenase - Marine methanotroph
ATGACGATCGTGAACGGCAAGACCTGGCACTTCGAGCCGGAGTTCACCAAGCTG
EOF

# Eukaryotic markers
cat > "${SCRIPT_DIR}/marine_markers/eukaryotic_markers.fasta" << 'EOF'
>rbcL_diatom_1 RuBisCO large subunit - Marine diatom
ATGTCACCACAAACAGAGACTAAAGCAAGTGTTGGATTCAAAGCTGGTGTTAAA
>rbcL_dinoflagellate_1 RuBisCO large subunit - Dinoflagellate
ATGTCACCACAAACAGAAACTAAAGCAAGTGTTGGGTTCAAAGCTGGTGTTAAA
>18S_V4_phytoplankton Universal 18S V4 region - Marine phytoplankton
CCAGCACCCGCGGTAATTCCAGCTCCAATAGCGTATATTAAAGTTGCTGCAGTT
EOF

# Terrestrial contamination markers
cat > "${SCRIPT_DIR}/marine_markers/terrestrial_markers.fasta" << 'EOF'
>soil_bacterium_16S_1 Bacillus 16S rRNA - Common soil contaminant
AGAGTTTGATCCTGGCTCAGGATGAACGCTGGCGGCGTGCCTAATACATGCAAG
>plant_chloroplast_rbcL_1 Land plant chloroplast marker
ATGTCACCACAAACAGAGACTAAAGCAAGTGTTGGATTCAAAGCTGGTGTTAAA
>human_skin_16S_1 Staphylococcus 16S - Human contamination
AGAGTTTGATCCTGGCTCAGGACGAACGCTGGCGGCGTGCCTAATACATGCAAG
EOF

log "Created marine marker gene databases"

# 3. Marine metabolic pathways
echo -e "${GREEN}3. Marine Metabolic Pathways${NC}"

# Carbon cycling pathways
cat > "${SCRIPT_DIR}/ocean_metabolic_pathways/marine_carbon_cycling.txt" << 'EOF'
# Marine Carbon Cycling Pathways
# Format: PathwayID	PathwayName	KeyGenes	MarineImportance

DMS_degradation	Dimethylsulfoniopropionate degradation	dmdA,dddP,dddD,dddL	Climate_regulation
Carbon_concentration	Carbon concentrating mechanisms	ccmK,ccmL,ccmM,ccmN	Low_CO2_adaptation
Proteorhodopsin	Light-driven proton pump	proteorhodopsin	Energy_supplement
Anaplerotic_carbon	Anaplerotic carbon fixation	pckA,ppsA,maeB	Dark_carbon_fixation
EOF

# Nitrogen cycling pathways
cat > "${SCRIPT_DIR}/ocean_metabolic_pathways/nitrogen_cycling_marine.txt" << 'EOF'
# Marine Nitrogen Cycling Pathways
# Format: PathwayID	PathwayName	KeyGenes	MarineImportance

Marine_nitrification	Ammonia oxidation marine	amoA,amoB,amoC,hao	Primary_production
Anammox	Anaerobic ammonia oxidation	hzsA,hzsB,hzsC,hdh	OMZ_nitrogen_loss
Marine_N_fixation	Marine nitrogen fixation	nifH,nifD,nifK	New_nitrogen_input
Cyanate_utilization	Cyanate degradation	cynS,cynA,cynB	Alternative_N_source
EOF

# Sulfur cycling pathways
cat > "${SCRIPT_DIR}/ocean_metabolic_pathways/sulfur_cycling_ocean.txt" << 'EOF'
# Marine Sulfur Cycling Pathways  
# Format: PathwayID	PathwayName	KeyGenes	MarineImportance

DMSP_synthesis	DMSP biosynthesis	DSYB,TpMT1,TpMT2	Osmolyte_climate
DMSP_cleavage	DMSP lyase pathway	dddD,dddP,dddL,dddQ	DMS_production
DMSP_demethylation	DMSP demethylation	dmdA,dmdB,dmdC,dmdD	Carbon_source
Sulfur_oxidation	Marine sulfur oxidation	soxA,soxB,soxC,soxD	Energy_generation
EOF

log "Created marine metabolic pathway definitions"

# 4. Download SILVA marine subset (placeholder)
echo -e "${GREEN}4. SILVA Marine SSU Database${NC}"
mkdir -p "${DB_DIR}/SILVA"
echo "SILVA 138.2 Marine Subset - Placeholder" > "${DB_DIR}/SILVA/README.txt"
# Real download:
# download_with_progress \
#     "https://www.arb-silva.de/fileadmin/silva_databases/release_138/Exports/SILVA_138.2_SSURef_NR99_tax_silva.fasta.gz" \
#     "${DB_DIR}/SILVA/SILVA_138.2_SSURef_NR99.fasta.gz" \
#     "SILVA SSU database"

# 5. Create database index
echo -e "${GREEN}5. Creating Database Index${NC}"

cat > "${DB_DIR}/database_index.json" << EOF
{
  "version": "1.0",
  "created": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "databases": {
    "marine_chocophlan": {
      "path": "marine_chocophlan",
      "version": "v202212",
      "size_gb": 15,
      "status": "placeholder"
    },
    "marine_uniref90": {
      "path": "marine_uniref90", 
      "version": "2023_01",
      "size_gb": 25,
      "status": "placeholder"
    },
    "silva_marine": {
      "path": "SILVA",
      "version": "138.2",
      "size_gb": 1,
      "status": "placeholder"
    }
  },
  "markers": {
    "prokaryotic": "${SCRIPT_DIR}/marine_markers/prokaryotic_markers.fasta",
    "eukaryotic": "${SCRIPT_DIR}/marine_markers/eukaryotic_markers.fasta",
    "contamination": "${SCRIPT_DIR}/marine_markers/terrestrial_markers.fasta"
  },
  "pathways": {
    "carbon": "${SCRIPT_DIR}/ocean_metabolic_pathways/marine_carbon_cycling.txt",
    "nitrogen": "${SCRIPT_DIR}/ocean_metabolic_pathways/nitrogen_cycling_marine.txt",
    "sulfur": "${SCRIPT_DIR}/ocean_metabolic_pathways/sulfur_cycling_ocean.txt"
  }
}
EOF

log "Created database index"

# 6. Verify setup
echo -e "${GREEN}6. Verifying Setup${NC}"

# Check created files
echo "Checking created files..."
for file in \
    "${SCRIPT_DIR}/marine_markers/prokaryotic_markers.fasta" \
    "${SCRIPT_DIR}/marine_markers/eukaryotic_markers.fasta" \
    "${SCRIPT_DIR}/marine_markers/terrestrial_markers.fasta" \
    "${SCRIPT_DIR}/ocean_metabolic_pathways/marine_carbon_cycling.txt" \
    "${DB_DIR}/database_index.json"
do
    if [ -f "$file" ]; then
        echo -e "  ${GREEN}✓${NC} $(basename $file)"
    else
        echo -e "  ${RED}✗${NC} $(basename $file)"
    fi
done

# Summary
echo -e "${BLUE}"
echo "======================================"
echo "  Setup Complete!"
echo "======================================"
echo -e "${NC}"

echo -e "${YELLOW}Note:${NC} This script created placeholder databases for quick setup."
echo "To download full databases (~50GB), uncomment the download commands in this script."
echo ""
echo -e "${GREEN}Next steps:${NC}"
echo "1. Activate the conda environment: conda activate marine-edna-humann3"
echo "2. Run the tutorial: ./checkout_notebook.sh"
echo ""

log "Reference database setup completed"