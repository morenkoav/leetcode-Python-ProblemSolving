'''
Write a solution to find the users who have valid emails.

A valid e-mail has a prefix name and a domain where:

The prefix name is a string that may contain letters (upper or lower case), 
digits, underscore '_', period '.', and/or dash '-'. The prefix name must start 
with a letter.
The domain is '@leetcode.com'.
Return the result table in any order.
'''

import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    regex = r'^[a-zA-Z][a-zA-Z0-9\.\_\-]*@leetcode\.com$'
    users['valid_emails'] = users['mail'].apply(lambda x: x if re.match(regex,x) else 0)
    return users[users.valid_emails != 0][['user_id','name','mail']]