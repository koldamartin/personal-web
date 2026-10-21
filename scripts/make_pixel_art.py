"""
Generates rich, colorful 8-bit retro pixel art SVGs for Martin Kolda's TUI portfolio.
Uses 32x32 crisp pixel grids with vibrant Charm / Cyberpunk color palettes.
"""
import os

def grid_to_svg(pixel_grid, palette, width=32, height=32, scale=12):
    svg_w = width * scale
    svg_h = height * scale
    
    rects = []
    for y, row in enumerate(pixel_grid):
        for x, char in enumerate(row):
            if char in palette and palette[char] is not None:
                color = palette[char]
                rects.append(f'<rect x="{x * scale}" y="{y * scale}" width="{scale}" height="{scale}" fill="{color}" />')
                
    rect_str = "\n  ".join(rects)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}" shape-rendering="crispEdges">
  <defs>
    <filter id="retro-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="#ff5f87" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="{svg_w}" height="{svg_h}" fill="#10131e" rx="{scale}" />
  {rect_str}
</svg>"""

# 1. AVATAR: Python AI Developer with glowing cyber glasses, hoodie, terminal vibe
avatar_palette = {
    '.': None,             # Transparent/dark background
    'B': '#181b28',        # Dark shadow / base
    'H': '#2d334a',        # Hoodie dark blue
    'F': '#ffb07c',        # Skin tone
    'D': '#e09867',        # Darker skin / shadow
    'K': '#1f2430',        # Hair dark slate
    'C': '#00f5d4',        # Cyber visor neon cyan glow
    'M': '#ff5f87',        # Cyber visor neon magenta edge
    'W': '#ffffff',        # Specular glint
    'P': '#4b8bbe',        # Python Blue
    'Y': '#ffd43b',        # Python Gold
    'G': '#50fa7b',        # Terminal green accent
}

avatar_grid = [
    "................................",
    "............KKKKKKKK............",
    "..........KKKKKKKKKKKK..........",
    "........KKKKKKKKKKKKKKKK........",
    ".......KKKKKKKKKKKKKKKKKK.......",
    "......KKKKKKKKKKKKKKKKKKKK......",
    ".....KKKKFFFFFFFFFFKKKKKKK......",
    ".....KKKFFFFFFFFFFFFKKKKKK......",
    ".....KKFFFFFFFFFFFFFFKKKKK......",
    ".....KKFFMMMMMMMMMMFFKKKK.......",
    ".....KKFMMCCCCCCCCMMFFKKK.......",
    ".....KKFMCWCCCCWCCMFCKKK........",
    ".....KKFMMCCCCCCCCMMFFKK........",
    "......KFFFFFFFFFFFFFFKKK........",
    "......KFFFFFDFFDFFFFFKK.........",
    ".......FFFFFFFFFFDFFF...........",
    "........FFFFFFFDDDFF............",
    ".........FFDFFFFFFF.............",
    "........HHHHHHHHHHHH............",
    "......HHHHHHHHHHHHHHHH..........",
    "....HHHHHHHHHHHHHHHHHHHH........",
    "...HHHHHHHHPPHHYYHHHHHHHH.......",
    "..HHHHHHHHHPPHHYYHHHHHHHHH......",
    ".HHHHHHHHHHPPYYYYHHHHHHHHHH.....",
    ".HHHHHHHHHHPPYYYYHHHHHHHHHH.....",
    "HHHHHHHHHHHPPPPYYHHHHHHHHHHH....",
    "HHHHHHHHHHHPPPPYYHHHHHHHHHHH....",
    "HHHHHHHH.GGGGGGGGGG.HHHHHHHH....",
    "HHHHHHH.GGGGGGGGGGGG.HHHHHHH....",
    "HHHHHH.GGWGGGGGGGGGG.HHHHHHH....",
    "HHHHHH.GGGGGGGGGGWGG.HHHHHHH....",
    "................................"
]

# 2. CEZ AI: Energy Cooling Tower + Neural Network Grid (ČEZ a.s. AI solutions)
cez_palette = {
    '.': None,
    'S': '#0c101a',        # Deep night sky
    'T': '#3e445b',        # Cooling tower concrete
    'L': '#565f89',        # Lighter concrete
    'G': '#06d6a0',        # Energy green neon
    'C': '#00f5d4',        # Electric cyan
    'Y': '#ffd166',        # Electric spark yellow
    'M': '#f72585',        # Neural node pink
    'W': '#ffffff',        # Bright pulse
    'P': '#7aa2f7',        # Synapse line
    'O': '#ff9e64',        # ČEZ orange accent
}

cez_grid = [
    "................................",
    ".......P......P......P..........",
    "......PWP....PMP....PCP.........",
    ".......P......P......P..........",
    ".....P...P..P...P..P...P........",
    "....P.....PP.....PP.....P.......",
    "...P..PWP..P..PMP..P..PCP.P.....",
    "....P.....PP.....PP.....P.......",
    ".....P...P..P...P..P...P........",
    ".......P......P......P..........",
    "......TTTT..........TTTT........",
    ".....TTTLTT........TTTLTT.......",
    "....TTTLLTTT......TTTLLTTT......",
    "...TTTLLLLTTT....TTTLLLLTTT.....",
    "...TTTLLLLTTT....TTTLLLLTTT.....",
    "..TTTLLGLLTTTT..TTTLLCLLTTTT....",
    "..TTLLGGGLLTTT..TTLLCCCLLTTT....",
    "..TTLGGGGLLTTT..TTLCCCCCLLTT....",
    ".TTTLGGGGLLTTTT.TTTLCCCCLLTTT...",
    ".TTLLGGGGLLLTTT.TTLLCCCCLLLTT...",
    ".TTLLGGGGLLLTTT.TTLLCCCCLLLTT...",
    "TTTLLGGWGLLLTTTTTTLLCCWCLLLTTT..",
    "TTTLLGGGGLLLTTTTTTLLCCCCLLLTTT..",
    "TTTTLLLLLLLLTTTTTTLLLLLLLLTTTT..",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "..YYYY......CCCC......GGGG......",
    "....YYYY..CCCC......GGGG........",
    "......YYYYCCCC....GGGG..........",
    "........YYWWCC..GGWW............",
    "..........YYCCGGGG..............",
    "............YCGG................",
    "................................"
]

# 3. ROBOSALES: AI Shopping Assistant bot with smart cart
robosales_palette = {
    '.': None,
    'R': '#ff5f87',        # Assistant magenta
    'B': '#1e2238',        # Bot chassis dark
    'S': '#7aa2f7',        # Steel blue body
    'L': '#bb9af7',        # Light purple highlight
    'C': '#00f5d4',        # Eye screen cyan
    'W': '#ffffff',        # Bright sparkle
    'Y': '#ffb703',        # Gold coin / discount tag
    'G': '#06d6a0',        # Cart green / success
    'K': '#111424',        # Wheels / joints
}

robosales_grid = [
    "................................",
    "..............LL................",
    "..............LL................",
    ".............WWLL...............",
    "............SSSSSS..............",
    "...........SSSSSSSS.............",
    "..........SSCCCCCCSS............",
    "..........SCCWCCWCCS............",
    "..........SCCCCCCCCS............",
    "..........SCCWWWWCCS............",
    "...........SSSSSSSS.............",
    "............SSSSSS..............",
    ".............BBBB...............",
    "........RRRRRBBBBBRRRRR.........",
    ".......RRSSSSBBBBBSSSRRR........",
    ".......R.SSSSBBBBBSSSS.R........",
    ".......R.SSSSBBBBBSSSS.R........",
    ".........SSSSBBBBBSSSS..........",
    "..........SSSSSSSSSS............",
    "..........GGGGGGGGGGGG..........",
    ".........G.YY...WW..G.G.........",
    "........G..YY...WW..G..G........",
    ".......G...YYY..WW..G...G.......",
    "......GGGGGGGGGGGGGGGGGGG.......",
    "......G.G...G.G...G.G...G.......",
    "......GGGGGGGGGGGGGGGGGGG.......",
    ".......KK...........KK..........",
    "......KKKK.........KKKK.........",
    "......KKKK.........KKKK.........",
    ".......KK...........KK..........",
    "................................",
    "................................"
]

# 4. WEBSITES: CRT Terminal Workstation running modern Astro/TS code
websites_palette = {
    '.': None,
    'C': '#282c3f',        # Computer casing slate
    'L': '#3b4261',        # Casing light
    'K': '#0f111a',        # Screen frame dark
    'S': '#1a1b26',        # Screen glass
    'G': '#73daca',        # Code cyan/green
    'M': '#f7768e',        # Syntax pink
    'Y': '#e0af68',        # Syntax yellow
    'B': '#7aa2f7',        # Syntax blue
    'W': '#ffffff',        # Cursor white
    'A': '#ff5f87',        # Astro orange/pink logo
    'T': '#00f5d4',        # Terminal glow
}

websites_grid = [
    "................................",
    ".....LLLLLLLLLLLLLLLLLLLLL......",
    "....LCCCCCCCCCCCCCCCCCCCCC......",
    "...LCCKKKKKKKKKKKKKKKKKKKCC.....",
    "...LCKSSSSSSSSSSSSSSSSSSSKC.....",
    "...LCKSMGB...B...M...B...SKC....",
    "...LCKS..................SKC....",
    "...LCKSGM> astro.build...SKC....",
    "...LCKSMB> b2ts.cz.......SKC....",
    "...LCKSYB> vpt-lipno.cz..SKC....",
    "...LCKSGB> doteku.cz.....SKC....",
    "...LCKS..................SKC....",
    "...LCKSMM export default.SKC....",
    "...LCKSBB  Astro.props;..SKC....",
    "...LCKSYY return <HTML>;.SKC....",
    "...LCKSGG █..............SKC....",
    "...LCKSSSSSSSSSSSSSSSSSSSKC.....",
    "...LCKKKKKKKKKKKKKKKKKKKCC.....",
    "....LCCCCCCCCCCCCLCCCCCCC.......",
    ".....LLLLLLLLLLLLLLLLLLLL.......",
    "..........CCCCCCCC..............",
    ".........CCCCCCCCCC.............",
    ".......LLLLLLLLLLLLLL...........",
    "......LCCCCCCCCCCCCCCL..........",
    ".....LCCCCCCCCCCCCCCCCL.........",
    "....LCCCCKKKKKKKKCCCCCCL........",
    "...LCCCCKKKKKKKKKKCCCCCL........",
    "...LCCCCCCCCCCCCCCCCCCCCL.......",
    "...LLLLLLLLLLLLLLLLLLLLLL.......",
    "................................",
    "................................",
    "................................"
]

out_dir = "/home/martin/projects/personal-web/public/images"
os.makedirs(out_dir, exist_ok=True)

images = [
    ("avatar-8bit.svg", avatar_grid, avatar_palette),
    ("cez-ai-8bit.svg", cez_grid, cez_palette),
    ("robosales-8bit.svg", robosales_grid, robosales_palette),
    ("websites-8bit.svg", websites_grid, websites_palette),
]

for filename, grid, palette in images:
    svg_content = grid_to_svg(grid, palette)
    path = os.path.join(out_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {path}")

print("Pixel art generation completed!")
