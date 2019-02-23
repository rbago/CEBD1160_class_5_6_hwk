# CEBD1160_class_5_6_hwk

1. Write Pseudocode for how to 
A) load, 
B) "organize", 
C) compute summary statistics (all A-C were done in class today), 
D) Visualize the data, 1-feature (column) at a time, i.e. histogram, and save the figures to files 
E) Visualize the data, 2-features (columns) at a time, i.e. scatter plot, and save the figures to files,

2. (intermediate) 
F) Pseudocode for adding header data to your table, for an arbitrary one of these datasets,

3. (reach) 
G) Pseudocode for an additional type of plot (Google to find plot types of interest) for visualizing 2 or more of the features at a time.
Recommendation: plan to use `matplotlib` for plotting

Pseudocode

D-op1) Print out each column as a histogram
D1 - For n number of values add a symbol to represent it's repeated
D2 - Obtain name of column
D3 - Store or print the symbol * inline
D4 - Add new line for when the repeated number is complete
D5 - Save into a file with name of column

D-op2) Print out each column using the matplotlib library
D1 - Import matplolib library
D2 - For n number of features
D3 - Set labels for axis y and axis x
D4 - Create histogram with .hist function
D5 - Save into a file

E) Print out each 2 columns using the matplotlib library
E1 - If already matplolib already imported follow next steps below otherwise import
E2 - For column A prepare scatter plot with column B and then C until last column
E3 - Print and store in file
E4 - For column B prepare scatter plot with column C and the next until last
E5 - Repeat until reaching last 2 columns

2. 
F1 - Obtain first row
F2 - Try to turn into numeric
F3 - If there's an errror than take that row and add it as the header
F4 - If there's no error, request to input the name for each header for N number of columns
F5 - Add that input

