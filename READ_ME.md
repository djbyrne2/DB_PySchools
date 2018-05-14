





# PySchools 

## 3 Observable Trends in PySchools 

   ##### 1) The top 5 performing schools are all charter schools and the bottom 5  schools are all district schools.
   
   ##### 2) Within schools math and reading scores remain consistent across grades. There are modest differences between schools.
   
   ##### 3) Schools with higher budgets yield lower pass rates than schools with smaller budgets. Smaller & Medium size schools perform better than large schools.    


```python
#Dependencies
import pandas as pd
import os
```


```python
# define file path
schools_filepath_csv = os.path.join('raw_data','schools_complete.csv')
print(os.path.exists(schools_filepath_csv))

None
```

    True



```python
# define file path
students_filepath_csv = os.path.join('raw_data', 'students_complete.csv')
#print(os.path.exists(students_filepath_csv))

None
```


```python
# read schools file
schools_df = pd.read_csv(schools_filepath_csv)
#print(schools_df)

None
```


```python
#read student file
students_df = pd.read_csv(students_filepath_csv)
students_df.head()

None
```


```python
# Find Total Number of Schools within the District

dist_schools = schools_df['name'].unique()

school_numbers = len(dist_schools)

#print(school_numbers)

None
```


```python
# Find Total Number of Students within District

total_dist_students = schools_df['size'].sum()
#print(total_dist_students)

None
```


```python
#Find Total District Budget

total_dist_budget = schools_df['budget'].sum()

#print(total_dist_budget)

None
```


```python
# Find District's Average Math Score


dist_student_ave_math = students_df["math_score"].mean()

#print(dist_student_ave_math)

None
```


```python
# Find District's Average Reading Score

dist_student_ave_reading = students_df["reading_score"].mean()

#print(dist_student_ave_reading)

None
```


```python
# Find Total Number of Students Passing Math

total_passing_math = (students_df['math_score'] >= 60).sum()

#print(total_passing_math)

# Find Total % of Students Passing Math

percent_passing_math = (total_passing_math/total_dist_students)*100

#print(percent_passing_math)

None
```


```python
# Find Total Number of Students Passing Reading

total_passing_reading = (students_df['reading_score'] >= 60).sum()

#print(total_passing_reading)

# Find Total % of Students Passing Reading

percent_passing_reading = (total_passing_reading/total_dist_students)*100

#print(percent_passing_reading)

None
```


```python
# Find Overall Passing Rate (Average of the above two)

combined_dist_passing = ((percent_passing_reading + percent_passing_math)/2)

#print(combined_dist_passing)

None
```


```python
# Create District Summary Table

district_sum_table = pd.DataFrame({
    
    "Total Schools": [school_numbers],
    "Total Students": [total_dist_students],
    "Total Budget": [total_dist_budget],
    "Average Math Score": [dist_student_ave_math],
    "Average Reading Score": [dist_student_ave_reading],
    "% Passing Reading": [percent_passing_reading],
    "% Passing Math": [percent_passing_math],
    "Overall Passing Rate":[combined_dist_passing]
})




```


```python
district_sum_table = district_sum_table[["Total Schools", "Total Students","Total Budget",
                                     "Average Math Score", "Average Reading Score", 
                                     "% Passing Reading", "% Passing Math", "Overall Passing Rate"]]

district_sum_table.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>100.0</td>
      <td>92.445749</td>
      <td>96.222875</td>
    </tr>
  </tbody>
</table>
</div>



# District Summary


```python
district_sum_table["Total Students"] = district_sum_table["Total Students"].map("{: ,}".format)
district_sum_table["Total Budget"] = district_sum_table["Total Budget"].map("${:,.2f}".format)
district_sum_table["Average Math Score"] = district_sum_table["Average Math Score"].map("{:.2f}%".format)
district_sum_table["Average Reading Score"] = district_sum_table["Average Reading Score"].map("{:.2f}%".format)
district_sum_table["% Passing Math"] = district_sum_table["% Passing Math"].map("{:.2f}%".format)
district_sum_table["% Passing Reading"] = district_sum_table["% Passing Reading"].map("{:.2f}%".format)
district_sum_table["Overall Passing Rate"] = district_sum_table["Overall Passing Rate"].map("{:.2f}%".format)

district_sum_table.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39,170</td>
      <td>$24,649,428.00</td>
      <td>78.99%</td>
      <td>81.88%</td>
      <td>100.00%</td>
      <td>92.45%</td>
      <td>96.22%</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Top Performing Schools (By Passing Rate)


# Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:


# School Name
# School Type
# Total Students
# Total School Budget
# Per Student Budget
# Average Math Score
# Average Reading Score
# % Passing Math
# % Passing Reading
# Overall Passing Rate (Average of the above two)


```


```python
#Rename Columns to Consolidate/Merge/Join/Group CSV files??

schools_df = schools_df.rename(columns={"name":"school"})
students_df = students_df.rename(columns={"school":"school"})
```


```python
top_schools_df = students_df.groupby(['school'])

#top_schools_df.head()
```


```python
#Group by School Type

school_type = schools_df.set_index('school')['type']
#print(school_type)

```


```python
#Find Average Math Score for all schools

top_schools_ave_math_df = pd.DataFrame(top_schools_df["math_score"].mean())

#print(top_schools_ave_math_df)
```


```python
#Find Average Reading Score for all schools

top_schools_ave_reading_df = pd.DataFrame(top_schools_df["reading_score"].mean())

#print(top_schools_ave_reading_df)

```


```python
#Group students passing math and reading by school

school_stu_passing_math = students_df[students_df["math_score"]>= 60].groupby(["school"])
                                                                   
school_stu_passing_reading = students_df[students_df["reading_score"]>= 60].groupby(["school"])
                                                                   
```


```python
#Number of Students Per School
school_student_count = top_schools_df['name'].count()
#print(school_student_count)
```


```python
#Find Budget per School

schools_budgets = schools_df.set_index('school')['budget']

#print(schools_budgets)
```


```python
#Schools spending per Student

student_spending = schools_budgets/school_student_count
#print(student_spending)
```


```python
#Average Math Score by School
average_school_math = top_schools_df['math_score'].mean()
#print(average_school_math)
```


```python
#Average Reading Score by School

