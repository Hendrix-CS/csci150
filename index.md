---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: course-multi
---

# <a name="description">Overview</a>

{{ site.description }}

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

{% include resources.html content=site.resources %}

## <a name="additional-resources">Optional Resources</a>

{% include resources.html content=site.extra-resources %}

<hr>

# <a name="inclasscode">Lecture Schedule</a>

When we write code together in class, it will be posted here!

| Date | Topic | Code |
|:----:|------||-----||
| F 21 Aug | Intro to Python ||
| M 24 Aug | Variables, Types, Functions, Math ||
| W 26 Aug | Booleans ||
| F 28 Aug | Conditionals ||
| M 31 Aug | Tracing ||
| W  2 Sep | Information Encoding ||
| F  4 Sep | Information Encoding ||
| M  7 Sep | Project 1 Overview ||
| W  9 Sep | Exam I Review ||
| F 11 Sep | Exam I ||
| M 14 Sep | PyCharm and While Loops ||
| W 16 Sep | Function Stack Tracing and Collatz ||
| F 18 Sep | Project 1 Workshop ||
| M 21 Sep | Project 1 Workshop ||
| W 23 Sep | Strings: Slicing and Concatenating ||
| F 25 Sep | More Strings ||
| M 28 Sep | Lists I ||
| W 30 Sep | Lists II ||
| F  2 Oct | Lists III ||
| M  5 Oct | For Loops I ||
| W  7 Oct | For Loops II ||
| F  9 Oct | Project 2 Overview ||
| M 12 Oct | Exam 2 Review || 
| W 14 Oct | Exam 2 ||
| F 16 Oct | Functional Abstraction ||
| M 19 Oct | Dictionaries I ||
| W 21 Oct | File I/O ||
| F 23 Oct | Dictionaries II ||
| M 26 Oct | Classes and Objects I ||
| W 28 Oct | Classes and Objects II ||
| F 30 Oct | Classes and Objects III ||
| M  2 Nov | Animation I ||
| W  4 Nov | Animation II ||
| F  6 Nov | Data Abstraction ||
| M  9 Nov | Recursion I ||
| W 11 Nov | Recursion II ||
| F 13 Nov | Project 3 Overview ||
| M 16 Nov | Exam 3 Review ||
| W 18 Nov | Exam 3 ||
| F 20 Nov | Designing Larger Programs ||
| M 23 Nov | Concluding Thoughts ||


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

## <a name="hwqz">Quizzes</a>: 140 points
Most class periods featuring new material will end with a quiz. Some quizzes will be adminstered via <a href="https://moodle.hendrix.edu/">Moodle</a>, 
while others will be coding assignments using <a href="https://codingbat.com/python">CodingBat</a>. Each quiz is worth 5 points, and must be completed by 5 pm of that class day.

## <a name="participation">Participation</a>: 110 points
Participation points will be assigned as follows:
* Each student is required to have a one-on-one meeting with the instructor 4 times per semester. Scheduling and following through on each meeting is worth 10 points/meeting.
* Each student is expected to meet multiple times during each of the 14 lab periods with the instructor and TA. Following through on all lab meetings for a given lab is worth 5 points.
* Asking the instructor a question during lecture earns 1 extra credit point. (Maximum 1/day)

## <a name="labs">Labs</a>: 220 points

<div style="text-align: center">
<a class="btn btn-primary" href="https://moodle.hendrix.edu/">
  Lab submission (moodle.hendrix.edu)
</a>
</div>
<br/>

