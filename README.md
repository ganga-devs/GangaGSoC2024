# Challenge for Ganga projects in GSoC 2023

The challenge that forms part of the Ganga projects in GSoC is divided up into two pieces.

1) A part that demonstrates a basic proficiency in Ganga and the ability to work with Python
2) A part the demonstrates how you can work with the tools required for interfacing Ganga with external code

## Setup
Following the steps below will ensure that you can work freely on your project, can submit code through pushing it to GitHub but at the same time keep it private. Please avoid making your repository public as we want each student to work on this independently.

- Create a duplicate of the repository following the [instructions](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository). Then make that duplicate private. Please do not make a normal fork as that will then prevent you from making the repository private.
- Give the GitHub users `egede`, `alexanderrichards`, `mesmith75` access to your repository as collaborators.

For performing actual work for the challenge you need to work within a linux environment. This can be either as a native linux machine, on a virtual machine or using WSL. Your python version should be python 3.8 or higher. To setup the working environment, we suggest to use a virtual environment in the follwing way:

```bash
python3 -m venv GSoC
cd GSoC/
. bin/activate
python -m pip install --upgrade pip wheel setuptools
python -m pip install -e git+https://github.com/YOUR-GITHUB-USERNAME-HERE/GangaGSoC2023#egg=gangagsoc
```

Through the dependency, this will install Ganga as well, such that you can work with it directly inside the virtualenv.

## Communication

Communication is an important part of working in GSoC. We use the CERN Mattermost server for instant messaging about the project. Please
- Create a CERN external account by following the [instructions](https://account.cern.ch/account/externals/)
- Follow [the link](https://mattermost.web.cern.ch/signup_user_complete/?id=6t4p1zptyp8pdn6ptore9ex9hw) to
  join the Ganga Team in MatterMost. You can install MatterMost as an application, or you can just use it inside your browser.
- When you have joined the Ganga Team, please join the [GSoC2023 channel](https://mattermost.web.cern.ch/ganga/channels/gsoc2023).
- Introduce yourself with a few words to the channel.

It is by far the best if most communication is public in the MatterMost channel, but you can also instant message @egede, @masmith and @arichard for more specific issues. Please do not post solutions to the challenge to the public channel but you are welcome to discuss issues regarding the challenge.

## Completing challenge

To complete the challenge you should push everything to the main branch of your forked repository. In the repository, we expect
- That the [setup.py](setup.py) file is updated with any extra `python` package dependencies that you may have introduced.
- Update the file [PROJECT.md](PROJECT.md) to document what you have done and how we can test it. You can also include images or short screen grabbed movies that illustrate functionality.
- Add a file CV.pdf that contains your CV.
- That you have implemented tests of the code that can be tested with running `python -m unittest` to illustrate that everything works as expected. Tests should be placed in the directory `test` and have self-explaining names.

## Ganga initial task

Start by performing this task.

1) Demonstrate that you can run a simple `Hello World` Ganga job that executes on a `Local` backend.
2) Create a job in Ganga that demonstrates splitting a job into multiple pieces and then collates the results at the end.
  - Use the included file `LHC.pdf`.
  - Create a job in Ganga that in python (or through using system calls) split the pdf file into individual pages. 
  - Create a a second job in Ganga that will count the number of occurences of the word "it" in the text of the PDF file. It should be counted whether it is capitalised or not. Make sure not to count other words that have the letters "it" inside them. So "It is best when it uses Ganga" should have a count of two, while "The initial test did no work" should have a count of zero.
  - Using the `ArgSplitter` create subjobs that each will count the occurences for a single page.
  - Create a merger that adds up the number extracted from each page and places the total number into a file.
 3) Create test cases that demonstrate what you have done and that it is working. In the `test` directory you will find an example of a trivial test. All tests can be executed by `python -m unittest` when executed from the `gangagsoc` directory. To make tests that include Ganga objects, be inspired by tests in [existing tests](https://github.com/ganga-devs/ganga/blob/develop/ganga/GangaCore/test/GPI/TestArgSplitter.py). Note the use of `sleep_until_completed`.

## Interfacing Ganga

The purpose of this challenge is to illustrate that you can think about what it will require to interface Ganga and the Snakemake system. 

1) Install [Snakemake](https://snakemake.readthedocs.io/) by making it a dependency of your GSoC project. Once installed, you might want to work yourself through the [short tutorial](https://snakemake.readthedocs.io/en/stable/tutorial/short.html) to get the general idea of how it works.
2) Write a `Snakefile` that will execute your ganga job that you used for counting words above. The `input` to your `rule all` should be the file that your script writes with the number of words. Remember that you can execute a script in Ganga from the shell as `ganga script.py`. You probably want to use `sleep_until_completed` again to make your script block the execution flow until the Ganga job has finished.
3) Try to implement a solution where you are not using `sleep_until_completed` and the script starting the Ganga job is simply starting it but finish without producingthe output file. This should make `snakemake` fail as the output is not produced. Now implement a way such that you can run `snakemake` a bit later. If the Ganga job has not finished yet, Snakemake should not start a new Ganga job, but simply fail again. If on the other hand the Ganga job has finished, snakemake should carry on as the output is now produced. You might need to introduce some artificial delay in your Ganga job to test this. This last bit might seems artificial but it is not unusual that Ganga jobs can take many hours or indeed days to finish.

## Feedback on challenge
You are welcome to seek feedback on your solution to the challenges while they are still work in progress. For feedback PM @egede, @masmith and @arichard in MatterMost. Make sure that you have given access in Github to us as directed above.

## Submission
When you are ready to submit, then please use the [Google form](https://docs.google.com/forms/d/e/1FAIpQLScCrQBFrm0auXYJqKuzDGkjoHdj-fV7hvo_TKBc85nJpIIY1A/viewform) to let us know.
