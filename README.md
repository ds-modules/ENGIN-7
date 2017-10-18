# Engineering 7 in Python Notebooks

## UCB Interact Links

- [Lab 1](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab01/staff.ipynb)
- [Lab 2](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab02/staff.ipynb)
- [Lab 3](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab03/staff.ipynb)
- [Lab 4](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab04/staff.ipynb)
- [Lab 5](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab05/staff.ipynb)
- [Lab 6](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab06/staff.ipynb)
- [Lab 7](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab07/staff.ipynb)
- [Lab 8](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab08/staff.ipynb)
- [Lab 9](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab09/staff.ipynb)
- [Lab 10](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab10/staff.ipynb)
- [Lab 11](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab11/staff.ipynb)
- [Lab 12](http://datahub.berkeley.edu/user-redirect/interact?account=ds-modules&repo=ENGIN-7&branch=master&path=Lab12/staff.ipynb)

---

This project is a proof of concept to convert the assignments of the Berkeley Engineering 7 course, which is currently taught in MATLAB, into a series of Jupyter Notebooks. Engineering 7 is a freshman-level introduction to programming for scientists and engineering students.

Our goal is to revamp the course materials to be fully python based, so that new students will have a more interactive and intutive experience in an open-source language. With Jupyter notebooks, students do not need to worry about the scaffolding of creating seperate files for every function, and can read and solve problems directly in one place. Instead, they can focus on learning the fundamentals of programming and writing the actual code itself, all managed in one place. Python and Jupyter Notebooks are also open-source and free to use, and also more extendable to future computer science and coding projects compared to MATLAB. For data science purposes, Jupyter notebooks are incredibly convient, as they support rendering of visuals directly in the notebook, which can be updated along with code.


## Structure

The repo is split between the 2016 and 2017 ENGIN-7 assignments, and currently we are focused on finishing the 2016 version. The raw python code is created in PyCharm, so the folders is structued for that IDE. Each lab will contain the MATLAB problems in PDF, some MATLAB helper files, a .py file with raw python solutions, and a .ipynb file that will be the completed notebook.


## Current Progress
- [x] 2016
	- [x] Converting the MATLAB assignments into raw python code
		- [x] Lab 1
		- [x] Lab 2
		- [x] Lab 3
		- [x] Lab 4
		- [x] Lab 5
		- [x] Lab 6
		- [x] Lab 7
		- [x] Lab 8
		- [x] Lab 9
		- [x] Lab 10
		- [x] Lab 11
		- [x] Lab 12 (12, 2.2 cutoff)
	- [x] Translating the MATLAB PDF assignments into markdown and LaTeX in the Jupyter notebook
		- [x] Lab 1
		- [x] Lab 2
		- [x] Lab 3
		- [x] Lab 4
		- [x] Lab 5
		- [x] Lab 6
		- [x] Lab 7
		- [x] Lab 8
		- [x] Lab 9
		- [x] Lab 10
		- [x] Lab 11
		- [x] Lab 12
	- [x] Finishing soluton notebooks with finished python code
		- [x] Lab 1
		- [x] Lab 2
		- [x] Lab 3
		- [x] Lab 4
		- [x] Lab 5
		- [x] Lab 6
		- [x] Lab 7
		- [x] Lab 8
		- [x] Lab 9
		- [x] Lab 10
		- [x] Lab 11
		- [x] Lab 12 (12, 2.2 cutoff)

## Wish List
- [ ] Writing autograders for each notebook with Python `unittest`s
- [ ] Convert `.mat` data files to `.csv`
- [ ] Polishing the notebooks and creating student notebooks
	- Replace markdown pictures with html, and make nice captions
	- replace vectors with `\mathbf{}` font
	- fix wording for lists/vectors/arrays
	- make sure MATLAB remnants are replaced with python
		- especially headers
	- add equation numbers where needed
	- update bigo to `\mathcal{O}`
	- space equation numbers using \qquad\qquad
	- how to deal with classes

- [ ] 2017
	- Development halted for now.


## Developers
Daniel Ho, Adam Sequoia, Jack Zhang, Robert Sweeney
