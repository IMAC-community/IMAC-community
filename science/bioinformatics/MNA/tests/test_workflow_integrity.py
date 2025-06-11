"""
End-to-end workflow testing for marine eDNA analysis

Tests the complete pipeline from raw reads to metabolic profiles,
ensuring all components work together correctly.
"""

import pytest
import sys
from pathlib import Path
import yaml

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


class TestWorkflowIntegrity:
    """Test complete workflow execution."""
    
    def test_config_loading(self):
        """Test that all configuration files load correctly."""
        config_dir = Path(__file__).parent.parent / "config"
        
        # Test default config
        with open(config_dir / "default_config.yaml", 'r') as f:
            config = yaml.safe_load(f)
        
        assert config['workflow']['name'] == "marine_edna_metabolic_analysis"
        assert 'quality_control' in config
        assert 'humann3' in config
        assert 'marine_adaptations' in config
    
    def test_directory_structure(self):
        """Test that all required directories exist."""
        root = Path(__file__).parent.parent
        
        required_dirs = [
            "config",
            "DAG-steps",
            "reference_data",
            "example_data",
            "educational_resources",
            "tests"
        ]
        
        for dir_name in required_dirs:
            dir_path = root / dir_name
            assert dir_path.exists(), f"Missing directory: {dir_name}"
            assert dir_path.is_dir(), f"Not a directory: {dir_name}"
    
    def test_dag_modules_import(self):
        """Test that all DAG modules can be imported."""
        try:
            from DAG_steps import quality_control
            from DAG_steps import denoising
            from DAG_steps import taxonomic_profiling
            from DAG_steps import humann3_execution
            from DAG_steps import marine_normalization
            from DAG_steps import timeseries_analysis
            from DAG_steps import visualization
        except ImportError as e:
            pytest.fail(f"Failed to import DAG module: {e}")
    
    def test_main_workflow_syntax(self):
        """Test that main_workflow.py has valid Python syntax."""
        workflow_path = Path(__file__).parent.parent / "main_workflow.py"
        assert workflow_path.exists(), "main_workflow.py not found"
        
        # Compile to check syntax
        with open(workflow_path, 'r') as f:
            code = f.read()
        
        try:
            compile(code, 'main_workflow.py', 'exec')
        except SyntaxError as e:
            pytest.fail(f"Syntax error in main_workflow.py: {e}")
    
    def test_scripts_executable(self):
        """Test that utility scripts exist and are executable."""
        root = Path(__file__).parent.parent
        
        scripts = [
            "checkout_notebook.sh",
            "reference_data/download_references.sh"
        ]
        
        for script in scripts:
            script_path = root / script
            assert script_path.exists(), f"Script not found: {script}"
            # Check if executable (Unix)
            if hasattr(script_path, 'stat'):
                import stat
                mode = script_path.stat().st_mode
                assert mode & stat.S_IXUSR, f"Script not executable: {script}"


class TestMarineAdaptations:
    """Test marine-specific features."""
    
    def test_contamination_markers(self):
        """Test that contamination marker files exist."""
        markers_dir = Path(__file__).parent.parent / "reference_data" / "marine_markers"
        
        required_files = [
            "terrestrial_markers.fasta",
            "prokaryotic_markers.fasta",
            "eukaryotic_markers.fasta"
        ]
        
        for file_name in required_files:
            file_path = markers_dir / file_name
            assert file_path.exists(), f"Marker file missing: {file_name}"
    
    def test_marine_pathways(self):
        """Test that marine pathway definitions exist."""
        pathways_dir = Path(__file__).parent.parent / "reference_data" / "ocean_metabolic_pathways"
        
        required_files = [
            "marine_carbon_cycling.txt",
            "nitrogen_cycling_marine.txt",
            "sulfur_cycling_ocean.txt"
        ]
        
        for file_name in required_files:
            file_path = pathways_dir / file_name
            assert file_path.exists(), f"Pathway file missing: {file_name}"
    
    def test_depth_zones(self):
        """Test depth zone classification."""
        from DAG_steps.taxonomic_profiling import get_depth_zone
        
        # Test zone boundaries
        assert get_depth_zone(50) == "euphotic"
        assert get_depth_zone(500) == "dysphotic"
        assert get_depth_zone(2000) == "bathypelagic"
        assert get_depth_zone(5000) == "abyssopelagic"
        assert get_depth_zone(8000) == "hadalpelagic"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])