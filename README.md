# Name of the Project <a id="name-of-project"></a>
## **THE PENSION ADVISER**
![Site Mockup](/readme-docs/mockup.png)
## Live Site <a id="live-site"></a>
[Hosted Live Here](https://pension-adviser.herokuapp.com/)
## Repository

[View Repository Here](https://github.com/Polyanyanwu/pension-adviser-pp3)

## **Objective**

Design and deploy an interactive Command Line (CLI) application that enables the user to gain insight into the performance rates of returns of Pension Fund Administrators (PFA) published by the National Pension Commission (PenCom) of Nigeria (pencom.gov.ng). This will assist contributors in the pension fund make informed decision on which PFA to chose as their retirement savings account fund manager based on performance rates of return over a period. The project shall be deployed through Heroku, run on a command line and programmed using Python.

The Nigerian pension indistry permits contributors to change their PFA once in a year. It becomes necessary to analyse performance data published by the PenCom to make it easy for the user to quickly know which PFAs are best performing in terms of rate of returns on investment.

## **Aims of the Site**

The aim of this site is to provide an interactive application to enable the user to obtain information on PFA performance on any of the funds in the Nigerian pension industry. When completed the final product should:
*	Enable the user chose the fund type of interest
*	Obtain data on PFA performance on the chosen fund
*	Obtain industry average performance on a chosen fund type for a given year
*	be programmatically error free
*	be written using Python
*	check all input errors and handle the gracefully with appropriate messages to the user
*	educate the user regarding use of the application and validity of inputs

## **User Experience Design**

### **User Stories**
The user stories that will guide the development of this application include:
1. As a contributor in the pension industry in Nigeria I like to know the performance of each retirement savings account fund type for a fund manager (PFA) of my interest to enable me decide to change my fund type or the fund manager.
2. As a citizen interested in the economic growth of Nigeria I like to know the pension industry performance over a given period and fund type.
3. As a user of the application I like to view my previous enquiries.

### **Initial Design Concept**
My intention is to guide the contributor in the pension industry in Nigeria to easily find out which PFAs are best performing in terms of returns on investment. This will be achieved by analysing the data that PenCom (the regulator of the industry) posted on its website. It is a simple design that would ask the user the PFA and fund of interest and reply with the performance of that PFA plus the industry performance. It will also produce which PFA has the best performance for a given fund. I intend to give the user the option to select the period of interest, that is starting year and ending year for the analysis. Since the data available is limited, the user will be guided on the years that are available.

#### **Wireframe**
The application is of a Command Line type with limitations on the width and height of the interaction area. Therefore, the wirframe is a simple one as given below:

![Application Wirefrme](/readme-docs/pp3_wireframe.png)

#### **Color Scheme**
In order to enhance the user experience within the Python terminal, I chose to apply some colors available through the color escape codes of Python. I implemented a module that has functions for the colors I used in the application.

For the look and feel of the surrounding areas of the Python terminal, I chose a color scheme through the [Colors.co] (https://coolors.co/). The colors pallete used is shown below:
![Color Pallete](/readme-docs/color_scheme.png)

#### **Fonts**
The font for the Title is "Press Start 2P", which was chosen from Google fonts. This font looks classic to me and fitting for a Command Line application of this nature.

#### **Background Image**
The background image was downloaded from [PngTree](https://pngtree.com/free-backgrounds). It contains an image of someone using a laptop and different sizes of up arrow. These invoke feelins of an investment adviser and growth of funds, which I consider apt for this application.

#### **Flowchart**
The initial flowchart of the application has been produced to guide the application development. It may differ slightly from the final application as more insights may be gathered as the application is being developed.

![Application Flowchart](/readme-docs/pension_adviser_flowchart.png)

## **Features**

***I like to know the performance of each retirement savings account fund type for a fund manager*** 
***As a citizen interested in the economic growth of Nigeria I like to know the pension industry performance over a given period and fund type***

To achieve this User Story the application shall request the fund type, start and end year of interest and PFA. If the PFA is not chosen, as is the case with second User Story above, only the industry average performance for the Fund type is computed and displayed. The application shall display the performance of the selected PFA, the industry average performance for the fund type chosen and the best fund manager for the fund type.

***As a user of the application I like to view my previous enquiries.***

To achieve this requirement it is necessary to input a user name and persist the result of the user enquiries to be able to retrieve them subsequently.

The above requirements led to the design of the main menu of the application given below:

![Application Main Menu](/readme-docs/main_menu.png)

Before the menu is displayed, the user is prompted to enter a user name. A user name is mandatory as it is used by the application as the name of the Worksheet to be used in saving the results of the user enquiries. If same user name is provided as an existing one, the user is requested to confirm if he/she is returing user. If not returning, another name is requested from the user. The user name is not case sensitive, is required to be alphanumeric, between 3 and 15 characters and is not a profane word.

When a user inputs an option 1, 2, 3, 4 or 9 the user is requested to iput the choice a second time to confirm. If the confirmation is same as the initial input, the option is accepted and the desired feature is executed. If the confirmation fails the menu is displayed once more.

The "*Go through the Instructions*" feature
This option, when confirmed by the user, displays the instructions for using the application.

![Instructions](/readme-docs/go_thru_instructions.png)

The instructions are displayed in sets of 5 lines. The user is prompted to press any key to continue to see the next set of instructions. At the end of the instructions, the user is requested to repeat the instructions or not. If not repeating, the menu is displayed once more.


## **Data Model**
As at the commencement of this application design on 10 January, 2022 the regulator of the Pension industry in Nigeria (PenCom) had published performance data (rates of return on investment) for its 22 licensed PFAs between 2016 and 2019.


![Performance Data from PenCom](/readme-docs/pfa_performance_from_pencom.png)

From the data available I had to produce a workbook with two Excel sheets that would be hosted at Google sheets.
The first Excel sheet contains the serial number of the PFAs which will server as the ID, the abbreviated name and the full names. This will enable me display meaningful prompts to the user when selecting a PFA.

![PFA IDs](/readme-docs/pfa_names.png)

The second Excel Sheet contains data for each PFA, Fund type, Year and the return rate. The structure of this Excel sheet will enable me add more rows for performance data for 2020 or any subsequent years when they become available from the PenCom. Also the structure enables the use of Python to query the data in an efficient manner and produce either averages for a PFA and Fund type or for the entire pension industry.

![Performance Data Model for Computation](/readme-docs/return-rates.png)

In this model when additional data becomes available, it could be added to the Excel sheet and be used in the computation.