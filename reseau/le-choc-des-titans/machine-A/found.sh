#!/bin/bash

network="192.168.26"
subnet_mask="/24"

for ((i=1; i<=255; i++)); do
    ip_address="$network.$i"
    ping -c 1 -W 1 "$ip_address" &> /dev/null

    if [ $? -eq 0 ]; then
        echo "Adresse IP $ip_address atteignable."
    fi
done


