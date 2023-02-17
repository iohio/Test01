def cryptoTax():    
    file = open('crypto_tax.txt')
    sum_profix = 0
    i = 0
    wallet = {}
    for crypto in file:
        tCrypto = str(crypto)
        aCrypto = tCrypto.split()
        if aCrypto[0] == 'B':
            if aCrypto[1] in wallet:
                wallet[aCrypto[1]].append(aCrypto[2]+' '+aCrypto[3])
            else:
                wallet[aCrypto[1]] = []
                wallet[aCrypto[1]].append(aCrypto[2]+' '+aCrypto[3])
        elif aCrypto[0] == 'S':
            #ถ้าวอเลทมีเงินที่จะขา่ยจริง
            if aCrypto[1] in wallet:
                sellPrice = float(aCrypto[2])
                totalSell = float(aCrypto[3])            
                walletCrypto = wallet[aCrypto[1]][0].split()
                priceWalletCrypto = float(walletCrypto[0])
                totalWalletCrypto = float(walletCrypto[1])
                if totalSell > totalWalletCrypto:
                    totalSell = totalSell - totalWalletCrypto
                    total = (sellPrice - priceWalletCrypto) * totalWalletCrypto
                    sum_profix += total
                    del wallet[aCrypto[1]][0]
                    while totalSell > 0:
                        walletCrypto = wallet[aCrypto[1]][0].split()                      
                        priceWalletCrypto = float(walletCrypto[0])
                        totalWalletCrypto = float(walletCrypto[1])
                        if totalSell <= totalWalletCrypto:
                            
                            totalWalletCrypto = totalWalletCrypto - totalSell
                            total = (sellPrice - priceWalletCrypto) * totalSell
                            sum_profix += total
                            del wallet[aCrypto[1]][0]
                            if totalWalletCrypto > 0:
                                wallet[aCrypto[1]].insert(0, str(walletCrypto[0])+' '+str(totalWalletCrypto))
                                totalSell = 0
                        else:
                                return print('เหรียญไม่พอสำหรับการขาย')
                elif totalSell <= totalWalletCrypto:
                    totalWalletCrypto = totalWalletCrypto - totalSell
                    total = (sellPrice - priceWalletCrypto) * totalWalletCrypto
                    sum_profix += total
                    del wallet[aCrypto[1]][0]
                    wallet[aCrypto[1]].insert(0, str(walletCrypto[0])+' '+str(totalWalletCrypto))
    file.close()
    return print(wallet,sum_profix)

cryptoTax()
    