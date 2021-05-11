def yesorno(self,yesact,noact):
    opt = [1,0]
    while True:
        try:
            output = int(input(f"Type '1' for {yesact} or '0' for {noact}: "))
            if output not in opt:
                print("You can only enter '1' or '0'" )
                continue
            else: 
                break
        except Exception as e:
            print("Enter a right option!")
            continue
    return output
def takeinput(self,typeofinput,text,exceptext):
    if typeofinput == 'int':
        while True:
            try:
                output = int(input(text))
                break
            except:
                print(exceptext)
        return output
    elif typeofinput == 'string':
        while True:
            try:
                output = input(text)
                break
            except:
                print(exceptext)
        return output

