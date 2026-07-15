const terminal = document.getElementById('log-output');

function log(text, isAi = true) {
    const p = document.createElement('p');
    p.className = isAi ? 'ai-text' : 'user-text';
    p.innerText = isAi ? `> [MATRIX]: ${text}` : `> [USER]: ${text}`;
    terminal.appendChild(p);
    terminal.scrollTop = terminal.scrollHeight;
}

function saveKey() {
    localStorage.setItem('GEMINI_KEY', document.getElementById('api-key-input').value);
    log("API Key stored in local browser session.");
}

async function processCommand(input) {
    const apiKey = localStorage.getItem('GEMINI_KEY');
    if (!apiKey) { log("Error: API Key not set."); return; }
    log(input, false);

    try {
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ contents: [{parts: [{text: input}]}] })
        });
        const data = await response.json();
        log(data.candidates[0].content.parts[0].text);
    } catch (e) {
        log("Connection error. Check API Key validity.");
    }
}

document.getElementById('command-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') { processCommand(e.target.value); e.target.value = ''; }
});
