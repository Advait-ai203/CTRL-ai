# tools/advanced_gaming_dept/shader_graph_gen.py

def compile_glow_fragment_shader(glow_intensity: float, neon_color_vector: tuple) -> str:
    """Compiles a fragment shader string applying emissive light parameters to visual entities."""
    r, g, b = neon_color_vector
    return f"""#version 330 core
out vec4 FragColor;
in vec2 TexCoords;

uniform sampler2D screenTexture;

void main() {{
    vec4 baseColor = texture(screenTexture, TexCoords);
    vec3 glowColor = vec3({r:.2f}, {g:.2f}, {b:.2f}) * {glow_intensity:.4f};
    FragColor = vec4(baseColor.rgb + glowColor, baseColor.a);
}}"""
