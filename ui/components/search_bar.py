# ui/components/search_bar.py
# Advanced Animated Search Bar for the ctrl platform

def get_ctrl_search_bar(placeholder: str = "Search the ctrl matrix...") -> str:
    """
    Generates a cyberpunk-styled, animated search input field 
    with rotating gradient borders and a grid background.
    """
    return f"""
    <style>
    .ctrl-search-container .grid {{
      height: 100%;
      width: 100%;
      background-image: linear-gradient(to right, #0f0f10 1px, transparent 1px),
        linear-gradient(to bottom, #0f0f10 1px, transparent 1px);
      background-size: 1rem 1rem;
      background-position: center center;
      position: absolute;
      top: 0;
      left: 0;
      z-index: -1;
      filter: blur(1px);
    }}
    
    .ctrl-search-container .white,
    .ctrl-search-container .border,
    .ctrl-search-container .darkBorderBg,
    .ctrl-search-container .glow {{
      max-height: 70px;
      max-width: 314px;
      height: 100%;
      width: 100%;
      position: absolute;
      overflow: hidden;
      z-index: -1;
      border-radius: 12px;
      filter: blur(3px);
    }}
    
    .ctrl-search-container .input {{
      background-color: #010201;
      border: none;
      width: 301px;
      height: 56px;
      border-radius: 10px;
      color: white;
      padding-inline: 59px;
      font-size: 16px;
    }}
    
    .ctrl-search-container #poda {{
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      margin: 20px auto;
    }}
    
    .ctrl-search-container .input::placeholder {{
      color: #c0b9c0;
    }}

    .ctrl-search-container .input:focus {{
      outline: none;
    }}

    .ctrl-search-container #main:focus-within > #input-mask {{
      display: none;
    }}

    .ctrl-search-container #input-mask {{
      pointer-events: none;
      width: 100px;
      height: 20px;
      position: absolute;
      background: linear-gradient(90deg, transparent, black);
      top: 18px;
      left: 70px;
    }}
    
    .ctrl-search-container #pink-mask {{
      pointer-events: none;
      width: 30px;
      height: 20px;
      position: absolute;
      background: #cf30aa;
      top: 10px;
      left: 5px;
      filter: blur(20px);
      opacity: 0.8;
      transition: all 2s;
    }}
    
    .ctrl-search-container #main:hover > #pink-mask {{
      opacity: 0;
    }}

    .ctrl-search-container .white {{
      max-height: 63px;
      max-width: 307px;
      border-radius: 10px;
      filter: blur(2px);
    }}

    .ctrl-search-container .white::before {{
      content: "";
      z-index: -2;
      text-align: center;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) rotate(83deg);
      position: absolute;
      width: 600px;
      height: 600px;
      background-repeat: no-repeat;
      background-position: 0 0;
      filter: brightness(1.4);
      background-image: conic-gradient(
        rgba(0, 0, 0, 0) 0%,
        #a099d8,
        rgba(0, 0, 0, 0) 8%,
        rgba(0, 0, 0, 0) 50%,
        #dfa2da,
        rgba(0, 0, 0, 0) 58%
      );
      transition: all 2s;
    }}
    
    .ctrl-search-container .border {{
      max-height: 59px;
      max-width: 303px;
      border-radius: 11px;
      filter: blur(0.5px);
    }}
    
    .ctrl-search-container .border::before {{
      content: "";
      z-index: -2;
      text-align: center;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) rotate(70deg);
      position: absolute;
      width: 600px;
      height: 600px;
      filter: brightness(1.3);
      background-repeat: no-repeat;
      background-position: 0 0;
      background-image: conic-gradient(
        #1c191c,
        #402fb5 5%,
        #1c191c 14%,
        #1c191c 50%,
        #cf30aa 60%,
        #1c191c 64%
      );
      transition: all 2s;
    }}
    
    .ctrl-search-container .darkBorderBg {{
      max-height: 65px;
      max-width: 312px;
    }}
    
    .ctrl-search-container .darkBorderBg::before {{
      content: "";
      z-index: -2;
      text-align: center;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) rotate(82deg);
      position: absolute;
      width: 600px;
      height: 600px;
      background-repeat: no-repeat;
      background-position: 0 0;
      background-image: conic-gradient(
        rgba(0, 0, 0, 0),
        #18116a,
        rgba(0, 0, 0, 0) 10%,
        rgba(0, 0, 0, 0) 50%,
        #6e1b60,
        rgba(0, 0, 0, 0) 60%
      );
      transition: all 2s;
    }}
    
    .ctrl-search-container #poda:hover > .darkBorderBg::before {{ transform: translate(-50%, -50%) rotate(262deg); }}
    .ctrl-search-container #poda:hover > .glow::before {{ transform: translate(-50%, -50%) rotate(240deg); }}
    .ctrl-search-container #poda:hover > .white::before {{ transform: translate(-50%, -50%) rotate(263deg); }}
    .ctrl-search-container #poda:hover > .border::before {{ transform: translate(-50%, -50%) rotate(250deg); }}
    
    .ctrl-search-container #poda:focus-within > .darkBorderBg::before {{ transform: translate(-50%, -50%) rotate(442deg); transition: all 4s; }}
    .ctrl-search-container #poda:focus-within > .glow::before {{ transform: translate(-50%, -50%) rotate(420deg); transition: all 4s; }}
    .ctrl-search-container #poda:focus-within > .white::before {{ transform: translate(-50%, -50%) rotate(443deg); transition: all 4s; }}
    .ctrl-search-container #poda:focus-within > .border::before {{ transform: translate(-50%, -50%) rotate(430deg); transition: all 4s; }}

    .ctrl-search-container .glow {{
      overflow: hidden;
      filter: blur(30px);
      opacity: 0.4;
      max-height: 130px;
      max-width: 354px;
    }}
    
    .ctrl-search-container .glow:before {{
      content: "";
      z-index: -2;
      text-align: center;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) rotate(60deg);
      position: absolute;
      width: 999px;
      height: 999px;
      background-repeat: no-repeat;
      background-position: 0 0;
      background-image: conic-gradient(
        #000,
        #402fb5 5%,
        #000 38%,
        #000 50%,
        #cf30aa 60%,
        #000 87%
      );
      transition: all 2s;
    }}

    @keyframes rotate {{
      100% {{ transform: translate(-50%, -50%) rotate(450deg); }}
    }}

    .ctrl-search-container #filter-icon {{
      position: absolute;
      top: 8px;
      right: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 2;
      max-height: 40px;
      max-width: 38px;
      height: 100%;
      width: 100%;
      isolation: isolate;
      overflow: hidden;
      border-radius: 10px;
      background: linear-gradient(180deg, #161329, black, #1d1b4b);
      border: 1px solid transparent;
      cursor: pointer;
    }}
    
    .ctrl-search-container .filterBorder {{
      height: 42px;
      width: 40px;
      position: absolute;
      overflow: hidden;
      top: 7px;
      right: 7px;
      border-radius: 10px;
    }}

    .ctrl-search-container .filterBorder::before {{
      content: "";
      text-align: center;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) rotate(90deg);
      position: absolute;
      width: 600px;
      height: 600px;
      background-repeat: no-repeat;
      background-position: 0 0;
      filter: brightness(1.35);
      background-image: conic-gradient(
        rgba(0, 0, 0, 0),
        #3d3a4f,
        rgba(0, 0, 0, 0) 50%,
        rgba(0, 0, 0, 0) 50%,
        #3d3a4f,
        rgba(0, 0, 0, 0) 100%
      );
      animation: rotate 4s linear infinite;
    }}
    
    .ctrl-search-container #main {{
      position: relative;
    }}
    
    .ctrl-search-container #search-icon {{
      position: absolute;
      left: 20px;
      top: 15px;
    }}
    </style>

    <div class="ctrl-search-container" style="position: relative; padding: 40px; border-radius: 15px; overflow: hidden;">
        <div class="grid"></div>
        <div id="poda">
            <div class="glow"></div>
            <div class="darkBorderBg"></div>
            <div class="darkBorderBg"></div>
            <div class="darkBorderBg"></div>
            <div class="white"></div>
            <div class="border"></div>
            
            <div id="main">
                <input type="text" class="input" placeholder="{placeholder}">
                <div id="input-mask"></div>
                <div id="pink-mask"></div>
                
                <div class="filterBorder"></div>
                <div id="filter-icon">
                    <svg preserveAspectRatio="none" height="27" width="27" viewBox="4.8 4.56 14.832 15.408" fill="none">
                        <path d="M8.16 6.65002H15.83C16.47 6.65002 16.99 7.17002 16.99 7.81002V9.09002C16.99 9.56002 16.7 10.14 16.41 10.43L13.91 12.64C13.56 12.93 13.33 13.51 13.33 13.98V16.48C13.33 16.83 13.1 17.29 12.81 17.47L12 17.98C11.36 18.39 10.53 17.93 10.53 17.16V13.91C10.53 13.5 10.29 12.98 10.06 12.69L7.67 10.55C7.38 10.26 7.15 9.73002 7.15 9.32002V7.81002C7.15 7.17002 7.62 6.65002 8.16 6.65002Z" fill="#d6d6e6" stroke="#d6d6e6" stroke-width="1" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                </div>
                
                <div id="search-icon">
                    <svg preserveAspectRatio="none" height="24" width="24" viewBox="0 0 24 24" fill="none">
                        <path d="M21 21L15 15M17 10C17 13.866 13.866 17 10 17C6.13401 17 3 13.866 3 10C3 6.13401 6.13401 3 10 3C13.866 3 17 6.13401 17 10Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                </div>
            </div>
        </div>
    </div>
    """
