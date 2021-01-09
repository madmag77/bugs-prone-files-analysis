# bugs-prone-files-analysis

In order to run the script type in a terminal:
`python main.py ~/Downloads/project_name/`

It prints 500 most frequently changed files and save this info as csv file (files.cvs).

The columns in the above cvs file are:
* file name (relative path of the file with code) 
* commits count (number of commits in the file during last year)
* bugs count (number of commits messages that contain pattern ` bug`)
* file size (code file size in bytes)
* median (median of all the code file sizes)
* xTimes bigger than median (`file size`/`median` in order to understand how big is the code file comparing to the median)
* metric (`commits*bugs*bigger_than_median` - so it's just simple product of 3 main parameters that can help to understand if the file is bugs prone or not)

Once you open csv file just sort it descending using the last column - `metric` and see what files are likely need refactoring.
