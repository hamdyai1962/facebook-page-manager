const agentMessage = document.getElementById('agentMessage');
const agentOutput = document.getElementById('agentOutput');
const sendAgent = document.getElementById('sendAgent');

sendAgent.addEventListener('click', async () => {
  const message = agentMessage.value.trim();
  if (!message) {
    agentOutput.textContent = 'Please type a message first.';
    return;
  }

  agentOutput.textContent = 'Thinking...';
  const res = await fetch('/api/agent/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  });

  const json = await res.json();
  agentOutput.textContent = json.response || 'No response.';
});

const pagePost = document.getElementById('pagePost');
const pageLink = document.getElementById('pageLink');
const publishOutput = document.getElementById('publishOutput');
const publishToPage = document.getElementById('publishToPage');

publishToPage.addEventListener('click', async () => {
  const message = pagePost.value.trim();
  if (!message) {
    publishOutput.textContent = 'Post message cannot be empty.';
    return;
  }

  publishOutput.textContent = 'Publishing...';
  const res = await fetch('/api/pages/publish', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, link: pageLink.value || null })
  });

  const json = await res.json();
  publishOutput.textContent = JSON.stringify(json, null, 2);
});

const fileInput = document.getElementById('fileInput');
const extractFile = document.getElementById('extractFile');
const fileOutput = document.getElementById('fileOutput');

extractFile.addEventListener('click', async () => {
  if (!fileInput.files.length) {
    fileOutput.textContent = 'Please choose a file first.';
    return;
  }

  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  fileOutput.textContent = 'Extracting text...';
  const res = await fetch('/api/pages/upload', {
    method: 'POST',
    body: formData
  });

  const json = await res.json();
  fileOutput.textContent = json.text || JSON.stringify(json, null, 2);
});
