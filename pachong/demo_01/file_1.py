if __name__ == '__main__':
    file = "D:\\Users\panrui\AppData\\1771924786\FileRecv\MobileFile\完美世界.txt"
    file_1 = "D:\\Users\panrui\AppData\\1771924786\FileRecv\MobileFile\\1.txt"
    file_sou = open(file, 'rb')
    f = open(file_1, 'a', encoding='utf-8')
    for line in file_sou.readlines():
        line = bytes.decode(line)
        if len(line) > 3:
            if len(line) <= 55 :
                f.write(line + "\n")
            else:
                while True:
                    str1 = line[0:55]
                    f.write(str1 + "\n")
                    # f.write(str.encode("\n"))
                    line = line[55:]
                    if len(line) > 55:
                        f.write("    ")
                        continue
                    else:
                        f.write("    " + line + "\n")
                        # f.write(str.encode("\n"))
                        break
                pass
    f.close()
