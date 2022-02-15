
censurado = ("Baba-ovo", "Babaovo", "Babaca", "Bacura", "Bagos", "Baitola", "Bebum", "Besta", "Bicha", "Bisca", "Bixa", "Boazuda", "Boceta", "Boco", "Boiola", "Bolagato", "Boquete", "Bolcat", "Bosseta", "Bosta", "Bostana", "Brecha", "Brexa", "Brioco", "Bronha", "Buca", "Buceta", "Bunda", "Bunduda", "Burra", "Burro", "Busseta", "Cachorra", "Cachorro", "Cadela", "Caga", "Cagado", "Cagao", "Cagona", "Canalha", "Caralho", "Casseta", "Cassete", "Checheca", "Chereca", "Chibumba", "Chibumbo", "Chifruda", "Chifrudo", "Chota", "Chochota", "Chupada", "Chupado", "Clitoris", "Cocaina", "Coco", "Corna", "Corno", "Cornuda", "Cornudo", "Corrupta", "Corrupto", "Cretina", "Cretino", "Cruz-credo", "Cu", "Culhao", "Curalho", "Cuzao", "Cuzuda", "Cuzudo", "Debil", "Debiloide", "Defunto", "Demonio", "Difunto", "Doida", "Doido", "Egua", "Escrota", "Escroto", "Esporrada", "Esporrado", "Esporro", "Estupida", "Estupidez", "Estupido", "Fedida", "Fedido", "Fedor", "Fedorenta", "Feia", "Feio", "Feiosa", "Feioso", "Feioza", "Feiozo", "Felacao", "Fenda", "Foda", "Fodao", "Fode", "Fodida", "Fodido", "Fornica", "Fudendo", "Fudecao", "Fudida", "Fudido", "Furada", "Furado", "Furão", "Furnica", "Furnicar", "Furo", "Furona", "Gaiata", "Gaiato", "Gonorrea", "Gonorreia", "Gosma", "Gosmenta", "Gosmento", "Grelinho", "Grelo", "Idiota", "Idiotice", "Imbecil", "Iscrota", "Iscroto", "Japa", "Ladra", "Ladrao", "Ladroeira", "Ladrona", "Lalau", "Leprosa", "Leproso", "Macaca", "Macaco", "Machona", "Machorra", "Manguaca", "Mangua¦a", "Masturba", "Meleca", "Merda", "Mija", "Mijada", "Mijado", "Mijo", "Mocrea", "Mocreia", "Moleca", "Moleque", "Mondronga", "Mondrongo", "Naba", "Nadega", "Nojeira", "Nojenta", "Nojento", "Nojo", "Olhota", "Otaria", "Otária", "Otario", "Otário", "Paca", "Paspalha", "Paspalhao", "Paspalho", "Pau", "Peia", "Peido", "Pemba", "Pênis", "Pentelha", "Pentelho", "Perereca", "Peru", "Pica", "Picao", "Pilantra", "Piranha", "Piroca", "Piroco", "Piru", "Porra", "Prega", "Prostibulo", "Prostíbulo", "Prostituta", "Prostituto", "Punheta", "Punhetao", "Pus", "Pustula", "Puta", "Puto", "Puxa-saco", "Puxasaco", "Rabao", "Rabo", "Rabuda", "Rabudao", "Rabudo", "Rabudona", "Racha", "Rachada", "Rachadao", "Rachadinha", "Rachadinho", "Rachado", "Ramela", "Remela", "Retardada", "Retardado", "Ridícula", "Rola", "Rolinha", "Rosca", "Sacana", "Safada", "Safado", "Sapatao", "Sifilis", "Siririca", "Tarada", "Tarado", "Testuda", "Tezao", "Tezuda", "Tezudo", "Trocha", "Trolha", "Troucha", "Trouxa", "Troxa", "Vaca", "Vagabunda", "Vagabundo", "Veadao", "Viada", "Víado", "Viadao", "Xavasca", "Xerereca", "Xexeca", "Xibiu", "Xibumba", "Xota", "Xochota", "Xoxota", "Xana", "Xaninha")

tweet = input("Escreva um Tweet de até 280 caracteres: ")

tweet_censurado = False
for palavra_censurada in censurado:
    if palavra_censurada.lower() in tweet:
        tweet_censurado = True
        break

if tweet_censurado:
    print('#### CENSURADO ####')
else:
    print('####', tweet ,'####')
