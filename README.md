[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=312342&assignment_repo_type=GroupAssignmentRepo)
# Group 6022 - Toronto COVID-19 Cases

## Milestones

Details for Milestone are available on Canvas (left sidebar, Course Project) or [here](https://firas.moosvi.com/courses/data301/project/milestone01.html).

## Describe your topic/interest in about 150-200 words

2020 marked the beginning of a very difficult and unprecedented time when the Coronavirus disease overtook the globe and changed countless lives forever. Coronavirus disease, or COVID-19, is an “infectious disease caused by a newly discovered coronavirus” (WHO, 2020). The virus causes those infected “mild to moderate respiratory illness” (WHO, 2020); The majority of people diagnosed can recover without special treatment, although it is more likely for vulnerable populations to be predisposed to more severe symptoms. Those in the vulnerable category include the elderly and those with underlying medical conditions eg: “cardiovascular disease, diabetes, chronic respiratory disease, and cancer,” (WHO, 2020). In Canada, the province with the second highest amount of confirmed COVID-19 cases is Ontario, and one of the hardest hit cities in Ontario is Toronto. Given the global state of cases, it is the public’s right to know of the severity of the pandemic and the toll its taken on densely populated Toronto.

## Describe your dataset in about 150-200 words

Our data set contains all demographic, geographic, and information pertaining to the severity of confirmed and probable COVID-19 cases reported and managed by Toronto Public Health. This data set is accurate, robust and was extracted from the provincial communicable disease reporting system (IPHIS) and Toronto’s COVID-19 case management system (CORES). Both sources have been combined for reporting this particular set.  

### Columns Breakdown:
	
**Identifiers and Location**
<br>*(Columns: ID, Neighbourhood Name, FSA, Classification)*
<br>These columns communicate an individual ID, and names and Forward Sortation Areas (Postal) codes, which is of immense importance for epidemiologists. It also allows us to hypothetically transform our data and build a heatmap based on locations. 

**Information on Spread and transmission** 
<br>*(Columns: Outbreak Associated, Source of infection)*
	<br>These columns allow us to view if individual cases are related to a pandemic outbreak, and, if not, how exactly the virus was transmitted.

**Chronological Dating**
<br>*(Columns: Outbreak Associated, Source of infection)*
	<br>These columns provide observations for the episode date and the reported date. It should be noted that the earliest chronological observation in the data set is January 21st, 2020 while the latest observation is September 13th, 2020. 

**Demographics**
<br>*(Columns: Age, Gender)* 
	<br>Allows us to view and identify relationships between demographics with the highest and lowest infection count. 

**Outcomes**
<br>*(Columns: Outcome, Currently Hospitalized, Currently in ICU, Currently Intubated, Ever Hospitalized, Ever in ICU, Ever Intubated)*
	<br>Columns provide observations for the following outcomes and specifics of those who contracted the virus. 


## Team Members

- Hannah Willoner: I'm in my final year of study at UBCO, majoring in Anthropology. I'm looking forward to completing my degree and exploring places outside the Okanagan where I was born and raised and seeing more of this beautiful country. *Hannah has dropped the course and is no longer active in this project*
- Jonathan Chou: I am a 3rd year Computer Science major currently living in Vancouver, my hometown. Although I was born and raised here, I attended high school in Taiwan, where my parents are from.
- Matthew Kuelker: I love all things music and I'm a 2nd year CS major who's probably adequate at coding. 

## References
https://www.who.int/health-topics/coronavirus#tab=tab_1 <br>
https://open.toronto.ca/dataset/covid-19-cases-in-toronto/ <br>
https://www.kaggle.com/divyansh22/toronto-covid19-cases <br>
