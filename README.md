# **NIGERIAN PENSION ADVISER**

![Site Mockup](/readme-docs/mockup.png)

## **Live Site**

[Hosted Live Here](https://pension-adviser.onrender.com)

## **Repository**

[View Repository Here](https://github.com/Polyanyanwu/pension-adviser-pp3)

## **Table of Contents**
- [**NIGERIAN PENSION ADVISER**](#nigerian-pension-adviser)
  - [**Live Site**](#live-site)
  - [**Repository**](#repository)
  - [**Table of Contents**](#table-of-contents)
  - [**Objective**](#objective)
  - [**Aims of the Site**](#aims-of-the-site)
  - [**User Experience Design**](#user-experience-design)
    - [**User Stories**](#user-stories)
    - [**Initial Design Concept**](#initial-design-concept)
      - [**Wireframe**](#wireframe)
      - [**Color Scheme**](#color-scheme)
      - [**Fonts**](#fonts)
      - [**Background Image**](#background-image)
      - [**Flowchart**](#flowchart)
  - [**Features**](#features)
    - [*Go through the Instructions*](#go-through-the-instructions)
    - [*Print existing result of enquiries*](#print-existing-result-of-enquiries)
    - [*Run new enquiry*](#run-new-enquiry)
    - [*Delete all existing enquiry results*](#delete-all-existing-enquiry-results)
  - [**Future Features**](#future-features)
  - [**Data Model**](#data-model)
  - [**Technologies Used**](#technologies-used)
    - [**Python Libraries**](#python-libraries)
    - [**Ancillary Technologies**](#ancillary-technologies)
    - [**VSCode Extensions Used**](#vscode-extensions-used)
  - [**Testing**](#testing)
    - [**PEP8 Testing**](#pep8-testing)
    - [**Python Testing during Development**](#python-testing-during-development)
    - [**Manual Testing**](#manual-testing)
    - [**HTML W3C Validator**](#html-w3c-validator)
      - [**HTML Validation Outcome**](#html-validation-outcome)
      - [**CSS Validation Outcome**](#css-validation-outcome)
    - [**Lighthouse**](#lighthouse)
  - [**Bugs**](#bugs)
    - [**Current Bugs**](#current-bugs)
    - [**Resolved Bugs**](#resolved-bugs)
  - [**Deployment**](#deployment)
  - [**Credits**](#credits)
    - [**Content**](#content)
    - [**Code**](#code)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

## **Objective**

Design and deploy an interactive Command Line (CLI) application that enables the user to gain insight into the performance rates of returns of Pension Fund Administrators (PFA) published by the National Pension Commission [PenCom](http:\\www.pencom.gov.ng) of Nigeria . This will assist contributors in the pension fund make informed decision on which PFA to chose as their retirement savings account fund manager based on performance rates of return over a period. The project shall be deployed through Heroku, run on a command line and programmed using Python.

The Nigerian pension industry permits contributors to change their PFA once in a year. It becomes necessary to analyse performance data published by the PenCom to make it easy for the user to quickly know which PFAs are best performing in terms of rate of returns on investment.

## **Aims of the Site**

The aim of this site is to provide an interactive application to enable the user to obtain information on PFA performance on any of the funds in the Nigerian pension industry. When completed the final product should:

- Enable the user chose the fund type of interest
- Obtain data on PFA performance on the chosen fund
- Obtain industry average performance on a chosen fund type for a given year
- Be programmatically error free
- Be written using Python
- Check all input errors and handle them gracefully with appropriate messages to the user
- Educate the user regarding use of the application and validity of inputs
- If any task is likely to last more than a second, provide a feedback to the user on what the application is doing.

## **User Experience Design**

### **User Stories**

The user stories that will guide the development of this application include:

1. As a contributor in the pension industry in Nigeria I like to know the performance of each retirement savings account fund type for a fund manager (PFA) of my interest to enable me decide to change my fund type or the fund manager.
2. As a citizen interested in the economic growth of Nigeria I like to know the pension industry performance over a given period and fund type.
3. As a user of the application I like to view my previous enquiries.

### **Initial Design Concept**

My intention is to guide the contributor in the pension industry in Nigeria to easily find out which PFAs are best performing in terms of returns on investment. This will be achieved by analyzing the data that PenCom (the regulator of the industry) posted on its website. It is a simple design that would ask the user the PFA and fund of interest and reply with the performance of that PFA plus the industry performance. It will also produce which PFA has the best performance for a given fund. I intend to give the user the option to select the period of interest, that is starting year and ending year for the analysis. Since the data available is limited, the user will be guided on the years that are available.

#### **Wireframe**

The application is of a Command Line type with limitations on the width and height of the interaction area. Therefore, the Wirframe is a simple one as given below:

![Application Wireframe](/readme-docs/pp3_wireframe.png)

#### **Color Scheme**

In order to enhance the user experience within the Python terminal, I chose to apply some colors available through the color escape codes of Python. I implemented a module that has functions for the colors I used in the application.

For the look and feel of the surrounding areas of the Python terminal, I chose a color scheme through the [Colors.co](https://coolors.co/). The color palette used is shown below:

![Color Pallet](/readme-docs/color_scheme.png)

#### **Fonts**

The font for the Title is "Press Start 2P", which was chosen from Google fonts. This font looks classic to me and fitting for a Command Line application of this nature.

#### **Background Image**

The background image was downloaded from [PngTree](https://pngtree.com/free-backgrounds). It contains an image of someone using a laptop and different sizes of up arrow. These invoke feelings of an investment adviser and growth of funds, which I consider apt for this application.

#### **Flowchart**

The initial flowchart of the application has been produced to guide the application development. It may differ slightly from the final application as more insights may be gathered as the application is being developed.

![Application Flowchart](/readme-docs/pension_adviser_flowchart.png)

## **Features**

***I like to know the performance of each retirement savings account fund type for a fund manager.***

***As a citizen interested in the economic growth of Nigeria I like to know the pension industry performance over a given period and fund type***

To achieve these User stories the application shall request the fund type, start and end year of interest and PFA. If the PFA is not chosen, as is the case with second User Story above, only the industry average performance for the Fund type is computed and displayed. The application shall display the performance of the selected PFA, the industry average performance for the fund type chosen and the best fund manager for the fund type.

***As a user of the application I like to view my previous enquiries.***

To achieve this requirement it is necessary to input a user name and persist the result of the user enquiries to be able to retrieve them subsequently.

The above requirements led to the design of the main menu of the application given below:

![Application Main Menu](/readme-docs/main_menu.png)

Before the menu is displayed, the user is prompted to enter a user name. A user name is mandatory as it is used by the application as the name of the Worksheet to be used in saving the results of the user enquiries. If same user name is provided as an existing one, the user is requested to confirm if he/she is a returning user. If not returning, another name is requested from the user. The user name is not case sensitive, is required to be alphanumeric, between 3 and 15 characters and is not a profane word.

When a user inputs an option 1, 2, 3, 4 or 9 the user is requested to input the choice a second time to confirm. If the confirmation is same as the initial input, the option is accepted and the desired feature is executed. If the confirmation fails, the menu is displayed once more.

### *Go through the Instructions*

This option, when confirmed by the user, displays the instructions for using the application.

![Instructions](/readme-docs/go_thru_instructions.png)

The instructions are displayed in sets of 5 lines. The user is prompted to press any key to continue to see the next set of instructions. At the end of the instructions, the user is requested to repeat the instructions or not. If not repeating, the menu is displayed once more.

### *Print existing result of enquiries*

This feature enables the user to retrieve and view the previous result of enquiries made on the application. This is used for both the enquiries made during the current user session or enquiries made previously provided the same user name is used.

![Enquiry Results](/readme-docs/enquiry_result.png)

The application uses the `set` feature of Python to ensure that no enquiry result item is saved more than once in the Worksheet of the user. The data is static and historical, thus not expected to change over time.

### *Run new enquiry*

The Run new enquiry feature is selected by typing 3 when the menu is displayed. This is the main feature that enables the user input the fund type of interest, the start and end year, the PFA of interest before the enquiry result is displayed.

![Select Fund Type](/readme-docs/select_fund.png)

After selecting a fund type, the user is presented with prompts for the start and end years. The performance data for the PFAs are stored per fund type and year. The application goes through the data and determines the available year range of data displayed to the user. The user input is validated against the valid years displayed.

![Select Year](/readme-docs/select_year.png)

The PFA is displayed including the option 0 for No PFA. The instruction includes n for next set of PFAs and p for previous set of PFAs. The application ensures the p and n are available only when useful, e.g for the first set of PFAs the p is not available.

![Select PFA](/readme-docs/select_pfa.png)

After selecting a PFA or No PFA, the application displays the result of the enquiry and a message for saving the enquiry result. A success or failure message is displayed afterwards.

![Save enquiry](/readme-docs/save_enquiry.png)

### *Delete all existing enquiry results*

A user may decide to delete all previous enquiries made on the application by selecting option 4. The application will proceed and clear all the enquiries saved on the user's Worksheet.

![Delete Enquiries](/readme-docs/delete_enquiry.png)

Message is displayed at the starting of the deletion and after successful deletion or otherwise. If there are no enquiry results to delete, the user is notified.

## **Future Features**

- Implement a password to ensure returning user is same person
- Addition of new data for subsequent years from the application instead of directly on the Google sheet
  
## **Data Model**

As at the commencement of this application design on 10 January, 2022 the regulator of the Pension industry in Nigeria (PenCom) had published performance data (rates of return on investment) for its 22 licensed PFAs between 2016 and 2019.

![Performance Data from PenCom](/readme-docs/pfa_performance_from_pencom.png)

From the data available I had to produce a workbook with two Excel sheets that would be hosted at Google sheets.
The first Excel sheet contains the serial number of the PFAs which will server as the ID, the abbreviated name and the full names. This will enable me display meaningful prompts to the user when selecting a PFA.

![PFA IDs](/readme-docs/pfa_names.png)

The second Excel Sheet contains data for each PFA, Fund type, Year and the return rate. The structure of this Excel sheet will enable me add more rows for performance data for 2020 or any subsequent years when they become available from the PenCom. Also the structure enables the use of Python to query the data in an efficient manner and produce either averages for a PFA and Fund type or for the entire pension industry.

![Performance Data Model for Computation](/readme-docs/return-rates.png)

In this model when additional data becomes available, it could be added to the Excel sheet and be used in the computation.

## **Technologies Used**
  
  The main technologies used are:

  1. Python3 (the main language used in programming all the data manipulation and user interactions)
  
  2. HTML (used to display background image, the terminal, button and footer)
  
  3. CSS (used in styling the html elements on the page)

The Python libraries and ancillary technologies used are given below.

### **Python Libraries**

- [gspread](https://pypi.org/project/gspread/)
  - The `gspread` library enables communication with Google Sheets. It is the library I used to open, read and write data to the Spreadsheet used in the application.
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html)
  - contains Credentials: used to validate credentials and grant access to Google service accounts
- [time](https://docs.python.org/3/library/time.html#time.sleep)
  - The time library contains sleep member that permits stalling the program for a stated time. I used this to pause the application for 2 seconds after displaying the initial "PEN - A" logo of the application, just for a better user experience.
- [better_profanity](https://pypi.org/project/better-profanity/)
  - profanity: checks that words are not profane. I used this when validating new user name.
- [py-getch](https://github.com/joeyespo/py-getch)
  - contains the `getch`: used to enable *'Press any key to continue...'* function. I used this when displaying sets of instructions to the user, and when a user need to read a validation message before proceeding with other tasks.

### **Ancillary Technologies**

- *[Balsamiq](https://balsamiq.com/)*
  - Balsamiq was used to create  the Wireframe for the application.
- *[Font Awesome](https://fontawesome.com/)*
  - The application used icons from Font Awesome version at the footer.
- *[Google Fonts](https://fonts.google.com/)*
  - Google Fonts was used for the Page Title.
- *[Multi Device Mockup Generator](https://techsini.com/multi-mockup/index.php)*
  - The Mockup image at the top of the README was created using the Techsini website
- *[PEP8 validation](http://pep8online.com/)*
  - A Python code online validation application.
- *[W3C Markup Validation Service](validator.w3.org)*
  - A free application that was used to check the HTML and CSS files for errors.
- *[Visual Studio Code](https://code.visualstudio.com/)*
  - The code editor used for the application development. With numerous [extensions](#vscode-extensions-used)
  available it is an excellent environment for writing efficient codes.

### **VSCode Extensions Used**

Some VSCode extensions were used during the development of the application. They are:

- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)
This extension assisted to give meaningful messages on the Python code regarding structure and syntax.
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
This assisted with production of this README with Table of Contents in particular.
- [markdown lint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
This extension assisted with the structure of README content.
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
This was very useful to check spelling errors in the code.

## **Testing**

### **PEP8 Testing**

I have tested all the Python files using [PEP8 online](http://pep8online.com) tool and the outcome is displayed [here](/readme-docs/pep8_validation.md). Only the W503 warning came up on two of the Python files.

![W503 warning](/readme-docs/pep8_warning.png)

I chose to leave the two files with the warning since the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator) supports writing code in a more reader friendly manner as I have done.

### **Python Testing during Development**

I used two Python linters during the development of this application.

* [Flake8](https://flake8.pycqa.org/en/latest/)
  
* [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)

The two linters assisted me a lot to write code free of syntax errors and well structured. As a result there are no warnings left in any of the Python files.

### **Manual Testing**

I have done comprehensive manual testing both during the development of the application and after it had been deployed. The documented manual testing is available [HERE](/readme-docs/Testing.md).

### **HTML W3C Validator**

The W3C validator was used to test the HTML and CSS, and no errors were found.

#### **HTML Validation Outcome**

![W3C Validation HTML](/readme-docs/html_validation.png)

#### **CSS Validation Outcome**

![W3C Validation CSS](/readme-docs/css_validation.png)

### **Lighthouse**

Lighthouse testing was carried out on the deployed site with satisfactory result.

![Lighthouse test](/readme-docs/lighthouse.png)

## **Bugs**

### **Current Bugs**

- Another user could access the enquiry results of someone if the user name is known

*This is due to the fact that the application is not using any means of ensuring unique identity of a user. There is no password maintained in the application as it is presently. To resolve this could have involved maintaining passwords and associating them with the user name. Full validation of passwords, hashing, expiration and all that goes into password maintenance would require more time than is available to me for this project.*

- The application is not responsive in mobile devices and small screens.

*This seem to be from the setup of the terminal template and beyond scope for me to deal with. As a result the program is easily usable only on computer screens*

- The application seems to stop accepting input after some inactive time

*Again this seems to be from the terminal setup and beyond my scope*

### **Resolved Bugs**

1. Delete existing result of enquiry returns successful even on an empty worksheet.

  This was resolved with Commit [4629107](https://github.com/Polyanyanwu/pension-adviser-pp3/commit/462910724d333966d89fa417e001496b3b4f6ffe) by deleting the Worksheet for the user instead of only clearing the content. The intended behavior is to delete the Worksheet, then the application will return the correct message.

2. I was getting warning of formatting a regular string which could be done with f-string.

  This was resolved in Commit [7aaec39](https://github.com/Polyanyanwu/pension-adviser-pp3/commit/7aaec39ba050335a441159358957d0ac0bfc6333) by changing the statement using f-string.

3. User name was case sensitive making the application create a new user due to case sensitivity

  Resolution was via Commit [4a5d13](https://github.com/Polyanyanwu/pension-adviser-pp3/commit/4a5d13f531f2a51aa9e4c85adac07bf5fd28ce42) which changed user names to lower case before saving the Worksheet.

4. The application was crashing when a user try to print empty existing data

  Resolved by initializing the existing data to an empty list `existing_data = []` via Commit [31c8be9](https://github.com/Polyanyanwu/pension-adviser-pp3/commit/31c8be957b5f3f9c24915eab4ad84050891a0f0a)

5. Newly created user was not able to continue using the application

  Resolved by returning `True` to `validate_existing_user` function via Commit [e795527](https://github.com/Polyanyanwu/pension-adviser-pp3/commit/e795527120cea7643413a47dd85aadd577f31000)

## **Deployment**

The application was developed using the Code Institute template for [Python Essentials application](https://github.com/Code-Institute-Org/python-essentials-template) and deployed at [Heroku](https://heroku.com). The live site is accessible at [Nigerian Pension Adviser](https://pension-adviser.herokuapp.com/).

Find below steps that were used to effectively deploy the application to the Heroku platform.

1. Sign up / Log in to [Heroku](https://heroku.com) and create an account.

2. From the Heroku Dashboard page select 'New' and then 'Create New App'

![Heroku New App](/readme-docs/create_application.png)

3. From the Create New App form that opens, input an App Name and chose a Region (Europe or United States). When you enter an App Name if it is available, Heroku will indicate that it is available. If its not available you chose another name. Application names in Heroku are unique. I created the app (pension-adviser).

![Heroku New](/readme-docs/create_new_app.png)

4. The application is created within Heroku and you are positioned to the *deploy* tab. The deploy tab will be used later, for the next step click on the *Settings* tab.

5. From the Settings tab, click on the Reveal Config Vars button to open the Config Vars which shows empty KEY and VALUE settings. In my own application I am using Google credential to access the spreadsheet and created a `creds.json`.

6. In the KEY field input CREDS in capitals and copy and paste the contents of the `creds.json` file into the VALUE field. Click the Add button to add the CREDS key to the settings.

7. Add another KEY for PORT with the VALUE of 8000; click the Add button to the right. The settings Config Var entries will look like below:

![Config Vars](/readme-docs/config_vars.png)

8. Next click on the Add buildpack button below the config vars section. Select Python as the first build pack and click on save changes. Repeat the step to add node.js to the buildpack.

![Build pack list](/readme-docs/build_pack_list.png)

Ensure that the Python is listed first with Node.js second as the order of the listing is important. The order could be changed by clicking and dragging any of them. The saved Buildpack should look like the following:

![Build Packs](/readme-docs/build_packs.png)

9. Next scroll up and click on the Deploy tab.

10. Click on a Deployment method, in this case it is Github. Click on Connect to Github.

11. At the Connect to GitHub section, select your Github account; enter the name of the repository and click on the Search button.
  
![Connect Github](/readme-docs/connect_github.png)

12. If the account and repository are located by Heroku , click on Connect button. This action will connect the Github repository to the application created in Heroku.

13. Next is to choose either Automatic deploy or Manual deploy. The Automatic deploy will execute each time you push a commit to your Github repository connected to the application. You can also choose manual deployment, select the branch to deploy and click on Deploy Branch.

![Deployment Method](/readme-docs/deployment_method.png)

14. Heroku will then build the application and after completion of the build process you will see *Your App Was Successfully Deployed* message and a link to the application's live site is displayed.

## **Credits**

### **Content**

- The data on the yearly investment returns for each Pension Fund Administrator (PFA) in Nigeria was downloaded from the website of the regulator of Pension industry in Nigeria - [National Pension Commission -PenCom](https://www.pencom.gov.ng/wp-content/uploads/2020/11/RATES-OF-RETURN-DATA-2016-TO-2019-RSAs.pdf).
  
### **Code**

- The code for the SCOPE and opening the Spreadsheet from Google was taken from the LoveSandwiches application of the Code Institute.

- Credit to [Snyk Advisor](https://snyk.io/advisor/python/better-profanity) for guidance on the installation and use of the `better-profanity` library which I used in validation of user name.

- The idea to find min and max value of a common key in a list of dictionary items was gotten from the contribution of [Hugh Bothwell in stackoverflow.com](https://stackoverflow.com/questions/5320871/how-to-find-the-min-max-value-of-a-common-key-in-a-list-of-dicts)

```Python
lst = [{'price': 99, 'barcode': '2342355'}, {'price': 88, 'barcode': '2345566'}]

maxPricedItem = max(lst, key=lambda x:x['price'])
minPricedItem = min(lst, key=lambda x:x['price'])
 
```

- The idea of using the escape codes and programming functions to print on different colors was gotten from [GeeksforGeeks](https://www.geeksforgeeks.org/print-colors-python-terminal/)

### **Media**

- The investment background image used as the page background was downloaded from [PngTree.com](https://pngtree.com/free-backgrounds).

### **Acknowledgements**

- Many thanks to my mentor [Brian O'Hare](https://code-institute-room.slack.com/team/U02H67B6DS6) for the encouragement and especially the idea to resolve the import of Python files from other folders.

- I remain grateful to [Dave Horrocks](https://github.com/DaveyJH) for ever being there to criticize my work and assisting in testing the application. I was inspired by his own PP3 project work and borrowed some ideas from it.

- Thanks to [Simen Daehlin](https://code-institute-room.slack.com/team/U4MVA9YQP) for his encouraging words and recommending the use of Error Lens even before the Python project was conceptualized. This was invaluable in coming up with well structured code.

- I'm grateful to my family for their support as I take this bold step to change residence and update skills.
  