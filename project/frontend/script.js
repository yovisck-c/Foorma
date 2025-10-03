const API_BASE_URL = 'http://host.docker.internal:8000'; 

const fileInput = document.getElementById('fileInput');
const convertButton = document.getElementById('convertButton');
const statusMessage = document.getElementById('statusMessage');

function downloadFile(blob, filename) {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
    a.remove();
}

async function handleConversion() {
    statusMessage.textContent = 'Status: Preparing to convert...';
    convertButton.disabled = true;

    if (!fileInput.files.length) {
        statusMessage.textContent = 'Error: Please select a file first.';
        convertButton.disabled = false;
        return;
    }

    const selectedFile = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', selectedFile);

    const fileExtension = selectedFile.name.split('.').pop().toLowerCase();
    let endpoint = '';
    let targetFilename = selectedFile.name.replace(`.${fileExtension}`, '');

    if (fileExtension === 'pdf') {
        endpoint = '/convert/pdf-to-docx';
        targetFilename += '.docx';
    } else if (fileExtension === 'docx' || fileExtension === 'doc') {
        endpoint = '/convert/docx-to-pdf';
        targetFilename += '.pdf';
    } else {
        statusMessage.textContent = `Error: Unsupported file type: ${fileExtension}`;
        convertButton.disabled = false;
        return;
    }
    
    statusMessage.textContent = `Status: Sending file for conversion (${fileExtension.toUpperCase()} to ${targetFilename.split('.').pop().toUpperCase()})...`;

    try {
        const response = await fetch(API_BASE_URL + endpoint, {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const fileBlob = await response.blob();
            const contentDisposition = response.headers.get('Content-Disposition');
            let finalFilename = targetFilename;
            
            if (contentDisposition) {
                const match = contentDisposition.match(/filename="(.+?)"/);
                if (match) {
                    finalFilename = match[1];
                }
            }

            downloadFile(fileBlob, finalFilename);
            statusMessage.textContent = `Success! File "${finalFilename}" downloaded.`;
            
        } else {
            const errorText = await response.json();
            statusMessage.textContent = `Conversion Failed (HTTP ${response.status}): ${errorText.detail || 'Server error.'}`;
        }
    } catch (error) {
        statusMessage.textContent = `Network Error: Could not reach the API. Is the Docker container running on ${API_BASE_URL}?`;
        console.error('Fetch error:', error);
    } finally {
        convertButton.disabled = false;
        fileInput.value = null;
    }
}

convertButton.addEventListener('click', handleConversion);