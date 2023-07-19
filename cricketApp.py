import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

odi_bat=pd.read_csv("D:\\pyfolder\\aiWithPython\\odi\\ODI data.csv")
odi_bowl=pd.read_csv("D:\\pyfolder\\aiWithPython\\odi\\Bowling_ODI.csv")
odi_field=pd.read_csv("D:\\pyfolder\\aiWithPython\\odi\\Fielding_ODI.csv")
t20_bat=pd.read_csv("D:\\pyfolder\\aiWithPython\\t20\\t20.csv")
t20_bowl=pd.read_csv("D:\\pyfolder\\aiWithPython\\t20\\Bowling_t20.csv")
t20_field=pd.read_csv("D:\\pyfolder\\aiWithPython\\t20\\Fielding_t20.csv")
test_bat=pd.read_csv("D:\\pyfolder\\aiWithPython\\test\\test.csv")
test_bowl=pd.read_csv("D:\\pyfolder\\aiWithPython\\test\\Bowling_test.csv")
test_field=pd.read_csv("D:\\pyfolder\\aiWithPython\\test\\Fielding_test.csv")
odi_bat=odi_bat.iloc[:,1:]
odi_bowl=odi_bowl.iloc[:,1:]
odi_field=odi_field.iloc[:,1:]
t20_bat=t20_bat.iloc[:,1:]
t20_bowl=t20_bowl.iloc[:,1:]
t20_field=t20_field.iloc[:,1:]
test_bat=test_bat.iloc[:,1:]
test_bowl=test_bowl.iloc[:,1:]
test_field=test_field.iloc[:,2:]



st.title('Cricket App')
st.write("""
# Simple Cricket App
Shown are the stats of the players
""")

# Sidebar options
view_option = st.sidebar.radio('Select View', ['Statistics', 'Scatter Plots'])
Format=st.sidebar.selectbox('Select Format', ['ODI', 'T20', 'Test'])
selected_format = st.sidebar.selectbox('Select Role', ['Bowling', 'Batting', 'Fielding'])


def showDetails_Fielding(DataFrame,noOfCatches,noOfStumpings):
    if noOfCatches>0:
        if noOfStumpings>0:
            return DataFrame[(DataFrame["Ct"]>=noOfCatches)&(DataFrame["St"]>=noOfStumpings)]
        else:
            return DataFrame[(DataFrame["Ct"]>=noOfCatches)]
    else:
        if noOfStumpings>0:
            return DataFrame[(DataFrame["St"]>=noOfStumpings)]
        else:
            return DataFrame

def showDetails_Batting(DataFrame,avg_range,num_50,num_100):
    if avg_range[1]>0:
            if num_100>0:
                if num_50>0:
                    return DataFrame[(DataFrame["Ave"]>=avg_range[0])& (DataFrame["Ave"]<=avg_range[1]) &(DataFrame["100"]>=num_100 )&(DataFrame["50"]>=num_50)]
            if num_100>0:
                return DataFrame[(DataFrame["Ave"]>=avg_range[0])& (DataFrame["Ave"]<=avg_range[1]) &(DataFrame["100"]>=num_100)]
            if num_50>0:
                return DataFrame[(DataFrame["Ave"]>=avg_range[0])& (DataFrame["Ave"]<=avg_range[1]) &(DataFrame["50"]>=num_50)]    
    if avg_range[1]>0:
         return DataFrame[(DataFrame["Ave"]>=avg_range[0])&(DataFrame["Ave"]<=avg_range[1])]
    if num_100>0:
        return DataFrame[(DataFrame["100"]==num_100)]
    if num_50>0:
        return DataFrame[(DataFrame["50"]==num_50)]
    else:
        return DataFrame

def ShowDetails_Bowling(DataFrame,num_wickets,num_5w,avg_range):
    if num_wickets>0:
        if num_5w>0:
            if avg_range[1]>0:
                return DataFrame[(DataFrame["Wkts"]>=num_wickets)&(DataFrame["5"]>=num_5w)&(DataFrame["Ave"]>=avg_range[0])&(DataFrame["Ave"]<=avg_range[1])]
            else:
                return DataFrame[(DataFrame["Wkts"]>=num_wickets)&(DataFrame["5"]>=num_5w)]
        else:
            if avg_range[1]>0:
                return DataFrame[(DataFrame["Wkts"]>=num_wickets)&(DataFrame["Ave"]>=avg_range[0])&(DataFrame["Ave"]<=avg_range[1])]
            else:
                return DataFrame[(DataFrame["Wkts"]>=num_wickets)]
    else:
        if num_5w>0:
            if avg_range[1]>0:
                return DataFrame[(DataFrame["5"]>=num_5w)&(DataFrame["Ave"]>=avg_range[0])&(DataFrame["Ave"]<=avg_range[1])]
            else:
                return DataFrame[(DataFrame["5"]==num_5w)]
        else:
            if avg_range[1]>0:
                return DataFrame[(DataFrame["Ave"]>=avg_range[0])&(DataFrame["Ave"]<=avg_range[1])]
            else:
                return DataFrame

