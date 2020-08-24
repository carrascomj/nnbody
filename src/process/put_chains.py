"""Annotate chains of the PDB file.

The PDBs from MOE don't contain the chain, so a custom parser is needed to deal
with them and apply the chain (alphabetic order).

author: Jorge Carrasco Muriel
contact: carrascomurielj@gmail.com
"""
import os
import re

from os.path import join, pardir, split
from string import ascii_uppercase
from typing import List

pat = re.compile(r"[A-Z]")


def annotate_chains(path: str, path_out: str):
    """Set PDB chain."""
    curr_chain = 0
    last_seg = -1
    with open(path, "r") as fin:
        with open(path_out, "w") as fout:
            for f in fin.readlines():
                line_out = f
                if f.startswith("ATOM"):
                    atom_num = int(pat.sub("", f.split()[4]))
                    if atom_num < last_seg:
                        curr_chain += 1
                    line_out = f[:21] + ascii_uppercase[curr_chain] + f[22:]
                    last_seg = atom_num
                fout.write(line_out)


def annotate_all(paths: List, out_dir: str = "."):
    """Set correct chains for a list of pdb `paths`."""
    for path in paths:
        tail = split(path)[1]
        annotate_chains(path, join(out_dir, f"{tail[:tail.find('_L')]}.pdb"))


if __name__ == '__main__':
    data = join(pardir, pardir, "data", "interm", "moe_out")
    out_dir = join(data, pardir, "moe_chained")
    pdbs = [
        join(data, file) for file in os.listdir(data) if file.endswith(".pdb")
    ]
    annotate_all(pdbs, out_dir)
