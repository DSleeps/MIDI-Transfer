import rtmidi #pip install python-rtmidi
import time

#Start the midi
midi_in = rtmidi.MidiIn()
midi_out = rtmidi.MidiOut()

#Get all of the devices plugged in
in_ports = midi_in.get_ports()
out_ports = midi_out.get_ports()

print("In Ports:")
for port in in_ports:
    print(port)

print("Out Ports")
for port in out_ports:
    print(port)

#This is the keyboard
midi_in.open_port(1)
#This is the Op-1
midi_out.open_port(2)

#This controls whether or not the volume knob sets the velocity
velocity_control = False
current_velocity = 64
while True:
    message = midi_in.get_message()
    if (message):
        midi_message = message[0]
        #This means a control button/knob was pressed
        if (midi_message[0] == 176):
            if (midi_message[1] == 7):
                current_velocity = midi_message[2]
            elif (midi_message[1] == 0 and midi_message[2] == 0):
                #Flip it on and off
                velocity_control = not velocity_control
        else:
            if (velocity_control == True):
                midi_message[2] = current_velocity

            midi_out.send_message(midi_message)

        print("Last message: " + str(midi_message) + " | " +
                "Velocity Control: " + str(velocity_control) + " | " +
                "Current Velocity: " + str(current_velocity) + "     ", end="\r")
