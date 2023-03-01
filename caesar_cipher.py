the_alpha_bet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
asci_art="""/
                                                                             /$$           /$$                          
                                                                            |__/          | $$                          
  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$         /$$$$$$$ /$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
 /$$_____/ |____  $$ /$$__  $$ /$$_____/ |____  $$ /$$__  $$       /$$_____/| $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$        /$$$$$$$| $$$$$$$$|  $$$$$$   /$$$$$$$| $$  \__/      | $$      | $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$       /$$__  $$| $$_____/ \____  $$ /$$__  $$| $$            | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$      
|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$$$$$$/|  $$$$$$$| $$            |  $$$$$$$| $$| $$$$$$$/| $$  | $$|  $$$$$$$| $$      
 \_______/ \_______/ \_______/|_______/  \_______/|__/             \_______/|__/| $$____/ |__/  |__/ \_______/|__/      
                                                                                | $$                                    
                                                                                | $$                                    
                                                                                |__/                                    
"""
def encode(text,shift):
    the_alpha_bet_len = len(the_alpha_bet) 
    text_array=list(text)
    temp_text=''
    for i in range(0,len(text_array)):
        is_word_exists= False
        for j in range(0,the_alpha_bet_len):
            if (text_array[i] == the_alpha_bet[j]):
                if(j+shift < the_alpha_bet_len):
                    temp_text += the_alpha_bet[j+shift]
                    is_word_exists = True
                else:
                    out_of_Range_true_val = (j+shift) - the_alpha_bet_len
                    temp_text += the_alpha_bet[out_of_Range_true_val]
                    is_word_exists = True
        if(is_word_exists == False):
            temp_text += text_array[i]
    return temp_text

def decode(text,shift):
    the_alpha_bet_len = len(the_alpha_bet) 
    text_array=list(text)
    temp_text=''
    for i in range(0,len(text_array)):
        is_word_exists= False
        for j in range(0,the_alpha_bet_len):
            if(text_array[i] == the_alpha_bet[j]):
                if(j-shift >=0):
                    temp_text += the_alpha_bet[j-shift]
                    is_word_exists = True
                else:
                    out_of_Range_true_val = the_alpha_bet_len - (shift-j)
                    temp_text += the_alpha_bet[out_of_Range_true_val]
                    is_word_exists = True
        if(is_word_exists == False):
            temp_text += text_array[i]
    return temp_text

print(asci_art)

while True:
    method= input("Please enter 'encode' , 'decode' or 'exit'\n").lower()
    if(method == 'exit'):
        break
    text = input('please enter your text\n').lower()
    shift = int(input("Type the Shift number\n"))
    if(method == 'encode'):
        print(encode(text,shift))
    elif(method == 'decode'):
        print(decode(text,shift))
    print('=========================================================')        
