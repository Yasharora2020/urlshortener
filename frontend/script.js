document.getElementById('url-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const longUrlInput = document.getElementById('long-url');
    const resultDiv = document.getElementById('result');

    try {
        const response = await fetch('https://.execute-api.ap-southeast-2.amazonaws.com/dev/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: longUrlInput.value })
        });

        if (response.ok) {
            const data = await response.json();
            resultDiv.innerHTML = `Short URL: <a href="${data.short_url}" target="_blank">${data.short_url}</a>`;
        } else {
            resultDiv.textContent = `Error: ${response.statusText}`;
        }
    } catch (error) {
        resultDiv.textContent = `Error: ${error.message}`;
    }
});