average_school_reading = top_schools_df['reading_score'].mean()
#print(average_school_reading)
```


```python
#Find the total number of students that passed math by school

pass_math_school_numbers = students_df[students_df['math_score'] >= 60].groupby('school')['name'].count()
#print(pass_math_school_numbers)
```


```python
#Find the total number of students that passed reading by school

pass_reading_school_numbers = students_df[students_df['reading_score'] >= 60].groupby('school')['name'].count()
#print(pass_reading_school_numbers)
```


```python
#Find the total percent of students that passed math by school
percent_pass_math_school = (pass_math_school_numbers/school_student_count)
#print(percent_pass_math_school)
```


```python
#Find the total percent of students that passed reading by school
percent_pass_reading_school = percent_pass_reading_school = (pass_reading_school_numbers/school_student_count)
#print(percent_pass_reading_school)
```


```python
#Calculate total percent passing by school
total_percent_pass = (percent_pass_reading_school + percent_pass_math_school)/2
#print(total_percent_pass)
```


```python
school_summary_table = pd.DataFrame({
    "School Type": school_type,
    "Total Students": school_student_count,
    "Per Student Budget": student_spending ,
    "Total School Budget": schools_budgets,
    "Average Math Score": average_school_math ,
    "Average Reading Score": average_school_reading,
    '% Passing Math': percent_pass_math_school,
    '% Passing Reading': percent_pass_reading_school,
    "Overall Passing Rate": total_percent_pass
})

```


```python
#rearranging column order
school_summary_table = school_summary_table[['School Type', 
                          'Total Students', 
                          'Total School Budget', 
                          'Per Student Budget', 
                          'Average Math Score', 
                          'Average Reading Score',
                          '% Passing Math',
                          '% Passing Reading',
                          'Overall Passing Rate']]
```


```python
#formatting table cells
school_summary_table.style.format({'Total Students': '{:,}', 
                          "Total School Budget": "${:,}", 
                          "Per Student Budget": "${:.0f}",
                          'Average Math Score': "{:.1f}", 
                          'Average Reading Score': "{:.1f}", 
                          "% Passing Math": "{:.2%}", 
                          "% Passing Reading": "{:.2%}", 
                          "Overall Passing Rate": "{:.2%}"})
