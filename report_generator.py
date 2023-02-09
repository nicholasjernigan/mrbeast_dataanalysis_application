# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:58:42 2023

@author: nicho
"""

import pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
import os 
os.chdir(r"C:\Users\nicho\Documents\Job Application\Click-through_rate_analysis")
colors = [(171,212,255), (234,67,124,255)]



class FPDF(FPDF):
    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font('Arial', '', 8)
        # Print centered page number
        self.cell(151)
        self.cell(50, 10, '*Data from https://www.kaggle.com/datasets/kristhecoder/youtube-revenue-data-20182021?select=Table+data+2020.csv', 0, 0, 'C')
# df = pd.DataFrame()
# df['Question'] = ["Q1", "Q2", "Q3", "Q4"]
# df['Charles'] = [3, 4, 5, 3]
# df['Mike'] = [3, 3, 4, 4]

# title("Professor Criss's Ratings by Users")
# xlabel('Question Number')
# ylabel('Score')

# c = [2.0, 4.0, 6.0, 8.0]
# m = [x - 0.5 for x in c]

# xticks(c, df['Question'])

# bar(m, df['Mike'], width=0.5, color="#91eb87", label="Mike")
# bar(c, df['Charles'], width=0.5, color="#eb879c", label="Charles")

# legend()
# axis([0, 10, 0, 8])
# savefig('barchart.png')

pdf = FPDF()
pdf.add_page()
pdf.set_xy(0, 0)
pdf.set_font('arial', 'B', 12)
pdf.set_fill_color(0,171,212)
pdf.rect(0,0, 210,60,'F')


pdf.image('mrbeast-logo-with-text-veq.png', x = 92, y = 7, w = 28)
pdf.image('CTR_relation_to Revenue.png', x = 10, y = 70, w = 90)
pdf.image('APV_relation_to Revenue.png', x = 10, y = 148, w = 90)
pdf.image('coefficients_of_features.png', x = 15, y = 220, w = 87)



pdf.set_fill_color(0, 0, 0)
pdf.set_text_color(255,255,255)  
#pdf.cell(0)
#pdf.cell(w = 0, h = 74, txt='SIGN OWNER NAME', align='R')


pdf.set_font('arial', 'B', 34)
pdf.cell(0,35, ln=True)
pdf.cell(0, 0, "CTR, AVP Impact on Revenue", align='C', ln=True)
pdf.cell(0,10, ln=True)
pdf.set_font('arial', '', 17) 
pdf.cell(0, 0, "Prepared by Nicholas Jernigan", align='C', ln=True)
pdf.link(x = 0, y = 0, w = 210, h = 100, link='www.linkedin.com/in/jernigan-nicholas')

pdf.set_font('arial', 'B', 12)
pdf.set_text_color(0, 172, 210)  
pdf.cell(18)
pdf.cell(25, 45, "CTR Correlation with Revenue")


#First part of points
pdf.set_text_color(0, 0, 0) 

#Y here controls Takeaways placement
pdf.cell(190,16, ln=True)
#X here controls takeaways placement
pdf.cell(133)
pdf.cell(225, 12, "Takeaways", ln=True)
pdf.set_font('arial', '', 12)
pdf.cell(100,0)
pdf.multi_cell(90, 5, "- CTR independent of other variables does NOT positively correlate with revenue" +
               "\n\n- APV independent of other variables does positively correlate with revenue" +
               "\n\n- HOWEVER, both variables impact is clearly understood only when looked at with other key success variables")

#Graph 2 title
pdf.set_font('arial', 'B', 12)
pdf.set_text_color(0, 172, 210)  
pdf.cell(18)
#Y here controls Y
pdf.cell(25, 55, "APV Correlation with Revenue")



#Full Picture Title
pdf.set_text_color(0, 0, 0) 

#Y here controls Takeaways placement
pdf.cell(190,22, ln=True)
#X here controls takeaways placement
pdf.cell(133)
pdf.cell(225, 12, "Full Picture", ln=True)


#Full picture explanation
pdf.set_font('arial', '', 12)
pdf.cell(100,0)
pdf.multi_cell(90, 5, "- Without considering other variables CTR will appear to negatively impact or have no impact on revenue while APV will seem to have a major positive impact" +
               "\n\n- When considering all variables, APV and CTR do have significant impacts on revenue, but only in conjunction with other variables" +
               "\n\n- In this case, returning viewers is an important variable")



#Graph 3 title
pdf.set_font('arial', 'B', 12)
pdf.set_text_color(0, 172, 210)  
#Controls X
pdf.cell(28)
#Y here controls Y
pdf.cell(25, 20, "Variable Significance")



#Conclusion title
pdf.set_text_color(0, 0, 0) 

#Y here controls Takeaways placement
pdf.cell(190,5, ln=True)
#X here controls takeaways placement
pdf.cell(133)
pdf.cell(225, 12, "Conclusion", ln=True)



#Conclusion

pdf.set_font('arial', '', 12)
pdf.cell(100,0)
pdf.multi_cell(90, 5, "- Without engaged viewers, high CTR will not improve your revenue" +
               "\n\n- APV is important, but particularly when paired with other variables like CTR" +
               "\n\n- YouTubers need to consider APV and CTR as metrics for success alongside other critical metrics such as in this case, returning viewers")





#Notes on data in footer




#pdf.cell(0, 60, ln=True)

# pdf.cell(75, 10, "A Tabular and Graphical Report of Professor Criss's Ratings by Users Charles and Mike", 0, 2, 'C')
# pdf.cell(90, 10, " ", 0, 2, 'C')
# pdf.cell(-40)
# pdf.cell(50, 10, 'Question', 1, 0, 'C')
# pdf.cell(40, 10, 'Charles', 1, 0, 'C')
# pdf.cell(40, 10, 'Mike', 1, 2, 'C')
# pdf.cell(-90)
# pdf.set_font('arial', '', 12)
# for i in range(0, len(df)):
#     pdf.cell(50, 10, '%s' % (df['Question'].iloc[i]), 1, 0, 'C')
#     pdf.cell(40, 10, '%s' % (str(df.Mike.iloc[i])), 1, 0, 'C')
#     pdf.cell(40, 10, '%s' % (str(df.Charles.iloc[i])), 1, 2, 'C')
#     pdf.cell(-90)
# pdf.cell(90, 10, " ", 0, 2, 'C')
# pdf.cell(-30)
# pdf.image('barchart.png', x = None, y = None, w = 0, h = 0, type = '', link = '')
pdf.output('test_1.pdf', 'F')


