#!/bin/bash

if [ -f "server.jar" ]; then
    cp server.jar forge-1.7.10-10.13.4.1614-1.7.10-universal.jar
fi

java -jar packwiz-installer-bootstrap.jar --no-gui --side server "https://deeplerg.github.io/103-ntm-space/pack.toml"

java -Xms128M -XX:MaxRAMPercentage=95.0 -Dterminal.jline=false -Dterminal.ansi=true @java9args.txt @gc-args.txt -jar lwjgl3ify-3.0.26-forgePatches.jar