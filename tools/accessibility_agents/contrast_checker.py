# tools/accessibility_agents/contrast_checker.py

def parse_hex_to_rgb(hex_str: str) -> tuple:
    """Helper to convert #RRGGBB hex string into normalized float RGB channels."""
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:
        hex_str = ''.join([c*2 for c in hex_str])
    return tuple(int(hex_str[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def get_relative_luminance(color_hex: str) -> float:
    """Calculates relative luminance of a color based on WCAG standards."""
    r, g, b = parse_hex_to_rgb(color_hex)
    # Apply standard sRGB gamma correction transformations
    rs = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    gs = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    bs = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
    return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs

def evaluate_contrast_compliance(foreground_hex: str, background_hex: str) -> str:
    """Calculates contrast ratios to verify absolute compliance thresholds."""
    try:
        l1 = get_relative_luminance(foreground_hex)
        l2 = get_relative_luminance(background_hex)
        
        # Ensure l1 is the lighter color luminance
        if l1 < l2:
            l1, l2 = l2, l1
            
        ratio = (l1 + 0.05) / (l2 + 0.05)
        
        pass_aa_normal = ratio >= 4.5
        pass_aaa_normal = ratio >= 7.0
        
        return f"""
        👁️ **WCAG Contrast Verification Matrix:**
        - Foreground Color: `{foreground_hex}`
        - Background Color: `{background_hex}`
        - Calculated Contrast Ratio: **{ratio:.2f}:1**
        
        **Compliance Assessment:**
        - AA Level (Normal Text): {"🟢 PASSED" if pass_aa_normal else "❌ FAILED"}
        - AAA Level (Normal Text): {"🟢 PASSED" if pass_aaa_normal else "❌ FAILED"}
        """
    except Exception as e:
        return f"⚠️ Contrast Evaluator Error: {str(e)}"