if view_option=="Statistics":
    if selected_format=="Batting":
        
        avg_range = (st.sidebar.slider('Select average range', min_value=0.0, max_value=100.0, value=(0.0,100.0)))
        num_50 = int(st.sidebar.number_input('Number of 50s:', min_value=0, max_value=100))
        num_100 = int(st.sidebar.number_input('Number of 100s:', min_value=0, max_value=100))
        print(type(odi_bat["Ave"]))
        if st.button('View Stats'):
            if Format=="ODI":
                
                st.write(showDetails_Batting(odi_bat,avg_range,num_50,num_100))
            elif Format=="T20":
                st.write( showDetails_Batting(t20_bat,avg_range,num_50,num_100))
            elif Format=="Test":
                st.write(showDetails_Batting(test_bat,avg_range,num_50,num_100))


    

        
    if selected_format=="Bowling":
        avg_range_bowl = (st.sidebar.slider('Select average range', min_value=0.0, max_value=100.0, value=(0.0,100.0)))
        num_wickets = st.sidebar.number_input('Number of wickets:', min_value=0, max_value=1000)
        num_5w = st.sidebar.number_input('Number of 5w:', min_value=0, max_value=100)
        if st.button('View Stats'):
            if Format=="ODI":
                st.write(ShowDetails_Bowling(odi_bowl,num_wickets,num_5w,avg_range_bowl))
            elif Format=="T20":
                st.write(ShowDetails_Bowling(t20_bowl,num_wickets,num_5w,avg_range_bowl))
            elif Format=="Test":
                st.write(ShowDetails_Bowling(test_bowl,num_wickets,num_5w,avg_range_bowl))
    
    if selected_format=="Fielding":
        noOfCatches = st.sidebar.number_input('Number of catches:', min_value=0, max_value=500)
        noOfStumpings = st.sidebar.number_input('Number of stumpings:', min_value=0, max_value=1000)
        if st.button('View Stats'):
            if Format=="ODI":
                st.write(showDetails_Fielding(odi_field,noOfCatches,noOfStumpings))
            elif Format=="T20":
                st.write(showDetails_Fielding(t20_field,noOfCatches,noOfStumpings))
            elif Format=="Test":
                st.write(showDetails_Fielding(test_field,noOfCatches,noOfStumpings))

if view_option=="Scatter Plots":
    if selected_format=="Batting":
        if Format=="ODI":
            st.write("""# ODI Batting""")
            fig, ax = plt.subplots()
            ax.scatter(odi_bat['Mat'], odi_bat['Ave'])
            ax.set_xlabel('Number of Matches')
            ax.set_ylabel('Batting Average')
            ax.set_title('Batting Average vs Number of Matches')
            st.pyplot(fig)
        elif Format=="T20":
            st.write("""# T20 Batting""")
            fig, ax = plt.subplots()
            ax.scatter(t20_bat['Mat'], t20_bat['Ave'])
            ax.set_xlabel('Number of Matches')
            ax.set_ylabel('Batting Average')
            ax.set_title('Batting Average vs Number of Matches')
            st.pyplot(fig)

        elif Format=="Test":
            st.write("""# Test Batting""")
            fig, ax = plt.subplots()
            ax.scatter(test_bat['Mat'], test_bat['Ave'])
            ax.set_xlabel('Number of Matches')
            ax.set_ylabel('Batting Average')
            ax.set_title('Batting Average vs Number of Matches')
            st.pyplot(fig)
    if selected_format=="Bowling":
        if Format=="ODI":
            st.write("""# ODI Bowling""")
            fig, ax = plt.subplots()
            ax.scatter(odi_bowl['Mat'], odi_bowl['Ave'])
            ax.set_xlabel('Number of Matches')
            ax.set_ylabel('Bowling Average')
            ax.set_title('Bowling Average vs Number of Matches')
            st.pyplot(fig)
        elif Format=="T20":
            st.write("""# T20 Bowling""")
            fig, ax = plt.subplots()
            ax.scatter(t20_bowl['Mat'], t20_bowl['Ave'])
            ax.set_xlabel('Number of Matches')
            ax.set_ylabel('Bowling Average')
            ax.set_title('Bowling Average vs Number of Matches')
            st.pyplot(fig)

        elif Format=="Test":
            st.write("""# Test Bowling""")
            fig, ax = plt.subplots()
            ax.scatter(test_bowl['Mat'], test_bowl['Ave'])
            ax.set_xlabel('Number of Matches')
            ax.set_ylabel('Bowling Average')
            ax.set_title('Bowling Average vs Number of Matches')
            st.pyplot(fig)
    if selected_format=="Fielding":
        if Format=="ODI":
            st.write("""# ODI Fielding""")
            fig, ax = plt.subplots()
            ax.scatter(odi_field['Mat'], odi_field['Ct'])
            ax.set_xlabel('Number of Matches')
            ax.set_ylabel('Number of Catches')
            ax.set_title('Number of Catches vs Number of Matches')
            st.pyplot(fig)
        elif Format=="T20":
            st.write("""# T20 Fielding""")
            fig, ax = plt.subplots()
            ax.scatter(t20_field['Mat'], t20_field['Ct'])
            ax.set_xlabel('Number of Matches')
            ax.set_ylabel('Number of Catches')
            ax.set_title('Number of Catches vs Number of Matches')
            st.pyplot(fig)
        elif Format=="Test":
            st.write("""# Test Fielding""")
            fig, ax = plt.subplots()
            ax.scatter(test_field['Mat'], test_field['Ct'])
            ax.set_xlabel('Number of Matches')
            ax.set_ylabel('Number of Catches')
            ax.set_title('Number of Catches vs Number of Matches')
            st.pyplot(fig)















# st.write("""
# # ODI Batting
# """)
# st.write("""
# # ODI Bowling
# """)
# st.write("""
# # ODI Fielding
# """)
# st.write("""
# # T20 Batting
# """)
# st.write("""
# # T20 Bowling
# """)
# st.write("""
# # T20 Fielding
# """)
# st.write("""
# # Test Batting
# """)
# st.write("""
# # Test Bowling
# """)
# st.write("""
# # Test Fielding
# """)
