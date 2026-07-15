// Tab Switching Controller
function switchTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active'));
    
    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
}

// Simulated Matrix Operations
function runFounderPitch() {
    const brand = document.getElementById('brand-select').value;
    const output = document.getElementById('founder-output');
    output.innerHTML = `> COMPILING PITCH NARRATIVE FOR: ${brand.toUpperCase()}\n> Hook: Dual-threat venture studio operational.\n> Market: Multi-billion TAM target mapped.\n> Status: READY FOR METROLITE BOARDROOM REVIEW.`;
}

function runHardwareEstimate() {
    const mah = parseFloat(document.getElementById('mah-input').value) || 0;
    const draw = parseFloat(document.getElementById('draw-input').value) || 1;
    const hours = ((mah * 0.85) / draw).toFixed(2);
    
    const output = document.getElementById('hardware-output');
    output.innerHTML = `> CALCULATING POWER DRAW MATRIX...\n- Battery Cell: ${mah} mAh (85% usable depth)\n- System Load: ${draw} mA\n> ESTIMATED CONTINUOUS RUNTIME: [ ${hours} HOURS ]`;
}

function runAdGen() {
    const prod = document.getElementById('prod-input').value || "Core Asset";
    const output = document.getElementById('marketing-output');
    output.innerHTML = `> GENERATING MARKETING HOOKS...\n- Product: ${prod}\n- Hook: "Engineered for absolute performance. Own your workflow."\n> STATUS: Deployed to social queues.`;
}

function runTaskDelegation() {
    const task = document.getElementById('task-input').value || "System optimization";
    const assignee = document.getElementById('assignee-select').value;
    const output = document.getElementById('team-output');
    output.innerHTML = `> LOGGING KANBAN NODE...\n- Task: "${task}"\n- Assigned Owner: ${assignee}\n> STATUS: Task securely committed to sync ledger.`;
}
