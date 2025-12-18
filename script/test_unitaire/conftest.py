"""Configuration pytest pour résoudre les imports"""
import sys
from pathlib import Path

# Ajouter le répertoire script (parent de test_unitaire) au path
script_dir = Path(__file__).parent.parent
sys.path.insert(0, str(script_dir))