#!/bin/env python3

import sys
from pathlib import Path
from collections import defaultdict

def usage():
	print("""usage: ext_info.py path
displays number of files and total size of files per extension in the specified path.""")

def analyze_path(path_s):
	sfx_stats = defaultdict(lambda: dict(num=0,sz_sum=0))

	for p in Path(path_s).iterdir():
		if p.is_file():
			sfx = p.suffix[1:] if p.suffix else "."

			sfx_stats[sfx]['num'] += 1
			sfx_stats[sfx]['sz_sum'] += p.stat().st_size

	for k in sorted(sfx_stats):
		print("{} {} {}".format(
			k,sfx_stats[k]['num'],
			sfx_stats[k]['sz_sum']))


if __name__ == "__main__":
	
	if len(sys.argv) != 2:
		usage()
		sys.exit(1)

	analyze_path(sys.argv[1])
