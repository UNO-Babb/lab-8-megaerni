#ProcessData.py
#Name: Meg Aerni
#Date: 10.27.2025
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file

  line = inFile.readline()
  for line in inFile:
    data = line.split()
    studentID = makeID(data[0], data[1], data[3])
    studentmajoryear = majorYear(data[6], data[5])
    print(studentID)
    print(studentmajoryear)
  




  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()


def majorYear(major, year):
  abbrMajor = major[0:3]
  abbrYear = year[0:2]
  combined = abbrMajor + abbrYear
  return combined 

def makeID(firstname, lastname, id_num):
  nameLength = len(lastname)
  while nameLength < 5:
    lastname = lastname + "Z"
    nameLength = nameLength + 1
  id = firstname[0] + lastname + id_num[8:11]
  return id

if __name__ == '__main__':
  main()
