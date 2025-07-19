# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

locale.setlocale(locale.LC_ALL, '') #passa a utilizar o locale
                                    #do sistema operacional
                                    #atualiza tudo (all)

locale.setlocale(locale.LC_ALL, 'pt_BR')
#print(locale.getlocale())
print(calendar.calendar(2022))

# comando para ver o locale do sistema: Get-WinSystemLocale