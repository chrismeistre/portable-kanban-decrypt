# portable-kanban-decrypt

PortableKanban 4.3.6578.38136 - Decrypt Stored Password

I recently did the Atom box on HackTheBox, and came across this vulnerability while researching.

Although there were tools out there already, I decided to modify it slightly to work for my own use case.

Source: https://www.exploit-db.com/exploits/49409

Installation:

```bash
git clone https://github.com/chrismeistre/portable-kanban-decrypt
cd portable-kanban-decrypt
pip3 install -r requirements.txt
```

Usage:

```bash
python3 decrypt.py <hash>
```