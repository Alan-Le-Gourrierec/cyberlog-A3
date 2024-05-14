#!/bin/bash

generate_random_mac() {
    printf "%02x:%02x:%02x:%02x:%02x:%02x\n" \
        $((RANDOM % 256)) $((RANDOM % 256)) $((RANDOM % 256)) \
        $((RANDOM % 256)) $((RANDOM % 256)) $((RANDOM % 256))
}

change_mac() {
    interface="$1"
    random_mac=$(generate_random_mac)

    echo "Changing MAC address of $interface to $random_mac"
    sudo ifconfig "$interface" down
    sudo ifconfig "$interface" hw ether "$random_mac"
    sudo ifconfig "$interface" up
    sudo python MITM.py
}

network_interface="wlan0"

change_mac "$network_interface"

