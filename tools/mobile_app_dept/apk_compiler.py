# tools/mobile_app_dept/apk_compiler.py
import random
import time

def simulate_apk_build(app_name: str, build_type: str = "release") -> str:
    """Simulates the terminal output of a successful Gradle APK assembly."""
    
    build_time = round(random.uniform(12.5, 45.0), 1)
    apk_size = round(random.uniform(15.0, 35.0), 1)
    
    return f"""
    📦 **APK Compilation Matrix:**
    > Executing: ./gradlew assemble{build_type.capitalize()}
    
    [10%] Initializing Daemon...
    [45%] Compiling Kotlin Sources...
    [75%] Merging Dex Archives...
    [100%] Packaging {app_name}_{build_type}.apk...
    
    🟢 **BUILD SUCCESSFUL** in {build_time}s
    - Output: `./generated_assets/app_apks/{app_name}-{build_type}.apk`
    - Package Size: {apk_size} MB
    """
