encodedWord = "tx33dom"
#encodedWord = "t3xb3f"
#encodedWord = "koxb3zpond3nk3"
#encodedWord = "fako fim3"
#encodedWord = "zom3 xafz bun"	
#encodedWord = "txiday tun tob tx3nkh tbi3z"
#encodedWord = "kafz kan kafkh kakfuz3z wifh klawz"
	
	
	
#encodedWord = "UUHO"  		#Used for Bonus
#encodedWord = "BOUUUUOUU" 	#Used for Bonus

decodedWord = ""
for char in encodedWord:  #
    if char == 't':
        decodedWord += 'f'
    elif char == 'f':
        decodedWord += 't'
    elif char == '3':
        decodedWord += 'e'
    elif char == 'k':
        decodedWord += 'c'
    elif char == 'z':
        decodedWord += 's'
    elif char == 'b':
        decodedWord += 'r'
    elif char == 'x':
        decodedWord += 'r'
    elif char == 'U':
        if len(decodedWord) > 0 and decodedWord[-1] == 'W':
            continue
        decodedWord += 'W'
    else:
        decodedWord += char

print(decodedWord)
