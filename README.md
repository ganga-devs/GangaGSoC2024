# Challenge for Ganga projects in GSoC 2022

The challenge that forms part of the Ganga projects in GSoC is divided up into two pieces.

1) A part that demonstrates a basic proficiency in Ganga and the ability to work with Python
2) A part the demonstrates how you can work with the tools required for concurrency and asynchronous code

## Setup
Following the steps below will ensure that you can work freely on your project, can submit code through pushing it to GitHub but at the same time keep it private. Please avoid making your repository public as we want each student to work on this independently.

- Create a duplicate of the repository following the instructions at https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository . Then make that duplicate private. Please do not make a normal fork as that will then prevent you from making the repository private.
- Give the GitHub users `egede`, `alexanderrichards`, `mesmith75` access to your repository as collaborators.

For performing actual work for the challenge, we suggest something like

```bash
python3 -m venv GSoC
cd GSoC/
. bin/activate
python -m pip install --upgrade pip wheel setuptools
python -m pip install -e git+https://github.com/YOUR-GITHUB-USERNAME-HERE/GangaGSoC2022#egg=gangagsoc
```

Through the dependency, this will install Ganga as well, such that you can work with it directly inside the virtualenv. Please note that while the Ganga code is all python3, there are a few of the wrapper scripts that are still in python2. So you will need to have a working python2 installation available on your system. Also note that Ganga will only work on linux/unix like systems.

## Communication

Communication is an important part of working in GSoC. We use the CERN Mattermost server for instant messaging about the project. Please
- Create a CERN external account by following the instructions at https://account.cern.ch/account/externals/
- Follow the link https://mattermost.web.cern.ch/signup_user_complete/?id=6t4p1zptyp8pdn6ptore9ex9hw to
  join the Ganga Team in MatterMost. You can install MatterMost as an application, or you can just use it inside your browser.
- When you have joined the Ganga Team, please join the GSoC2022 channel at https://mattermost.web.cern.ch/ganga/channels/gsoc2022.
- Introduce yourself with a few words to the channel.

It is by far the best if most communication is public in the MatterMost channel, but you can also instant message Ulrik (@egede) for more specific issues. Please do not post solutions to the challenge to the channel but you are welcome to discuss issues regarding the challenge.

## Completing challenge

To complete the challenge you should push everything to the main branch of your forked repository. Then please send an email to us that you have finished. In the repository, we expect
- That the `setup.py` file is updated with any extra `python` package dependencies that you may have introduced.
- That there is a file `PROJECT.md` that documents what you have done and how we can test it. You can also include images or short screen grabbed movies that illustrate the functionality.
- Add a file CV.pdf that cotains your CV.
- That you have implemented tests of the code that can be tested with `unittest` to illustrate that everything works as expected. Tests should be placed in the directory `test` and have self-explaining names.

## Ganga initial task

Start by performing this task.

1) Demonstrate that you can run a simple `Hello World` Ganga job that executes on a `Local` backend.
2) Create a job in Ganga that demonstrates splitting a job into multiple pieces and then collates the results at the end.
  - Use the included file `LHC.pdf`.
  - Create a job in Ganga that in python (or through using system calls) split the pdf file into individual pages. 
  - Create a a second job in Ganga that will count the number of occurences of the word "it" in the text of the PDF file. It should be counted whether it is capitalised or not. Make sure not to count other words that have the letters "it" inside them. So "It is best when it uses Ganga" should have a count of two, while "The initial test did no work" should have a count of zero.
  - Using the `ArgSplitter` create subjobs that each will count the occurences for a single page.
  - Create a merger that adds up the number extracted from each page and places the total number into a file.
 3) Create test cases that demonstrate what you have done and that it is working. In the `test` directory you will find an example of a trivial test. All tests can be executed by `python -m unittest` when executed from the `src/gangagsoc` directory`. To make tests that include Ganga objects, be inspired by tests in `ganga/GangaCore/test/GPI`.

## Concurrency handling

1) Using docker, set up (a) virtual server(s) that can host an `HTCondor` batch sytem. Be inspired by the [HTCondor QuickStart guide](https://htcondor.readthedocs.io/en/latest/getting-htcondor/admin-quick-start.html).
2) Demonstrate that you can submit jobs from the command line of the host machine to this batch system.
3) Show that you can submit jobs from Ganga to this batch system using the `Condor` backend.
4) Develop a way to measure the average time it takes for Ganga to submit the job to Condor, the time it takes for Condor to start the job if the batch queue is empty and the time it takes before Ganga discover that the job has finished. The `time` attribute of completed jobs might be useful for this. 
