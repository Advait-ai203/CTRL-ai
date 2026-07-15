# tools/mobile_app_dept/flutter_widget_gen.py

def generate_flutter_card(title: str, subtitle: str) -> str:
    """Generates a styled, cross-platform Flutter Card widget in Dart."""
    
    dart_code = f"""
import 'package:flutter/material.dart';

class MatrixCard extends StatelessWidget {{
  const MatrixCard({{Key? key}}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return Card(
      color: const Color(0xFF1A1A1A),
      elevation: 4,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: const [
            Text("{title}", style: TextStyle(color: Color(0xFF00FF88), fontSize: 18, fontWeight: FontWeight.bold)),
            SizedBox(height: 8),
            Text("{subtitle}", style: TextStyle(color: Colors.white70, fontSize: 14)),
          ],
        ),
      ),
    );
  }}
}}
"""
    return f"🦋 **Flutter Widget Matrix:**\n```dart\n{dart_code}\n```"
