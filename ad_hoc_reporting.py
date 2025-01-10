import os
import random
import datetime
import subprocess

# Set the repository path (replace with your repo path)
REPO_PATH = '/path/to/your/repo'

# Change to your repository directory
os.chdir(REPO_PATH)

# Get today's date
today = datetime.date.today()
date_str = today.strftime('%Y-%m-%d')

# Generate a random time for the commit
hour = random.randint(0, 23)
minute = random.randint(0, 59)

# Format the random time
commit_time = f'{date_str}T{hour:02}:{minute:02}:00'

# Create a new report file
filename = f'ad-hoc-report-{date_str}.txt'
with open(filename, 'w') as f:
    f.write(f'Ad Hoc Report generated on {date_str} at {hour:02}:{minute:02}')

# Git commands to add, commit, and push
subprocess.run(['git', 'add', filename])
subprocess.run(['git', 'commit', '--date', commit_time, '-m', f'Ad Hoc Report generated on {date_str}'])
subprocess.run(['git', 'push'])
