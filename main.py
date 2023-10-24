def on_button_pressed_a():
    global onOff
    onOff = onOff * -1
input.on_button_pressed(Button.A, on_button_pressed_a)

onOff = 0
taeller = 1
antalRange01 = 9
antalRange02 = 14
antalRange03 = 24
antalRange04 = 34
min02 = 11
min03 = 25
min04 = 51
maxLight = 60
minLight = 5
pauseLength = 200
strip = neopixel.create(DigitalPin.P0, 100, NeoPixelMode.RGB)
range01 = strip.range(0, antalRange01)
range02 = strip.range(min02, antalRange02)
range03 = strip.range(min03, antalRange03)
range04 = strip.range(min04, antalRange04)
onOff = 1

def on_every_interval():
    global taeller
    if onOff == -1:
        basic.show_leds("""
            . . . . .
            . . . # .
            . # . # .
            . . . # .
            . . . . .
            """)
    if onOff == 1:
        taeller = 1
        basic.show_leds("""
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            """)
        if taeller == 1:
            basic.show_leds("""
                . . . . .
                . # . . .
                . . . . .
                . . . . .
                . . . . .
                """)
            # Start with low brightness
            basic.pause(pauseLength)
            range01.show_color(neopixel.colors(NeoPixelColors.WHITE))
            range01.set_brightness(maxLight)
            # Increase brightness
            taeller = taeller + 1
        if taeller == 2:
            basic.show_leds("""
                . . . . .
                . # . # .
                . . . . .
                . . . . .
                . . . . .
                """)
            # Start with low brightness
            basic.pause(pauseLength)
            range02.show_color(neopixel.colors(NeoPixelColors.WHITE))
            range02.set_brightness(maxLight)
            # Increase brightness
            taeller = taeller + 1
        if taeller == 3:
            basic.show_leds("""
                . . . . .
                . # . # .
                . . . . .
                . # . . .
                . . . . .
                """)
            # Start with low brightness
            basic.pause(pauseLength)
            range03.show_color(neopixel.colors(NeoPixelColors.WHITE))
            range03.set_brightness(maxLight)
            # Increase brightness
            taeller = taeller + 1
        if taeller == 4:
            basic.show_leds("""
                . . . . .
                . # . # .
                . . . . .
                . # . # .
                . . . . .
                """)
            # Start with low brightness
            basic.pause(pauseLength)
            range04.show_color(neopixel.colors(NeoPixelColors.WHITE))
            range04.set_brightness(maxLight)
            # Increase brightness
            taeller = taeller + 1
            # Start with low brightness
            basic.pause(pauseLength)
            strip.clear()
loops.every_interval(pauseLength * 6, on_every_interval)
