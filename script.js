// script.js - Advanced Matrix Logic
const terminal = document.getElementById('log-output');

function log(text, isAi = true) {
    const p = document.createElement('p');
    p.innerHTML = isAi ? `<span class="ai-text">> [MATRIX]: ${text}</span>` : `> [USER]: ${text}`;
    terminal.appendChild(p);
    terminal.scrollTop = terminal.scrollHeight;
}

// Simple AI Brain Simulation
function processCommand(input) {
    log(input, false);
    
    // Simulate "thinking"
    setTimeout(() => {
        let response = "";
        const cmd = input.toLowerCase();

        if (cmd.includes("pitch")) {
            response = "Compiling board narrative for 'ctrl'... [SUCCESS] Strategy: Growth-First. Vision: Scalable SaaS.";
        } else if (cmd.includes("battery")) {
            response = "Calculating runtime... [NOMINAL] Based on current load, estimated uptime is 14.2 hours.";
        } else if (cmd.includes("assign")) {
            response = "Routing task to team node... [ACKNOWLEDGED] Task updated in the Kanban registry.";
        } else {
            response = "Command not recognized. Current nodes: [PITCH, BATTERY, ASSIGN].";
        }
        log(response);
    }, 800);
}

// Add event listener to your command input
document.getElementById('command-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        processCommand(this.value);
        this.value = '';
    }
});
