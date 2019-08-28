---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: course-multi
number: CSCI 150
title: Foundations of Computer Science
semester: Fall 2019
image: images/system-2457648_1920.jpg
offerings:
  - name: LECTURE 01
    loc: MCREY 110
    time: MWF 8:10am - 9:00am
    instructor: Dr. Brent Yorgey
    instemail: yorgey@hendrix.edu
    instweb: http://ozark.hendrix.edu/~yorgey
    instphone: (501) 450-1377
    officehours: https://byorgey.youcanbook.me
  - name: LECTURE 02
    loc: WAC 249 (2nd Floor)
    time: MWF 11:10am - 12:00pm
    instructor: Dr. Mark Goadrich
    instemail: goadrich@hendrix.edu
    instweb: http://mark.goadrich.com
    instphone: (501) 450-1367
    officehours: http://mark.goadrich.com/schedule.html
  - name: LAB 01
    loc: Snoddy Computer Lab
    time: R 1:10pm - 4:00pm
    instructor: Dr. Brent Yorgey
    instemail: yorgey@hendrix.edu
    instweb: http://ozark.hendrix.edu/~yorgey
    instphone: (501) 450-1377
    officehours: https://byorgey.youcanbook.me
  - name: LAB 02
    loc: Snoddy Computer Lab
    time: W 1:10pm - 4:00pm
    instructor: Dr. Mark Goadrich
    instemail: goadrich@hendrix.edu
    instweb: http://mark.goadrich.com
    instphone: (501) 450-1367
    officehours: http://mark.goadrich.com/schedule.html
resources:
  - name: Python 3
    image: assets/images/pythonlogo.png
    url: http://python.org
  - name: Azure Notebooks
    image: assets/images/azure.png
    url: https://notebooks.azure.com/
  - name: Pycharm
    image: assets/images/pycharmlogo.png
    url: https://www.jetbrains.com/pycharm/
  - name: repl.it
    image: assets/images/replit.png
    url: https://repl.it/
  - name: Python Tutor
    image: assets/images/python_tutor.png
    url: https://pythontutor.com/
---

# <a name="description">Overview</a>

Introduction to solving computational problems, including the fundamentals of computer programming. Topics include imperative programming constructs (variables, loops, conditionals, functions, recursion), basic object-oriented constructs (classes, objects), and some fundamental algorithms and data structures (dictionaries, arrays, linked lists). Student learn these concepts through studying the Python programming language.

## <a name="goals">Learning Goals</a>

Upon completing this course, our goal is for you to be able to:

* Build computer programs to:
  * Effectively solve realistic problems.
  * Organize, analyze, and summarize realistic data sets.
* Read, understand, and explain a computer program.
* Understand and explain computation through:
  * Thinking logically and precisely.
  * Making and testing hypotheses.
* Use modular components to decompose problems and assemble solutions.
* Create abstract, generalized models from specific, complex examples.

## <a name="resources">Resources</a>

<div class="row">
{% for res in page.resources %}
<div class="col-md-{{ 12 | divided_by: page.resources.size }}">
<img src="{{site.baseurl}}/{{ res.image }}" height="100" border="1">
<p>
<a href="{{ res.url }}">{{ res.name }}</a><br>
</p>
</div>
{% endfor %}
</div>

Please **do not bring laptops to lecture**. This may seem strange in a computer science class. But lab is the place where you will get plenty of experience working on the computer; lecture is a time for thinking and learning without the distraction of a computer.

Exceptions may be made on a case-by-case basis if you can prove to me that you really do benefit from using your laptop to take notes.

<hr>

# <a name="inclasscode">In-Class Code</a>

When we write code together in class, it will be posted here!

<hr>

# Coursework

Each student has **four late days** to spend throughout the semester as they wish.
Simply inform the instructor any time *prior* to the due date for an assignment
that you wish to use a late day; you may then turn in the assignment up to 24
hours late. Multiple late days may be used on the same assignment. There are no
partial late days; turning in an assignment 2 hours late or 20 hours late will
both use 1 late day. Note that late days are intended to cover both normal
circumstances (you simply want more time to work on the assignment) and
exceptional circumstances (you get sick, travel for a game or family
obligation, *etc.*). After you have used up your late days, late assignments
will receive at most half credit.

## <a name="hwqz">Homework and Quizzes</a>: 140 points

