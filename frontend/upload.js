const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('fileInput');
const chooseFileBtn = document.getElementById('chooseFileBtn');
const uploadStatus = document.getElementById('upload-status');

chooseFileBtn.addEventListener('click', () => fileInput.click());

fileInput.addEventListener('change', () => {
  if (fileInput.files.length > 0) {
    uploadFile(fileInput.files[0]);
  }
});

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

async function uploadFile(file) {
  uploadStatus.classList.remove('hidden');
  uploadStatus.textContent = "Загрузка...";

  let formData = new FormData();
  formData.append("file", file);

  let response = await fetch("http://127.0.0.1:8000/upload", {
    method: "POST",
    body: formData
  });

  let data = await response.json();

  localStorage.setItem("resumeAnalysis", JSON.stringify(data.result));

  window.location.href = "result.html";

}