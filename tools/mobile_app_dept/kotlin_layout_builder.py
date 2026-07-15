# tools/mobile_app_dept/kotlin_layout_builder.py
import os

def generate_compose_screen(screen_name: str, elements: list) -> str:
    """Scaffolds a native Android Jetpack Compose UI screen."""
    target_dir = "./generated_assets/app_apks/source"
    os.makedirs(target_dir, exist_ok=True)
    
    compose_code = f"""package com.ctrl.matrix.ui

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

// Architect: Advait
// Auto-generated Compose Matrix Screen: {screen_name}

@Composable
fun {screen_name}Screen() {{
    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp)
    ) {{
        Text(text = "{screen_name} Active", style = MaterialTheme.typography.headlineMedium)
        Spacer(modifier = Modifier.height(20.dp))
"""
    for el in elements:
        if el.lower() == "button":
            compose_code += '        Button(onClick = { /* TODO */ }) { Text("Execute") }\n'
        elif el.lower() == "input":
            compose_code += '        OutlinedTextField(value = "", onValueChange = {}, label = { Text("Input Matrix Data") })\n'
        
    compose_code += "    }\n}\n"
    
    file_path = os.path.join(target_dir, f"{screen_name}Screen.kt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(compose_code)
        
    return f"📱 **Kotlin Compose Matrix:** Screen generated at `{file_path}`"
