# Tackling Teenage Pregnancy in the USA


EXECUTIVE SUMMARY


# Aims and Objectives


For this project, you will be acting as a consultant for a fictional firm. As a part of your data exploration, come up with a driving question based on this data.
The goal of this project is to have you complete a very common real-world task with regards to Regression Modelling. However, real world problems often come with a significant degree of ambiguity, which requires you to use your knowledge of statistics and data science to think critically about and answer.

Dataset
The Data was gathered in a collaboration between the University of Wisconsin and the Robert Wood Johnson Foundation. The rankings and the data information used in this project were obtained from the 2019 County Health Ranking. The dataset comprises 3142 rows, 25 columns out of 534.
The rankings measure everything from high-school graduation rates, to obesity, to unemployment in nearly every county in America, providing a revealing snapshot of how health is influenced by where we live, learn, work and play. They also can provide a starting point for change in communities.


# Deliverables


A Jupyter Notebook containing well-formatted, professional looking markdown cells explaining any substantial code. All functions have docstrings that act as professional-quality documentation. The notebook is written to technical audiences with a way to both understand the approach and reproduce the results. The target audience for this deliverable is other data scientists looking to validate your findings. The notebook should be well organized, easy to follow, and code is commented where appropriate. Finally, notebook should clearly show how the results were achieved for each hypothesis test, including how the p-values were calculated.
A user focused README.md file that explains the process, methodology and findings, and clearly showing both technical expertise and ability to communicate the results.
PowerPoint/Google Slide presentation that explains the hypothesis testing, findings, and their relevance to the company/stakeholders. Contain between 5-10 professional quality slides detailing: (a) A high-level overview of your methodology; (b) The results of your hypothesis tests; (3) Any real-world recommendations it can be made based on the findings.


# Introduction


In 2017, a total of 194,377 babies were born to women aged 15–19 years, for a birth rate of 18.8 per 1,000 women in this age group.  This is another record low for U.S. teens and a drop of 7% from 2016.1 Birth rates fell 10% for women aged 15–17 years and 6% for women aged 18–19 years (Centres for Disease Control and preventions, 2020). 
Although reasons for the declines are not totally clear, evidence suggests these declines are due to more teens abstaining from sexual activity, and more teens who are sexually active using birth control than in previous years. Still, the U.S. teen pregnancy rate is substantially higher than in other western industrialized nations5, and racial/ethnic and geographic disparities in teen birth rates persist.6
Teen pregnancy and childbearing bring substantial social and economic costs through immediate and long-term impacts on teen parents and their children. Pregnancy and birth are significant contributors to high school dropout rates among girls. Only about 50% of teen mothers receive a high school diploma by 22 years of age, whereas approximately 90% of women who do not give birth during adolescence graduate from high school. The children of teenage mothers are more likely to have lower school achievement and to drop out of high school, have more health problems, be incarcerated at some time during adolescence, give birth as a teenager, and face unemployment as a young adult. 
On a positive note, between 1991 and 2015, the teen birth rate dropped 64%, which resulted in $4.4 billion in public savings in 2015 alone. 
The present study aimed to investigate the predicting features contributing to teenage pregnancy and make recommendations to the stakeholders regarding what type of interventions, in which money should be invested. 


# Methodology


The dataset was uploaded into a Jupyter notebook in .csv format. The data was thoroughly screened from missing values, and those were replaced appropriately. Moreover, the multicollinearity tests were conducted in order to intercept and discard highly correlated variables. 
The dataset was then split into county, state and national data frames. The county ranking for teen births were assessed, and the remaining analysis were focused on the national data frame. 
A simple baseline model was conducted in order to investigate the data, which was then analysed with over 40 different models, in order to optimize everything above the baseline. Furthermore, clusters of features were identified, in order to understand which influenced the teen birth rate. A series was statistical steps were conducted in order to validate the model.


# Findings


From this research, we could conclude that the features affect teen pregnancy include poor or fair health, education, low birthweight, income inequality, unemployment, rural environments, access to exercise. 

The above sentence indicates that the factors that triggered teenagers into early pregnancy might be lack of access to proper education; detrimental health, which can cause slower cognitive development and lead to poor judgement. Unemployment is particularly interesting, as it could be the consequence of poor education, as well as a contributing feature regarding lack of career directions, or even boredom. Meanwhile, high school education seems to allow teenagers to have access to proper education, which could also include sexual education, leading them to recognise the importance of pregnancy prevention.


# Recommendations


Education is key. We strongly advise the health and education departments to invest their resources on a series of educational interventions, including: Increasing the quality of mainstream education; Sexual education; Focus on educating teenagers regarding cooking and eating behaviour; and Increase the access to physical activities in rural areas. 
