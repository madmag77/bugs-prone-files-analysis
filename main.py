import os
import subprocess
import sys

project_path = sys.argv[1]

files_dict = {}
bugs = {}
key = 'M\t'
number_of_top_changeable_files = 500
output_file = 'files.csv'

git_history_command = f"cd {project_path}; git log --since=1.years --name-status"
process = subprocess.Popen(git_history_command, stdout=subprocess.PIPE, shell=True)
commit_history = process.communicate()[0].decode("utf-8")
commit_history = commit_history.split("\n")

for line in commit_history:
    if 'Date: ' in line:
        is_bug = False

    if ' bug' in line.lower():
        is_bug = True

    if key in line and ('.dart' in line or '.java' in line or '.swift' in line):
        filename = line.split(key)[1]
        files_dict[filename] = files_dict.get(filename, 0) + 1
        if is_bug:
            bugs[filename] = bugs.get(filename, 0) + 1

files = []

for k, v in files_dict.items():
    files.append((k, v, bugs.get(k, 0)))

files.sort(key=lambda x: -x[1])

sizes = []
for i, file in enumerate(files):
    try:
        file_size = os.path.getsize(project_path + file[0])
        sizes.append(file_size)
    except:
        file_size = 0
        # doesn't make sense to use zero size in median calculation

sizes.sort()

median = sizes[int(len(sizes)/2)]

with open(output_file, 'w') as file:
    headers = 'file name, commits count, bugs count, file size, median, xTimes bigger than median, ' \
              'metric = commits*bugs*bigger_than_median\n'
    file.write(headers)
    for i, file_metrics in enumerate(files):
        try:
            file_size = os.path.getsize(project_path + file_metrics[0])
        except:
            file_size = 0
        if i < number_of_top_changeable_files:
            bigger_than_median = file_size/median
            metric = file_metrics[1]*file_metrics[2]*bigger_than_median
            output_line = f'{file_metrics[0]}, {file_metrics[1]}, {file_metrics[2]}, {file_size}, {median}, ' \
                          f'{bigger_than_median}, {metric}'
            file.write(output_line + '\n')
            print(output_line)
