def takeinput(typeofinput,text,exceptext):
    #usage
    # usr_input = takeinput('int', 'What is your age: ', 'wrong age entered!')
    # print(usr_input)
    if typeofinput == 'int':
        while True:
            try:
                output = int(input(text))
                return output
                break
            except:
                print(exceptext)
