while True:
    userInput = input('Enter IP address (type x to end): ')

    if userInput == 'x':
        break

    userInputList = userInput.split('.')

    isIP = True
    
    if len(userInputList) != 4:
        isIP = False
        
    for octet in userInputList:
        if not octet.isnumeric():
            isIP = False
            break
        if int(octet) > 255:
            isIP = False
            break
    
    if userInputList[0] == 0:
        isIP = False
    
    if isIP:
        print(userInput, 'is a valid IP address.')
    else:
        print(userInput, 'is not a valid IP address.')



