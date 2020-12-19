import os, time, json, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
os.system('clear')

#utama
tanggal = input("Masukan tanggal [dd/mm/tttt] : ")
namper = input("Masukan nama siswa pertama : ")
msg = "Absen tanggal "+tanggal+"\n"+"01. "+namper+"\n"+"02. "+"\n"+"03. "+"\n"+"04. "+"\n"+"05. "+"\n"+"06. "+"\n"+"07. "+"\n"+"08. \n"+"09. \n"+"10. \n"+"11. \n"+"12. \n"+"13. \n"+"14. \n"+"15. \n"+"16. \n"+"17. \n"+"18. \n"+"19. \n"+"20. \n"+"21. \n"+"22. \n"+"23. \n"+"24. \n"+"24. \n"+"25. \n"+"26. \n"+"27. \n"+"28. \n"+"29. \n"
os.system('clear')
print(f"Gas absen? [y/n] : ")
pilih = input(f"pilih : ")
if pilih == 'y':
    os.system(f"xdg-open https://wa.me/+6283148261552?text={urllib.parse.quote(msg, safe='')}")
else:
	exit("Kenapa bro? ini instant absen lho..")