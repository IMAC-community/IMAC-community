#!/bin/bash
# checkout_notebook.sh - Convert .py to .ipynb for analysis
#
# This script creates a timestamped Jupyter notebook from the main_workflow.py
# file using Jupytext. This allows version control of the source (.py) while
# providing interactive notebooks for analysis sessions.

set -e  # Exit on error

# Color codes for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# ASCII art ocean wave
echo -e "${BLUE}"
echo "   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "  ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈"
echo "   🌊 Marine eDNA Analysis Pipeline 🌊"
echo "  ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈"
echo "   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo -e "${NC}"

echo -e "${GREEN}Creating Jupyter notebook from main_workflow.py...${NC}"

# Check if jupytext is installed
if ! command -v jupytext &> /dev/null; then
    echo -e "${RED}Error: jupytext is not installed!${NC}"
    echo "Please install it with: pip install jupytext"
    exit 1
fi

# Check if main_workflow.py exists
if [ ! -f "main_workflow.py" ]; then
    echo -e "${RED}Error: main_workflow.py not found!${NC}"
    echo "Please run this script from the project root directory."
    exit 1
fi

# Generate timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
NOTEBOOK_NAME="analysis_${TIMESTAMP}.ipynb"

# Convert using jupytext
echo -e "${BLUE}Converting Python script to notebook...${NC}"
jupytext --to notebook main_workflow.py -o "$NOTEBOOK_NAME"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Created $NOTEBOOK_NAME${NC}"
    echo ""
    echo -e "${YELLOW}To start your analysis:${NC}"
    echo -e "  ${BLUE}jupyter notebook $NOTEBOOK_NAME${NC}"
    echo ""
    echo -e "${YELLOW}Or use JupyterLab:${NC}"
    echo -e "  ${BLUE}jupyter lab $NOTEBOOK_NAME${NC}"
    echo ""
    echo -e "${RED}⚠️  Remember:${NC} Edit main_workflow.py for permanent changes!"
    echo -e "This notebook is for ${GREEN}analysis only${NC} and won't be version controlled."
    echo ""
    
    # Create a marker file to track generated notebooks
    echo "$NOTEBOOK_NAME" >> .generated_notebooks.log
    
else
    echo -e "${RED}❌ Failed to create notebook!${NC}"
    echo "Please check the error messages above."
    exit 1
fi

# Optional: Launch notebook immediately
read -p "Launch notebook now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${GREEN}Launching Jupyter notebook...${NC}"
    jupyter notebook "$NOTEBOOK_NAME"
fi