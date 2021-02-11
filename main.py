
import streamlit as st
import pandas as pd

''' Tämä on aikas mahtava.  Minkä tahansa CSV -tiedoston tarkasteluun. Just run  
streamlit run main.py 
tuosta alta Terminalista (tai komentoriviltä jos niikseen tulee) '''

st.title('Tutki mitä vaan CSV -muotoista numerodataa')
st.sidebar.subheader('Lataa tarkasteluun')

uploaded_file = st.sidebar.file_uploader("Etsi .csv -tiedosto")

if uploaded_file is not None:  
	df = pd.read_csv(uploaded_file)
	st.sidebar.info('TIedosto ladattu!')

	row1 = st.beta_container()
	col1, col2 = st.beta_columns(2)
	row2 = st.beta_container()
	row3 = st.beta_container()

	with row1:
		st.subheader('Tässä raakadata')
		st.write(df)

	with col1:
		st.subheader('Valitse sarakkeita')
		columns = list(df.columns)
		columns_sel = st.multiselect('Valitse/poista sarake', columns, columns)
		df = df[columns_sel]
		st.write(df)

	with col2:
		st.subheader('Valitse rivejä')
		start, stop = st.slider('Rivejä', 0, len(df), [0, len(df)], 1)
		df = df.iloc[start:stop]
		st.write(df)

	with row2:
		st.subheader('Näytä iso kuva')
		value = st.radio('Muuttuja', columns_sel)
		df = df[value]
		st.line_chart(df)

	with row3:
		st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = 
		\sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)''')
		st.text('Tähän myöhemmin Black-Scholes optiolaskuri')
		st.text(r''' 
		C = osto-option nykyinen arvo
		S = option kohde-etuuden eli osakkeen nykyinen hinta
		N(d) = normaalijakauman kertymäfunktion arvo
		X = option toteutus- tai lunastushinta (engl. strike price tai exercise price)
		e = luonnollisen logaritmin kantaluku, eli Neperin luku
		r = riskitön korkokanta muunnettuna jatkuvalla korkolaskulla vuotuiseksi
		T = option voimassaoloaika vuosina ennen sopimuksen erääntymistä eli maturiteettia
		sigma = kohde-etuuden tuoton volatiliteetti ''')





