#!/usr/bin/env bash
# This Programm Write by Mr.nope
# Black-Recon v1.0
if [[ "$(id -u)" -ne 0 ]]; then
  echo "
Please, Run This Programm as Root"
  exit 1
fi
main() {
  printf '\033]2;Black-Recon/Installing'
  clear
  echo "Installing Black-Recon..."
  chmod +x brecon.py
  sleep 2
  apt install python
  apt install python3
  apt install python3-pip
  pip3 install --upgrade pip
  echo "
Finish...!
Usage:
      python3 brecon.py"
  exit 1
}
main