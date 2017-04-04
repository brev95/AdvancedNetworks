////////////////////////////////////////////////////////////////
// Student name: Instructor
// Course: COSC 4653
// Assignment: #6 - Robust TCP Client/Server Programming
// File name: protocol-records.h
// Purpose: Provides the #define constants and type definitions
//          for the query record and response record that are 
//          used by both the client and server programs 
// Limitations: None known
// Development Computer: Dell 
// Operating System: Windows XP using CYGWIN
// Integrated Development Environment (IDE): wordpad
// Compiler: gcc
// Operational Status: Fullfills the requirements
////////////////////////////////////////////////////////////////

#ifndef PROTOCOL_RECORD_HEADER
#define PROTOCOL_RECORD_HEADER

#define MAX_MESSAGE_TEXT 30
#define MAX_ID_TEXT 5
#define MAX_SECTOR_TEXT 15

typedef struct
   {
   char command; 
   char text[MAX_MESSAGE_TEXT];
   } queryRecordType;

typedef struct
   {
   char ID[MAX_ID_TEXT];
   char sector[MAX_SECTOR_TEXT];
   } databaseRecordType;

typedef union
   {
   databaseRecordType record;
   char text[MAX_MESSAGE_TEXT]; 
   } payloadType;


typedef struct
   {
   char command;
   char status; // 0 - not found, 1 - found
   payloadType data;
   } responseRecordType;

#endif