```




<style  type="text/css" >
</style>  
<table id="T_97ed67a6_571c_11e8_a5bd_720002f9a650" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >School Type</th> 
        <th class="col_heading level0 col1" >Total Students</th> 
        <th class="col_heading level0 col2" >Total School Budget</th> 
        <th class="col_heading level0 col3" >Per Student Budget</th> 
        <th class="col_heading level0 col4" >Average Math Score</th> 
        <th class="col_heading level0 col5" >Average Reading Score</th> 
        <th class="col_heading level0 col6" >% Passing Math</th> 
        <th class="col_heading level0 col7" >% Passing Reading</th> 
        <th class="col_heading level0 col8" >Overall Passing Rate</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row0" class="row_heading level0 row0" >Bailey High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row0_col0" class="data row0 col0" >District</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row0_col1" class="data row0 col1" >4,976</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row0_col2" class="data row0 col2" >$3,124,928</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row0_col3" class="data row0 col3" >$628</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row0_col4" class="data row0 col4" >77.0</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row0_col5" class="data row0 col5" >81.0</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row0_col6" class="data row0 col6" >89.53%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row0_col7" class="data row0 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row0_col8" class="data row0 col8" >94.76%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row1" class="row_heading level0 row1" >Cabrera High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row1_col0" class="data row1 col0" >Charter</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row1_col1" class="data row1 col1" >1,858</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row1_col2" class="data row1 col2" >$1,081,356</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row1_col3" class="data row1 col3" >$582</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row1_col4" class="data row1 col4" >83.1</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row1_col5" class="data row1 col5" >84.0</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row1_col6" class="data row1 col6" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row1_col7" class="data row1 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row1_col8" class="data row1 col8" >100.00%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row2" class="row_heading level0 row2" >Figueroa High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row2_col0" class="data row2 col0" >District</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row2_col1" class="data row2 col1" >2,949</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row2_col2" class="data row2 col2" >$1,884,411</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row2_col3" class="data row2 col3" >$639</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row2_col4" class="data row2 col4" >76.7</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row2_col5" class="data row2 col5" >81.2</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row2_col6" class="data row2 col6" >88.44%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row2_col7" class="data row2 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row2_col8" class="data row2 col8" >94.22%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row3" class="row_heading level0 row3" >Ford High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row3_col0" class="data row3 col0" >District</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row3_col1" class="data row3 col1" >2,739</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row3_col2" class="data row3 col2" >$1,763,916</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row3_col3" class="data row3 col3" >$644</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row3_col4" class="data row3 col4" >77.1</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row3_col5" class="data row3 col5" >80.7</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row3_col6" class="data row3 col6" >89.30%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row3_col7" class="data row3 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row3_col8" class="data row3 col8" >94.65%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row4" class="row_heading level0 row4" >Griffin High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row4_col0" class="data row4 col0" >Charter</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row4_col1" class="data row4 col1" >1,468</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row4_col2" class="data row4 col2" >$917,500</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row4_col3" class="data row4 col3" >$625</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row4_col4" class="data row4 col4" >83.4</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row4_col5" class="data row4 col5" >83.8</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row4_col6" class="data row4 col6" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row4_col7" class="data row4 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row4_col8" class="data row4 col8" >100.00%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row5" class="row_heading level0 row5" >Hernandez High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row5_col0" class="data row5 col0" >District</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row5_col1" class="data row5 col1" >4,635</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row5_col2" class="data row5 col2" >$3,022,020</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row5_col3" class="data row5 col3" >$652</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row5_col4" class="data row5 col4" >77.3</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row5_col5" class="data row5 col5" >80.9</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row5_col6" class="data row5 col6" >89.08%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row5_col7" class="data row5 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row5_col8" class="data row5 col8" >94.54%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row6" class="row_heading level0 row6" >Holden High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row6_col0" class="data row6 col0" >Charter</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row6_col1" class="data row6 col1" >427</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row6_col2" class="data row6 col2" >$248,087</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row6_col3" class="data row6 col3" >$581</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row6_col4" class="data row6 col4" >83.8</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row6_col5" class="data row6 col5" >83.8</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row6_col6" class="data row6 col6" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row6_col7" class="data row6 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row6_col8" class="data row6 col8" >100.00%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row7" class="row_heading level0 row7" >Huang High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row7_col0" class="data row7 col0" >District</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row7_col1" class="data row7 col1" >2,917</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row7_col2" class="data row7 col2" >$1,910,635</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row7_col3" class="data row7 col3" >$655</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row7_col4" class="data row7 col4" >76.6</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row7_col5" class="data row7 col5" >81.2</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row7_col6" class="data row7 col6" >88.86%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row7_col7" class="data row7 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row7_col8" class="data row7 col8" >94.43%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row8" class="row_heading level0 row8" >Johnson High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row8_col0" class="data row8 col0" >District</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row8_col1" class="data row8 col1" >4,761</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row8_col2" class="data row8 col2" >$3,094,650</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row8_col3" class="data row8 col3" >$650</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row8_col4" class="data row8 col4" >77.1</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row8_col5" class="data row8 col5" >81.0</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row8_col6" class="data row8 col6" >89.18%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row8_col7" class="data row8 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row8_col8" class="data row8 col8" >94.59%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row9" class="row_heading level0 row9" >Pena High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row9_col0" class="data row9 col0" >Charter</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row9_col1" class="data row9 col1" >962</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row9_col2" class="data row9 col2" >$585,858</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row9_col3" class="data row9 col3" >$609</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row9_col4" class="data row9 col4" >83.8</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row9_col5" class="data row9 col5" >84.0</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row9_col6" class="data row9 col6" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row9_col7" class="data row9 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row9_col8" class="data row9 col8" >100.00%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row10" class="row_heading level0 row10" >Rodriguez High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row10_col0" class="data row10 col0" >District</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row10_col1" class="data row10 col1" >3,999</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row10_col2" class="data row10 col2" >$2,547,363</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row10_col3" class="data row10 col3" >$637</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row10_col4" class="data row10 col4" >76.8</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row10_col5" class="data row10 col5" >80.7</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row10_col6" class="data row10 col6" >88.55%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row10_col7" class="data row10 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row10_col8" class="data row10 col8" >94.27%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row11" class="row_heading level0 row11" >Shelton High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row11_col0" class="data row11 col0" >Charter</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row11_col1" class="data row11 col1" >1,761</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row11_col2" class="data row11 col2" >$1,056,600</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row11_col3" class="data row11 col3" >$600</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row11_col4" class="data row11 col4" >83.4</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row11_col5" class="data row11 col5" >83.7</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row11_col6" class="data row11 col6" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row11_col7" class="data row11 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row11_col8" class="data row11 col8" >100.00%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row12" class="row_heading level0 row12" >Thomas High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row12_col0" class="data row12 col0" >Charter</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row12_col1" class="data row12 col1" >1,635</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row12_col2" class="data row12 col2" >$1,043,130</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row12_col3" class="data row12 col3" >$638</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row12_col4" class="data row12 col4" >83.4</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row12_col5" class="data row12 col5" >83.8</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row12_col6" class="data row12 col6" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row12_col7" class="data row12 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row12_col8" class="data row12 col8" >100.00%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row13" class="row_heading level0 row13" >Wilson High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row13_col0" class="data row13 col0" >Charter</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row13_col1" class="data row13 col1" >2,283</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row13_col2" class="data row13 col2" >$1,319,574</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row13_col3" class="data row13 col3" >$578</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row13_col4" class="data row13 col4" >83.3</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row13_col5" class="data row13 col5" >84.0</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row13_col6" class="data row13 col6" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row13_col7" class="data row13 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row13_col8" class="data row13 col8" >100.00%</td> 
    </tr>    <tr> 
        <th id="T_97ed67a6_571c_11e8_a5bd_720002f9a650level0_row14" class="row_heading level0 row14" >Wright High School</th> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row14_col0" class="data row14 col0" >Charter</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row14_col1" class="data row14 col1" >1,800</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row14_col2" class="data row14 col2" >$1,049,400</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row14_col3" class="data row14 col3" >$583</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row14_col4" class="data row14 col4" >83.7</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row14_col5" class="data row14 col5" >84.0</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row14_col6" class="data row14 col6" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row14_col7" class="data row14 col7" >100.00%</td> 
        <td id="T_97ed67a6_571c_11e8_a5bd_720002f9a650row14_col8" class="data row14 col8" >100.00%</td> 
    </tr></tbody> 
</table> 



# Top 5 Performing Schools By Pass Rate


```python
# Arrange(sort) schools by passing rates (PRINT!)
top_5_performing_schools = school_summary_table.sort_values("Overall Passing Rate", ascending = False)
top_5_performing_schools.head().style.format({'Total Students': '{:,}',
                           "Total School Budget": "${:,}", 
                           "Per Student Budget": "${:.0f}", 
                           "% Passing Math": "{:.1%}", 
                           "% Passing Reading": "{:.1%}", 
                           "Overall Passing Rate": "{:.1%}"})

