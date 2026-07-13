# tools/web_agents/react_scaffolder.py
import os

def generate_react_component(component_name: str, props: list) -> str:
    """Scaffolds a modern React functional component."""
    target_dir = "./generated_assets/web_builds/react_components"
    os.makedirs(target_dir, exist_ok=True)

    props_string = ", ".join(props)

    react_code = f"""import React, {{ useState, useEffect }} from 'react';

// ctrl Matrix: Auto-generated React Component
const {component_name} = ({{ {props_string} }}) => {{
    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {{
        setIsLoaded(true);
    }}, []);

    return (
        <div className="p-6 bg-gray-900 rounded-xl border border-gray-700 shadow-lg">
            <h2 className="text-2xl font-bold text-green-400">{{'{component_name}'}}</h2>
            {{isLoaded ? (
                <div className="mt-4 text-gray-300">
                    <p>Component successfully mounted into the matrix.</p>
                </div>
            ) : (
                <div className="animate-pulse flex space-x-4 mt-4">
                    <div className="flex-1 space-y-4 py-1">
                        <div className="h-4 bg-gray-700 rounded w-3/4"></div>
                        <div className="h-4 bg-gray-700 rounded"></div>
                    </div>
                </div>
            )}}
        </div>
    );
}};

export default {component_name};
"""
    file_path = os.path.join(target_dir, f"{component_name}.jsx")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(react_code)

    return f"⚛️ **React Scaffolding Complete:** Component mapped to `{file_path}`"
