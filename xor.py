import sys

def main(input,output) :
  with open(output,"wb") as o:
    with open(input,"rb") as i:
      while True:
        c = i.read(1)
        if len(c) == 0:
          return
        print("%02x" % (c[0] ^ 0xff))
        o.write(int(c[0] ^ 0xff).to_bytes(1, byteorder='big', signed=False)  )

if __name__ == '__main__':
  main(sys.argv[1],sys.argv[2])

