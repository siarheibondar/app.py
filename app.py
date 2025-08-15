import streamlit as st
import pandas as pd

# Функция для генерации данных (фиктивные данные)
def get_candidates_by_skill_and_country(skills, countries):
    data = []
    for skill in skills:
        for country in countries:
            num_candidates = len(skill) * len(country) * 5  # Пример подсчёта
            data.append({"Skill": skill, "Country": country, "Candidates": num_candidates})
    return pd.DataFrame(data)

# Заголовок приложения
st.title("Анализ кандидатов по навыкам и странам")

# Ввод от пользователя
skills = st.text_input("Введите навыки через запятую (например, OFSC, Salesforce, AWS):")
countries = st.text_input("Введите страны через запятую (например, USA, India, Germany):")

# Кнопка для запуска анализа
if st.button("Анализировать"):
    if skills and countries:  # Проверяем, что оба поля заполнены
        # Обрабатываем ввод
        skill_list = [skill.strip() for skill in skills.split(",")]
        country_list = [country.strip() for country in countries.split(",")]

        # Получаем данные
        df = get_candidates_by_skill_and_country(skill_list, country_list)

        # Отображаем таблицу результатов
        st.subheader("Результаты анализа:")
        st.dataframe(df)

        # Показываем сводку по странам
        st.subheader("Сводка по странам:")
        country_summary = df.groupby("Country")["Candidates"].sum().reset_index()
        st.table(country_summary)

    else:
        st.error("Пожалуйста, заполните оба поля: навыки и страны!")
