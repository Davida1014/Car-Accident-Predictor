import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.title('NYC Car Accident Predictor')

@st.cache
def load_data():
	# Load data
	bkln = pd.read_csv('./Data/data_preds_bkln.csv')
	qns = pd.read_csv('./Data/data_preds_qns.csv')

	# Clean data
	# Set date column to datetime object
	bkln['Date'] = pd.to_datetime(bkln['Unnamed: 0'])
	bkln.drop(columns='Unnamed: 0', inplace=True)

	qns['Date'] = pd.to_datetime(qns['Unnamed: 0'])
	qns.drop(columns='Unnamed: 0', inplace=True)

	bkln.set_index('Date', inplace=True)

	qns.set_index('Date', inplace=True)

	# Rename accidents column
	bkln.rename(columns={'0': 'Accidents'}, inplace=True)

	qns.rename(columns={'0': 'Accidents'}, inplace=True)

	# Convert accidents to integers
	bkln['Accidents'] = bkln['Accidents'].astype(int)

	qns['Accidents'] = qns['Accidents'].astype(int)

	return bkln, qns

@st.cache
def load_latlong():
	# Load data
	df_latlong = pd.read_csv('./Data/df_latlong.csv')


	# Convert date to datetime object
	df_latlong['Date'] = pd.to_datetime(df_latlong['Date'])

	# Change lat/lon column names
	df_latlong(columns={'LATITUDE': 'lat', 'LONGITUDE': 'lon'}, inplace=True)

	return df_latlong


bkln, qns = load_data()
df_latlong = load_latlong()

if st.checkbox('View All Historical Data'):
	st.map(df_latlong)

	st.pydeck_chart(pdk.Deck(
		map_style='mapbox://styles/mapbox/light-v9',
		initial_view_state=pdk.ViewState(
			latitude=40.650002,
			longitude=-73.949997,
			zoom=10,
			pitch=0)))

if st.checkbox('View Specific Date'):
	# Borough selection
	borough = st.selectbox('Select Borough',['Brooklyn','Queens','All'],2)

	# Date selection
	# Define date range
	dates = pd.date_range(start='2012-07-31', end='2022-07-01')
	date = st.selectbox('Select Date', dates, 0)
	st.write('Note: Data through 2021-01-29 is historical. Later accident counts are 	predictions.') 

	# Output
	if borough == 'Brooklyn':
		st.subheader('Brooklyn Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Brooklyn on this date was: ', bkln['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Brooklyn on this date is 	predicted to be: ', bkln['Accidents'][date])
		st.line_chart(bkln)

	if borough == 'Queens':
		st.subheader('Queens Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Queens on this date was: ', qns['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Queens on this date is predicted to be: ', qns['Accidents'][date])
		st.line_chart(qns)

	if borough == 'All':
		st.subheader('Brooklyn Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Brooklyn on this date was: ', bkln['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Brooklyn on this date is predicted to be: ', bkln['Accidents'][date])
		st.line_chart(bkln)

		st.subheader('Queens Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Queens on this date was: ', qns['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Queens on this date is predicted to be: ', qns['Accidents'][date])
		st.line_chart(qns)


