# ui/components/loading_spinners.py
# Advanced CSS Animated Loader for the ctrl platform

def get_ctrl_prime_loader(word: str = "CTRL") -> str:
    """
    Generates an advanced glowing 3D loader.
    The CSS supports up to 10 animated letters.
    """
    
    # Ensure the word isn't longer than what the CSS can handle
    word = word[:10].upper()
    
    # Dynamically generate the HTML spans for the bouncing letters
    letters_html = ""
    for char in word:
        # Replace spaces with actual HTML non-breaking spaces so the layout doesn't break
        display_char = "&nbsp;" if char == " " else char
        letters_html += f'<span class="loader-letter">{display_char}</span>\n'
    
    return f"""
    <style>
    .ctrl-loader-container .loader-wrapper {{
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 180px;
      height: 180px;
      font-family: "Inter", "Courier New", sans-serif;
      font-size: 1.5em;
      font-weight: 700;
      color: white;
      border-radius: 50%;
      background-color: transparent;
      user-select: none;
      margin: 20px auto; /* Centers the loader in the chat */
    }}

    .ctrl-loader-container .loader {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      aspect-ratio: 1 / 1;
      border-radius: 50%;
      background-color: transparent;
      animation: loader-rotate 2s linear infinite;
      z-index: 0;
    }}

    @keyframes loader-rotate {{
      0% {{
        transform: rotate(90deg);
        box-shadow:
          0 10px 20px 0 #fff inset,
          0 20px 30px 0 #ad5fff inset,
          0 60px 60px 0 #471eec inset;
      }}
      50% {{
        transform: rotate(270deg);
        box-shadow:
          0 10px 20px 0 #fff inset,
          0 20px 10px 0 #d60a47 inset,
          0 40px 60px 0 #311e80 inset;
      }}
      100% {{
        transform: rotate(450deg);
        box-shadow:
          0 10px 20px 0 #fff inset,
          0 20px 30px 0 #ad5fff inset,
          0 60px 60px 0 #471eec inset;
      }}
    }}

    .ctrl-loader-container .loader-letter {{
      display: inline-block;
      opacity: 0.4;
      transform: translateY(0);
      animation: loader-letter-anim 2s infinite;
      z-index: 1;
      border-radius: 50ch;
      border: none;
      margin: 0 2px;
      letter-spacing: 2px;
    }}

    .ctrl-loader-container .loader-letter:nth-child(2) {{ animation-delay: 0.0s; }}
    .ctrl-loader-container .loader-letter:nth-child(3) {{ animation-delay: 0.1s; }}
    .ctrl-loader-container .loader-letter:nth-child(4) {{ animation-delay: 0.2s; }}
    .ctrl-loader-container .loader-letter:nth-child(5) {{ animation-delay: 0.3s; }}
    .ctrl-loader-container .loader-letter:nth-child(6) {{ animation-delay: 0.4s; }}
    .ctrl-loader-container .loader-letter:nth-child(7) {{ animation-delay: 0.5s; }}
    .ctrl-loader-container .loader-letter:nth-child(8) {{ animation-delay: 0.6s; }}
    .ctrl-loader-container .loader-letter:nth-child(9) {{ animation-delay: 0.7s; }}
    .ctrl-loader-container .loader-letter:nth-child(10) {{ animation-delay: 0.8s; }}
    .ctrl-loader-container .loader-letter:nth-child(11) {{ animation-delay: 0.9s; }}

    @keyframes loader-letter-anim {{
      0%,
      100% {{
        opacity: 0.4;
        transform: translateY(0);
      }}
      20% {{
        opacity: 1;
        transform: scale(1.15);
      }}
      40% {{
        opacity: 0.7;
        transform: translateY(0);
      }}
    }}
    </style>

    <div class="ctrl-loader-container">
        <div class="loader-wrapper">
            <div class="loader"></div>
            {letters_html}
        </div>
    </div>
    """
