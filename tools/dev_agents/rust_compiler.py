# tools/dev_agents/rust_compiler.py
import os

def generate_rust_cargo(project_name: str) -> str:
    """Generates the file structure for a safe, concurrent Rust binary."""
    base_dir = f"./generated_assets/web_builds/{project_name}"
    src_dir = os.path.join(base_dir, "src")
    os.makedirs(src_dir, exist_ok=True)
    
    toml_code = f"""[package]
name = "{project_name}"
version = "0.1.0"
edition = "2021"

[dependencies]
# ctrl matrix high-performance dependencies
"""
    
    main_rs = """// ctrl Matrix: High-Performance Rust Execution Node
fn main() {
    println!("Matrix secure connection established. Rust binary operational.");
}
"""
    
    with open(os.path.join(base_dir, "Cargo.toml"), "w", encoding="utf-8") as f:
        f.write(toml_code)
        
    with open(os.path.join(src_dir, "main.rs"), "w", encoding="utf-8") as f:
        f.write(main_rs)
        
    return f"🦀 **Rust Architecture Scaffolding Complete:** Initialized in `{base_dir}`"
