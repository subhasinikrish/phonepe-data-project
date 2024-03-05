import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import json
import os
import requests
import json
import mysql.connector

#agg_ins_table from mysql
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query='''select * from agg_ins_table'''
mycursor.execute(query)
q=mycursor.fetchall()
agg_ins_table=pd.DataFrame(q,columns=["State","Year","Quarter","Transaction_name","Transaction_amount","Transaction_count"])

#agg_trans_table from mysql
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query='''select * from agg_trans_table'''
mycursor.execute(query)
q=mycursor.fetchall()
agg_trans_table=pd.DataFrame(q,columns=["State","Year","Quarter","Transaction_name","Transaction_amount","Transaction_count"])

#agg_user_table from mysql
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query='''select * from agg_user_table'''
mycursor.execute(query)
q=mycursor.fetchall()
agg_user_table=pd.DataFrame(q,columns=["State","Year","Quarter","Brand","Percentage","Transaction_count"])

#map_ins_table from mysql
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query='''select * from map_ins_table'''
mycursor.execute(query)
q=mycursor.fetchall()
map_ins_table=pd.DataFrame(q,columns=["State","Year","Quarter","District_name","Transaction_amount","Transaction_count"])

#map_trans_table from mysql
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query='''select * from map_trans_table'''
mycursor.execute(query)
q=mycursor.fetchall()
map_trans_table=pd.DataFrame(q,columns=["State","Year","Quarter","District_name","Transaction_amount","Transaction_count"])

#map_user_table from mysql
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query='''select * from map_user_table'''
mycursor.execute(query)
q=mycursor.fetchall()
map_user_table=pd.DataFrame(q,columns=["State","Year","Quarter","District_name","Registered_users","App_opens"])

#top_ins_table from mysql

connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query='''select * from top_ins_dist_table'''
mycursor.execute(query)
q=mycursor.fetchall()
top_ins_table=pd.DataFrame(q,columns=["State","Year","Quarter","District_name","Transaction_count","Transaction_amount"])

#top_trans_table from mysql

connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query='''select * from top_trans_dist_table'''
mycursor.execute(query)
q=mycursor.fetchall()
top_trans_table=pd.DataFrame(q,columns=["State","Year","Quarter","District_name","Transaction_count","Transaction_amount"])

#top_user_table from mysql
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query='''select * from top_user_dist_table'''
mycursor.execute(query)
q=mycursor.fetchall()
top_user_table=pd.DataFrame(q,columns=["State","Year","Quarter","District_name","Registered_users"])












#streamlit code

st.set_page_config(layout= "wide")
st.title("PHONEPE DATA VISUVALIZATION AND EXPLORATION")


st.header("MYSQL DATABASE DISPLAY")

DATAS=st.radio("select the option",("AGGREGATE TABLES","MAP TABLES","TOP TABLES"))


view_table= st.selectbox("select the table",("Choose an option","INSURANCE TABLE",
                    "TRANSACTION TABLE",
                    "USER TABLE"))
if DATAS=="Choose an option":
    pass

if DATAS=="AGGREGATE TABLES":
   
    if view_table=="INSURANCE TABLE": 
        st.table(agg_ins_table)
    elif view_table=="TRANSACTION TABLE":
        st.table(agg_trans_table)
    elif view_table=="USER TABLE":
        st.table(agg_user_table)
if DATAS=="MAP TABLES":

    if view_table=="INSURANCE TABLE":
         st.table(map_ins_table)
    elif view_table=="TRANSACTION TABLE":
        st.table(map_trans_table)
    elif view_table=="USER TABLE":
        st.table(map_user_table)

if DATAS=="TOP TABLES":
   

    if view_table=="INSURANCE TABLE":
         st.table(top_ins_table)
    elif view_table=="TRANSACTION TABLE":
        st.table(top_trans_table)
    elif view_table=="USER TABLE":
        st.table(top_user_table)











with st.sidebar:
    st.title(":blue[PROJECT DETAILS ]")
    st.header(":red[STEPS FOLLOWED]")
    st.caption("EXTRACTED DATA FROM PHONEPE PULSE GITHUB REPOSITORY")
    st.caption("TRANSFORMED THE DATA INTO SUITABLE FORMAT")
    st.caption("INSERTED THE TRANSFORMED DATA INTO MYSQL DB")
    st.caption("CREATED A LIVE GEO VISUVALIZATION DASHBOARD USING STREAMLIT AND PLOTLY")
    st.caption("FETCHED THE DATA FROM MYSQL TO DISPLAY IN THE DASHBOARD")
    st.caption("ANALYSIS 10 DIFFERENT QUERIES OF DATAS TO DISPLAY IN THE DASHBOARD")
    






