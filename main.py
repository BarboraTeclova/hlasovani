radio.set_group(69)
#key value
#vote 1..znak A(64)
#     2..znak B(65)
#     3..znak C(66)
#     4..znak D(67)
# server povolí/zakáže hlasování
# klient odesílá hlas (i opakovaně)
#klient (volitelně) indikuje zda lze hlasovat
# enabled 1/0
#value = Math.constrain(value, 1, 10)
#char = string.from_char_code(65)

#    cislo = 0
#    pocet = 0
#    radio.set_group(69)
#    pocet = 0
#    cislo = 0

#def on_button_pressed_a():
#    global poradi
#    if poradi == 0:

#def on_received_number_deprecated(receivedNumber):
#    if receivedNumber < len(pocet_odpovedi):
#        pocet_odpovedi[receivedNumber] = pocet_odpovedi[receivedNumber] + 1
#radio.on_received_number_deprecated(on_received_number_deprecated)

#def on_button_pressed_ab():
#    index = 0
#    while index <= len(pocet_odpovedi) - 1:
#        basic.show_number(pocet_odpovedi[index])
#        basic.pause(200)
#        index += 1
#input.on_button_pressed(Button.AB, on_button_pressed_ab)

#pocet_odpovedi: List[number] = []
#radio.set_group(69)
#pocet_odpovedi = [0, 0, 0, 0]
#        poradi = len(odpovedi)
#    poradi += -1
#    basic.show_string("" + (odpovedi[poradi]))
#input.on_button_pressed(Button.A, on_button_pressed_a)

#def on_button_pressed_ab():
#    radio.send_number(poradi)
#input.on_button_pressed(Button.AB, on_button_pressed_ab)

#def on_button_pressed_b():
#    global poradi
#    poradi += 1
#    if poradi == len(odpovedi):
#    if poradi == len(odpovedi):
#        poradi = 0
#    basic.show_string("" + (odpovedi[poradi]))
#input.on_button_pressed(Button.B, on_button_pressed_b)

#poradi = 0
#odpovedi: List[str] = []
#radio.set_group(100)
#odpovedi = ["A", "B", "C", "D"]
#poradi = 0
#basic.show_string("" + (odpovedi[poradi]))

#    def on_received_number_deprecated(receivedNumber):
#        global pocet
#        if receivedNumber == cislo:
#            pocet += 1
#    radio.on_received_number_deprecated(on_received_number_deprecated)

#    def on_button_pressed_a():
#        global cislo
#        cislo += -1
#        basic.show_number(cislo)
#    input.on_button_pressed(Button.A, on_button_pressed_a)

#    def on_button_pressed_ab():
#        global pocet
#        pocet = 0
#    input.on_button_pressed(Button.AB, on_button_pressed_ab)

#    def on_button_pressed_b():
#        global cislo
#        cislo += 1
#        basic.show_number(cislo)
#    input.on_button_pressed(Button.B, on_button_pressed_b)