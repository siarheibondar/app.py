import streamlit as st
import pandas as pd
import plotly.express as px

# Заглушка данных: фиктивные данные
def get_candidates_by_skill_and_country(skills, countries):
    # Генерация фиктивных данных для тестирования
    data = []
    for skill in skills:
        for country in countries:
            num_candidates = len(skill) * len(country) * 5  # Пример формулы подсчёта
            data.append(
                {"Skill": skill, "Country": country, "Candidates": num_candidates}
            )
    return pd.DataFrame(data)

# Заголовок приложения
st.title("Анализ кандидатов по навыкам и странам")

# Ввод данных от пользователя
skills = st.text_input("Введите навыки через запятую (например, OFSC, Salesforce, AWS):")
countries = st.text_input("Введите страны через запятую (например, USA, India, Germany):")

# Кнопка для анализа данных
if st.button("Анализировать"):
    if skills and countries:
        # Форматирование данных ввода
        skill_list = [skill.strip() for skill in skills.split(",")]
        country_list = [country.strip() for country in countries.split(",")]

        # Получение данных
        df = get_candidates_by_skill_and_country(skill_list, country_list)

        # Отображение таблицы с результатами
        st.subheader("Результаты:")
        st.dataframe(df)

        # Построение графиков
        fig = px.bar(
            df,
            x="Country",
            y="Candidates",
            color="Skill",
            barmode="group",
            title="Количество кандидатов по странам и навыкам",
        )
        st.plotly_chart(fig)

    else:
        st.error("Пожалуйста, введите и навыки, и страны!")
