#!/bin/bash

git config --global core.attributesfile .gitattributes
git config --global filter.dropoutput_ipynb.clean util/ipynb_output_filter.py
git config --global filter.dropoutput_ipynb.smudge cat
