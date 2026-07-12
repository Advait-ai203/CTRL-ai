# tools/video_agents/subtitle_gen.py
import os

def generate_srt(filename: str, dialogue_map: list) -> str:
    """
    Creates an SRT file. 
    dialogue_map should be a list of dicts: [{'start': '00:00:01,000', 'end': '00:00:04,000', 'text': 'Hello world'}]
    """
    target_dir = "./generated_assets/web_builds/subs"
    os.makedirs(target_dir, exist_ok=True)
    
    srt_content = ""
    for idx, line in enumerate(dialogue_map, 1):
        srt_content += f"{idx}\n{line['start']} --> {line['end']}\n{line['text']}\n\n"
        
    file_path = os.path.join(target_dir, f"{filename}.srt")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(srt_content)
        
    return f"💬 **Subtitles Compiled:** SRT file saved to `{file_path}`"
