"""Mutate sequences given the mutation sites.

author: Jorge Carrasco Muriel
contact: carrascomurielj@gmail.com
"""
from os.path import join, pardir
from typing import Dict

import pandas as pd


def mutate(parent: str, sites: Dict):
    """Mutate a parent string given the sites."""
    child = list(parent)
    for site, letter in sites.items():
        child[int(site)] = letter
    return "".join(child)


def write_fasta(path: str, header: str, seq: str):
    """Write `seq` to fasta at `path`."""
    with open(path, "a") as f:
        f.write(f">{header}\n{seq}\n")


def _transform_row(row):
    mut_dict = row[~row.isna()].to_dict()
    id = mut_dict["ID"]
    del mut_dict["ID"]
    return id, mut_dict


def mutate_all(parent_light: str, parent_heavy: str, mut_light: pd.DataFrame,
               mut_heavy: pd.DataFrame, data_path: str, separate=False):
    """Apply mutations to parent chains."""
    fasta = join(data_path, "all_variants.fasta")
    for r_light, r_heavy in zip(mut_light.iterrows(), mut_heavy.iterrows()):
        id, mut_dict = _transform_row(r_light[1])
        if separate:
            fasta = join(data_path, f"{id}.fasta")
        write_fasta(fasta, f"{id}_L", mutate(parent_light, mut_dict))
        _, mut_dict = _transform_row(r_heavy[1])
        write_fasta(fasta, f"{id}_H", mutate(parent_heavy, mut_dict))


if __name__ == '__main__':
    data = join(pardir, pardir, "data", "processed")
    with open(join(data, pardir, "raw", "parent.fasta")) as f:
        lines = f.readlines()
        parent = lines[1]
        parent_light = lines[3]
        print(parent, parent_light, sep="\n")
    mutate_all(
        parent_light, parent,
        pd.read_csv(join(data, "light_chains.tsv"), sep="\t"),
        pd.read_csv(join(data, "heavy_chains.tsv"), sep="\t"),
        join(data, "fasta")
    )
