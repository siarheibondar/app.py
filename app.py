import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Функция для генерации данных (вместо реального API или запроса)
def get_candidates_by_skill_and_country(skills, countries):
    # Создаем фиктивные данные
    data = []
    for skill in skills:
        for country in countries:
            num_candidates = len(skill) * len(country) * 5  # Пример подсчёта
            data.append({"Skill": skill, "Country": country, "Candidates": num_candidates})
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
        st.subheader("Результаты анализа:")
        st.dataframe(df)

        # Визуализация с помощью Matplotlib
        fig, ax = plt.subplots()
        df_grouped = df.groupby("Country")["Candidates"].sum()
        df_grouped.plot(kind="bar", ax=ax)
        ax.set_title("Количество кандидатов по странам (в сумме для всех навыков)")
        ax.set_ylabel("Кандидатов")
        ax.set_xlabel("Страны")
        st.pyplot(fig)

    else:
        st.error("Пожалуйста, укажите навыки и страны!")
