import os
import subprocess
import time
import requests
from PIL import Image, ImageDraw, ImageFont

# ============================================================
# SETTINGS
# ============================================================

OUTPUT = "tech-stack.gif"

WIDTH = 1200
HEIGHT = 620

FRAMES = 48
FRAME_DURATION = 70

ICON_SIZE = 90


# ============================================================
# COLORS
# ============================================================

BG_TOP = (255, 247, 252)
BG_BOTTOM = (232, 218, 247)

PINK = (247, 168, 210)
LAVENDER = (220, 200, 242)
DARK_LAVENDER = (126, 91, 157)

TEXT = (91, 68, 105)
WHITE = (255, 255, 255)


# ============================================================
# REAL DEVICON SVG LINKS
# ============================================================

TECH = {

    "Python":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg",

    "Java":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg",

    "JavaScript":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg",

    "HTML":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg",

    "CSS":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg",

    "Bash":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/bash/bash-original.svg",

    "React":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg",

    "FastAPI":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg",

    "Flask":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg",

    "Node.js":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original.svg",

    "Docker":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg",

    "MySQL":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg",

    "PostgreSQL":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original.svg",

    "MongoDB":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original.svg",

    "Redis":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original.svg",

    "Git":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg",

    "GitHub":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg",

    "VS Code":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg",

    "Linux":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg",

    "Postman":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/postman/postman-original.svg",

    "Wireshark":
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/wireshark/wireshark-original.svg"
}


# ============================================================
# CATEGORIES
# ============================================================

LANGUAGES = [
    "Python",
    "Java",
    "JavaScript",
    "HTML",
    "CSS",
    "Bash"
]

DEVELOPMENT = [
    "React",
    "FastAPI",
    "Flask",
    "Node.js",
    "Docker"
]

DATABASES = [
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Redis"
]

TOOLS = [
    "Git",
    "GitHub",
    "VS Code",
    "Linux",
    "Postman",
    "Wireshark"
]

CATEGORY_NAMES = {
    tuple(LANGUAGES): "LANGUAGES",
    tuple(DEVELOPMENT): "DEVELOPMENT",
    tuple(DATABASES): "DATABASES",
    tuple(TOOLS): "TOOLS"
}


# ============================================================
# FIND GOOGLE CHROME
# ============================================================

def find_chrome():

    possible_paths = [

        r"C:\Program Files\Google\Chrome\Application\chrome.exe",

        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",

        os.path.expandvars(
            r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
        )

    ]

    for path in possible_paths:

        if os.path.exists(path):

            return path

    return None


CHROME = find_chrome()


if CHROME is None:

    print()
    print("ERROR: Google Chrome was not found.")
    print()
    print("Please make sure Google Chrome is installed.")
    print()

    input("Press Enter to close...")

    raise SystemExit


print()
print("Chrome found!")
print(CHROME)
print()


# ============================================================
# FONTS
# ============================================================

def get_font(size):

    fonts = [

        r"C:\Windows\Fonts\BASKVILL.TTF",

        r"C:\Windows\Fonts\Baskerville.ttf",

        r"C:\Windows\Fonts\arial.ttf"

    ]

    for font in fonts:

        if os.path.exists(font):

            try:

                return ImageFont.truetype(
                    font,
                    size
                )

            except:
                pass

    return ImageFont.load_default()


TITLE_FONT = get_font(42)

SUBTITLE_FONT = get_font(18)

LABEL_FONT = get_font(15)

SMALL_FONT = get_font(13)


# ============================================================
# FOLDERS
# ============================================================

ICON_FOLDER = "icons"

SVG_FOLDER = os.path.join(
    ICON_FOLDER,
    "svg"
)

PNG_FOLDER = os.path.join(
    ICON_FOLDER,
    "png"
)

os.makedirs(
    SVG_FOLDER,
    exist_ok=True
)

os.makedirs(
    PNG_FOLDER,
    exist_ok=True
)


# ============================================================
# DOWNLOAD SVG ICONS
# ============================================================

print()
print("==========================================")
print(" DOWNLOADING REAL TECHNOLOGY ICONS")
print("==========================================")
print()


for name, url in TECH.items():

    safe_name = (

        name
        .lower()
        .replace(" ", "_")
        .replace(".", "")
    )

    svg_path = os.path.join(
        SVG_FOLDER,
        safe_name + ".svg"
    )

    try:

        if not os.path.exists(svg_path):

            print(
                "Downloading:",
                name
            )

            response = requests.get(

                url,

                timeout=30,

                headers={
                    "User-Agent": "Mozilla/5.0"
                }

            )

            response.raise_for_status()

            with open(
                svg_path,
                "wb"
            ) as file:

                file.write(
                    response.content
                )

        print(
            "Loaded SVG:",
            name
        )

    except Exception as error:

        print(
            "FAILED:",
            name
        )

        print(error)


