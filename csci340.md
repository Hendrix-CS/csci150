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
    loc: Bailey Computer Lab
    time: R 1:10pm - 4:00pm
    instructor: Dr. Brent Yorgey
    instemail: yorgey@hendrix.edu
    instweb: http://ozark.hendrix.edu/~yorgey
    instphone: (501) 450-1377
    officehours: https://byorgey.youcanbook.me
  - name: LAB 02
    loc: Bailey Computer Lab
    time: W 1:10pm - 4:00pm
    instructor: Dr. Mark Goadrich
    instemail: goadrich@hendrix.edu
    instweb: http://mark.goadrich.com
    instphone: (501) 450-1367
    officehours: http://mark.goadrich.com/schedule.html
resources:
  - name: Draw.io
    image: images/drawio.jpeg
    url: http://draw.io
  - name: Moqups
    image: images/moqups.jpg
    url: https://moqups.com/
  - name: Vertabelo
    image: images/vertabelo.jpg
    url: https://www.vertabelo.com/
  - name: SQLite
    image: images/sqlite.png
    url: https://www.sqlite.org/index.html
---

# Overview

A study of designing and using a database management system (DBMS) and of developing
Web applications. Topics include HTML, CSS, the JavaScript language, relational database
theory, techniques for supporting ACID properties, and frontiers in database research.
As part of a large team, students design and develop a system using both Web and mobile
front ends that interacts with a DBMS using SQL.

## Learning Goals

By the end of this course, you should be able to:
* model and capture database design, queries, and entity relationships in SQL
* design and construct a well-designed mobile-friendly Web application, incorporating HTML5, CSS, and JavaScript (with jQuery)
* use version control software
* style a blogging framework and publish entries
* utilize a web framework to access a backend database
* describe the basic theory and algorithms underlying implementation of database management systems

## Resources

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

We will be using no textbook but instead supplemental material such as
relevant web-pages for the course.
Readings will be assigned before material will be covered in class.  You are expected
to review the material and come to class prepared.  As readings are assigned,
they will be posted here.

<hr>

# Schedule

I have organized our course topics using a
[Gantt Chart](https://prod.teamgantt.com/gantt/schedule/?ids=1447720&public_keys=QL7w9J3pEbGs&zoom=d100&font_size=12&estimated_hours=0&assigned_resources=0&percent_complete=0&documents=0&comments=0&col_width=355&hide_header_tabs=0&menu_view=1&resource_filter=1&name_in_bar=0&name_next_to_bar=0&resource_names=1#user=&company=&custom=&date_filter=&hide_completed=false&color_filter=)
to help you see the timeline of activities and the
relationships between topics. This website also provides a
calendar view of these topics to help you organize your schedule
this semester.

<hr>

# Coursework

There will be three methods used to reinforce your mastery of the
course material: small individual labs to support the fundamentals of
web programming and SQL, group presentations to facilitate personal
discovery and information sharing, and a large term project to engage with
the course material in concert with a community partner.

## Labs: 20%

Some of your experience with databases in this course will be through semi-weekly labs.
* Lab 1: <a href="labs/lab1.html">Website Annotation</a> - Due Aug 30
* Lab 2: <a href="labs/lab2.html">HTML and CSS</a> - Due Sep 13
* Lab 3: <a href="labs/lab3.html">Jekyll Blog</a> - Due Sep 18
* Lab 4: <a href="labs/lab4.html">Jekyll Styling</a> - Due Sep 23
* Lab 5: <a href="labs/lab5.html">Data Modeling</a> - Due Sep 30
* Lab 6: <a href="labs/lab6.html">SQL Queries</a> - Due Oct 9
* Lab 7: <a href="labs/lab7.html">Javascript and jQuery</a> - Due Nov 1

## Presentations: 15%

You will be assigned [teams of three or four students](https://docs.google.com/spreadsheets/d/15ofyjJHfOBVLmj8EJh2_CeIy9-GFizrjHdcyS1fK3QY/edit?usp=sharing) and will be giving two presentations to the class as
described below.
* <a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Web_frameworks">Web Frameworks</a> - Oct 11, 14<br>
	<a href="https://docs.google.com/forms/d/e/1FAIpQLSe_tn7Yuo_o22aE62MqmcxKyMDM7FwCGjUDa4xhJ3zw_lVXWg/viewform?usp=sf_link">Presentation Rubric</a>
* <a href="https://en.wikipedia.org/wiki/Database_model">Alternate Database Models</a> - Nov 20, 22<br>
	<a href="https://docs.google.com/forms/d/e/1FAIpQLSelOrHz2JSkcqldojsD1UzwoBPUdMczz6LnRAUreVWZtO-KOw/viewform?usp=sf_link">Presentation Rubric</a>

Following each set of presentations, make a post to your Jekyll blog with your
impressions of each framework or model other than your own presentation. Please only
evaluate the frameworks or models and not the presentations on this public blog,
the presentations are evaluated privately through the Rubric links above.

## Project: 65%

For the bulk of this semester, you will be participating in teams of five or six to
develop a database and web application
in coordination with a local non-profit organization.

* [Project Description](project/project.html)

## Grading Scale

| Score  | Grade  |
|---|---|
| 90-100  | A  |
| 80-89  | B  |
| 70-79  | C  |
| 60-69  | D  |
| 0-59  | F  |