| #  | Name | Assigned | Due
|:-:|-||:-:|:-:|
|0 | [Info Sheet](https://docs.google.com/forms/d/e/1FAIpQLSdtxgmw2tL6IzzK0qq3Fw2h2FTFmGHoTRs8p6wTfTToUn7pZg/viewform?usp=sf_link) | Aug 28 | Aug 30 |
|1 | [Minecraft by hand]({{site.baseurl}}/homework/minecraft.html) | Aug 30 | Sep 2 |

There will often be short homework assignments to be completed over the weekend, assigned on Friday and due Wednesday, sometimes with a corresponding quiz at the beginning of class on Wednesday.


## <a name="labs">Labs</a>: 260 points

| #  | Name | Assigned | Due
|:-:|-||:-:|:-:|
|1 | [Minecraft Hour of Code]({{site.baseurl}}/labs/minecraft.html) | Aug 28-29 | Sep 4-5 |
|2 | [Kepler and Newton](https://notebooks.azure.com/goadrich/projects/kepler-vs-newton) | Sep 4-5 | ? |
|3 | [Diagnosing Heart Disease](https://notebooks.azure.com/goadrich/projects/heart-disease-lab) | Sep 11-12 | ? |
|4 | This Day in History | Sep 18-19 | ? |
|5 | [Guess My Number]({{site.baseurl}}/labs/guess.html) | Sep 25-26 | ? |
|6 | [Mutation is the Word]({{site.baseurl}}/labs/doublets.html) | Oct 2-3 | ? |
|7 | [Todo Manager]({{site.baseurl}}/labs/todo-manager.html) | Oct 9-10 | ? |
|8 | [Caesar’s Secrets](https://notebooks.azure.com/goadrich/projects/caesar-s-secrets) | Oct 23-24 | ? |
|9 | [Sentiment Analysis](https://notebooks.azure.com/goadrich/projects/sentiment-analysis) | Oct 30-31 | ? |
|10| [Water Jugs]({{site.baseurl}}/labs/waterjug.html) | Nov 6-7 | ? |
|11| [Graphics and Animation]({{site.baseurl}}/labs/graphics.html) | Nov 13-14 | ? |
|12| Enron’s Secrets | Nov 20-21 | ? |
|13| [On Stuckness and Debugging]({{site.baseurl}}/labs/debugging.html) | Dec 4-5 | ? |

Much of your experience with programming in this course will be through weekly labs. Each lab will be assigned Wednesday/Thursday in lab with time allotted to work through the materials, and will be due **by the start of the following lab**. All labs are weighted equally within the lab portion of your final grade.

On these labs, you will work with a partner on the lab assignments if you choose. Their name must be listed on any code you hand in as joint work. A partnership should only turn in a **single copy** of the assignment. If students working as partners wish to turn in a lab late, both students must use a late day.

**Lab attendance is required**. Labs take place in the **Snoddy Computer Lab**, in the Bailey Library. As you go through the exterior door of the library, turn immediately to your left and enter the Snoddy Academic Resource Center. Continue through the door at the far end of the hall into the first computer lab, and then enter the second lab at the back.

Labs should follow the [Python style guide](python_style_guide.html). You may use the automated style checker to help you catch common style errors.

For many of the labs, we will be using Azure Notebooks. Here are specific instructions
on how to get started with these notebooks.

* First, you will need to create a free Microsoft Azure Notebook
  account. [Visit this webpage to start the process](https://notebooks.azure.com/).

* Click on the <kbd>Sign in</kbd> text in the upper-right corner of the
  page. Log in with your Hendrix email account and password.

* Next, the specific lab for the week, and click on the green <kbd>Clone</kbd> button in the
  upper-right corner of the screen.

* This should make a copy of the project for you in your projects
  folder. Now click on <kbd>My Projects</kbd> and the "Civic Hacking Lab"
  section.

* In your copy of the project, click on the `.ipynb`
  file in the project listing. This should open the
  notebook in the Azure Jupyter system in a separate browser tab, and
  you can start editing the file with your code. Follow the
  instructions in the file to complete this lab.

* You can save your progress using <kbd>Ctrl-S</kbd> or <kbd>Cmd-S</kbd>, and then
  return to this file any time.

* To submit your file for grading when you are finished, return to
  the lab folder listing in the <kbd>My Projects</kbd>
  tab. Select the circle to the left of the `.ipynb` file.
  Then, click on the down arrow icon in the menu, to
  the left of the trash can icon.  This will allow you to download
  the file onto your computer; then you can upload it using the
  usual turnin form.

## <a name="projects">Projects</a>: 350 points

| #  | Name | Points | Assigned | Due
|:-:|-||:-:|:-:|:-:|
|1 | ? | 50  | Sep 16 | Sep 30 |
|2 | ? | 100 | Oct 14 | Nov 1 |
|3 | ? | 200 | Nov 18 | Final Exam Day |

You will have three projects in this course, one about every five weeks. These projects will cover concepts we have discussed in class and in labs, and will be due approximately one week after they are assigned.

**You must work individually on the first two projects.** You may discuss concepts and ideas with your classmates, but the code you turn in must be your own. You will be graded not only on correctness, but also technique, documentation and evaluation of your solution. Further details on the grading standards and handin instructions for each project will be given when they are assigned.

## <a name="exams">Exams</a>: 250 points

There will be three in-class exams, the first worth 50 points and the second and
third worth 100 of your final grade. They will consist of short answer
questions along with writing and debugging code.

* Exam 1: Sep 20, covering input/output, math, numerical data, conditionals, and binary encoding
* Exam 2: Oct 16, covering functions, while loops, lists, and strings
* Exam 3: Nov 25

There is no final exam; you will complete a final project instead, as described above under Projects.

## <a name="scale">Grading Scale</a>

| Score  | Grade  |
|:-:|:-:|
| 900-1000  | A  |
| 800-899  | B  |
| 700-799  | C  |
| 600-699  | D  |
| 0-599  | F  |