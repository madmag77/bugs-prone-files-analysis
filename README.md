# bugs-prone-files-analysis


## What is it?
The purpose of this code is to find `hot` files in your repository. `Hot` file means that in this file there is a high probability to meet a bug. 
What are the attributes that make those files `hot`?
* **Big file*s*. The bigger your file the more it errors prone because it most likely has many reasons to be changed and the logic inside is complex as it wasn't split. 
* **Frequenlty changing files**. Again, why these files are begin changed often? probably because they have a way many responsibilities or/and bugs that are being fixed.
* **Files with many authors**. The more people touch the file the more probability they introduce a bug (sure thing it's not always the case but still worth to check) 

So this script checks all the commits to your repo for 1 year and calculates the `hot` metric. The bigger the metric the more suspicios, `hot`, error-prone the file.

Some exceptions:
* DI files
* Autogenerated files
* Localisations
* Schemas, jsons and etc


## Looks good, how to run it?
In order to run the script type in a terminal:
`python main.py ~/Downloads/project_name/`

It prints 500 most frequently changed files and save this info as csv file (files.cvs).

The columns in the above cvs file are:
* file name (relative path of the file with code) 
* commits count (number of commits in the file during last year)
* bugs count (number of commits messages that contain pattern ` bug`)
* authors (number of authors which change the file)
* file size (code file size in bytes)
* median (median of all the code file sizes)
* xTimes bigger than median (`file size`/`median` in order to understand how big is the code file comparing to the median)
* metric (`commits*(bugs+1)*bigger_than_median` - so it's just simple product of 3 main parameters that can help to understand if the file is bugs prone or not)

Once you open csv file just sort it descending using the last column - `metric` and see what files are likely need refactoring.


## Hm, what about opensource project as a sample?
For instance, let's analyze https://github.com/TelegramMessenger/Telegram-iOS repository using this script. These are first 3 lines sorted by last column: 

| file name        | commits count           | bugs count  | authors | file size | median | xTimes bigger than median | metric = commits*(bugs + 1)*bigger_than_median |
| ------------- |----- | ----- | ----- | ----- | ----- | ----- | ----- |
| submodules/TelegramUI/Sources/ChatController.swift | 211 | 1 | 2 | 670211 | 11810 | 56.7 | 23948.2 |
| submodules/TelegramApi/Sources/Api1.swift | 83 | 1 | 2 | 1097420 | 11810 | 92.9 | 15425.2 |
| submodules/TelegramPresentationData/Sources/PresentationStrings.swift | 163 | 1 | 2 | 421412 | 11810 | 35.68 | 11632.5 |

We can see that `ChatController.swift` is being changed very often almost every working day there is a commit to this file and considering it's size 670k (or 11k lines of code!) we can assume that probability of introducing bugs is rather high for this file. The second item is file with API and it seems to me it could be autogenerated so we can skip it as well as the third one which is autogenerated too.