```




<style  type="text/css" >
</style>  
<table id="T_9e9e7f9a_571c_11e8_988e_720002f9a650" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >School Type</th> 
        <th class="col_heading level0 col1" >Total Students</th> 
        <th class="col_heading level0 col2" >Total School Budget</th> 
        <th class="col_heading level0 col3" >Per Student Budget</th> 
        <th class="col_heading level0 col4" >Average Math Score</th> 
        <th class="col_heading level0 col5" >Average Reading Score</th> 
        <th class="col_heading level0 col6" >% Passing Math</th> 
        <th class="col_heading level0 col7" >% Passing Reading</th> 
        <th class="col_heading level0 col8" >Overall Passing Rate</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_9e9e7f9a_571c_11e8_988e_720002f9a650level0_row0" class="row_heading level0 row0" >Cabrera High School</th> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row0_col0" class="data row0 col0" >Charter</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row0_col1" class="data row0 col1" >1,858</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row0_col2" class="data row0 col2" >$1,081,356</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row0_col3" class="data row0 col3" >$582</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row0_col4" class="data row0 col4" >83.0619</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row0_col5" class="data row0 col5" >83.9758</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row0_col6" class="data row0 col6" >100.0%</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row0_col7" class="data row0 col7" >100.0%</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row0_col8" class="data row0 col8" >100.0%</td> 
    </tr>    <tr> 
        <th id="T_9e9e7f9a_571c_11e8_988e_720002f9a650level0_row1" class="row_heading level0 row1" >Griffin High School</th> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row1_col0" class="data row1 col0" >Charter</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row1_col1" class="data row1 col1" >1,468</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row1_col2" class="data row1 col2" >$917,500</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row1_col3" class="data row1 col3" >$625</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row1_col4" class="data row1 col4" >83.3515</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row1_col5" class="data row1 col5" >83.8168</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row1_col6" class="data row1 col6" >100.0%</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row1_col7" class="data row1 col7" >100.0%</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row1_col8" class="data row1 col8" >100.0%</td> 
    </tr>    <tr> 
        <th id="T_9e9e7f9a_571c_11e8_988e_720002f9a650level0_row2" class="row_heading level0 row2" >Holden High School</th> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row2_col0" class="data row2 col0" >Charter</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row2_col1" class="data row2 col1" >427</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row2_col2" class="data row2 col2" >$248,087</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row2_col3" class="data row2 col3" >$581</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row2_col4" class="data row2 col4" >83.8033</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row2_col5" class="data row2 col5" >83.815</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row2_col6" class="data row2 col6" >100.0%</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row2_col7" class="data row2 col7" >100.0%</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row2_col8" class="data row2 col8" >100.0%</td> 
    </tr>    <tr> 
        <th id="T_9e9e7f9a_571c_11e8_988e_720002f9a650level0_row3" class="row_heading level0 row3" >Pena High School</th> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row3_col0" class="data row3 col0" >Charter</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row3_col1" class="data row3 col1" >962</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row3_col2" class="data row3 col2" >$585,858</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row3_col3" class="data row3 col3" >$609</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row3_col4" class="data row3 col4" >83.8399</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row3_col5" class="data row3 col5" >84.0447</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row3_col6" class="data row3 col6" >100.0%</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row3_col7" class="data row3 col7" >100.0%</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row3_col8" class="data row3 col8" >100.0%</td> 
    </tr>    <tr> 
        <th id="T_9e9e7f9a_571c_11e8_988e_720002f9a650level0_row4" class="row_heading level0 row4" >Shelton High School</th> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row4_col0" class="data row4 col0" >Charter</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row4_col1" class="data row4 col1" >1,761</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row4_col2" class="data row4 col2" >$1,056,600</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row4_col3" class="data row4 col3" >$600</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row4_col4" class="data row4 col4" >83.3595</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row4_col5" class="data row4 col5" >83.7257</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row4_col6" class="data row4 col6" >100.0%</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row4_col7" class="data row4 col7" >100.0%</td> 
        <td id="T_9e9e7f9a_571c_11e8_988e_720002f9a650row4_col8" class="data row4 col8" >100.0%</td> 
    </tr></tbody> 
</table> 



# Bottom 5 Performing Schools By Pass Rate


```python
#Find the 5 lowest performing school and arrange(sort) from the worst to best (DO NOT PRINT!)
bottom_5_performing_schools = top_5_performing_schools.tail()
bottom_5_performing_schools = bottom_5_performing_schools.sort_values('Overall Passing Rate', ascending = True)
bottom_5_performing_schools.head().style.format({'Total Students': '{:,}', 
                       "Total School Budget": "${:,}", 
                       "Per Student Budget": "${:.0f}", 
                       "% Passing Math": "{:.1%}", 
                       "% Passing Reading": "{:.1%}", 
                       "Overall Passing Rate": "{:.1%}"})


```




<style  type="text/css" >
</style>  
<table id="T_a2298a24_571c_11e8_825e_720002f9a650" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >School Type</th> 
        <th class="col_heading level0 col1" >Total Students</th> 
        <th class="col_heading level0 col2" >Total School Budget</th> 
        <th class="col_heading level0 col3" >Per Student Budget</th> 
        <th class="col_heading level0 col4" >Average Math Score</th> 
        <th class="col_heading level0 col5" >Average Reading Score</th> 
        <th class="col_heading level0 col6" >% Passing Math</th> 
        <th class="col_heading level0 col7" >% Passing Reading</th> 
        <th class="col_heading level0 col8" >Overall Passing Rate</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_a2298a24_571c_11e8_825e_720002f9a650level0_row0" class="row_heading level0 row0" >Figueroa High School</th> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row0_col0" class="data row0 col0" >District</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row0_col1" class="data row0 col1" >2,949</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row0_col2" class="data row0 col2" >$1,884,411</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row0_col3" class="data row0 col3" >$639</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row0_col4" class="data row0 col4" >76.7118</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row0_col5" class="data row0 col5" >81.158</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row0_col6" class="data row0 col6" >88.4%</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row0_col7" class="data row0 col7" >100.0%</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row0_col8" class="data row0 col8" >94.2%</td> 
    </tr>    <tr> 
        <th id="T_a2298a24_571c_11e8_825e_720002f9a650level0_row1" class="row_heading level0 row1" >Rodriguez High School</th> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row1_col0" class="data row1 col0" >District</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row1_col1" class="data row1 col1" >3,999</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row1_col2" class="data row1 col2" >$2,547,363</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row1_col3" class="data row1 col3" >$637</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row1_col4" class="data row1 col4" >76.8427</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row1_col5" class="data row1 col5" >80.7447</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row1_col6" class="data row1 col6" >88.5%</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row1_col7" class="data row1 col7" >100.0%</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row1_col8" class="data row1 col8" >94.3%</td> 
    </tr>    <tr> 
        <th id="T_a2298a24_571c_11e8_825e_720002f9a650level0_row2" class="row_heading level0 row2" >Huang High School</th> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row2_col0" class="data row2 col0" >District</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row2_col1" class="data row2 col1" >2,917</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row2_col2" class="data row2 col2" >$1,910,635</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row2_col3" class="data row2 col3" >$655</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row2_col4" class="data row2 col4" >76.6294</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row2_col5" class="data row2 col5" >81.1827</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row2_col6" class="data row2 col6" >88.9%</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row2_col7" class="data row2 col7" >100.0%</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row2_col8" class="data row2 col8" >94.4%</td> 
    </tr>    <tr> 
        <th id="T_a2298a24_571c_11e8_825e_720002f9a650level0_row3" class="row_heading level0 row3" >Hernandez High School</th> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row3_col0" class="data row3 col0" >District</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row3_col1" class="data row3 col1" >4,635</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row3_col2" class="data row3 col2" >$3,022,020</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row3_col3" class="data row3 col3" >$652</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row3_col4" class="data row3 col4" >77.2898</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row3_col5" class="data row3 col5" >80.9344</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row3_col6" class="data row3 col6" >89.1%</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row3_col7" class="data row3 col7" >100.0%</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row3_col8" class="data row3 col8" >94.5%</td> 
    </tr>    <tr> 
        <th id="T_a2298a24_571c_11e8_825e_720002f9a650level0_row4" class="row_heading level0 row4" >Johnson High School</th> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row4_col0" class="data row4 col0" >District</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row4_col1" class="data row4 col1" >4,761</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row4_col2" class="data row4 col2" >$3,094,650</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row4_col3" class="data row4 col3" >$650</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row4_col4" class="data row4 col4" >77.0725</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row4_col5" class="data row4 col5" >80.9664</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row4_col6" class="data row4 col6" >89.2%</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row4_col7" class="data row4 col7" >100.0%</td> 
        <td id="T_a2298a24_571c_11e8_825e_720002f9a650row4_col8" class="data row4 col8" >94.6%</td> 
    </tr></tbody> 
</table> 




```python
#Find and breakdown grades data by year in school 

