#include "SPI.h"
#include "PN532_SPI.h"
#include "snep.h"
#include "NdefMessage.h"

PN532_SPI pn532spi(SPI, 10);
SNEP nfc(pn532spi);
uint8_t ndefBuf[128];
uint8_t recordBuf[128];
String serialString;

void nfcSend(String str)
{
      NdefMessage msgSend = NdefMessage();
      msgSend.addTextRecord(str);
      int msgSize = msgSend.getEncodedSize();
      if (msgSize > sizeof(ndefBuf)) 
      {
          Serial.println("ndefBuf is too small");
      }
      msgSend.encode(ndefBuf);
      if (0 >= nfc.write(ndefBuf, msgSize)) 
      {
          Serial.println("Failed");
      }else{
          Serial.println("finsih");
      }
}

void nfcRead()
{
  while(1)
  {
    //Serial.println("Waiting for Phone...");
    int msgSize = nfc.read(ndefBuf, sizeof(ndefBuf));
    if (msgSize > 0) 
    {
      NdefMessage msg  = NdefMessage(ndefBuf, msgSize);
      Serial.print(msgTag + ":");
      NdefRecord record = msg.getRecord(0);
      int recordLength = record.getPayloadLength();    
      record.getPayload(recordBuf);
      Serial.write(recordBuf, recordLength);
      break;
    }else{
      Serial.println("Failed,try again.");
    }
  }
}


void loop()
{
   str="";
   while(1)
  {
    str = Serial.readString();
	if(str=="write")
	{
		Serial.print("write");
		str = Serial.readString();
		nfcSend(str);
		
	}
	else if(str=="read")
	{
		Serial.print("read");
		nfcRead()	
	} 
  }
}   

