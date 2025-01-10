import os
import random
import datetime
import subprocess

# Set the repository path (replace with your own)
REPO_PATH = '/path/to/your/repo'

# Change to your repository directory
os.chdir(REPO_PATH)

# Number of reports to create per week (random between 1 to 5)
reports_per_week = random.randint(1, 5)

# Get today's date
today = datetime.date.today()

# Get the start of the week (Monday)
start_of_week = today - datetime.timedelta(days=today.weekday())

# Generate random days to create reports this week
days_to_report = random.sample(range(5), reports_per_week)

# Loop through the days and create ad hoc reports
for day in days_to_report:
    date = start_of_week + datetime.timedelta(days=day)
    date_str = date.strftime('%Y-%m-%d')

    # Create a report file and commit
    filename = f'ad-hoc-report-{date_str}.txt'
    with open(filename, 'w') as f:
        f.write(f'Ad Hoc Report generated on {date_str}')

    # Git commands to add, commit, and push
    subprocess.run(['git', 'add', filename])
    subprocess.run(['git', 'commit', '--date', f'{date_str}T12:00:00', '-m', f'Ad Hoc Report generated on {date_str}'])
    subprocess.run(['git', 'push'])