freshman_df = students_df.loc[students_df["grade"] == "9th"].groupby("school", as_index=False)
sophomore_df = students_df.loc[students_df["grade"] == "10th"].groupby("school", as_index=False)
junior_df = students_df.loc[students_df["grade"] == "11th"].groupby("school", as_index=False)
senior_df = students_df.loc[students_df["grade"] == "12th"].groupby("school", as_index=False)
```


```python
# freshman_df.head()
```


```python
#Group and find average math score by grade 
freshman_math_mean = pd.DataFrame(freshman_df["math_score"].mean())
sophomore_math_mean = pd.DataFrame(sophomore_df["math_score"].mean())
junior_math_mean = pd.DataFrame(junior_df["math_score"].mean())
senior_math_mean = pd.DataFrame(senior_df["math_score"].mean())

```


```python
#Group and find average readin score by grade 
freshman_reading_mean = pd.DataFrame(freshman_df["reading_score"].mean())
sophomore_reading_mean = pd.DataFrame(sophomore_df["reading_score"].mean())
junior_reading_mean = pd.DataFrame(junior_df["reading_score"].mean())
senior_reading_mean = pd.DataFrame(senior_df["reading_score"].mean())
```


```python
#Merge math by grade to summary table (merge on right error??)

math_grade = pd.merge(freshman_math_mean, sophomore_math_mean, on="school")
# math_grade = pd.merge(sophomore_math_mean, on="school")
math_grade = pd.merge(math_grade, junior_math_mean, on="school") 
math_grade = pd.merge(math_grade, senior_math_mean, on="school")
math_grade.columns = ["school","freshman","sophomore","junior","senior"]

#print(math_grade)
```


```python
#Merge reading by grade to summary table (merge on right error?? still..)

