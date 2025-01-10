import os
import random
import datetime
import subprocess

# Automatically set the working directory to the repository root
REPO_PATH = os.getenv('GITHUB_WORKSPACE')

# Change to your repository directory
os.chdir(REPO_PATH)

# Get today's date
today = datetime.date.today()
date_str = today.strftime('%Y-%m-%d')

# Randomly decide how many commits to make (0 to 5)
num_commits = random.randint(0, 5)

# Loop to create multiple commits
for i in range(num_commits):
    # Generate a random time for each commit
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)

    # Format the random time
    commit_time = f'{date_str}T{hour:02}:{minute:02}:00'

    # Create a new report file
    filename = f'ad-hoc-report-{date_str}-{i+1}.txt'
    with open(filename, 'w') as f:
        f.write(f'Ad Hoc Report generated on {date_str} at {hour:02}:{minute:02}')

    # Git commands to add, commit, and push
    subprocess.run(['git', 'add', filename])
    subprocess.run(['git', 'commit', '--date', commit_time, '-m', f'Ad Hoc Report generated on {date_str} at {hour:02}:{minute:02}'])

# Push all commits to GitHub
if num_commits > 0:
    subprocess.run(['git', 'push'])