#agg_ins_year
    
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query1='''select sum(Transaction_amount),sum(Transaction_count),State,Year from agg_ins_table group by State,Year'''
mycursor.execute(query1)
q1=mycursor.fetchall()
agg_ins_year=pd.DataFrame(q1,columns=["Transaction_amount","Transaction_count","State","Year"])

#agg-trans-year

connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query2='''select sum(Transaction_amount),sum(Transaction_count),State,Year from agg_trans_table group by State,Year'''
mycursor.execute(query2)
q2=mycursor.fetchall()
agg_trans_year=pd.DataFrame(q2,columns=["Transaction_amount","Transaction_count","State","Year"])


#agg_ins_quarter

connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query3='''select sum(Transaction_amount),sum(Transaction_count),State,Year,Quarter from agg_trans_table group by State,Year,Quarter'''
mycursor.execute(query3)
q3=mycursor.fetchall()
agg_ins_quarter=pd.DataFrame(q3,columns=["Transaction_amount","Transaction_count","State","Year","Quarter"])




#agg_trans_quarter

connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query4='''select sum(Transaction_amount),sum(Transaction_count),State,Year,Quarter from agg_trans_table group by State,Year,Quarter'''
mycursor.execute(query4)
q4=mycursor.fetchall()
agg_trans_quarter=pd.DataFrame(q4,columns=["Transaction_amount","Transaction_count","State","Year","Quarter"])

#agg transaction type with states

connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query6=connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()
query6='''select sum(Transaction_amount),sum(Transaction_count),Transaction_name,State from agg_trans_table  group by Transaction_name,State'''
mycursor.execute(query6)
q6=mycursor.fetchall()
agg_trans_type=pd.DataFrame(q6,columns=["Transaction_amount","Transaction_count","Transaction_name","State"])



#map_ins_table
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query5='''select sum(Transaction_amount),sum(Transaction_count),State,Year from map_ins_table group by State,Year'''
mycursor.execute(query5)
q5=mycursor.fetchall()
map_ins_year=pd.DataFrame(q5,columns=["Transaction_amount","Transaction_count","State","Year"])

#agg-user analysis  brand and transaction count with respect to year

connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()
query7='''select sum(Transaction_count),Brand,avg(Percentage),Year from agg_user_table group by Brand,Year'''
mycursor.execute(query7)
q7=mycursor.fetchall()
agg_user_brand_count=pd.DataFrame(q7,columns=["Transaction_count","Brand","Percentage","Year"])


#map insurance quarter analysis
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query8='''select sum(Transaction_amount),sum(Transaction_count),State,Year,Quarter from map_ins_table group by State,Year,Quarter'''
mycursor.execute(query8)
q8=mycursor.fetchall()
map_ins_quarter=pd.DataFrame(q8,columns=["Transaction_amount","Transaction_count","State","Year","Quarter"])

#top_innsurance year vice analysis
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query9='''select sum(Transaction_amount),sum(Transaction_count),State,Year from top_ins_dist_table group by State,Year'''
mycursor.execute(query9)
q9=mycursor.fetchall()
top_ins_year=pd.DataFrame(q9,columns=["Transaction_amount","Transaction_count","State","Year"])

#top insurance quarter analysis
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query10='''select sum(Transaction_amount),sum(Transaction_count),State,Year,Quarter from top_ins_dist_table group by State,Year,Quarter'''
mycursor.execute(query10)
q10=mycursor.fetchall()
top_ins_quarter=pd.DataFrame(q10,columns=["Transaction_amount","Transaction_count","State","Year","Quarter"])



#State wise registred users and app opens with respect to year from map user analysis
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query11='''select sum(Registered_users),sum(App_opens),Year,District_name,State from map_user_table group by Year,State,District_name'''
mycursor.execute(query11)
q11=mycursor.fetchall()
map_user_year=pd.DataFrame(q11,columns=["Registered_users","App_opens","Year","District_name","State"])

#State wise registred users and app opens with respect to Quarter,year from map user analysis
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query12='''select sum(Registered_users),sum(App_opens),Year,District_name,State,Quarter from map_user_table group by Year,State,District_name,Quarter'''
mycursor.execute(query12)
q12=mycursor.fetchall()
map_user_quarter=pd.DataFrame(q12,columns=["Registered_users","App_opens","Year","District_name","State","Quarter"])

