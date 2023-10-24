input.onButtonPressed(Button.A, function () {
    onOff = onOff * -1
})
let onOff = 0
let taeller = 1
let antalRange01 = 9
let antalRange02 = 14
let antalRange03 = 24
let antalRange04 = 34
let min02 = 11
let min03 = 25
let min04 = 51
let maxLight = 100
let minLight = 5
let pauseLength = 200
let strip = neopixel.create(DigitalPin.P0, 100, NeoPixelMode.RGB)
let range01 = strip.range(0, antalRange01)
let range02 = strip.range(min02, antalRange02)
let range03 = strip.range(min03, antalRange03)
let range04 = strip.range(min04, antalRange04)
onOff = 1
loops.everyInterval(pauseLength * 6, function () {
    if (onOff == -1) {
        basic.showLeds(`
            . . . . .
            . . . # .
            . # . # .
            . . . # .
            . . . . .
            `)
    }
    if (onOff == 1) {
        taeller = 1
        basic.showLeds(`
            . . . . .
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            `)
        if (taeller == 1) {
            basic.showLeds(`
                . . . . .
                . # . . .
                . . . . .
                . . . . .
                . . . . .
                `)
            // Start with low brightness
            basic.pause(pauseLength)
            range01.showColor(neopixel.colors(NeoPixelColors.White))
            range01.setBrightness(maxLight)
            // Increase brightness
            taeller = taeller + 1
        }
        if (taeller == 2) {
            basic.showLeds(`
                . . . . .
                . # . # .
                . . . . .
                . . . . .
                . . . . .
                `)
            // Start with low brightness
            basic.pause(pauseLength)
            range02.showColor(neopixel.colors(NeoPixelColors.White))
            range02.setBrightness(maxLight)
            // Increase brightness
            taeller = taeller + 1
        }
        if (taeller == 3) {
            basic.showLeds(`
                . . . . .
                . # . # .
                . . . . .
                . # . . .
                . . . . .
                `)
            // Start with low brightness
            basic.pause(pauseLength)
            range03.showColor(neopixel.colors(NeoPixelColors.White))
            range03.setBrightness(maxLight)
            // Increase brightness
            taeller = taeller + 1
        }
        if (taeller == 4) {
            basic.showLeds(`
                . . . . .
                . # . # .
                . . . . .
                . # . # .
                . . . . .
                `)
            // Start with low brightness
            basic.pause(pauseLength / 4)
            range04.showColor(neopixel.colors(NeoPixelColors.White))
            range04.setBrightness(maxLight)
            // Increase brightness
            taeller = taeller + 1
            strip.clear()
        }
    }
})
