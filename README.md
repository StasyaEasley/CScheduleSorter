# CS Schedule Sorter

This Python app, developed using the Tkinter library, is designed to assist Computer Science majors at the University of Arizona in sorting and planning their class schedules.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Files](#files)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)

## Introduction

The CS Schedule Sorter is a GUI app built using Tkinter. It helps in the planning of CS class schedules by guiding users through the selection of courses based on different types of classes. The pandas and BeautifulSoup libraries were also used to help wrangle data from the UA CS course catalogue's source code and effectively use that data in the application.


## Features
* Built and used with Python
* User-friendly interface with navigation buttons
* Real-time updates on course selections
* Clear visualization of curated plan for each user
* Descriptive information for each course

## Files

1. form.py

This file contains the main logic and design for the CS Schedule Sorter app. It uses the Tkinter library for the GUI. The program guides the user through different pages corresponding to different class types, in addition to saving the selections of users and using selections to direct users through the app.

2. merged_data.tsv

This file is a TSV file containing  information about each CS class, such as class code, title, description, etc. This data is used to display additional information when a user clicks on a specific class.

4. data_cs_courses.py

This file, using the libraries pandas and BeautifulSoup, creates the merged_data.tsv file by parsing an HTML file containing all of the CS course catalog information.

## Dependencies

- Python 3.11.5
- Tkinter (included in most Python installations)
- pandas

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/StasyaEasley/CScheduleSorter.git
   cd CScheduleSorter

