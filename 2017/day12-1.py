regs = [0, 0, 0, 0]

def get_val(operand):
    if operand.isnumeric() or operand[0] == '-' and operand[1:].isnumeric():
        return int(operand)
    else:
        return regs[ord(operand)-97]

def get_reg(operand):
    return ord(operand)-97

instructions = [ins for ins in open("input12.txt")]

c = 0
while c < len(instructions):
    instruction = instructions[c].split()[0]
    op1 = instructions[c].split()[1]
    op2 = instructions[c].split()[2] if len(instructions[c].split()) > 2 else None
    if instruction == "cpy":
        regs[get_reg(op2)] = get_val(op1)
    elif instruction == "inc":
        regs[get_reg(op1)] += 1
    elif instruction == "dec":
        regs[get_reg(op1)] -= 1
    elif instruction == "jnz" and get_val(op1) != 0:
        c += get_val(op2)
        continue

    c += 1

print(regs[0])
