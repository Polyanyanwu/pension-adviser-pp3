# **THE PENSION ADVISSER**
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

### **Initial Design Concept**
My intention is to guide the contributor in the pension industry in Nigeria to easily find out which PFAs are best performing in terms of returns on investment. This will be achieved by analysing the data that PenCom (the regulator of the industry) posted on its website. It is a simple design that would ask the user the PFA and fund of interest and reply with the performance of that PFA plus the industry performance. It will also produce which PFA has the best performance for a given fund. If time permits I intend to give the user the option to select the period of interest, that is starting year and ending year for the analysis.

#### **Wireframe**
The application is of a Command Line type with limitations on the width and height of the interaction area. Therefore, the wirframe is a simple one as given below:

![Application Wirefrme](/readme-docs/pp3_wireframe.png)

## **Features**

Please enter your name: Poly

	Select PFA of interest:
1	AIICO Pension Managers Limited
2	APT Pension Funds Managers Limited
3	ARM Pension Managers Limited
4	AXA Mansard Pensions Limited
5	Crusader Sterling Pension Limited

If PFA is not selected, analysis will be based on industry wide data.

Select fund type of interest:

1.	Fund I: Retirement Savings Account Fund I (An Active Contributor who is below 50 yrs of age and chooses for his contribution to be invested in this fund)
2.	Fund II: Retirement Savings Account Fund II (default fund for all Active Contributors who are below 50 yrs of age )
3.	Fund III: Retirement Savings Account Fund III (default fund for all Active Contributors who are  50 yrs and above ) 
4.	Fund IV:  Retirement Savings Account Fund IV (Fund for Retirees only)
Confirm selection: 

Average return on investment for Fund I (2018 – 2019) and PFA  yyy is  : xx.xx   (available if PFA was selected)
Pension Industry Average return on investment for Fund I (2018 – 2019) is: xx.xx
Best performing PFA for Fund I (2018 – 2019) is : pfa name with xx.xx rate of return.
Thank you for using the application

Would you like to make another enquiry? y/n

## **Data Model**
As at the commencement of this application design on 10 January, 2022 the regulator of the Pension industry in Nigeria (PenCom) had published performance data (rates of return on investment) for its 22 licensed PFAs between 2016 and 2019.


![Performance Data from PenCom](/readme-docs/pfa_performance_from_pencom.png)

From the data available I had to produce a workbook with two Excel sheets that would be hosted at Google sheets.
The first Excel sheet contains the serial number of the PFAs which will server as the ID, the abbreviated name and the full names. This will enable me display meaningful prompts to the user when selecting a PFA.

![PFA IDs](/readme-docs/pfa_names.png)

The second Excel Sheet contains data for each PFA, Fund type, Year and the return rate. The structure of this Excel sheet will enable me add more rows for performance data for 2020 or any subsequent years when they become available from the PenCom. Also the structure enables the use of Python to query the data in an efficient manner and produce either averages for a PFA and Fund type or for the entire pension industry.

![Performance Data Model for Computation](/readme-docs/return-rates.png)

In this model when additional data becomes available, it could be added to the Excel sheet and be used in the computation.