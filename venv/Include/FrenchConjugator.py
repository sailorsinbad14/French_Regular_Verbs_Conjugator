#print(float("210" * int(input("Enter a number:" ))))
#enter number: 2
#int ( 2 ) * "210"
# => "210210"
#float("210210")
#=> 210210.0

#Input a word
x = input("Enter a French verb (press Enter to exit): \n")
#print(x[(l-2):(l)])
ck = True
# loop
while ck :
    l = len(x)
    #check conditions
    if x == '':
        break
    if x[(l-2):(l)] == 'ir':
        drop = x[0: (l-2)]
        #print(drop)
        je = 'is'
        tu = 'is'
        ilElle = 'it'
        nous = 'issons'
        vous  = 'issez'
        ilsElles = 'issent'
        print('Je ' + drop + je  )
        print('Tu ' + drop + tu)
        print('Il / Elle / On ' + drop + ilElle)
        print('Nous ' + drop + nous)
        print('Vous ' + drop + vous)
        print('Ils / Elles ' + drop + ilsElles)
    elif x[(l-2):(l)] == 'er' :
        print( 'It is regular verb. ')
        drop = x[0: (l - 2)]
        # print(drop)
        je = 'e'
        tu = 'es'
        ilElle = 'e'
        nous = 'ons'
        vous = 'ez'
        ilsElles = 'ent'
        print('Je ' + drop + je)
        print('Tu ' + drop + tu)
        print('Il / Elle / On ' + drop + ilElle)
        print('Nous ' + drop + nous)
        print('Vous ' + drop + vous)
        print('Ils / Elles ' + drop + ilsElles)
    elif x[(l-2):(l)] == 're' :
        print( 'It is regular verb. ')
        drop = x[0: (l - 2)]
        # print(drop)
        je = 's'
        tu = 's'
        ilElle = ''
        nous = 'ons'
        vous = 'ez'
        ilsElles = 'ent'
        print('Je ' + drop + je)
        print('Tu ' + drop + tu)
        print('Il / Elle / On ' + drop + ilElle)
        print('Nous ' + drop + nous)
        print('Vous ' + drop + vous)
        print('Ils / Elles ' + drop + ilsElles)
        print()
    else :
        print("Not a regular verb, TYPO or Irregular Verb (>,<)")
        x = input("Try another French noun (press Enter to exit): \n")
        continue
    x = input("Enter another French noun (press Enter to exit): \n")