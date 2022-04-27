import multiprocessing

from colorama import Fore
from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL2
from hdwallet.symbols import DASH as SYMBOL5
from hdwallet.symbols import DOGE as SYMBOL4
from hdwallet.symbols import ETH as SYMBOL1
from hdwallet.symbols import TRX as SYMBOL3

from hexer import mHash

# =========================================================================================
mmdrza = '''
                        
                        ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗ 
                        ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗
                        ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║
                        ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║
                        ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║
                        ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                
                        -------------------------------------------------------
                        [+] Programmer Mmdrza
                        [+] Personal Blog: httpS://Mmdrza.Com
                        [+] PyMmdrza.Github.Com
                        [+] Dev.to/Mmdrza
                        [+] x4@Mmdrza.Com
                        -------------------------------------------------------
                        Donate BTC=> 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
                        =======================================================
                      ___  ___  __                       ___  __   __     __       
                       |  |__  |__) |  /\  |       \  / |__  |__) /__` | /  \ |\ | 
                       |  |___ |  \ | /~~\ |___     \/  |___ |  \ .__/ | \__/ | \| 
                        =======================================================
                        For Buy and order Pro Version Follow https://Mmdrza.Com                                                                                                                     
'''
# ============================================================================================

r = 1
cores = 8


def seek(r) :
    print(mmdrza)

    fileETH = "eth500.txt"
    with open(fileETH) as f :
        add = f.read().split()
        addeth = set(add)

    fileBTC = "btc500.txt"
    with open(fileBTC) as f :
        add = f.read().split()
        addbtc = set(add)

    fileTRX = "trx500.txt"
    with open(fileTRX) as f :
        add = f.read().split()
        addtrx = set(add)

    fileDG = "doge500.txt"
    with open(fileDG) as f :
        add = f.read().split()
        addDG = set(add)

    fileDS = "Dash500.txt"
    with open(fileDS) as f :
        add = f.read().split()
        addDS = set(add)

    w = 0
    z = 0
    while True :
        hex64 = mHash()
        PRIVATE_KEY: str = hex64
        # =============================================
        HDETH: HDWallet = HDWallet(symbol = SYMBOL1)
        HDETH.from_private_key(private_key = PRIVATE_KEY)
        privETH = HDETH.private_key()
        ethadd = HDETH.p2pkh_address()
        # =============================================
        HDBTC: HDWallet = HDWallet(symbol = SYMBOL2)
        HDBTC.from_private_key(private_key = privETH)
        privBTC = HDBTC.private_key()
        btcadd = HDBTC.p2pkh_address()
        btcadd2 = HDBTC.p2sh_address()
        btcadd3 = HDBTC.p2wpkh_address()
        btcadd4 = HDBTC.p2wsh_address()
        btcadd5 = HDBTC.p2wsh_in_p2sh_address()
        btcadd6 = HDBTC.p2wpkh_in_p2sh_address()
        # =============================================
        HDTRX: HDWallet = HDWallet(symbol = SYMBOL3)
        HDTRX.from_private_key(private_key = privBTC)
        privTRX = HDTRX.private_key()
        trxadd = HDTRX.p2pkh_address()
        # =============================================
        HDDG: HDWallet = HDWallet(symbol = SYMBOL4)
        HDDG.from_private_key(private_key = privBTC)
        dgpriv = HDDG.private_key()
        dgaddr = HDDG.p2pkh_address()
        # =============================================
        HDDS: HDWallet = HDWallet(symbol = SYMBOL5)
        HDDS.from_private_key(private_key = privBTC)
        dashaddr = HDDS.p2pkh_address()
        dashpriv = HDDS.private_key()
        # =============================================

        print('Total Scan' , str(z) , ' Rich Wallet (Bitcoin/Ethereum/TRON/Dogecoin/Dash)' , end = '\r')

        z += 1

        if btcadd in addbtc or btcadd2 in addbtc or btcadd3 in addbtc or btcadd4 in addbtc or btcadd5 in addbtc or btcadd6 in addbtc :
            w += 1
            print(Fore.GREEN , 'Address BTC Saved On File Text' , Fore.YELLOW , 'Key=' , str(privBTC))
            f = open("BTCWinnerMultiFinder.txt" , "a")
            f.write('\nBTC PRIVATEKEY ======> ' + str(privBTC))
            f.write('\nAddressBTC =========> ' + str(btcadd))
            f.write('\nAddressBTC =========> ' + str(btcadd2))
            f.write('\nAddressBTC =========> ' + str(btcadd3))
            f.write('\nAddressBTC =========> ' + str(btcadd4))
            f.write('\nAddressBTC =========> ' + str(btcadd5))
            f.write('\nAddressBTC =========> ' + str(btcadd6))
            f.close()
        if ethadd in addeth :
            w += 1
            print('Ethereum Wallet Finder Now = ' , str(privETH))
            f1 = open("EthWinnerWalletFinder.txt" , "a")
            f1.write('\nPrivateKey ===========> ' + str(privETH))
            f1.write('\nETHaddress ===========> ' + str(ethadd))
            f1.close()
        if trxadd in addtrx :
            w += 1
            print('TRX Wallet Winner Now Saved On File PrivateKey ====> ' , str(privTRX))
            f2 = open("TRXWinnerWalletFinderMulti.txt" , "a")
            f2.write('\nPrivateKey ==============> ' + str(privTRX))
            f2.write('\nAddressTRX ==============> ' + str(trxadd))
            f2.close()
        if dgaddr in addDG :
            w += 1
            print('Doge Wallet Winner Now Saved On File PrivateKey ====> ' , str(dgpriv))
            f2 = open("DogeWinnerWalletFinderMulti.txt" , "a")
            f2.write('\nPrivateKey ==============> ' + str(dgpriv))
            f2.write('\nAddress==============> ' + str(dgaddr))
            f2.close()

        if dashaddr in addDS :
            w += 1
            print('Dash Wallet Winner Now Saved On File PrivateKey ====> ' , str(dashpriv))
            f2 = open("DashWinnerWalletFinderMulti.txt" , "a")
            f2.write('\nPrivateKey ==============> ' + str(dashpriv))
            f2.write('\nAddress==============> ' + str(dashaddr))
            f2.close()


seek(r)

if __name__ == '__main__' :
    jobs = []
    for r in range(cores) :
        p = multiprocessing.Process(target = seek , args = (r ,))
        jobs.append(p)
        p.start()
