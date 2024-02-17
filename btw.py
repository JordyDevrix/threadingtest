
def main():
    keuze = input('kies een optie\n'
          '[1] BTW berekenen\n')

    if int(keuze) == 1:
        dienst_bedrag = input('gerekend tarief (21% BTW): ')
        btw_percentage = 1.21
        klant_betaald_bedrag = float(dienst_bedrag) * btw_percentage
        btw_bedrag = (float(dienst_bedrag) * btw_percentage) - float(dienst_bedrag)
        print(f'Dit is wat de klant betaalt excl. BTW\t-\t-\t-\t-\t{dienst_bedrag} euro\n'
              f'Dit is het BTW percentage\t-\t-\t-\t-\t-\t-\t-\t{btw_percentage}%\n'
              f'Dit is wat de klant betaalt incl. BTW\t-\t-\t-\t-\t{round(klant_betaald_bedrag, 2)} euro\n'
              f'Dit is de BTW die wordt bijgetelt\t-\t-\t-\t-\t-\t{round(btw_bedrag, 2)} euro\n'
              f'Dit is het bedrag wat je aan de belastingdienst aflegt\t{round(btw_bedrag, 2)} euro\n')


if __name__ == '__main__':
    main()
