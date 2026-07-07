"""Crop and enhance professional profile photo. Run: python assets/process-profile.py"""

from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
DUO = ROOT / "assets" / "source-duo.png"
SOLO = ROOT / "assets" / "source-solo.png"
OUT = ROOT / "assets" / "profile.jpg"


def enhance(img: Image.Image) -> Image.Image:
    img = ImageEnhance.Contrast(img).enhance(1.08)
    img = ImageEnhance.Brightness(img).enhance(1.04)
    img = ImageEnhance.Color(img).enhance(0.95)
    img = ImageEnhance.Sharpness(img).enhance(1.15)
    return img


def crop_right_person(duo: Image.Image) -> Image.Image:
    w, h = duo.size
    left = int(w * 0.48)
    person = duo.crop((left, 0, w, h))

    pw, ph = person.size
    top = int(ph * 0.04)
    bottom = int(ph * 0.40)
    side = int(pw * 0.06)
    return person.crop((side, top, pw - side, bottom))


def crop_solo_professional(solo: Image.Image) -> Image.Image:
    w, h = solo.size
    top = int(h * 0.06)
    bottom = int(h * 0.52)
    side = int(w * 0.12)
    return solo.crop((side, top, w - side, bottom))


def to_square_portrait(img: Image.Image, size: int = 480) -> Image.Image:
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    sq = img.crop((left, top, left + side, top + side))
    return sq.resize((size, size), Image.Resampling.LANCZOS)


def main():
    duo_src = Path(
        r"C:\Users\ETA SETUP\.cursor\projects\c-Users-ETA-SETUP-Desktop-GITHUB-PORTFOLIO-2025\assets\c__Users_ETA_SETUP_AppData_Roaming_Cursor_User_workspaceStorage_cfdd76dd76241437744b9c764aefc0cc_images_composer-annotation-109abada-91f9-4377-a6b3-579cd5767fcd.png"
    )
    solo_src = Path(
        r"C:\Users\ETA SETUP\.cursor\projects\c-Users-ETA-SETUP-Desktop-GITHUB-PORTFOLIO-2025\assets\c__Users_ETA_SETUP_AppData_Roaming_Cursor_User_workspaceStorage_cfdd76dd76241437744b9c764aefc0cc_images_composer-annotation-955fb84a-52df-4e5f-8d4c-f11acd0fc310.png"
    )

    duo_src.copy(ROOT / "assets" / "source-duo.png")
    solo_src.copy(ROOT / "assets" / "source-solo.png")

    duo = Image.open(duo_src).convert("RGB")
    solo = Image.open(solo_src).convert("RGB")

    duo_crop = enhance(crop_right_person(duo))
    solo_crop = enhance(crop_solo_professional(solo))

    duo_crop.save(ROOT / "assets" / "profile-duo-crop.jpg", "JPEG", quality=90)
    solo_crop.save(ROOT / "assets" / "profile-solo-crop.jpg", "JPEG", quality=90)

    # Use solo crop: best head-and-shoulders framing, friendly professional smile
    portrait = to_square_portrait(solo_crop, 480)
    portrait.save(OUT, "JPEG", quality=92, optimize=True)
    print(f"Saved {OUT} (selected: solo portrait — head & shoulders)")


if __name__ == "__main__":
    main()
