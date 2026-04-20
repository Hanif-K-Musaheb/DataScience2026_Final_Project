import matplotlib.pyplot as plt
import pandas as pd

class Chart:
    def __init__(self, chart_type, df, x_col, pie_arr=[], y_col=None, figX=8, figY=4,bins=20):
        self.chart_type = chart_type.lower()
        self.figX = figX
        self.figY = figY
        self.df = df
        self.x_col = x_col
        self.y_col = y_col
        self.bins=bins
        self.pie_arr=pie_arr

    def make_chart(self):
        plt.figure(figsize=(self.figX, self.figY))
        
        if self.chart_type == 'bar': 
            self.__make_bar_chart()
        elif self.chart_type == 'scatter':
            if self.y_col is None:
                print("Error: A scatter plot requires a y_col to be specified!")
                return
            self.__make_scatter_chart()
        elif self.chart_type == 'density':
            self.__make_density_chart()
        elif self.chart_type == 'histogram':
            self.__make_histogram_chart()
        elif self.chart_type == 'pie':
            self.__make_pie_chart()
            
        plt.tight_layout()
        plt.show()

    def __make_bar_chart(self):
        self.df[self.x_col].value_counts().plot(kind='bar')
        plt.title(f'Bar Chart of {self.x_col}')
        plt.xlabel(self.x_col)
        plt.ylabel('Number of People')

    def __make_scatter_chart(self):
        plt.scatter(self.df[self.x_col], self.df[self.y_col])
        plt.title(f'Scatter Plot: {self.x_col} vs {self.y_col}')
        plt.xlabel(self.x_col)
        plt.ylabel(self.y_col)
        
    def __make_density_chart(self):
        # Creates the smooth line plot
        self.df[self.x_col].plot(kind='density')
        plt.title(f'Density Plot of {self.x_col}')
        plt.xlabel(self.x_col)
        plt.ylabel('Density')
        plt.xlim(left=0)
        plt.ylim(bottom=0)

    def __make_histogram_chart(self):
        self.df[self.x_col].plot(kind='hist', bins=self.bins, edgecolor='black')
        plt.title(f'Histogram of {self.x_col}')
        plt.xlabel(self.x_col)
        plt.ylabel('Frequency')
    
    def __make_pie_chart(self):
        # The autopct argument formats the numbers as percentages with one decimal place
        self.pie_arr.plot(kind='pie', autopct='%1.1f%%')
        plt.title(f'Pie Chart of {self.x_col}')
        plt.ylabel('') # Keeps the side of the chart looking clean
