import json
import os
from datetime import datetime

def test_merge_order():
    temp = os.popen('gh pr list --state merged --json author,baseRefName,commits,headRefName,mergeCommit,mergeStateStatus,mergeable,mergedAt,number,state,title,url')
    history = json.loads(temp.read())
    merge_sort_strings_string_date = None
    merge_cli_string_date = None

    for obj in history:
        if obj["state"] == "MERGED" and obj["baseRefName"] == "main" and obj["headRefName"] == "add/sort_strings":
            merge_sort_strings_string_date = obj["mergedAt"]
        elif obj["state"] == "MERGED" and obj["baseRefName"] == "main" and obj["headRefName"] == "add/cli":
            merge_cli_string_date = obj["mergedAt"]
        else:
            continue

    assert merge_sort_strings_string_date != None
    assert merge_cli_string_date != None

    date_time_format = '%Y-%m-%dT%H:%M:%SZ'
    sort_strings_merge_date = None
    cli_merge_date = None

    sort_strings_merge_date = datetime.strptime(merge_sort_strings_string_date, date_time_format)
    cli_merge_date = datetime.strptime(merge_cli_string_date, date_time_format)    
    assert (sort_strings_merge_date != None) and (cli_merge_date != None) and (sort_strings_merge_date < cli_merge_date)