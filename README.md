# PiMidi

Add some links 

https://neuma.studio/rpi-as-midi-host.html
https://github.com/Hecsall/arduino-midi-footswitch/issues/3#issuecomment-968376104



Notes from a website

https://blog.fearcat.in/a?ID=00650-a146705a-fe56-4c39-b0f8-906ec789b96c
Development environment: Debian 9.3

1. Download
wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.49.tar.xz

 See http://www.bluez.org/download/or http://www.kernel.org/pub/linux/bluetooth/for the latest version

2. Unzip
tar xf bluez-5.49.tar.xz

3. Compile
3.1 Step
# sudo apt-get install libglib2.0-dev libudev-dev libsbc-dev libreadline-dev libical-dev libelf-dev elfutils libdw-dev libjson-c-dev libalsa-ocaml-dev libspeexdsp-dev

# cd bluez-5.49

# ./bootstrap-configure # Equivalent to ./configure, it is estimated that bluez does not need to be maintained by autoconf tools

# make

3.2 Handling errors
Error: Checking for GLIB ... NO            configure: error: GLib >= 2.28 is required
the Solve: after sudo apt-get install libglib2.0-dev # version of this estimate is large, anyway, after the installation of error is not reported version is too low
------------------------------------------------------------

Error: checking for UDEV... no            configure: error: libudev >= 143 is required
Solve: sudo apt-get install libudev-dev
------------------------------------------------------------

Error: configure: error: SBC library >= 1.2 is required Solve: sudo apt-get install libsbc-dev

------------------------------------------------------------

Error: checking for readline/readline.h... no         configure: error: readline header files are required
Solve: sudo apt-get install libreadline-dev

------------------------------------------------------------

Error: checking elfutils/libdwfl.h usability... no           checking elfutils/libdwfl.h presence... no
          checking for elfutils/libdwfl.h... no

          configure: error: elfutils support is required

Solve: sudo apt-get install libelf-dev elfutils libdw-dev

Finally, after installing libdw-dev to solve the problem, libelf-dev elfutils is not sure, I will not test it, you can try without installing it.

------------------------------------------------------------

Error: checking for JSONC... no

            configure: error: json-c is required

Solve: sudo apt-get install libjson-c-dev

------------------------------------------------------------

Error : checking for ICAL... no

          configure: error: libical is required

Solve: sudo apt-get install libical-dev

------------------------------------------------------------

Error: checking for ALSA... no

          configure: error: ALSA lib is required for MIDI support

Solve: sudo apt-get install libalsa-ocaml-dev

------------------------------------------------------------Error: checking for DBUS... no
           configure: error: D-Bus >= 1.6 is required

Solve : sudo apt-get install libdbus-1-dev # or libdbus-c++-dev

------------------------------------------------------------
Error: configure: error: SPEEXDSP library >= 1.2 is required

Solve: sudo apt-get install libspeexdsp-dev

------------------------------------------------------------

In short: sudo apt-get install libical-dev libglib2.0-dev libreadline-dev libdbus-1-dev libudev-dev libsbc-dev libelf-dev elfutils libdw-dev libjson-c-dev libalsa-ocaml-dev libspeexdsp-dev