# ============================================================
# CONVERT SVG TO PNG USING CHROME
# ============================================================

print()
print("==========================================")
print(" CONVERTING ICONS")
print("==========================================")
print()


icons = {}


for name in TECH:

    safe_name = (

        name
        .lower()
        .replace(" ", "_")
        .replace(".", "")
    )

    svg_path = os.path.abspath(
        os.path.join(
            SVG_FOLDER,
            safe_name + ".svg"
        )
    )

    png_path = os.path.abspath(
        os.path.join(
            PNG_FOLDER,
            safe_name + ".png"
        )
    )


    if not os.path.exists(svg_path):

        continue


    # --------------------------------------------------------
    # HTML wrapper
    # --------------------------------------------------------

    html_path = os.path.abspath(
        os.path.join(
            SVG_FOLDER,
            safe_name + ".html"
        )
    )


    html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<style>

html, body {{

    margin: 0;

    padding: 0;

    width: 128px;

    height: 128px;

    background: transparent;

    overflow: hidden;

}}

img {{

    width: 100px;

    height: 100px;

    object-fit: contain;

    display: block;

    margin: 14px;

}}

</style>

</head>

<body>

<img src="file:///{svg_path.replace(chr(92), '/')}">

</body>

</html>
"""


    with open(
        html_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)


    try:

        subprocess.run(

            [

                CHROME,

                "--headless=new",

                "--disable-gpu",

                "--hide-scrollbars",

                "--disable-extensions",

                "--default-background-color=00000000",

                "--window-size=128,128",

                "--screenshot="
                + png_path,

                "file:///"
                + html_path.replace(
                    "\\",
                    "/"
                )

            ],

            stdout=subprocess.DEVNULL,

            stderr=subprocess.DEVNULL,

            timeout=20

        )


        if os.path.exists(png_path):

            icon = Image.open(
                png_path
            ).convert("RGBA")

            icon.thumbnail(
                (58, 58),
                Image.Resampling.LANCZOS
            )

            icons[name] = icon

            print(
                "Converted:",
                name
            )

        else:

            print(
                "Could not convert:",
                name
            )


    except Exception as error:

        print(
            "Conversion error:",
            name
        )

        print(error)


print()
print(
    "Icons ready:",
    len(icons)
)
print()


# ============================================================
# BACKGROUND
# ============================================================

def create_background():

    image = Image.new(
        "RGB",
        (
            WIDTH,
            HEIGHT
        )
    )

    pixels = image.load()

    for y in range(HEIGHT):

        ratio = y / HEIGHT

        r = int(
            BG_TOP[0] * (1 - ratio)
            +
            BG_BOTTOM[0] * ratio
        )

        g = int(
            BG_TOP[1] * (1 - ratio)
            +
            BG_BOTTOM[1] * ratio
        )

        b = int(
            BG_TOP[2] * (1 - ratio)
            +
            BG_BOTTOM[2] * ratio
        )

        for x in range(WIDTH):

            pixels[x, y] = (
                r,
                g,
                b
            )

    return image.convert("RGBA")


# ============================================================
# DECORATION
# ============================================================

def draw_decoration(draw):

    circles = [

        (-100, 40, 190),

        (1060, 35, 190),

        (-120, 450, 220),

        (1080, 440, 230)

    ]

    for x, y, size in circles:

        draw.ellipse(

            (
                x,
                y,
                x + size,
                y + size
            ),

            fill=(248, 231, 248)

        )


# ============================================================
# HEADER
# ============================================================

def draw_header(draw):

    title = "TECH STACK"

    box = draw.textbbox(
        (0, 0),
        title,
        font=TITLE_FONT
    )

    title_width = (
        box[2] - box[0]
    )

    draw.text(

        (
            (WIDTH - title_width) / 2,
            25
        ),

        title,

        font=TITLE_FONT,

        fill=DARK_LAVENDER

    )


    subtitle = (
        "AI  ×  CYBERSECURITY  ×  DEVELOPMENT"
    )

    box = draw.textbbox(
        (0, 0),
        subtitle,
        font=SUBTITLE_FONT
    )

    subtitle_width = (
        box[2] - box[0]
    )

    draw.text(

        (
            (WIDTH - subtitle_width) / 2,
            80
        ),

        subtitle,

        font=SUBTITLE_FONT,

        fill=TEXT

    )


# ============================================================
# DRAW ROW
# ============================================================

def draw_row(
    image,
    draw,
    names,
    y,
    frame,
    direction,
    speed
):

    # Category label

    label_x = 30

    label_y = y + 5

    label_width = 175

    label_height = 65


    draw.rounded_rectangle(

        (
            label_x,
            label_y,
            label_x + label_width,
            label_y + label_height
        ),

        radius=30,

        fill=(255, 237, 247),

        outline=PINK,

        width=2

    )


    category = CATEGORY_NAMES.get(
        tuple(names),
        "TECH"
    )


    box = draw.textbbox(
        (0, 0),
        category,
        font=LABEL_FONT
    )

    text_width = (
        box[2] - box[0]
    )


    draw.text(

        (
            label_x
            +
            (label_width - text_width) / 2,

            label_y + 24
        ),

        category,

        font=LABEL_FONT,

        fill=DARK_LAVENDER

    )


    # Moving cards

    spacing = 135

    start_x = 230

    total_width = (
        len(names) * spacing
    )

    movement = (
        frame
        * speed
        * direction
    )


    for index, name in enumerate(names):

        if name not in icons:

            continue


        x = (

            start_x
            +
            index * spacing
            +
            movement

        )


        while x < 210:

            x += total_width


        while x > WIDTH:

            x -= total_width


        card_x = int(x)

        card_y = y


        # Shadow

        draw.rounded_rectangle(

            (
                card_x + 4,
                card_y + 5,
                card_x + 114,
                card_y + 90
            ),

            radius=22,

            fill=(215, 195, 225)

        )


        # Card

        draw.rounded_rectangle(

            (
                card_x,
                card_y,
                card_x + 110,
                card_y + 85
            ),

            radius=22,

            fill=(255, 252, 254),

            outline=LAVENDER,

            width=2

        )


        # Icon

        icon = icons[name]


        icon_x = (

            card_x
            +
            (110 - icon.width) // 2

        )

        icon_y = card_y + 7


        image.alpha_composite(

            icon,

            (
                icon_x,
                icon_y
            )

        )


        # Name

        box = draw.textbbox(

            (0, 0),
            name,
            font=SMALL_FONT

        )

        text_width = (
            box[2] - box[0]
        )


        draw.text(

            (
                card_x
                +
                (110 - text_width) / 2,

                card_y + 64
            ),

            name,

            font=SMALL_FONT,

            fill=TEXT

        )


# ============================================================
# FOOTER
# ============================================================

def draw_footer(draw):

    footer = (
        "BUILD  •  SECURE  •  INNOVATE"
    )

    box = draw.textbbox(

        (0, 0),

        footer,

        font=SUBTITLE_FONT

    )

    footer_width = (
        box[2] - box[0]
    )


    draw.text(

        (
            (WIDTH - footer_width) / 2,
            585
        ),

        footer,

        font=SUBTITLE_FONT,

        fill=DARK_LAVENDER

    )


# ============================================================
# CREATE ANIMATION
# ============================================================

frames = []


print()
print("==========================================")
print(" CREATING ANIMATED TECH STACK")
print("==========================================")
print()


for frame in range(FRAMES):

    print(
        "Creating frame "
        +
        str(frame + 1)
        +
        "/"
        +
        str(FRAMES)
    )


    image = create_background()

    draw = ImageDraw.Draw(image)


    draw_decoration(draw)

    draw_header(draw)


    # Languages - LEFT

    draw_row(

        image,
        draw,
        LANGUAGES,
        125,
        frame,
        -1,
        4

    )


    # Development - RIGHT

    draw_row(

        image,
        draw,
        DEVELOPMENT,
        235,
        frame,
        1,
        5

    )


    # Databases - LEFT

    draw_row(

        image,
        draw,
        DATABASES,
        345,
        frame,
        -1,
        3

    )


    # Tools - RIGHT

    draw_row(

        image,
        draw,
        TOOLS,
        455,
        frame,
        1,
        4

    )


    draw_footer(draw)


    frames.append(

        image.convert(
            "P",
            palette=Image.Palette.ADAPTIVE
        )

    )


# ============================================================
# SAVE GIF
# ============================================================

print()
print("==========================================")
print(" SAVING GIF")
print("==========================================")
print()


frames[0].save(

    OUTPUT,

    save_all=True,

    append_images=frames[1:],

    duration=FRAME_DURATION,

    loop=0,

    optimize=True

)


print()
print("==========================================")
print(" SUCCESS!")
print("==========================================")
print()

print(
    "Created:",
    os.path.abspath(OUTPUT)
)

print()

print(
    "Your animated tech-stack.gif is ready!"
)

print()