#District wise registred users and app opens with respect to State from map user analysis
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query13='''select sum(Registered_users),sum(App_opens),State,District_name from map_user_table group by State,District_name'''
mycursor.execute(query13)
q13=mycursor.fetchall()
map_user_dist=pd.DataFrame(q13,columns=["Registered_users","App_opens","State","District_name"])

#Pincode wise registered userswith respect to year,State from top user analysis
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query13='''select sum(Registered_users),State,Year,Pincode from top_user_pin_table group by State,Year,Pincode'''
mycursor.execute(query13)
q13=mycursor.fetchall()
top_user_pin=pd.DataFrame(q13,columns=["Registered_users","State","Year","Pincode"])

#District wise registred userswith respect to year,State from top user analysis
connection=mysql.connector.connect(host="localhost",user="root",password="12345",database="phonepeproject")
mycursor=connection.cursor()

query14='''select sum(Registered_users),State,Year,District_name from top_user_dist_table group by State,Year,District_name'''
mycursor.execute(query14)
q14=mycursor.fetchall()
top_user_dist=pd.DataFrame(q14,columns=["Registered_users","State","Year","District_name"])




















#function for Transaction amount and count with respect to year

def Trans_amount_count(table,year):
    df1=table[table["Year"]==year]
    df1.reset_index(drop=True,inplace=True)

    col1,col2=st.columns(2)

    with col1:

        fig1=px.bar(df1,x="State",y="Transaction_amount",title=f"{year} TRANSACTION AMOUNT")
        st.plotly_chart(fig1)
    
    with col2:

        fig2=px.bar(df1,x="State",y="Transaction_count",title=f"{year} TRANSACTION COUNT")
        st.plotly_chart(fig2)

    
    india_url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(india_url)
    json_file=json.loads(response.content)
    
    states_list=[]
    for i in json_file["features"]:
        states_list.append(i['properties']['ST_NM'])
    states_list.sort()

    col1,col2=st.columns(2)

    with col1:
        fig_india1=px.choropleth(df1, geojson=json_file, locations="State", featureidkey="properties.ST_NM",
                                    color="Transaction_amount", color_continuous_scale="Rainbow", 
                                    range_color=(df1["Transaction_amount"].min(),df1["Transaction_amount"].max()),
                                    hover_name="State", title=f"{year} TRANSACTION AMOUNT", fitbounds="locations",height=600,width=600)
        
        fig_india1.update_geos(visible=False)

        st.plotly_chart(fig_india1)
    with col2:

        fig_india2=px.choropleth(df1, geojson=json_file, locations="State", featureidkey="properties.ST_NM",
                                    color="Transaction_count", color_continuous_scale="Rainbow", 
                                    range_color=(df1["Transaction_count"].min(),df1["Transaction_count"].max()),
                                    hover_name="State", title=f"{year} TRANSACTION COUNT", fitbounds="locations",height=600,width=600)
        
        fig_india2.update_geos(visible=False)

        st.plotly_chart(fig_india2)


    return

#function for Transaction amount and count with respect to quarter

def Trans_amount_count_quarter(table1,year,quarter):
    df=table1[table1["Year"]==year]
    df2=df[df["Quarter"]==quarter]
    df2.reset_index(drop=True,inplace=True)

    col1,col2=st.columns(2)

    with col1:
        fig1=px.bar(df2,x="State",y="Transaction_amount",title=f"{year} Quarter{quarter} TRANSACTION AMOUNT",height=600,width=600)
        st.plotly_chart(fig1)
    
    with col2:
        fig2=px.bar(df2,x="State",y="Transaction_count",title=f"{year} Quarter{quarter} TRANSACTION COUNT",height=600,width=600)
        st.plotly_chart(fig2)
    


    india_url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response=requests.get(india_url)
    json_file=json.loads(response.content)
    
    states_list=[]
    for i in json_file["features"]:
        states_list.append(i['properties']['ST_NM'])
    states_list.sort()

    col1,col2=st.columns(2)

    with col1:
    
        fig_india1=px.choropleth(df2, geojson=json_file, locations="State", featureidkey="properties.ST_NM",
                                    color="Transaction_amount", color_continuous_scale="Rainbow", 
                                    range_color=(df2["Transaction_amount"].min(),df2["Transaction_amount"].max()),
                                    hover_name="State", title=f"{year} Quarter{quarter} TRANSACTION AMOUNT", fitbounds="locations",height=600,width=600)
        
        fig_india1.update_geos(visible=False)

        st.plotly_chart(fig_india1)
    with col2:

        fig_india2=px.choropleth(df2, geojson=json_file, locations="State", featureidkey="properties.ST_NM",
                                    color="Transaction_count", color_continuous_scale="thermal", 
                                    range_color=(df2["Transaction_count"].min(),df2["Transaction_count"].max()),
                                    hover_name="State", title=f"{year} Quarter{quarter} TRANSACTION COUNT", fitbounds="locations",height=600,width=600)
        
        fig_india2.update_geos(visible=False)

        st.plotly_chart(fig_india2)

    return

