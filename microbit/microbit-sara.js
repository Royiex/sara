function A () {
    basic.clearScreen()
    basic.showString("Hau ar ju")
}
input.onButtonPressed(Button.A, function () {
    state = 2
    A()
    state = 1
})
input.onGesture(Gesture.TiltLeft, function () {
    basic.showString("Haj puki Sawa")
    state = 1
})
function B () {
    basic.clearScreen()
    basic.showString("I")
    basic.showIcon(IconNames.SmallHeart)
    basic.clearScreen()
    basic.showString("Sara")
}
function Shake () {
    basic.clearScreen()
    basic.showString("Baj puki  Lav ju")
}
input.onButtonPressed(Button.B, function () {
    state = 2
    B()
    state = 1
})
input.onGesture(Gesture.Shake, function () {
    state = 2
    Shake()
    state = 0
    while (state == 0) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
let state = 0
basic.showString("Haj puki Sawa")
state = 1
basic.forever(function () {
    while (state == 1) {
        basic.showIcon(IconNames.Heart)
    }
})
