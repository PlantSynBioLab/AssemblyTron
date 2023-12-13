# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import src.AssemblyTron.Update_Input
import src.AssemblyTron.opentrons_demo_script
import src.AssemblyTron.pathswriter
import src.AssemblyTron.static_wired_IP_address
import src.AssemblyTron.j5_to_csvs
import src.AssemblyTron.j5_to_csvs_digests
import src.AssemblyTron

import src.AssemblyTron.Golden_Gate.GoldenGate_nodigests_separatepcrruns_gradient_writer
import src.AssemblyTron.Golden_Gate.Setup_digests_gradient
import src.AssemblyTron.Golden_Gate.Setup_nodigests_seppcr_gradient_24
import src.AssemblyTron.Golden_Gate.Setup_nodigests_seppcr_gradient_96
import src.AssemblyTron.Golden_Gate.dilution_24_writer
import src.AssemblyTron.Golden_Gate.dilution_96_writer
import src.AssemblyTron.Golden_Gate

import src.AssemblyTron.Cloning.IVA_separatepcrruns_gradient_writer
import src.AssemblyTron.Cloning.Setup_seppcr_gradient_24
import src.AssemblyTron.Cloning.Setup_seppcr_gradient_96
import src.AssemblyTron.Cloning.dilution_24_writer
import src.AssemblyTron.Cloning.dilution_96_writer
import src.AssemblyTron.Cloning

import src.AssemblyTron.Error_prone_PCR_Golden_Gate
import src.AssemblyTron.Error_prone_PCR_Golden_Gate.1_Setup_STD_GoldenGate_digests_PCR
import src.AssemblyTron.Error_prone_PCR_Golden_Gate.1_Setup_STD_GoldenGate_PCR
import src.AssemblyTron.Error_prone_PCR_Golden_Gate.dilution_24_digests_writer
import src.AssemblyTron.Error_prone_PCR_Golden_Gate.dilution_Error_prone_PCR_writer
import src.AssemblyTron.Error_prone_PCR_Golden_Gate.Error_prone_PCR_writer
import src.AssemblyTron.Error_prone_PCR_Golden_Gate.GoldenGate_digests_separatepcrruns_gradient_writer



# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AssemblyTron'
copyright = '2022, John Bryant, Clay Wright, Mason Kellinger, Cameron Longmire, Ryan Miller'
author = 'John Bryant, Clay Wright, Mason Kellinger, Cameron Longmire, Ryan Miller'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
