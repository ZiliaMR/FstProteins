#!/usr/bin/env python3

import nglview as nv
import mdtraj as md
import numpy as np

file_pdb = "Input_Files/4zh0.pdb"

nv.show_file(file_pdb)

protein = md.load(file_pdb)