#Transaction type with respect to state

def Trans_type_state(table,state):
    col1,col2=st.columns(2)

    with col1:
        fig_pie1=px.pie(table,names="Transaction_name",values="Transaction_amount",width=650,title=f"{state} TRANSACTION AMOUNT ",hole=0.6)
        st.plotly_chart(fig_pie1)
    
    with col2:
        fig_pie2=px.pie(table,names="Transaction_name",values="Transaction_count",width=650,title=f"{state}   TRANSACTION COUNT ",hole=0.6)
        st.plotly_chart(fig_pie2)
    return

#fuction for   brand and transaction count with respect to year

def User_brand_count(df7,year):
    
    df=df7[df7["Year"]==year]
    df.reset_index(drop=True,inplace=True)
    col1,col2=st.columns(2)
    with col1:
        fig1=px.bar(agg_user_brand_count,x="Brand", y="Transaction_count",height=650,width=650,title=f"{year}  BRANDS & TRANSACTION COUNT")
        st.plotly_chart(fig1)
    
    with col2:
        fig2=px.pie(agg_user_brand_count,names="Brand", values="Percentage",title=f"{year}  BRANDS & PERCENTAGE")
        st.plotly_chart(fig2)
    return

#State wise registred users and app opens from map user analysis

def Map_users_apps(table,year):
    df=table[table["Year"]==year]
    
    df.reset_index(drop=True,inplace=True)
    fig1=px.bar(df,x="State",y="Registered_users",title=f"{year} REGISTERED USERS",height=800,width=1000)
    st.plotly_chart(fig1)
    fig2=px.bar(df,x="State",y="App_opens",title=f"{year}  APP OPENS",height=900,width=700)
    st.plotly_chart(fig2)

#State wise registred users and app opens with respect to Quarter,year from map user analysis
def Map_users_apps_quarter(table,year,quarter):
    df=table[table["Year"]==year]
    df1=df[df['Quarter']==quarter]
    
    df1.reset_index(drop=True,inplace=True)
    fig1=px.bar(df1,x="State",y="Registered_users",title=f"{year} QUARTER {quarter} REGISTERED USERS",height=800,width=1000)
    st.plotly_chart(fig1)
    fig2=px.bar(df1,x="State",y="App_opens",title=f"{year} QUARTER {quarter} APP OPENS",height=900,width=700)
    st.plotly_chart(fig2)
    
#District wise registred users and app opens with respect to State from map user analysis    

def Map_user_dist(df,state):
    df1=df[df["State"]==state]
    df1.reset_index(drop=True,inplace=True)
    fig1=px.bar(df1,x="Registered_users",y="District_name",orientation="h",title=f"{state}  REGISTERED USERS")
    st.plotly_chart(fig1)
    fig2=px.bar(df1,x="App_opens",y="District_name",orientation="h",title=f"{state}  APP OPENS")
    st.plotly_chart(fig2)

#Pincode wise registered users with respect to State from top user analysis
    
def Top_user_pin(df,state):
    df1=df[df["State"]==state]
    df1.reset_index(drop=True,inplace=True)
    fig1=px.pie(df1,names="Pincode",values="Registered_users",title=f"{state}  REGISTERED USERS",height=800,width=1000)
    st.plotly_chart(fig1)

#District wise registred userswith respect to year,State from top user analysis
def Top_user_dist(df,state):
    df1=df[df["State"]==state]
    df1.reset_index(drop=True,inplace=True)
    fig1=px.pie(df1,names="District_name",values="Registered_users",title=f"{state}  REGISTERED USERS",height=800,width=1000)
    st.plotly_chart(fig1)
    









    


data_analysis=st.selectbox("select the query",("1.State ,year and quarter wise transaction amount,count analysis from aggregate insurance datas",
                                               "2. State , year and quarter wise trasaction amount, count  analysis from aggregate transaction datas",
                                               "3.State wise transaction type analysis from aggregate transaction datas",
                                               "4.brand wise transaction count from  aggregate user datas",
                                               "5.State,year and quarter wise transaction amount,count analysis from map insurance datas",
                                               "6.State,year and quarter wise transaction amount,count analysis from top insurance datas",
                                               "7.State wise registered users and app opens analysis with respect to year and quarter from map user datas",
                                               "8.District wise registered users and app opens with respect to State from map user analysis",
                                               "9.Pincode wise registered users with respect to State from top user analysis",
                                               "10.District wise registered users with respect to State from top user analysis"))



