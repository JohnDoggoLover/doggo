import sys
import time
import math

vars = {"inf": math.inf }

def compute(words, vars):
    labels = {}
    i = 0
    gt = False
    lt = False
    while i < len(words):
        tok = words[i].strip()
        parts = tok.split("-")
        cmd = parts[0]
        if cmd == "label":
            labels[parts[1]] = i
        i = i + 1
    i = 0
    while i < len(words):
        tok = words[i].strip()
        parts = tok.split("-")
        cmd = parts[0]

        # ----- out -----
        if cmd == "out":
            if len(parts) < 2:
                print("Error: missing argument for 'out'")
            else:
                arg = parts[1]
                if arg.startswith('"'):
                    print(arg[1:])  # literal string
                else:
                    print(vars.get(arg, f"<undefined {arg}>"))
        elif cmd == "sleep":
            time.sleep(float(parts[1]))
        elif cmd == "cmp":
            if len(parts) < 3:
                print("Invalid amount of inputs for cmp")
            else:
                a_raw, b_raw = parts[1], parts[2]

        # resolve values (vars or literals)
                def resolve(val):
            # handle numeric literal
                    if val.startswith("n"):
                        try:
                            return float(val[1:])
                        except ValueError:
                            return val
            # handle string literal
                    if val.startswith('"'):
                        return val[1:]
            # otherwise, variable lookup
                    return vars.get(val, val)

                a = resolve(a_raw)
                b = resolve(b_raw)

        # numeric compare
                if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                    if a > b:
                        gt, lt = True, False
                    elif a < b:
                        gt, lt = False, True
                    else:
                        gt = lt = False
                else:
            # fallback string compare
                    if str(a) > str(b):
                        gt, lt = True, False
                    elif str(a) < str(b):
                        gt, lt = False, True
                    else:
                        gt = lt = False

        elif cmd == "add":
            # syntax: add-result-op1-op2/
            try:
                if parts[2][0] == "n" and parts[3][0] != "n":
                    vars[parts[1]] = float(parts[2][1:]) + vars[parts[3]]
                elif parts[3][0] == "n" and parts[2][0] != "n":
                    vars[parts[1]] = vars[parts[2]] + float(parts[3][1:])
                elif parts[3][0] == "n" and parts[2][0] == "n":
                    vars[parts[1]] = float(parts[2][1:]) + float(parts[3][1:])
                else:
                    vars[parts[1]] = vars[parts[2]] + vars[parts[3]]
            except KeyError as e:
                print(f"[add error] undefined variable: {e}")
            except Exception as e:
                print(f"[add error] {e}")

        elif cmd == "sub":
            # syntax: add-result-op1-op2/
            try:
                if parts[2][0] == "n" and parts[3][0] != "n":
                    vars[parts[1]] = float(parts[2][1:]) - vars[parts[3]]
                elif parts[3][0] == "n" and parts[2][0] != "n":
                    vars[parts[1]] = vars[parts[2]] - float(parts[3][1:])
                elif parts[3][0] == "n" and parts[2][0] == "n":
                    vars[parts[1]] = float(parts[2][1:]) - float(parts[3][1:])
                else:
                    vars[parts[1]] = vars[parts[2]] - vars[parts[3]]
            except KeyError as e:
                print(f"[add error] undefined variable: {e}")
            except Exception as e:
                print(f"[add error] {e}")
        
        elif cmd == "mul":
            # syntax: add-result-op1-op2/
            try:
                if parts[2][0] == "n" and parts[3][0] != "n":
                    vars[parts[1]] = float(parts[2][1:]) * vars[parts[3]]
                elif parts[3][0] == "n" and parts[2][0] != "n":
                    vars[parts[1]] = vars[parts[2]] * float(parts[3][1:])
                elif parts[3][0] == "n" and parts[2][0] == "n":
                    vars[parts[1]] = float(parts[2][1:]) * float(parts[3][1:])
                else:
                    vars[parts[1]] = vars[parts[2]] * vars[parts[3]]
            except KeyError as e:
                print(f"[add error] undefined variable: {e}")
            except Exception as e:
                print(f"[add error] {e}")

        elif cmd == "div":
            # syntax: add-result-op1-op2/
            try:
                if parts[2][0] == "n" and parts[3][0] != "n":
                    vars[parts[1]] = float(parts[2][1:]) / vars[parts[3]]
                elif parts[3][0] == "n" and parts[2][0] != "n":
                    vars[parts[1]] = vars[parts[2]] / float(parts[3][1:])
                elif parts[3][0] == "n" and parts[2][0] == "n":
                    vars[parts[1]] = float(parts[2][1:]) / float(parts[3][1:])
                else:
                    vars[parts[1]] = vars[parts[2]] / vars[parts[3]]
            except KeyError as e:
                print(f"[add error] undefined variable: {e}")
            except Exception as e:
                print(f"[add error] {e}")

        elif cmd == "mod":
            # syntax: add-result-op1-op2/
            try:
                if parts[2][0] == "n" and parts[3][0] != "n":
                    vars[parts[1]] = float(parts[2][1:]) % vars[parts[3]]
                elif parts[3][0] == "n" and parts[2][0] != "n":
                    vars[parts[1]] = vars[parts[2]] % float(parts[3][1:])
                elif parts[3][0] == "n" and parts[2][0] == "n":
                    vars[parts[1]] = float(parts[2][1:]) % float(parts[3][1:])
                else:
                    vars[parts[1]] = vars[parts[2]] % vars[parts[3]]
            except KeyError as e:
                print(f"[add error] undefined variable: {e}")
            except Exception as e:
                print(f"[add error] {e}")


        elif cmd == "set":
            if parts[2][0] == "n":
                parts[2] = float(parts[2][1:])
            elif parts[2][0] == '"':
                parts[2] = str(parts[2][1:])
            elif parts[2] == "finp":
                parts[2]= float(input())
            elif parts[2] == "sinp":
                parts[2]= str(input())
            vars[parts[1]] = parts[2]


        # ----- jump if greater -----
        elif cmd == "jg":
            if gt:
                try:
                    target = int(parts[1])
                    if 0 <= target <= len(words):
                        if target == len(words):
                            break
                        i = target
                        continue
                except:
                    print(f"Invalid jump target: {parts[1]}")

        # ----- jump if less -----
        elif cmd == "jl":
            if lt:
                try:
                    target = int(parts[1])
                    if 0 <= target <= len(words):
                        if target == len(words):
                            break
                        i = target
                        continue
                except:
                    print(f"Invalid jump target: {parts[1]}")


        elif cmd[0] == "#":
            pass

        # ----- unconditional jump ----
        elif cmd == "label":
            pass
        elif cmd == "exit":
            break
        elif cmd == "jmp":
            try:
                target = int(parts[1])
                if 0 <= target <= len(words):
                    if target == len(words):
                        break
                    i = target
                    continue
            except:
                print(f"Invalid jump target: {parts[1]}")

        # ----- jump if greater -----
        elif cmd == "ljg":
            if gt:
                try:
                    target = int(labels[parts[1]])
                    if 0 <= target <= len(words):
                        if target == len(words):
                            break
                        i = target
                        continue
                except:
                    print(f"Invalid jump target: {parts[1]}")

        # ----- jump if less -----
        elif cmd == "ljl":
            if lt:
                try:
                    target = int(labels[parts[1]])
                    if 0 <= target <= len(words):
                        if target == len(words):
                            break
                        i = target
                        continue
                except:
                    print(f"Invalid jump target: {parts[1]}")

        elif cmd == "ljmp":
            try:
                target = int(labels[parts[1]])
                if 0 <= target <= len(words):
                    if target == len(words):
                        break
                    i = target
                    continue
            except:
                print(f"Invalid jump target: {parts[1]}")


        # ----- no-op -----
        elif cmd == "no":
            pass

        # ✅ increment at the *end of loop*
        else:
            print("INCORRECT COMMAND " + str(words[i]))
            break
        i += 1


# ------------- main -------------
if len(sys.argv) < 2:
    print("Usage: python main.py <file>")
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()

words = [word.strip() for word in content.split("/") if word.strip()]
compute(words, vars)