import json
import os

def test_pr_cli_main():
    log_json = os.popen('gh pr list --state merged --json author,baseRefName,commits,headRefName,mergeCommit,mergeStateStatus,mergeable,mergedAt,number,state,title,url')
    history = json.loads(log_json.read())
    branch_merge_found = False
    for obj in history:
        if obj["state"] == "MERGED" and obj["baseRefName"] == "main" and obj["headRefName"] == "add/cli":
            branch_merge_found = True

    assert branch_merge_found == True