if data_analysis=="1.State ,year and quarter wise transaction amount,count analysis from aggregate insurance datas":
         
        
    col1,col2=st.columns(2)

    with col1:

        years=st.slider("select the option",agg_ins_year['Year'].min(),agg_ins_year['Year'].max())
    Trans_amount_count(agg_ins_year,years)

    col1,col2=st.columns(2)

    with col1:

        quarter=st.slider("select the option",agg_ins_quarter['Quarter'].min(),agg_ins_quarter['Quarter'].max())

    Trans_amount_count_quarter(agg_ins_quarter,years,quarter)

           
           
elif data_analysis== "2. State , year and quarter wise trasaction amount, count  analysis from aggregate transaction datas":

    col1,col2=st.columns(2)

    with col1:

        years=st.slider("select the option",agg_trans_year['Year'].min(),agg_trans_year['Year'].max())

    Trans_amount_count(agg_trans_year,years)

    col1,col2=st.columns(2)

    with col1:


        quarter=st.slider("select the option",agg_trans_quarter['Quarter'].min(),agg_trans_quarter['Quarter'].max())
    
    Trans_amount_count_quarter(agg_trans_quarter,years,quarter)

elif data_analysis== "3.State wise transaction type analysis from aggregate transaction datas":
            col1,col2=st.columns(2)

            with col1:
                states=st.selectbox("select the state",agg_trans_type["State"].unique())
            
            Trans_type_state(agg_trans_type,states)
                                                                      


elif data_analysis=="4.brand wise transaction count from  aggregate user datas":

        
    col1,col2=st.columns(2)
    with col1:
        years=st.slider("select the option",agg_user_brand_count['Year'].min(),agg_user_brand_count['Year'].max())
    
    User_brand_count(agg_user_brand_count,years)


elif data_analysis=="5.State,year and quarter wise transaction amount,count analysis from map insurance datas":

        

    col1,col2=st.columns(2)

    with col1:

            years=st.slider("select the option",map_ins_year['Year'].min(),map_ins_year['Year'].max())

    Trans_amount_count(map_ins_year,years)

    col1,col2=st.columns(2)

    with col1:


        map_quarter=st.slider("select the quarter",map_ins_quarter['Quarter'].min(),map_ins_quarter['Quarter'].max())
    
    Trans_amount_count_quarter(map_ins_quarter,years,map_quarter)

elif data_analysis== "6.State,year and quarter wise transaction amount,count analysis from top insurance datas":

        
    col1,col2=st.columns(2)

    with col1:

        years=st.slider("select the option",top_ins_year['Year'].min(),top_ins_year['Year'].max())

    Trans_amount_count(top_ins_year,years)

    col1,col2=st.columns(2)

    with col1:


        quarter=st.slider("select the quartervalue",top_ins_quarter['Quarter'].min(),top_ins_quarter['Quarter'].max())
    
    Trans_amount_count_quarter(top_ins_quarter,years,quarter)

elif data_analysis== "7.State wise registered users and app opens analysis with respect to year and quarter from map user datas":

    col1,col2=st.columns(2)

    with col1:

        years=st.slider("select the option",map_user_year['Year'].min(),map_user_year['Year'].max())

    Map_users_apps(map_user_year,years)

    col1,col2=st.columns(2)

    with col1:


        quarter=st.slider("select the quartervalue",map_user_quarter['Quarter'].min(),map_user_quarter['Quarter'].max())
    
    Map_users_apps_quarter(map_user_quarter,years,quarter)

elif data_analysis== "8.District wise registered users and app opens with respect to State from map user analysis":
    col1,col2=st.columns(2)

    with col1:

        states=st.selectbox("select the state",map_user_dist["State"].unique())
    
    Map_user_dist(map_user_dist,states)

elif data_analysis== "9.Pincode wise registered users with respect to State from top user analysis":

    col1,col2=st.columns(2)

    with col1:

        states=st.selectbox("select the state",top_user_pin["State"].unique())
    
    Top_user_pin(top_user_pin,states)

elif data_analysis=="10.District wise registered users with respect to State from top user analysis":

    
    col1,col2=st.columns(2)

    with col1:

        states=st.selectbox("select the state",top_user_dist["State"].unique())
    
    Top_user_dist(top_user_dist,states)


    


    




            
                



                
                
                
             
             
           
        