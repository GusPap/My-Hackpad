# code.py — KMK Firmware for Hackpad
# Hardware: XIAO RP2040, 4x switches, 2x SK6812MINI LEDs

import board
import neopixel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros, Delay

# ── Keyboard ───────────────────────────────────────────────────────
keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# ── Switches ───────────────────────────────────────────────────────
# SW1 → GPIO1 | SW2 → GPIO2 | SW3 → GPIO4 | SW4 → GPIO3
PINS = [board.D1, board.D2, board.D4, board.D3]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# ── LEDs ───────────────────────────────────────────────────────────
# 2x SK6812MINI chained, data on GPIO6
pixels = neopixel.NeoPixel(
    board.D6,
    2,
    brightness=0.3,
    auto_write=True, # Changed to True so it actively manages the LEDs
    pixel_order=neopixel.GRBW
)
pixels[0] = (255, 0, 128, 0)
pixels[1] = (0, 128, 255, 0)

# ── Keymap ─────────────────────────────────────────────────────────
# SW1 → Open Google Chrome (Windows)
# SW2 → Open Spotify (Windows)
# SW3 → Copy  (Ctrl+C)
# SW4 → Paste (Ctrl+V)

keyboard.keymap = [
    [
        # Chrome Macro (Added 100ms delay for the Run window to open)
        KC.MACRO(
            Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
            Delay(100),
            Tap(KC.C), Tap(KC.H), Tap(KC.R), Tap(KC.O), Tap(KC.M), Tap(KC.E),
            Tap(KC.ENTER)
        ),

        # Spotify Macro (Added 100ms delay for the Run window to open)
        KC.MACRO(
            Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
            Delay(100),
            Tap(KC.S), Tap(KC.P), Tap(KC.O), Tap(KC.T), Tap(KC.I), Tap(KC.F), Tap(KC.Y),
            Tap(KC.ENTER)
        ),

        # Optimized clean shortcuts instead of multi-line macros
        KC.LCTL(KC.C), # Ctrl + C
        KC.LCTL(KC.V), # Ctrl + V
    ]
]

# ── Run ────────────────────────────────────────────────────────────
if __name__ == '__main__':
    keyboard.go()
