def main():
    bucketSize = int(input('Enter the bucket size: '))
    outputRate = int(input('Enter the output rate: '))
    n = int(input('Enter number of packets: '))
    for i in range(0, n):
        packetS = int(input('Enter packet size: '))
        if packetS < bucketSize:
            if(packetS <= outputRate):
                print('Bucket output successful!')
                print('Last bytes sent: ')
                print(packetS)
            else:
                print('Bucket output successful!')
                print('Bytes outputted: ')
                print(outputRate)
                sent = packetS - outputRate
                print('Last bytes sent: ')
                print(sent)
        else:
            print('Bucket is full !!')


main()
