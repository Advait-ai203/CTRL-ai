# tools/mobile_app_dept/gradle_manager.py

def inject_gradle_dependency(library: str, version: str) -> str:
    """Formats standard Gradle dependency strings for Android development."""
    
    # Common library mappings
    libraries = {
        "retrofit": f"implementation 'com.squareup.retrofit2:retrofit:{version}'",
        "room": f"implementation 'androidx.room:room-runtime:{version}'\nkapt 'androidx.room:room-compiler:{version}'",
        "firebase": f"implementation 'com.google.firebase:firebase-analytics-ktx:{version}'",
        "coil": f"implementation 'io.coil-kt:coil-compose:{version}'"
    }
    
    dependency_string = libraries.get(library.lower(), f"implementation '{library}:{version}'")
    
    return f"""
    🐘 **Gradle Matrix Updated:**
    Inject this directly into your `app/build.gradle` dependencies block:
    
    ```kotlin
    {dependency_string}
    ```
    *Status: Sync Project to download artifacts.*
    """
