import hashlib

bsmith = "4ddd4137b84ff2db7291b568289717f0"
timestamp = b"<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>"

with open ('/home/nobo/Documents/dictionnaire/rockyou.txt',encoding='latin',mode='r') as file:
	for line in file:
		line = line.replace('\n','')
		password = bytes(line, 'utf-8')
		bsmith_result = hashlib.md5(timestamp+password)
		if bsmith_result.hexdigest() == bsmith:
			print(f'Good job, password is : {line} \n')




#print(bsmith_result.hexdigest())