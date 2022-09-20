# https://leetcode.com/problems/find-duplicate-file-in-system/

from collections import defaultdict
from typing import List


class Solution:
    @classmethod
    def findDuplicate(cls, paths: List[str]) -> List[List[str]]:
        content_dict = defaultdict(list)
        for path in paths:
            contents = path.split()
            dir1 = contents[0]
            for file in contents[1:]:
                f = file.split('(')
                name = f[0]
                content_dict[f[1].split(')')[0]].append(dir1 + "/" + name)

        return [val for val in content_dict.values() if len(val) > 1]

def main():
    print("*"*25, "Example: 1", "*"*25)
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)",
             "root/c 3.txt(abcd)","root/c/d 4.txt(efgh)",
             "root 4.txt(efgh)"]
    print(f"Paths {paths}")
    dups = Solution.findDuplicate(paths)
    ans = [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],
           ["root/a/1.txt","root/c/3.txt"]]
    print(f"Expected duplicates: {ans}")
    print(f"Calculated duplicates: {dups}")
    assert set(map(tuple, ans)) == set(map(tuple, dups)),\
         f"Calculated duplicates {dups} doesn't"\
            + f" match with Expected duplicates {ans}"

    print("*"*25, "Example: 2", "*"*25)
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)",
             "root/c/d 4.txt(efgh)"]
    print(f"Paths {paths}")
    dups = Solution.findDuplicate(paths)
    ans = [["root/a/2.txt","root/c/d/4.txt"],
           ["root/a/1.txt","root/c/3.txt"]]
    print(f"Expected duplicates: {ans}")
    print(f"Calculated duplicates: {dups}")
    assert set(map(tuple, ans)) == set(map(tuple, dups)),\
        f"Calculated duplicates {dups} doesn't"\
            + f" match with Expected duplicates {ans}"

if __name__ == "__main__":
    main()
