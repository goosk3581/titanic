import streamlit as st
import pandas as pd

df = pd.read_csv('./data/titanic.csv')

st.title('Titanic Survivor Statistics')

st.set_page_config(
    page_title='Titanic Statistics',
    layout='wide',
)

with st.sidebar:
    st.header('조회 조건')

    gender = st.selectbox(
        'Sex',
        ['total','male', 'female'],
    )

if gender == 'total':
    filtered = df.copy()
else:
    filtered = df[df['Sex'] == gender]



# 1. 성별 생존자수
g_total_survivor = filtered['Survived'].sum()

# 2. 생존률
g_survivor_rate = filtered['Survived'].mean() * 100

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label = '총 생존자수',
        value = f'{g_total_survivor:,}명',
        border=True
    )

with col2:
    st.metric(
        label = '생존률',
        value = f'{g_survivor_rate:.0f}%',
        border=True,
    )
df['연령대'] = (df['Age'] // 10) * 10
age_count = (
    df.groupby('연령대', as_index=False)['Age'].count()
)


st.subheader('연령대별 생존자수')

st.dataframe(filtered)
if gender == 'total':
    st.bar_chart(
    age_count,
    x = '연령대',
    y = 'Age'
    )




