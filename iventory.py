while True:
	next=input ("input data baru  (Ya/Tidak)? ")
	if next == "ya" or next == "Ya":
		file = open ("db-iventory.txt","a")
		print("*"*40)
		nama_prangkat = input("Nama Perangkat :")
		lokasi = input("Lokasi :")
		print("-"*40)
		file.write("Nama perangkat :" + nama_prangkat + ",\t Lokasi : " + lokasi + "\n")
		file.close()
	elif next == "tidak" or next == "Tidak" :
		file = open("db-iventory.txt", "r")
		print("*"*40)
		for item in file:
			item = item.strip()
			print(item)
		break
