"""Select the given residues on a formatted file."""
import sys
from typing import Iterator, List, Tuple


def select_own_format(lines: List[str], ranges: List[Tuple[int, int]]):
    """Select the residues inside `ranges` from the `target_file`.

    It prints the selected lines to stdout.
    """
    s_ranges = sorted(ranges)[::-1]
    curr_range = s_ranges.pop()
    for line in lines:
        # coming split_chains, the lines are guaranteed to be safe
        res = int(line.split()[1])
        if curr_range[0] <= res <= curr_range[1]:
            print(line, end="")
        elif res > curr_range[1]:
            if len(s_ranges) > 0:
                curr_range = s_ranges.pop()


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
            chain.append(line)
            curr_resi = res


def main():
    """Define script function."""
    ranges = [[26, 32], [49, 57], [91, 96]], [[26, 34], [50, 66], [93, 102]]
    for i, chain in enumerate(split_chains(sys.argv[1])):
        print(i)
        select_own_format(chain, ranges[i])


if __name__ == "__main__":
    main()
