import json
import os

def test_pr_sort_strings_main():
    log_json = os.popen('gh pr list --state merged --json author,baseRefName,commits,headRefName,mergeCommit,mergeStateStatus,mergeable,mergedAt,number,state,title,url')
    temp = log_json.read()
    history = json.loads(temp)
    branch_merge_found = False
    for obj in history:
        if obj["state"] == "MERGED" and obj["baseRefName"] == "main" and obj["headRefName"] == "add/sort_strings":
            branch_merge_found = True

    assert branch_merge_found == True