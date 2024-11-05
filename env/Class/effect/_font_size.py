import data
font_20 = data.font(20)
font_22 = data.font(22)
font_24 = data.font(24)
font_26 = data.font(26)
font_28 = data.font(28)
font_30 = data.font(30)
font_32 = data.font(32)
font_34 = data.font(34)
font_36 = data.font(36)
font_38 = data.font(38)
font_40 = data.font(40)
font_42 = data.font(42)
def get_size_font(size):
    if size == 20:
        return font_20
    elif size == 22:
        return font_22
    elif size == 24:
        return font_24
    elif size == 26:
        return font_26
    elif size == 28:
        return font_28
    elif size == 30:
        return font_30
    elif size == 32:
        return font_32
    elif size == 34:
        return font_34
    elif size == 36:
        return font_36
    elif size == 38:
        return font_38
    elif size == 40:
        return font_40
    else:
        return font_42