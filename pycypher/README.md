# pycypher

---

Send messages safely, only the person with the keyword will be able to read your message.   

## How to use  

1. Copy the **pycypher** directory to your computer.
2. run the file with python3.   
   `python3 pycypher.py`
3. Choose what you would like to do, encode or decode a message.   
   ```console
    Choose an option:
        [ 1 ] - Encode
        [ 2 ] - Decode
        [ q ] - Exit
    Your option: 1
   ```
4. You will now enter the message you would like to encode.   
   ```console
    Type your message:
    No matter the size of the message, it can contain spaces, special characters, capital letters, accents, only it CANNOT contain line breaks. Everything will be coded.
   ```
5. Choose the keyword that will be used to encode and decode the message.   
   ```console
    ---> Write your keyword: Protego
   ```
6. The message will be encoded.   
   ```console
    Its encoded text is:
    (J&uf{{Í%&{1Í&ÚÕ!Í&J-&{1Í&uÍÚÚfPÍw&Õ{&"f]&"J]{fÕ]&ÚÓf"ÍÚw&ÚÓÍ"Õfç&"1f%f"{Í%Úw&"fÓÕ{fç&çÍ{{Í%Úw&f""Í]{Úw&J]ç_&Õ{&ej((êv&"J]{fÕ]&çÕ]Í&x%ÍfóÚl&AkÍ%_{1Õ]P&ÁÕçç&xÍ&"J$Í$l
   ```   

Now just send the message to someone and tell them the key word.   

To decode, follow the steps below:   

1. run the file with python3.   
   `python3 pycypher.py`   
2. Choose option [ 2 ], decode.   
   ```console
    Choose an option:
        [ 1 ] - Encode
        [ 2 ] - Decode
        [ q ] - Exit
    Your option: 2
   ```   
3. Copy the coded message.   
   ```console
   Type your message:
   (J&uf{{Í%&{1Í&ÚÕ!Í&J-&{1Í&uÍÚÚfPÍw&Õ{&"f]&"J]{fÕ]&ÚÓf"ÍÚw&ÚÓÍ"Õfç&"1f%f"{Í%Úw&"fÓÕ{fç&çÍ{{Í%Úw&f""Í]{Úw&J]ç_&Õ{&ej((êv&"J]{fÕ]&çÕ]Í&x%ÍfóÚl&AkÍ%_{1Õ]P&ÁÕçç&xÍ&"J$Í$l
   ```   
4. Enter the key word.   
   ```console
   ----> Write your keyword: Protego
   ```   
5. The decoded message will be shown.   
   ```console
   Your decoded text is:
   No matter the size of the message, it can contain spaces, special characters, capital letters, accents, only it CANNOT contain line breaks. Everything will be coded.
   ```   

