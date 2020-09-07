"""Select the given residues on a formatted file."""
import os

from typing import Iterator, List, Tuple

import click


def select_own_format(
    lines: List[str], ranges: List[Tuple[int, int]], write: str = None
):
    """Select the residues inside `ranges` from the `target_file`.

    It prints the selected lines to stdout.
    """
    s_ranges = sorted(ranges)[::-1]
    curr_range = s_ranges.pop()
    if write is not None:
        fout = open(write, "w")
    for line in lines:
        # coming split_chains, the lines are guaranteed to be safe
        res = int(line.split()[1])
        if curr_range[0] <= res <= curr_range[1]:
            if write is None:
                print(line, end="")
            else:
                fout.write(line)
        elif res > curr_range[1]:
            if len(s_ranges) > 0:
                curr_range = s_ranges.pop()
    if write is not None:
        fout.close()


def split_chains(file: str) -> Iterator[List[str]]:
    """Split internal formatted `file` in the chains of the protein."""
    curr_resi = -1
    chain = []
    with open(file, "r") as target:
        for line in target:
            res = line.split()[1]
            try:
                res = int(res)
            except Exception as e:
                raise Exception(f"check the format of the input file: {e}")
            if res < curr_resi:
                curr_resi = -1
                yield chain
                chain = []
            else:
                curr_resi = res
            chain.append(line)
    yield chain


def filter_format(file: str, path_out: str = None):
    """Define script function."""
    ranges = [[26, 32], [49, 57], [91, 96]], [[26, 34], [50, 66], [93, 102]]
    for i, chain in enumerate(split_chains(file)):
        select_own_format(chain, ranges[i], path_out)


@click.command()
@click.argument(
    "data_prots", type=click.Path(exists=True),
)
@click.argument(
    "data_out", type=click.Path(exists=True),
)
def main(data_prots, data_out):
    for prot in os.listdir(data_prots):
        if prot.endswith(".txt"):
            filter_format(
                os.path.join(data_prots, prot), os.path.join(data_out, prot)
            )


if __name__ == "__main__":
    main()
