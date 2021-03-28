# Challenge for Ganga projects in GSoC 2021

The challenge that forms part of the Ganga projects in GSoC is divided up into three pieces.

1) A part that everybody should attempt that demonstrates the ability to do a basic job in Ganga and work with python
2) A part that is related to the improved submission handling
3) A part that is specific to the GUI project where you will be required to create a webserver that can demonstrate its interaction with Ganga in a simple manner.

You are welcome to do all three parts, but if you are only interested in applying for the GUI project, you will not be disadvantaged by not attempting the one related to the persistent storage.

## Setup
Following the steps below will ensure that you can work freely on your project, can submit code through pushing it to GitHub but at the same time keep it private. Please avoid making your repository public as we want each student to work on this independently.

- Create a duplicate of the repository following the instructions at https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository . Then make that duplicate private. Please do not make a normal fork as that will then prevent you from making the repository private.
- Give the GitHub users `egede`, `alexanderrichards`, `mesmith75` access to your repository as collaborators.

For performing actual work for the challenge, we suggest something like

```bash
python3 -m venv GSoC
cd GSoC/
. bin/activate
python -m pip install --upgrade pip wheel
python -m pip install -e git+https://github.com/YOUR-GITHUB-USERNAME-HERE/GangaGSoC2021#egg=gangagsoc
```

Through the dependency, this will install Ganga as well, such that you can work with it directly inside the virtualenv. Please note that while the Ganga code is all python3, there are a few of the wrapper scripts that are still in python2. So you will need to have a working python2 installation available on your system. Also note that Ganga will only work on linux/unix like systems.

Communication is an important part of working in GSoC. Please just ask by email to all/any of the developers about anything that you are in doubt about. 

## Completing challenge

To complete the challenge you should push everything to the main branch of your forked repository. Then please send an email to us that you have finished. In the repository, we expect
- That the `setup.py` file is updated with any extra `python` package dependencies that you may have introduced.
- That there is a file `PROJECT.md` that documents what you have done and how we can test it. If you perform the GUI task below, make sure to include some images or short screen grabbed movies that illustrate the functionality.
- Add a file CV.pdf that cotains your CV.
- That you have implemented tests of the code that can be tested with `pytest` to illustrate that everything works as expected. Tests should be placed in the directory `test` and have self-explaining names.
- That anything (like interaction with GUI), that can not easily be made to work with `pytest` is fully explained.

## Ganga initial task

As stated above everybody should attempt to complete this task

1) Demonstrate that you can run a simple `Hello World` Ganga job that executes on a `Local` backend.
2) Create a job in Ganga that demonstrates splitting a job into multiple pieces and then collates the results at the end.
  - Use the included file `LHC.pdf`.
  - Create a job in Ganga that in python (or through using system calls) split the pdf file into individual pages. 
  - Create a a second job in Ganga that will count the number of occurences of the word "it" in the text of the PDF file. It should be counted whether it is capitalised or not. Make sure not to count other words that have the letters "it" inside them. So "It is best when it uses Ganga" should have a count of two, while "The initial test did no work" should have a count of zero.
  - Using the `ArgSplitter` create subjobs that each will count the occurences for a single page.
  - Create a merger that adds up the number extracted from each page and places the total number into a file.
  - Create test cases that demonstrate what you have done and that it is working. In the `test` directory you will find an example of a trivial test. All tests can be executed by `python -m unittest discover test "*.py"`, where `test` is the name of the directory. To make test that include Ganga objects, be inspired by tests in `ganga/GangaCore/test/GPI`.

## Submission handling

1) Using docker, set up (a) virtual server(s) that can host an `HTCondor` batch sytem. Be inspired by the [HTCondor QuickStart guide](https://htcondor.readthedocs.io/en/latest/getting-htcondor/admin-quick-start.html).
2) Demonstrate that you can submit jobs from the command line of the host machine to this batch system.
3) Show that you can submit jobs from Ganga to this batch system using the `Condor` backend.
4) Develop a way to measure the average time it takes for Ganga to submit the job to Condor, the time it takes for Condor to start the job if the batch queue is empty and the time it takes before Ganga discover that the job has finished. The `time` attribute of completed jobs might be useful for this. 


## Ganga GUI task
---

For this task we will not need to use the Ganga framework at all, you will need to show the following:

 - Ability to create a simple webserver using the Python based [`Flask`](https://flask.palletsprojects.com/en/1.1.x/) web framework
 - Have the webserver render dynamic content using the [`jinja2`](https://jinja.palletsprojects.com/en/2.11.x/) templating engine
 - Modify the server to allow updating of the content by making it a RESTful service.

(*__Note__ that the content for this task can be anything that you like and we would very much like to see you be as creative as possible with the actual design of the web page. The graphical design forms part of the challenge.*)
