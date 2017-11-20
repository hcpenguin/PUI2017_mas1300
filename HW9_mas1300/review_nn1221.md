![](https://github.com/ninanrh/PUI2017_nn1221/blob/master/HW8_nn1221/HW8.png)

**Figure 1.** Heating complaints frequencies through 311 calls data in New York City during Winter period of 2010-2016. 
[(Source code in Jupyter Notebook)](https://github.com/ninanrh/PUI2017_nn1221/blob/master/HW8_nn1221/HW8.ipynb)

I created plot for 311 calls that mentioned heating complaint during winter period between 2010 and 2017. 
I downloaded 311 data from [NYC Open Data](https://nycopendata.socrata.com/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/data). 
The data have been filtered by complaint type of heating and heat/hot water between October 1 and May 31, from 2010 - 2017. 
New York City regulation allows complaint regarding residential building that does not have enough heat only between October 1 and May 31 [(source)](http://www1.nyc.gov/site/hpd/owners/heat-hot-water.page), therefore this assignment use data from October 1 to May 31 for each winter term.

I used sources from [seaborn](https://seaborn.pydata.org/generated/seaborn.heatmap.html) package to plot. In this assignment, I'm working on my own.



----
Review:

This is an amazing plot! I love it!

CLARITY: 
Title and axis lables are all clear. Appreciate that the year range is in the title. The caption is a bit long, would suggest seperating caption from rest of readme information.  

Colorblindness: Using Color Oracle to check, only in the very rare type of color blindness (tritanopia) is information lost. The last two months of winter simply look white. To fix this you can change the lightest colors on the scale to slightly more pigmented, if possible. 

ESTHETIC:

Good esthetics. Colorscheme is evocative of winter. Easy to read and dechiper. 

HONESTY: 
Would like to know upper limit and lower limit of complaints. What is the scale for frequency? Plot seems honest. 
Maybe add an analytical conclusion to the caption. Any trends? Why are April and May included as winter by the city when there are so few heating complaints and in general that period is considered spring. Should it be recommended to remove them from the winter grouping? 

