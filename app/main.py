from app.core.extractor import extract_personal_info

if __name__ == "__main__":
    sample_text = """
    # Резюме Frontend-разработчика

    ## Контактная информация
    - **Имя:** Дмитрий Волков
    - **Город:** Казань
    - **Телефон:** +7 (900) 123-45-67
    - **Email:** d.volkov@example.com
    - **Telegram:** @dv_frontend
    - **GitHub:** github.com/dvolkov-dev

    ## Позиция
    **Frontend-разработчик (Vue.js/Nuxt)**
    - **Специализация:** Веб-разработка, SPA-приложения
    - **Занятость:** Полная/частичная
    - **График:** Удаленная работа, гибкий график
    - **Опыт:** 3.5 года коммерческой разработки

    ## Ключевые навыки
    ```plaintext
    Vue.js 2/3 | Nuxt 3 | TypeScript | Pinia | REST API 
    Tailwind CSS | SCSS | Webpack | Git | Docker

    Опыт работы
    ASI (Январь 2025 — н.в.)
    Frontend-разработчик
    Разработка финансового веб-приложения

    Стек: Nuxt 3, Pinia, Tailwind CSS

    Достижения:

    Оптимизировал загрузку страниц на 40% через lazy-loading

    Разработал систему динамических форм с кастомной валидацией

    Мигрировал с Vuex на модульную архитектуру Pinia

    Настроил интеграцию с банковскими API и ЭЦП

    AiEMR (Июнь 2024 — Февраль 2025)
    Frontend-разработчик
    Создание админ-панели и клиентского портала

    Стек: Vue 3, TypeScript, Pinia

    Реализовал:

    Систему управления контентом с rich-редактором

    Компонентную библиотеку на Storybook

    Интерактивные дашборды с Chart.js

    Peredelano Startups (Декабрь 2023 — Июнь 2024)
    Frontend-разработчик
    Платформа поиска мероприятий

    Стек: Nuxt 3, TypeScript, SCSS

    Ключевые задачи:

    Разработка геосервиса с фильтрацией мероприятий

    Интеграция с картографическими API

    Адаптивная кроссбраузерная верстка

    Технический стек
    Основные технологии:

    JavaScript/TypeScript (ES6+)

    Vue.js 2/3, Nuxt.js, Pinia

    HTML5/Pug, CSS3/SCSS, Tailwind CSS

    Дополнительно:

    Webpack, Vite, Docker

    REST API, Axios

    Jest, Cypress (unit/e2e тесты)

    Figma (работа с макетами)

    Образование
    Казанский Федеральный Университет
    2020-2024 | Прикладная информатика (бакалавр)
    """
    result = extract_personal_info(sample_text)
    print(result)