reading_grade = pd.merge(freshman_reading_mean, sophomore_reading_mean, on="school")
# math_grade = pd.merge(sophomore_reading_mean, on="school")
reading_grade = pd.merge(reading_grade, junior_reading_mean, on="school") 
reading_grade = pd.merge(reading_grade, senior_reading_mean, on="school")
reading_grade.columns = ["school","freshman","sophomore","junior","senior"]
print(reading_grade)
```

                       school   freshman  sophomore     junior     senior
    0      Bailey High School  81.303155  80.907183  80.945643  80.912451
    1     Cabrera High School  83.676136  84.253219  83.788382  84.287958
    2    Figueroa High School  81.198598  81.408912  80.640339  81.384863
    3        Ford High School  80.632653  81.262712  80.403642  80.662338
    4     Griffin High School  83.369193  83.706897  84.288089  84.013699
    5   Hernandez High School  80.866860  80.660147  81.396140  80.857143
    6      Holden High School  83.677165  83.324561  83.815534  84.698795
    7       Huang High School  81.290284  81.512386  81.417476  80.305983
    8     Johnson High School  81.260714  80.773431  80.616027  81.227564
    9        Pena High School  83.807273  83.612000  84.335938  84.591160
    10  Rodriguez High School  80.993127  80.629808  80.864811  80.376426
    11    Shelton High School  84.122642  83.441964  84.373786  82.781671
    12     Thomas High School  83.728850  84.254157  83.585542  83.831361
    13     Wilson High School  83.939778  84.021452  83.764608  84.317673
    14     Wright High School  83.833333  83.812757  84.156322  84.073171


# Math Score By Grade


```python
#format and display table Math Score by Grade
math_grade.style.format({'freshman': '{:.2f}', 
                          'sophomore': '{:.2f}', 
                          'junior': "{:.2f}", 
                          'senior': "{:.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_aa454a90_571c_11e8_9173_720002f9a650" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >school</th> 
        <th class="col_heading level0 col1" >freshman</th> 
        <th class="col_heading level0 col2" >sophomore</th> 
        <th class="col_heading level0 col3" >junior</th> 
        <th class="col_heading level0 col4" >senior</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row0_col0" class="data row0 col0" >Bailey High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row0_col1" class="data row0 col1" >77.08</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row0_col2" class="data row0 col2" >77.00</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row0_col3" class="data row0 col3" >77.52</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row0_col4" class="data row0 col4" >76.49</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row1_col0" class="data row1 col0" >Cabrera High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row1_col1" class="data row1 col1" >83.09</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row1_col2" class="data row1 col2" >83.15</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row1_col3" class="data row1 col3" >82.77</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row1_col4" class="data row1 col4" >83.28</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row2_col0" class="data row2 col0" >Figueroa High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row2_col1" class="data row2 col1" >76.40</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row2_col2" class="data row2 col2" >76.54</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row2_col3" class="data row2 col3" >76.88</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row2_col4" class="data row2 col4" >77.15</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row3" class="row_heading level0 row3" >3</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row3_col0" class="data row3 col0" >Ford High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row3_col1" class="data row3 col1" >77.36</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row3_col2" class="data row3 col2" >77.67</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row3_col3" class="data row3 col3" >76.92</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row3_col4" class="data row3 col4" >76.18</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row4" class="row_heading level0 row4" >4</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row4_col0" class="data row4 col0" >Griffin High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row4_col1" class="data row4 col1" >82.04</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row4_col2" class="data row4 col2" >84.23</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row4_col3" class="data row4 col3" >83.84</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row4_col4" class="data row4 col4" >83.36</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row5" class="row_heading level0 row5" >5</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row5_col0" class="data row5 col0" >Hernandez High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row5_col1" class="data row5 col1" >77.44</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row5_col2" class="data row5 col2" >77.34</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row5_col3" class="data row5 col3" >77.14</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row5_col4" class="data row5 col4" >77.19</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row6" class="row_heading level0 row6" >6</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row6_col0" class="data row6 col0" >Holden High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row6_col1" class="data row6 col1" >83.79</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row6_col2" class="data row6 col2" >83.43</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row6_col3" class="data row6 col3" >85.00</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row6_col4" class="data row6 col4" >82.86</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row7" class="row_heading level0 row7" >7</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row7_col0" class="data row7 col0" >Huang High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row7_col1" class="data row7 col1" >77.03</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row7_col2" class="data row7 col2" >75.91</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row7_col3" class="data row7 col3" >76.45</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row7_col4" class="data row7 col4" >77.23</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row8" class="row_heading level0 row8" >8</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row8_col0" class="data row8 col0" >Johnson High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row8_col1" class="data row8 col1" >77.19</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row8_col2" class="data row8 col2" >76.69</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row8_col3" class="data row8 col3" >77.49</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row8_col4" class="data row8 col4" >76.86</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row9" class="row_heading level0 row9" >9</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row9_col0" class="data row9 col0" >Pena High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row9_col1" class="data row9 col1" >83.63</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row9_col2" class="data row9 col2" >83.37</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row9_col3" class="data row9 col3" >84.33</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row9_col4" class="data row9 col4" >84.12</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row10" class="row_heading level0 row10" >10</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row10_col0" class="data row10 col0" >Rodriguez High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row10_col1" class="data row10 col1" >76.86</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row10_col2" class="data row10 col2" >76.61</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row10_col3" class="data row10 col3" >76.40</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row10_col4" class="data row10 col4" >77.69</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row11" class="row_heading level0 row11" >11</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row11_col0" class="data row11 col0" >Shelton High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row11_col1" class="data row11 col1" >83.42</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row11_col2" class="data row11 col2" >82.92</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row11_col3" class="data row11 col3" >83.38</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row11_col4" class="data row11 col4" >83.78</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row12" class="row_heading level0 row12" >12</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row12_col0" class="data row12 col0" >Thomas High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row12_col1" class="data row12 col1" >83.59</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row12_col2" class="data row12 col2" >83.09</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row12_col3" class="data row12 col3" >83.50</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row12_col4" class="data row12 col4" >83.50</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row13" class="row_heading level0 row13" >13</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row13_col0" class="data row13 col0" >Wilson High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row13_col1" class="data row13 col1" >83.09</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row13_col2" class="data row13 col2" >83.72</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row13_col3" class="data row13 col3" >83.20</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row13_col4" class="data row13 col4" >83.04</td> 
    </tr>    <tr> 
        <th id="T_aa454a90_571c_11e8_9173_720002f9a650level0_row14" class="row_heading level0 row14" >14</th> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row14_col0" class="data row14 col0" >Wright High School</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row14_col1" class="data row14 col1" >83.26</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row14_col2" class="data row14 col2" >84.01</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row14_col3" class="data row14 col3" >83.84</td> 
        <td id="T_aa454a90_571c_11e8_9173_720002f9a650row14_col4" class="data row14 col4" >83.64</td> 
    </tr></tbody> 
</table> 



# Reading Score By Grade


```python
#format and display table Reading Score by Grade
reading_grade.style.format({'freshman': '{:.2f}', 
                          'sophomore': '{:.2f}', 
                          'junior': "{:.2f}", 
                          'senior': "{:.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >school</th> 
        <th class="col_heading level0 col1" >freshman</th> 
        <th class="col_heading level0 col2" >sophomore</th> 
        <th class="col_heading level0 col3" >junior</th> 
        <th class="col_heading level0 col4" >senior</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row0_col0" class="data row0 col0" >Bailey High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row0_col1" class="data row0 col1" >81.30</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row0_col2" class="data row0 col2" >80.91</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row0_col3" class="data row0 col3" >80.95</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row0_col4" class="data row0 col4" >80.91</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row1_col0" class="data row1 col0" >Cabrera High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row1_col1" class="data row1 col1" >83.68</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row1_col2" class="data row1 col2" >84.25</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row1_col3" class="data row1 col3" >83.79</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row1_col4" class="data row1 col4" >84.29</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row2_col0" class="data row2 col0" >Figueroa High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row2_col1" class="data row2 col1" >81.20</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row2_col2" class="data row2 col2" >81.41</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row2_col3" class="data row2 col3" >80.64</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row2_col4" class="data row2 col4" >81.38</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row3" class="row_heading level0 row3" >3</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row3_col0" class="data row3 col0" >Ford High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row3_col1" class="data row3 col1" >80.63</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row3_col2" class="data row3 col2" >81.26</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row3_col3" class="data row3 col3" >80.40</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row3_col4" class="data row3 col4" >80.66</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row4" class="row_heading level0 row4" >4</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row4_col0" class="data row4 col0" >Griffin High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row4_col1" class="data row4 col1" >83.37</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row4_col2" class="data row4 col2" >83.71</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row4_col3" class="data row4 col3" >84.29</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row4_col4" class="data row4 col4" >84.01</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row5" class="row_heading level0 row5" >5</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row5_col0" class="data row5 col0" >Hernandez High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row5_col1" class="data row5 col1" >80.87</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row5_col2" class="data row5 col2" >80.66</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row5_col3" class="data row5 col3" >81.40</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row5_col4" class="data row5 col4" >80.86</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row6" class="row_heading level0 row6" >6</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row6_col0" class="data row6 col0" >Holden High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row6_col1" class="data row6 col1" >83.68</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row6_col2" class="data row6 col2" >83.32</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row6_col3" class="data row6 col3" >83.82</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row6_col4" class="data row6 col4" >84.70</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row7" class="row_heading level0 row7" >7</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row7_col0" class="data row7 col0" >Huang High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row7_col1" class="data row7 col1" >81.29</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row7_col2" class="data row7 col2" >81.51</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row7_col3" class="data row7 col3" >81.42</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row7_col4" class="data row7 col4" >80.31</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row8" class="row_heading level0 row8" >8</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row8_col0" class="data row8 col0" >Johnson High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row8_col1" class="data row8 col1" >81.26</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row8_col2" class="data row8 col2" >80.77</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row8_col3" class="data row8 col3" >80.62</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row8_col4" class="data row8 col4" >81.23</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row9" class="row_heading level0 row9" >9</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row9_col0" class="data row9 col0" >Pena High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row9_col1" class="data row9 col1" >83.81</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row9_col2" class="data row9 col2" >83.61</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row9_col3" class="data row9 col3" >84.34</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row9_col4" class="data row9 col4" >84.59</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row10" class="row_heading level0 row10" >10</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row10_col0" class="data row10 col0" >Rodriguez High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row10_col1" class="data row10 col1" >80.99</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row10_col2" class="data row10 col2" >80.63</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row10_col3" class="data row10 col3" >80.86</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row10_col4" class="data row10 col4" >80.38</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row11" class="row_heading level0 row11" >11</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row11_col0" class="data row11 col0" >Shelton High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row11_col1" class="data row11 col1" >84.12</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row11_col2" class="data row11 col2" >83.44</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row11_col3" class="data row11 col3" >84.37</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row11_col4" class="data row11 col4" >82.78</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row12" class="row_heading level0 row12" >12</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row12_col0" class="data row12 col0" >Thomas High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row12_col1" class="data row12 col1" >83.73</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row12_col2" class="data row12 col2" >84.25</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row12_col3" class="data row12 col3" >83.59</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row12_col4" class="data row12 col4" >83.83</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row13" class="row_heading level0 row13" >13</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row13_col0" class="data row13 col0" >Wilson High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row13_col1" class="data row13 col1" >83.94</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row13_col2" class="data row13 col2" >84.02</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row13_col3" class="data row13 col3" >83.76</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row13_col4" class="data row13 col4" >84.32</td> 
    </tr>    <tr> 
        <th id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650level0_row14" class="row_heading level0 row14" >14</th> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row14_col0" class="data row14 col0" >Wright High School</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row14_col1" class="data row14 col1" >83.83</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row14_col2" class="data row14 col2" >83.81</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row14_col3" class="data row14 col3" >84.16</td> 
        <td id="T_ae1e68d8_571c_11e8_8d9a_720002f9a650row14_col4" class="data row14 col4" >84.07</td> 
    </tr></tbody> 
</table> 




```python
# Scores by School Budget per Student
bins = [0, 584.999, 614.999, 644.999, 999999]
group_names = ["0 to 585", "585 to 615", "615 to 645", "645 to 675"]
school_student_budget_scores = school_summary_table[["Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "Overall Passing Rate"]].groupby(pd.cut(school_summary_table["Per Student Budget"], bins=bins, labels=group_names )).mean() 
```

# Scores By School Spending


```python
#formating school budget (spending) per student table cells
school_student_budget_scores.style.format({'Average Math Score': '{:.1f}', 
                              'Average Reading Score': '{:.1f}', 
                              '% Passing Math': '{:.1%}', 
                              '% Passing Reading':'{:.1%}', 
                              'Overall Passing Rate': '{:.1%}'})
```




<style  type="text/css" >
</style>  
<table id="T_b08324c2_571c_11e8_8f9a_720002f9a650" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Average Math Score</th> 
        <th class="col_heading level0 col1" >Average Reading Score</th> 
        <th class="col_heading level0 col2" >% Passing Math</th> 
        <th class="col_heading level0 col3" >% Passing Reading</th> 
        <th class="col_heading level0 col4" >Overall Passing Rate</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Per Student Budget</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_b08324c2_571c_11e8_8f9a_720002f9a650level0_row0" class="row_heading level0 row0" >0 to 585</th> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row0_col0" class="data row0 col0" >83.5</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row0_col1" class="data row0 col1" >83.9</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row0_col2" class="data row0 col2" >100.0%</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row0_col3" class="data row0 col3" >100.0%</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row0_col4" class="data row0 col4" >100.0%</td> 
    </tr>    <tr> 
        <th id="T_b08324c2_571c_11e8_8f9a_720002f9a650level0_row1" class="row_heading level0 row1" >585 to 615</th> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row1_col0" class="data row1 col0" >83.6</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row1_col1" class="data row1 col1" >83.9</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row1_col2" class="data row1 col2" >100.0%</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row1_col3" class="data row1 col3" >100.0%</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row1_col4" class="data row1 col4" >100.0%</td> 
    </tr>    <tr> 
        <th id="T_b08324c2_571c_11e8_8f9a_720002f9a650level0_row2" class="row_heading level0 row2" >615 to 645</th> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row2_col0" class="data row2 col0" >79.1</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row2_col1" class="data row2 col1" >81.9</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row2_col2" class="data row2 col2" >92.6%</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row2_col3" class="data row2 col3" >100.0%</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row2_col4" class="data row2 col4" >96.3%</td> 
    </tr>    <tr> 
        <th id="T_b08324c2_571c_11e8_8f9a_720002f9a650level0_row3" class="row_heading level0 row3" >645 to 675</th> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row3_col0" class="data row3 col0" >77.0</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row3_col1" class="data row3 col1" >81.0</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row3_col2" class="data row3 col2" >89.0%</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row3_col3" class="data row3 col3" >100.0%</td> 
        <td id="T_b08324c2_571c_11e8_8f9a_720002f9a650row3_col4" class="data row3 col4" >94.5%</td> 
    </tr></tbody> 
</table> 




```python
# Scores by School Size
bins = [0, 1000, 2500, 50000]
group_names = ["Small < 1000", "Medium 1000 to 2500", "Large 2500 to 10000"]
school_student_scores_size = school_summary_table[["Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "Overall Passing Rate"]].groupby(pd.cut(school_summary_table["Total Students"], bins=bins, labels=group_names )).mean()

```

# Scores By School Size


```python
#formating school by size table cells
school_student_scores_size.style.format({'Average Math Score': '{:.1f}', 
                              'Average Reading Score': '{:.1f}', 
                              '% Passing Math': '{:.1%}', 
                              '% Passing Reading':'{:.1%}', 
                              'Overall Passing Rate': '{:.1%}'})
```




<style  type="text/css" >
</style>  
<table id="T_b2642908_571c_11e8_a205_720002f9a650" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Average Math Score</th> 
        <th class="col_heading level0 col1" >Average Reading Score</th> 
        <th class="col_heading level0 col2" >% Passing Math</th> 
        <th class="col_heading level0 col3" >% Passing Reading</th> 
        <th class="col_heading level0 col4" >Overall Passing Rate</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Total Students</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_b2642908_571c_11e8_a205_720002f9a650level0_row0" class="row_heading level0 row0" >Small < 1000</th> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row0_col0" class="data row0 col0" >83.8</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row0_col1" class="data row0 col1" >83.9</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row0_col2" class="data row0 col2" >100.0%</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row0_col3" class="data row0 col3" >100.0%</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row0_col4" class="data row0 col4" >100.0%</td> 
    </tr>    <tr> 
        <th id="T_b2642908_571c_11e8_a205_720002f9a650level0_row1" class="row_heading level0 row1" >Medium 1000 to 2500</th> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row1_col0" class="data row1 col0" >83.4</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row1_col1" class="data row1 col1" >83.9</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row1_col2" class="data row1 col2" >100.0%</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row1_col3" class="data row1 col3" >100.0%</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row1_col4" class="data row1 col4" >100.0%</td> 
    </tr>    <tr> 
        <th id="T_b2642908_571c_11e8_a205_720002f9a650level0_row2" class="row_heading level0 row2" >Large 2500 to 10000</th> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row2_col0" class="data row2 col0" >77.0</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row2_col1" class="data row2 col1" >81.0</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row2_col2" class="data row2 col2" >89.0%</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row2_col3" class="data row2 col3" >100.0%</td> 
        <td id="T_b2642908_571c_11e8_a205_720002f9a650row2_col4" class="data row2 col4" >94.5%</td> 
    </tr></tbody> 
</table> 




```python
# Scores by School Type
school_type_summary_table = school_summary_table
school_type_summary_table["School Type"] = school_type_summary_table["School Type"].replace({"Charter": 1, "District": 2})

```


```python
#print(school_type_summary_table)
```


```python
bins = [0, 1, 2]
group_names = ["Charter", "District"]
student_scores_school_type  = school_type_summary_table[["Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "Overall Passing Rate"]].groupby(pd.cut(school_type_summary_table["School Type"], bins=bins, labels=group_names)).mean()
```


```python
#print(student_scores_school_type)
```


```python
#student_scores_school_type.head()
```

# Scores By School Type


```python
#formating
student_scores_school_type.style.format({'Average Math Score': '{:.1f}', 
                              'Average Reading Score': '{:.1f}', 
                              '% Passing Math': '{:.1%}', 
                              '% Passing Reading':'{:.1%}', 
                              'Overall Passing Rate': '{:.1%}'})

```




<style  type="text/css" >
</style>  
<table id="T_b94bf39a_571c_11e8_a3d6_720002f9a650" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Average Math Score</th> 
        <th class="col_heading level0 col1" >Average Reading Score</th> 
        <th class="col_heading level0 col2" >% Passing Math</th> 
        <th class="col_heading level0 col3" >% Passing Reading</th> 
        <th class="col_heading level0 col4" >Overall Passing Rate</th> 
    </tr>    <tr> 
        <th class="index_name level0" >School Type</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_b94bf39a_571c_11e8_a3d6_720002f9a650level0_row0" class="row_heading level0 row0" >Charter</th> 
        <td id="T_b94bf39a_571c_11e8_a3d6_720002f9a650row0_col0" class="data row0 col0" >83.5</td> 
        <td id="T_b94bf39a_571c_11e8_a3d6_720002f9a650row0_col1" class="data row0 col1" >83.9</td> 
        <td id="T_b94bf39a_571c_11e8_a3d6_720002f9a650row0_col2" class="data row0 col2" >100.0%</td> 
        <td id="T_b94bf39a_571c_11e8_a3d6_720002f9a650row0_col3" class="data row0 col3" >100.0%</td> 
        <td id="T_b94bf39a_571c_11e8_a3d6_720002f9a650row0_col4" class="data row0 col4" >100.0%</td> 
    </tr>    <tr> 
        <th id="T_b94bf39a_571c_11e8_a3d6_720002f9a650level0_row1" class="row_heading level0 row1" >District</th> 
        <td id="T_b94bf39a_571c_11e8_a3d6_720002f9a650row1_col0" class="data row1 col0" >77.0</td> 
        <td id="T_b94bf39a_571c_11e8_a3d6_720002f9a650row1_col1" class="data row1 col1" >81.0</td> 
        <td id="T_b94bf39a_571c_11e8_a3d6_720002f9a650row1_col2" class="data row1 col2" >89.0%</td> 
        <td id="T_b94bf39a_571c_11e8_a3d6_720002f9a650row1_col3" class="data row1 col3" >100.0%</td> 
        <td id="T_b94bf39a_571c_11e8_a3d6_720002f9a650row1_col4" class="data row1 col4" >94.5%</td> 
    </tr></tbody> 
</table> 




```python
######
```

#END
