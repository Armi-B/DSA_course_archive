hamburger = input()
beginning_slot = 0
ending_slot = 0
most_length = 0
length = 0
for layer in hamburger:
    index = hamburger.find(layer, beginning_slot, ending_slot)
    ending_slot += 1
    if index == -1:
        #اگر شرط برقرار بود طول را ۱ واحد افزایش میدهیم.
        length += 1
        if most_length < length:
            #اگر از بزرگترین بزرگ تر بود ان را به عنوان بزرگترین جدید میگیریم.
            most_length = length
    else:
        beginning_slot = index + 1
        length = ending_slot - beginning_slot
print(most_length)
