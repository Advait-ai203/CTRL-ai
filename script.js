const terminal = document.getElementById('log-output');
const input = document.getElementById('command-input');

input.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        let command = input.value;
        terminal.innerHTML += `<br>> ${command}`;
        
        // Simple AI logic simulation
        if (command.toLowerCase().includes('pitch')) {
            terminal.innerHTML += `<br>...Compiling pitch for matrix node... Pitch ready: "CTRL-ai: The future of autonomous venture."`;
        } else {
            terminal.innerHTML += `<br>...Command processed. Node status: Nominal.`;
        }
        input.value = '';
        terminal.scrollTop = terminal.scrollHeight;
    }
});
