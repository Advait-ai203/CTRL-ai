# tools/mobile_app_dept/ios_plist_editor.py

def generate_ios_permissions(requires_camera: bool, requires_location: bool) -> str:
    """Generates XML property list keys for iOS hardware access."""
    
    plist_xml = ""
    
    if requires_camera:
        plist_xml += """
    <key>NSCameraUsageDescription</key>
    <string>The matrix requires camera access to scan physical allmate inventory tags.</string>"""
        
    if requires_location:
        plist_xml += """
    <key>NSLocationWhenInUseUsageDescription</key>
    <string>Location services are required for real-time delivery tracking.</string>"""
        
    if not plist_xml:
        return "⚠️ **Plist Editor:** No hardware permissions requested."
        
    return f"🍏 **iOS Plist Configuration:**\nInject these keys into `Info.plist`:\n```xml{plist_xml}\n```"
