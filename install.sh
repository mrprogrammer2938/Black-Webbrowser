if [[ "$(id -u)" -ne 0 ]];
then
  echo "Please, Run Black Webbrowser as Root!"
  exit
fi 
function main() {
    printf '\033]2;Black-Webbrowser/Installing\a'
    clear
    echo "Installing..."
    sleep 2
    apt install python
    apt install python3
    apt install python3-pip
    pip install --upgrade pip
    echo "
Finish...

Usage:
     python install.py
"
    exit
}
main