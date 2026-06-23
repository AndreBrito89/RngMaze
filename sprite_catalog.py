DEFAULT_SPRITE_PATTERN = [
    "...HHH...",
    "..HBBBH..",
    ".BBE.EBB.",
    ".BBBBBBB.",
    "..BMMMB..",
    ".BBMMMBB.",
    "..BBBBB..",
    "...B.B...",
    "..H...H..",
]

DEFAULT_SPRITE_PALETTE = {
    "B": "#6d3a7f",
    "E": "#ff4d4d",
    "H": "#a35dbf",
    "M": "#2a0a35",
}

SPRITE_CATALOG = {
    "rat": {
        "pattern": [
            "....H....",
            "...HBH...",
            "..BBBBB..",
            ".BBE.EBB.",
            ".BBBBBBB.",
            "..BMMMB..",
            "...BBB...",
            "....B....",
        ],
        "palette": {
            "B": "#7a7572",
            "E": "#ff2c2c",
            "H": "#b7b2ad",
            "M": "#4a0f0f",
        },
    },
    "imp": {
        "pattern": [
            "...H.H...",
            "..HBBBH..",
            ".BBE.EBB.",
            ".BBBBBBB.",
            "..BMMMB..",
            "...BBB...",
            "..B...B..",
        ],
        "palette": {
            "B": "#8c4a2f",
            "E": "#ffd25e",
            "H": "#c57149",
            "M": "#2a0a0a",
        },
    },
    "ogre": {
        "pattern": [
            "...HHH...",
            "..HBBBH..",
            ".BBBBBBB.",
            ".BBE.EBB.",
            ".BBBBBBB.",
            "..BMMMB..",
            "..BBBBB..",
            "...BBB...",
            "...B.B...",
        ],
        "palette": {
            "B": "#587c39",
            "E": "#ffe16b",
            "H": "#80a95f",
            "M": "#3c2414",
        },
    },
    "revenant": {
        "pattern": [
            "...HHH...",
            "..HBBBH..",
            ".BBE.EBB.",
            ".BBBBBBB.",
            ".BMM.MM.B",
            "..BBBBB..",
            "..B...B..",
            "...B.B...",
        ],
        "palette": {
            "B": "#8a8a8a",
            "E": "#ff4d4d",
            "H": "#c2c2c2",
            "M": "#4a0f0f",
        },
    },
}


def get_enemy_sprite_data(sprite_key):
    sprite = SPRITE_CATALOG.get(sprite_key)
    if sprite is None:
        return DEFAULT_SPRITE_PATTERN, DEFAULT_SPRITE_PALETTE
    return sprite["pattern"], sprite["palette"]
