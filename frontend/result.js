document.addEventListener("DOMContentLoaded", () => {
    let data = JSON.parse(localStorage.getItem("resumeAnalysis") || "{}");

    if (!data.first_name) {
        document.getElementById("result-container").innerHTML = "<p>Нет данных для отображения</p>";
        return;
    }

    document.getElementById("result-container").innerHTML = `
        <section class="candidate-info">
            <h2>Информация о кандидате</h2>
            <p><strong>Имя:</strong> ${data.first_name} ${data.last_name}</p>
            <p><strong>Email:</strong> ${data.email}</p>
            <p><strong>Телефон:</strong> ${data.phone}</p>
            <p><strong>Город:</strong> ${data.place}</p>
            <p><strong>Позиция:</strong> ${data.position}</p>
            <p><strong>Опыт работы:</strong> ${data.work_experience_time}</p>
        </section>

        <section class="skills">
            <h3>Навыки</h3>
            <ul>
                ${data.skills.split(",").map(skill => `<li>${skill.trim()}</li>`).join("")}
            </ul>
        </section>

        <section class="work-experience">
            <h3>Опыт работы</h3>
            ${data.work_experiences_description.map(job => `
                <div class="job">
                    <h4>${job.organization} — ${job.position}</h4>
                    <p><em>${job.period}</em></p>
                    <p>${job.description || ""}</p>
                </div>
            `).join("")}
        </section>

        <section class="education">
            <h3>Образование</h3>
            ${data.education.map(edu => `
                <div class="edu">
                    <p><strong>${edu.year}</strong> — ${edu.educational_institution}</p>
                    <p>${edu.specialty}</p>
                </div>
            `).join("")}
        </section>
    `;
});
