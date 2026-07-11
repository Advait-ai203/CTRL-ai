# tools/dev_agents/swift_ios_gen.py
import os

def generate_swiftui_view(view_name: str) -> str:
    """Scaffolds a declarative SwiftUI view component."""
    target_dir = "./generated_assets/app_apks/ios_src"
    os.makedirs(target_dir, exist_ok=True)
    
    swift_code = f"""import SwiftUI

// ctrl Matrix: Auto-generated SwiftUI View
struct {view_name}: View {{
    var body: some View {{
        ZStack {{
            Color.black.edgesIgnoringSafeArea(.all)
            
            VStack(spacing: 20) {{
                Text("{view_name} Active")
                    .font(.system(size: 28, weight: .bold, design: .monospaced))
                    .foregroundColor(Color.green)
                
                Text("Secure Matrix Connection Established")
                    .font(.subheadline)
                    .foregroundColor(.gray)
            }}
        }}
    }}
}}

struct {view_name}_Previews: PreviewProvider {{
    static var previews: some View {{
        {view_name}()
    }}
}}
"""
    file_path = os.path.join(target_dir, f"{view_name}.swift")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(swift_code)
        
    return f"🍎 **SwiftUI Component Compiled:** Code written to `{file_path}`"