| #  | Name | Assigned | Due |
|:--:|-----||:--------:|:---:|
|1 | [Kepler and Newton](https://www.kaggle.com/gabrielferrer/kepler-and-newton) | Aug 26-27 | Sep 2-3 |
|2 | [Diagnosing Heart Disease](https://www.kaggle.com/gabrielferrer/diagnosing-heart-disease) | Sep 2-3 | Sep 9-10 |
|3 | [This Day in History](https://www.kaggle.com/gabrielferrer/this-day-in-history) | Sep 9-10 | Sep 16-17 |
|4 | [Guess My Number]({{site.baseurl}}/labs/guess.html) | Sep 16-17 | Sep 25 |
|5 | [Mutation is the Word]({{site.baseurl}}/labs/doublets.html) | Sep 23-24 | Sep 30-Oct 1 |
|6 | [Todo Manager]({{site.baseurl}}/labs/todo-manager.html) | Sep 30-Oct 1 | Oct 7-8 |
|7 | [Caesar’s Secrets](https://www.kaggle.com/gabrielferrer/caesar-s-secrets) | Oct 7-8 | Oct 14-15 |
|8 | [Project 2 Workshop] | Oct 14-15 | Oct 23 |
|9 | [Sentiment Analysis](https://www.kaggle.com/gabrielferrer/sentiment-analysis) | Oct 21-22 | Oct 28-29 |
|10| [Water Jugs]({{site.baseurl}}/labs/waterjug.html) | Oct 28-29 | Nov 4-5 |
|11| [Graphics and Animation]({{site.baseurl}}/labs/pygame.html) | Nov 4-5 | Nov 11-12 |

<!--
|12| [Enron's Secrets] | Nov 11-12 | Nov 18-19 |
|13| [Project 3 Workshop] | Nov 18-19 | Dec 7 |
-->

Much of your experience with programming in this course will be through weekly labs. Each lab will be assigned in lab with time allotted to work through the materials, and will be due **by the start of the following lab**. All labs are weighted equally within the lab portion of your final grade.

<!--On these labs, you will work with a partner on the lab assignments. Their name must be listed on any code you hand in as joint work. A partnership should only turn in a **single copy** of the assignment. If students working as partners wish to turn in a lab late, both students must use a late day.-->
On these labs, you will work with a partner on the lab assignments. Their name must be listed on any code you hand in as joint work. Each partner should **submit their own solution** to the assignment.

**Lab attendance is required**. For this semester, labs will meet virtually online in Microsoft Teams. <!--Labs take place in the **Snoddy Computer Lab**, in the Bailey Library. As you go through the exterior door of the library, turn immediately to your left and enter the Snoddy Academic Resource Center. Continue through the door at the far end of the hall into the first computer lab, and then enter the second lab at the back.-->

## <a name="projects">Projects</a>: 350 points

| #  | Name | Points | Assigned | Due |
|:--:|-----||:------:|:--------:|:---:|
|1 | [Civic Assistance Q/A System](https://www.kaggle.com/gabrielferrer/project-1)  | 50  | Sep 7 | Sep 25 |
|2 | [Word Games]({{site.baseurl}}/projects/project2.html) | 100 | Oct 9 | Oct 23 |
|3 | [Final Project]({{site.baseurl}}/projects/final_spring2020.html) | 200 | Nov 13 | Dec 7 |

[Project 3 Design Rubric](https://drive.google.com/open?id=13kDzy15b63Ibytd23pBZ_nQqiKLSfxEs)

[Project 3 Final Rubric](https://drive.google.com/open?id=1rASxQnFIQtA9l62bSoRigYzq5Z57_7um)

You will have three projects in this course. These projects will cover concepts we have discussed in class and in labs, and will be due approximately two to three weeks after they are assigned.

**You must work individually on the projects.** You may discuss concepts and ideas with your classmates, but the code you turn in must be your own. You will be graded not only on correctness, but also technique, documentation and evaluation of your solution. Further details on the grading standards and handin instructions for each project will be given when they are assigned.

## <a name="exams">Exams</a>: 180 points

There will be three in-class exams, the first worth 40 points and the second and
third worth 70 points. They will consist of short answer questions along with writing and debugging code.

* Exam 1: Sep 11, covering functions, math, numerical data, conditionals, and binary encoding  
* Exam 2: Oct 14, covering input/output, while loops, for loops, lists, and strings 
* Exam 3: Nov 18, covering dictionaries, classes and objects 

<!--
[Practice Exam 1](https://drive.google.com/open?id=1TucpuX2lwRqQ4d1y3QMO5ad9gm7DqKwt)
[Practice Exam 2](https://drive.google.com/open?id=199t6fRH6k7h6cuxvzyZUrlSf0IcGgkX4)
[Practice Exam 3](https://drive.google.com/open?id=19x3xRhRSXLz0qEw153hhjdhFL4P5kRbw)
-->

There is no final exam; you will complete a final project instead, as described above under Projects.

## <a name="scale">Grading Scale</a>

| Score  | Grade  |
|:------:|:------:|
| 900-1000  | A   |
| 800-899   | B   |
| 700-799   | C   |
| 600-699   | D   |
| 0-599     | F   |
