const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('fileInput');
const chooseFileBtn = document.getElementById('chooseFileBtn');
const uploadStatus = document.getElementById('upload-status');

// Открыть диалог выбора файла
chooseFileBtn.addEventListener('click', () => fileInput.click());

// При выборе файла
fileInput.addEventListener('change', () => {
  if (fileInput.files.length > 0) {
    uploadFile(fileInput.files[0]);
  }
});

// Drag & Drop события
dropArea.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropArea.classList.add('dragover');
});
dropArea.addEventListener('dragleave', () => {
  dropArea.classList.remove('dragover');
});
dropArea.addEventListener('drop', (e) => {
  e.preventDefault();
  dropArea.classList.remove('dragover');
  if (e.dataTransfer.files.length > 0) {
    uploadFile(e.dataTransfer.files[0]);
  }
});

// Отправка файла на backend
async function uploadFile(file) {
  uploadStatus.classList.remove('hidden');
  let formData = new FormData();
  formData.append("file", file);

  let response = await fetch("http://127.0.0.1:8000/upload", {
    method: "POST",
    body: formData
  });

  let data = await response.json();
  uploadStatus.textContent = "Файл загружен и проанализирован ✅";

  console.log("Результат анализа:", data);
}