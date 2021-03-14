
import streamlit as stream
import pandas as pd

''' Tämä on aikas mahtava.  Minkä tahansa CSV -tiedoston tarkasteluun. Tulossa erilaisia helpotushärpäkkeita.
Jos lataat koodit githubista, niin kehitysympäritössä tietty just run  
streamlit run main.py 
tuosta alta Terminalista (tai komentoriviltä jos niikseen tulee) '''

stream.title('Tutki mitä vaan CSV -muotoista numerodataa')
stream.sidebar.subheader('Lataa tarkasteluun')

uploaded_file = stream.sidebar.file_uploader("Etsi .csv -tiedosto")

if uploaded_file is not None:  
	df = pd.read_csv(uploaded_file)
	stream.sidebar.info('TIedosto ladattu!')

	row1 = stream.beta_container()
	col1, col2 = stream.beta_columns(2)
	row2 = stream.beta_container()
	row3 = stream.beta_container()

	with row1:
		stream.subheader('Tässä raakadata')
		stream.write(df)

	with col1:
		stream.subheader('Valitse sarakkeita')
		columns = list(df.columns)
		columns_sel = stream.multiselect('Valitse/poista sarake', columns, columns)
		dfcol1 = df[columns_sel]
		stream.write(dfcol1)

	with col2:
		stream.subheader('Valitse rivejä')
		start, stop = stream.slider('Rivejä', 0, len(df), [0, len(df)], 1)
		dfcol2 = df.iloc[start:stop]
		stream.write(dfcol2)

	with row2:
		stream.subheader('Näytä iso kuva')
		value = stream.radio('Muuttuja', columns_sel)
		dfrow2 = df[value]
		stream.line_chart(dfrow2)

	with row3:
		stream.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = 
		\sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)''')
		stream.text('Tähän myöhemmin Black-Scholes optiolaskuri')
		stream.text(r''' 
		C = osto-option nykyinen arvo
		S = option kohde-etuuden eli osakkeen nykyinen hinta
		N(d) = normaalijakauman kertymäfunktion arvo
		X = option toteutus- tai lunastushinta (engl. strike price tai exercise price)
		e = luonnollisen logaritmin kantaluku, eli Neperin luku
		r = riskitön korkokanta muunnettuna jatkuvalla korkolaskulla vuotuiseksi
		T = option voimassaoloaika vuosina ennen sopimuksen erääntymistä eli maturiteettia
		sigma = kohde-etuuden tuoton volatiliteetti ''')





